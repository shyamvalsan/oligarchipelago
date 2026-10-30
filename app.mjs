import {DIMENSIONS,wealthPosition,wealthDivider,plotGeometry,spectrumLabel} from './lib/spectrum.mjs';
import {launchUniverse} from './lib/universe.mjs';
import {layout,mergeTies,coastline,radius as isleRadius} from './lib/archipelago.mjs';
import {CONTINENTS,ORIGINS,ASSESSMENTS,assessment,coverage,DEFAULTS,QUADRANTS,footprint,influence,surprisePool,metric,quadrant,filterPeople,sortPeople,parseState,serializeState,money,percent,escapeHTML as h,exportCsv} from './lib/model.mjs';

const $ = selector => document.querySelector(selector);
const $$ = selector => [...document.querySelectorAll(selector)];
const SVG = 'http://www.w3.org/2000/svg';
let data, evidence, screening, state, filtered=[], chartPoints=[], toastTimer, previousDialogFocus;
let pageSize=25;

async function boot(){
  try {
    const responses=await Promise.all(['data/billionaires.json','data/assessments.json','data/screening.json'].map(url=>fetch(url)));
    if(responses.some(r=>!r.ok)) throw new Error('A local data file could not be loaded.');
    [data,evidence,screening]=await Promise.all(responses.map(r=>r.json()));
    if(!Array.isArray(data.people)||data.people.length!==500||!evidence.profiles) throw new Error('Dataset validation failed.');
    ({data,evidence}=launchUniverse(data,evidence));
    state=parseState(location.hash,data.people,data.countries);
    $('#total-wealth').textContent=money(data.people.reduce((sum,p)=>sum+p.wealth*1e9,0));
    $('#country-count').textContent=new Set(data.people.map(p=>p.country)).size;
    $('#country').insertAdjacentHTML('beforeend',Object.keys(data.countries).sort().map(c=>`<option value="${h(c)}">${h(c)}</option>`).join(''));
    $('#industry').insertAdjacentHTML('beforeend',[...new Set(data.people.map(p=>p.industry))].sort().map(c=>`<option value="${h(c)}">${h(c)}</option>`).join(''));
    $('#continents').innerHTML=`<button data-continent="all" aria-pressed="true">All waters</button>`+Object.entries(CONTINENTS).map(([name,color])=>`<button data-continent="${h(name)}" aria-pressed="false"><span class="legend-dot" style="--dot:${color}"></span>${h(name)}</button>`).join('');
    $('#origin-legend').innerHTML=Object.values(ORIGINS).map(o=>`<span><span class="legend-dot" style="--dot:${o.color}"></span>${h(o.label)}</span>`).join('');
    attachEvents();
    const advanced=['industry','gdp','income','ppp','color','scale'].some(k=>state[k]!==DEFAULTS[k]);
    setAdvanced(advanced);
    render();
    setTimeout(heroMap,0);
  } catch(error){
    console.error(error);
    $('#result-count').textContent='Data unavailable';
    $('#lens-note').innerHTML=`<span>OFFLINE?</span><div>The atlas couldn't load its local data files. Try reloading, or <a href="data/billionaires.json">open the dataset</a>. For local development, serve the folder over HTTP rather than opening index.html directly.</div>`;
    $('#profile').innerHTML='<div class="profile-welcome"><h3>A little lost at sea.</h3><p>The dataset could not be loaded. No estimated or replacement figures are being shown.</p><button class="outline-button" onclick="location.reload()">Try again</button></div>';
  }
}

function setAdvanced(open){
  $('#advanced-filters').hidden=!open;
  $('#more-filters').setAttribute('aria-expanded',String(open));
  $('#more-filters span').textContent=open?'−':'＋';
}
function attachEvents(){
  $('#search').addEventListener('input',e=>update({search:e.target.value.slice(0,150),page:1}));
  for(const key of ['assessment','country','origin','industry','gdp','income','ppp','color','scale']) $('#'+key).addEventListener('change',e=>update({[key]:e.target.value,page:1}));
  document.addEventListener('click',e=>{
    const button=e.target.closest('button');
    if(!button) return;
    if(button.dataset.assessment) update({assessment:button.dataset.assessment,lens:'influence',page:1});
    if(button.dataset.continent) update({continent:button.dataset.continent,page:1});
    if(button.dataset.lens) update({lens:button.dataset.lens,page:1});
    if(button.dataset.view) update({view:button.dataset.view});
    if(button.dataset.person) selectPerson(button.dataset.person);
    if(button.dataset.dialog) openDialog(button.dataset.dialog);
    if(button.dataset.sort) update({sort:button.dataset.sort,direction:state.sort===button.dataset.sort&&state.direction==='asc'?'desc':'asc',page:1});
  });
  $('#more-filters').addEventListener('click',()=>setAdvanced($('#advanced-filters').hidden));
  $('#reset').addEventListener('click',reset);
  $('#empty-reset').addEventListener('click',reset);
  $('#surprise').addEventListener('click',()=>{
    if(!filtered.length) return toast('No matches. Clear a filter to explore again.');
    const pool=surprisePool(filtered,state.lens,evidence);
    selectPerson(pool[Math.floor(Math.random()*pool.length)].id);
  });
  $('#share').addEventListener('click',share);
  $('#download').addEventListener('click',()=>{
    const blob=new Blob(['\ufeff'+exportCsv(filtered,data.countries,evidence)],{type:'text/csv;charset=utf-8'});
    const url=URL.createObjectURL(blob),a=document.createElement('a');
    a.href=url;a.download='oligarchipelago-2026-filtered.csv';a.click();
    setTimeout(()=>URL.revokeObjectURL(url),10000);
    toast(`Exported ${filtered.length} entries with years, units, and missing values preserved.`);
  });
  $('#prev-page').addEventListener('click',()=>update({page:Math.max(1,state.page-1)}));
  $('#next-page').addEventListener('click',()=>update({page:state.page+1}));
  $('#close-dialog').addEventListener('click',()=>$('#info-dialog').close());
  $('#info-dialog').addEventListener('click',e=>{if(e.target===$('#info-dialog')){const r=e.target.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)e.target.close();}});
  $('#info-dialog').addEventListener('close',()=>previousDialogFocus?.focus());
  $('#profile').addEventListener('click',e=>{
    if(e.target.closest('[data-close-profile]')){update({selected:''});$('#surprise').focus();}
  });
  window.addEventListener('hashchange',()=>{
    if(location.hash==='#explorer'||location.hash==='#hero-title') return;
    state=parseState(location.hash,data.people,data.countries);render();
  });
  $('#chart').addEventListener('keydown',e=>{
    if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home','End','Escape'].includes(e.key)) return;
    if(e.key==='Escape'){$('#tooltip').hidden=true;return;}
    e.preventDefault();
    const index=chartPoints.findIndex(p=>p.person.id===e.target.dataset.personId);
    const delta=['ArrowLeft','ArrowDown'].includes(e.key)?-1:1;
    const next=e.key==='Home'?0:e.key==='End'?chartPoints.length-1:(index+delta+chartPoints.length)%chartPoints.length;
    if(chartPoints[next]) $('#chart').querySelector(`[data-person-id="${CSS.escape(chartPoints[next].person.id)}"]`)?.focus();
  });
  new ResizeObserver(()=>{if(state?.view==='chart') requestAnimationFrame(renderChart);}).observe($('#chart-container'));
}
function update(patch){state={...state,...patch};render();}
function reset(){state={...DEFAULTS,lens:state.lens,view:state.view,selected:''};setAdvanced(false);render();toast('Fresh waters. All filters cleared.');}
function selectPerson(id){
  update({selected:id});
  if(matchMedia('(max-width:800px)').matches){$('#profile').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth',block:'nearest'});}
  $('#profile').focus({preventScroll:true});
}
function render(){
  filtered=filterPeople(data.people,state,data.countries,evidence);
  if(state.selected&&!filtered.some(p=>p.id===state.selected))state.selected='';
  state.page=Math.min(state.page,Math.max(1,Math.ceil(filtered.length/pageSize)));
  syncControls();
  const plotted=filtered.filter(p=>metric(p,state,data.countries,evidence)!==null);
  $('#result-count').textContent=`${filtered.length} of ${data.people.length} shown, ${plotted.length} positioned, ${filtered.length-plotted.length} without a position`;
  $('#chart-view').hidden=state.view!=='chart'||!filtered.length;
  $('#table-view').hidden=state.view!=='table'||!filtered.length;
  $('#empty-state').hidden=!!filtered.length;
  $('#origin-legend').hidden=state.color!=='origin';
  renderOverview();
  const pilot=state.lens==='influence';
  $('#lens-note').classList.toggle('pilot-note',pilot);
  $('#lens-note').innerHTML=pilot
    ? `<div><strong>A spectrum, not a guilty or innocent switch.</strong> Height is the reviewed wealth–power relationship; confidence and counterevidence stay in each file. Flags show Forbes citizenship. Missing evidence is never plotted as low influence.</div>`
    : '<div>Fortune divided by national annual GDP. This compares scale. It is <strong>not a political influence score</strong> or a share of GDP owned. Wealth is 2026, GDP is 2024.</div>';
  $('#metric-sort').textContent=pilot?'Spectrum ↕':'Footprint ↕';
  if(state.view==='chart'&&filtered.length)renderChart();
  if(state.view==='table')renderTable();
  renderProfile();renderQuadrants();renderUnmapped();
  const hash=serializeState(state);
  history.replaceState(null,'',location.pathname+location.search+(hash?'#'+hash:''));
}
function syncControls(){
  for(const key of ['assessment','search','country','origin','industry','gdp','income','ppp','color','scale']) if($('#'+key).value!==state[key])$('#'+key).value=state[key];
  for(const b of $$('[data-continent]'))b.setAttribute('aria-pressed',String(state.continent===b.dataset.continent));
  for(const b of $$('[data-lens]'))b.setAttribute('aria-pressed',String(state.lens===b.dataset.lens));
  for(const b of $$('[data-view]'))b.setAttribute('aria-pressed',String(state.view===b.dataset.view));
}

function el(name,attrs={},text){const e=document.createElementNS(SVG,name);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,v);if(text!==undefined)e.textContent=text;return e;}
function renderChart(){
  if(!data||$('#chart-view').hidden)return;
  renderSpectrumChart();
}
function addFlagPatterns(svg){
  const defs=el('defs');
  for(const iso of new Set(data.people.map(p=>p.iso))){
    const pattern=el('pattern',{id:`flag-${iso}`,patternContentUnits:'objectBoundingBox',width:1,height:1});
    pattern.append(el('image',{href:`assets/flags/${iso.toLowerCase()}.svg`,width:1,height:1,preserveAspectRatio:'xMidYMid slice'}));defs.append(pattern);
  }
  svg.append(defs);return defs;
}
function renderSpectrumChart(){
  const svg=$('#chart'),mobile=matchMedia('(max-width:600px)').matches,pilot=state.lens==='influence';
  const {W,H,L,R,T,B,cx,cy}=plotGeometry(mobile),divider=wealthDivider(state.scale);
  const x=v=>L+wealthPosition(v,state.scale)*(R-L);
  // Symmetric log GDP bounds around 1%; or continuous 0–100 editorial spectrum.
  const y=v=>B-(pilot?v/100:(Math.log10(v)+3)/6)*(B-T);
  svg.setAttribute('viewBox',`0 0 ${W} ${H}`);svg.setAttribute('role','group');$('#chart-container').style.aspectRatio=`${W} / ${H}`;
  svg.replaceChildren(el('title',{id:'chart-title'},pilot?'Wealth and oligarchic relationship spectrum':'Wealth and economic footprint'),el('desc',{id:'chart-desc'},'Four equal-sized quadrants. Circle markers carry citizenship flags. Tab then arrow keys navigate positioned entries; Enter opens evidence. Entries without sufficient evidence appear in the separate unplaced list, never at zero.'));
  $('#tooltip').hidden=true;
  const defs=addFlagPatterns(svg),gradient=el('linearGradient',{id:'spectrum-gradient',x1:0,y1:1,x2:0,y2:0});
  [['0%','#ffffff'],['100%','#ffffff']].forEach(([offset,color])=>gradient.append(el('stop',{offset,'stop-color':color})));defs.append(gradient);
  svg.append(el('rect',{x:L,y:T,width:R-L,height:B-T,fill:'none',class:'plot-frame'}));
  // These equal rectangles also expose testable geometry. No unequal category bands.
  [[L,T,'low-high'],[cx,T,'high-high'],[L,cy,'low-low'],[cx,cy,'high-low']].forEach(([xp,yp,id])=>svg.append(el('rect',{x:xp,y:yp,width:(R-L)/2,height:(B-T)/2,fill:'transparent','data-quadrant':id,'pointer-events':'none'})));
  const xticks=state.scale==='log'?[2.5,5,10,25,50,100,250,500,1000]:[0,100,250,500,750,1000];
  for(const tick of xticks){if(mobile&&[5,25,250].includes(tick))continue;svg.append(el('line',{x1:x(tick),x2:x(tick),y1:T,y2:B,class:'gridline'}),el('text',{x:x(tick),y:B+27,'text-anchor':'middle',class:'tick spectrum-tick'},tick===1000?'$1T':`$${tick}B`));}
  for(const tick of pilot?[0,25,50,75,100]:[.001,.01,.1,1,10,100,1000])svg.append(el('line',{x1:L,x2:R,y1:y(tick),y2:y(tick),class:'gridline'}),el('text',{x:L-14,y:y(tick)+5,'text-anchor':'end',class:'tick spectrum-tick'},pilot?String(tick):`${tick}%`));
  svg.append(el('line',{x1:cx,x2:cx,y1:T,y2:B,class:'divider'}),el('line',{x1:L,x2:R,y1:cy,y2:cy,class:'divider'}));
  const q=QUADRANTS[state.lens];
  [[q[2],L+18,T+32,'start'],[q[3],R-18,T+32,'end'],[q[0],L+18,B-20,'start'],[q[1],R-18,B-20,'end']].forEach(([v,xp,yp,anchor])=>svg.append(el('text',{x:xp,y:yp,'text-anchor':anchor,class:'spectrum-quadrant'},v.name)));
  svg.append(el('text',{x:L,y:T-24,class:'spectrum-endpoint'},pilot?'More oligarch ↑':'Larger economic footprint ↑'),el('text',{x:R,y:T-24,'text-anchor':'end',class:'tick'},`Wealth divider ${money(divider*1e9)}`));
  svg.append(el('text',{x:L,y:B+66,class:'spectrum-endpoint'},pilot?'Just another billionaire ↓':'Smaller economic footprint ↓'),el('text',{x:mobile?cx:R,y:B+(mobile?110:66),'text-anchor':mobile?'middle':'end',class:'axis-title'},`Net worth, ${state.scale==='log'?'log':'linear'} scale →`));
  svg.append(el('text',{x:25,y:(T+B)/2,transform:`rotate(-90 25 ${(T+B)/2})`,'text-anchor':'middle',class:'axis-title'},pilot?'Editorial wealth–power estimate':'Wealth / 2024 GDP, log scale'));
  chartPoints=filtered.map(person=>({person,value:metric(person,state,data.countries,evidence)})).filter(p=>p.value!==null).map(p=>({...p,x:x(p.person.wealth),y:y(p.value)}));
  const hasSelection=chartPoints.some(p=>p.person.id===state.selected);
  // No jitter in measured coordinates; overlapping people remain accessible in file and table.
  const layer=el('g');
  const selectedPoint=chartPoints.find(p=>p.person.id===state.selected);
  if(pilot&&selectedPoint){const a=assessment(selectedPoint.person,evidence);if(a.range)layer.append(el('line',{x1:selectedPoint.x,x2:selectedPoint.x,y1:y(a.range[0]),y2:y(a.range[1]),class:'editorial-range','aria-label':`Editorial plausible range ${a.range[0]} to ${a.range[1]}, not a statistical interval`}));}
  for(const point of [...chartPoints].sort((a,b)=>(a.person.id===state.selected?1:0)-(b.person.id===state.selected?1:0)||b.person.position-a.person.position)){
    const p=point.person,active=p.id===state.selected;
    if(active)layer.append(el('circle',{cx:point.x,cy:point.y,r:mobile?18:16,class:'halo'}));
    const circle=el('circle',{cx:point.x,cy:point.y,r:active?12:mobile?10:9,fill:dotColor(p),class:`bubble flag-bubble${active?' selected':''}`,role:'button',tabindex:active||(!hasSelection&&p.id===chartPoints[0]?.person.id)?0:-1,'data-person-id':p.id,'aria-label':`${p.name}, ${p.country}, ${money(p.wealth*1e9)}, ${pilot?spectrumLabel(assessment(p,evidence)):percent(point.value)+' of national annual GDP'}. Open details.`});
    circle.append(el('title',{},`${p.name} · ${p.country}`));
    circle.addEventListener('pointerenter',()=>showTooltip(point));circle.addEventListener('pointerleave',()=>$('#tooltip').hidden=true);circle.addEventListener('focus',()=>showTooltip(point));circle.addEventListener('blur',()=>$('#tooltip').hidden=true);circle.addEventListener('click',()=>selectPerson(p.id));circle.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();selectPerson(p.id);}});layer.append(circle);
  }
  svg.append(layer);
  if(selectedPoint)svg.append(el('text',{x:selectedPoint.x+(selectedPoint.x>R-200?-17:17),y:selectedPoint.y-18,'text-anchor':selectedPoint.x>R-200?'end':'start',class:'point-label'},selectedPoint.person.name.replace(' & family','')));
  if(!chartPoints.length)svg.append(el('text',{x:cx,y:cy-15,'text-anchor':'middle',class:'spectrum-quadrant'},'No defensible positions in this slice yet.'));
}
function showTooltip(point){
  const p=point.person,tip=$('#tooltip'),pilot=state.lens==='influence';
  const overlaps=chartPoints.filter(o=>o.x===point.x&&o.y===point.y).length;
  tip.innerHTML=`<strong>${h(p.name)}</strong><div class="tooltip-meta">${h(p.country)} · ${h(p.sourceOfWealth)}</div><dl><dt>Net worth</dt><dd>${money(p.wealth*1e9)}</dd><dt>${pilot?'Assessment':'Wealth / GDP'}</dt><dd>${pilot?spectrumLabel(assessment(p,evidence)):percent(point.value)}</dd><dt>Origin</dt><dd>${h(ORIGINS[p.origin].label)}</dd></dl>${overlaps>1?`<p class="quiet">${overlaps} entries share this position. Open details to choose.</p>`:''}`;
  tip.hidden=false;
  const box=$('#chart-container').getBoundingClientRect(),view=$('#chart').viewBox.baseVal;
  const tipBox=tip.getBoundingClientRect();
  // Account for SVG's xMidYMid letterboxing when a small viewport hits min-height.
  const fit=Math.min(box.width/view.width,box.height/view.height);
  const px=point.x*fit+(box.width-view.width*fit)/2,py=point.y*fit+(box.height-view.height*fit)/2;
  tip.style.left=Math.max(4,Math.min(px+13,box.width-tipBox.width-5))+'px';
  tip.style.top=Math.max(4,Math.min(py-tipBox.height-12,box.height-tipBox.height-4))+'px';
}
function renderUnmapped(){
  const missing=filtered.filter(p=>metric(p,state,data.countries,evidence)===null),pilot=state.lens==='influence';
  $('#unmapped').hidden=!missing.length;
  $('#unmapped').innerHTML=missing.length?`<details class="research-roster"><summary><strong>${missing.length} entries without a position</strong> · ${pilot?'further individual evidence needed':'GDP not available'} <span>Show every entry</span></summary><p>${pilot?'All names received source discovery, but discovery is not assessment. These people are not silently classified as ordinary billionaires, nor assigned arbitrary middle scores. Open a file to see the research trail.':'These citizenship-attributed economies have no matching GDP observation. No proxy has been invented.'}</p><div class="research-roster-grid">${missing.map(p=>`<button data-person="${h(p.id)}" title="${h(p.name)} · ${h(p.country)}"><img src="assets/flags/${p.iso.toLowerCase()}.svg" width="22" height="22" alt=""><span>${h(p.name)}</span></button>`).join('')}</div></details>`:'';
}
function renderTable(){
  const sorted=sortPeople(filtered,state,data.countries,evidence),start=(state.page-1)*pageSize;
  $('#table-body').innerHTML=sorted.slice(start,start+pageSize).map(p=>{
    const value=metric(p,state,data.countries,evidence);
    return `<tr class="${p.id===state.selected?'selected':''}"><td>${p.rank}</td><td><button data-person="${h(p.id)}">${h(p.name)}</button></td><td>${h(p.country)}</td><td>${money(p.wealth*1e9)}</td><td>${state.lens==='influence'?h(spectrumLabel(assessment(p,evidence))):value==null?'Uncharted':percent(value)}</td><td>${h(ORIGINS[p.origin].label)}</td></tr>`;
  }).join('');
  $('#page-label').textContent=`${filtered.length?start+1:0}–${Math.min(start+pageSize,filtered.length)} of ${filtered.length}`;
  $('#prev-page').disabled=state.page<=1;
  $('#next-page').disabled=state.page>=Math.ceil(filtered.length/pageSize);
  for(const button of $$('[data-sort]'))button.closest('th').setAttribute('aria-sort',button.dataset.sort===state.sort?(state.direction==='asc'?'ascending':'descending'):'none');
}
function sourceCard(r,index=0){return `<details class="receipt-item"><summary>${index+1}. ${h(r.kind)}</summary><p>${h(r.text)}</p><a href="${h(r.url)}" target="_blank" rel="noopener noreferrer">${h(r.source)}</a><p>Source date: ${h(r.date)}</p>${r.access?`<p class="quiet">Review access: ${h(r.access)}</p>`:''}</details>`;}
function renderProfile(){
  const panel=$('#profile'),p=filtered.find(p=>p.id===state.selected);
  if(!p){panel.innerHTML=`<div class="profile-welcome"><h3>Pick a dot.</h3><p>Choose a dot or a name to see the assessment, the mechanism and the evidence against it.</p>${filtered.length?`<button class="plain-link" data-person="${h(filtered[0].id)}">Start with ${h(filtered[0].name.replace(' & family',''))}</button>`:''}</div>`;return;}
  const a=assessment(p,evidence),label={color:a.score==null?'#6a7c76':a.score>=50?'#a04c34':'#357a74',label:spectrumLabel(a)},c=data.countries[p.country],fp=footprint(p,data.countries),screen=screening.profiles[p.id];
  const overlaps=chartPoints.filter(o=>o.person.id!==p.id&&o.person.wealth===p.wealth&&o.value===metric(p,state,data.countries,evidence));
  panel.innerHTML=`<div class="profile-kicker"><span>Forbes rank ${p.rank}</span><button data-close-profile aria-label="Close profile">Close</button></div>
    <div class="profile-identity"><img class="profile-flag" src="assets/flags/${p.iso.toLowerCase()}.svg" width="46" height="46" alt="${h(p.country)} flag"><div><h3>${h(p.name)}</h3><p>${h(p.country)}</p></div></div>
    <p class="profile-source">${h(p.sourceOfWealth)} · ${h(p.industry)}</p>
    <div class="assessment-verdict" style="--verdict:${label.color}"><small>Editorial estimate, not a legal finding</small><h4>${h(label.label)}</h4><p>${h(a.summary||'No individual case assessment yet. Neither a blank file nor a negative sanctions-name check is evidence of low political influence.')}</p>${a.confidence?`<div class="case-confidence">Confidence: ${h(a.confidence)}</div><small>${h(a.period)}</small>`:''}</div>
    ${renderRubric(a)}
    <div class="profile-metrics"><div><span>Net worth</span><strong>${money(p.wealth*1e9)}</strong><small>Forbes, 1 Mar 2026</small></div><div><span>Wealth / GDP</span><strong>${percent(fp)}</strong><small>Scale, not power. 2024 GDP.</small></div></div>
    ${a.fileState==='case-reviewed'?`<div class="profile-section"><h4>The money–power loop</h4><p class="mechanism">${h(a.mechanism||'No mechanism established in the narrowly reviewed sources.')}</p><h4>What supports the assessment</h4>${a.support.map(sourceCard).join('')}<h4 class="counter-title">What weakens or complicates it</h4>${a.counter.map(sourceCard).join('')}<div class="case-limit"><strong>What we still don’t know</strong><p>${h(a.limitations)}</p></div><p class="quiet">Reviewed ${h(a.reviewedAt)} · ${h(a.reviewDepth)}</p></div>`:'<div class="profile-section"><h4>Research still needed</h4><p>Trace political access, any specific economic benefit, reciprocal support, and credible alternative explanations. Nationality and inheritance cannot fill those gaps.</p></div>'}
    ${renderResearchTrail(a)}
    <div class="profile-section"><details class="receipt-item"><summary>Full-list screening · narrow name check</summary><p>All 500 names checked against one UK sanctions-list snapshot (${h(screening.reportDate)}). This is a research lead only, not an oligarch test or comprehensive sanctions clearance.</p>${screen.matches.length?`<strong>${screen.matches.length} candidate designation(s)—identity must be checked</strong>${screen.matches.map(m=>`<p><a href="${h(m.url)}" target="_blank" rel="noopener noreferrer">${h(m.name)} · ${h(m.designationId)}</a></p>`).join('')}`:'<p>No candidate name match under the script’s narrow matching rules. This does not mean no sanctions or no oligarchic influence.</p>'}<a href="data/screening.json">Screening provenance and exact reasons</a></details></div>
    <div class="profile-section"><details class="receipt-item"><summary>Fortune origin · ${h(ORIGINS[p.origin].label)}</summary><p>${originDescription(p)}</p><p>Origin adds no points and cannot establish political influence.</p></details></div>
    <div class="profile-section context-section"><h4>The home-country context <span class="quiet">2024</span></h4><p>Forbes citizenship attribution, not location of every asset or political relationship. Wealth is a stock; GDP is an annual flow.</p><div class="context-grid">${contextCell('GDP',c.gdp,'$')}${contextCell('GDP / person',c.gdpPerCapita,'$')}${contextCell('GDP · PPP',c.gdpPpp,'Int$')}${contextCell('PPP / person',c.gdpPerCapitaPpp,'Int$')}</div></div>
    ${overlaps.length?`<div class="profile-section"><h4>Same wealth and assessment / metric</h4><div class="unmapped-list">${overlaps.map(o=>`<button data-person="${h(o.person.id)}">${h(o.person.name)}</button>`).join('')}</div></div>`:''}
    <div class="profile-bottom"><a href="${h(p.profileUrl)}" target="_blank" rel="noopener noreferrer">Forbes profile</a><button class="text-button" data-dialog="methodology">Question the method</button></div>`;
}
function contextCell(label,observation,prefix){return `<div><span>${label}</span><strong>${observation?`<a href="${h(observation.url)}" target="_blank" rel="noopener noreferrer">${money(observation.value,prefix)}</a>`:'—'}</strong><small>${observation?observation.year:'No data'}</small></div>`;}
function originDescription(p){
  if(p.origin==='self-made')return 'Forbes marks this entry as self-made. This does not establish the size of any family assistance.';
  if(p.origin==='unknown')return 'The source does not provide a usable wealth-origin classification.';
  if(p.origin==='family-linked')return 'Forbes does not mark this entry as self-made. A more detailed self-made score is unavailable, so we do not distinguish pure inheritance from growth of a family business.';
  if(p.origin==='inherited')return `Forbes marks this entry as not self-made and reports a self-made score of ${p.forbesSelfMadeScore}/10. The app groups scores 1–2 as inherited.`;
  return `Forbes marks this entry as not self-made and reports a self-made score of ${p.forbesSelfMadeScore}/10. The app groups scores 3–5 as inherited-and-grown; this is a coarse editorial grouping, not an inheritance percentage.`;
}
function renderQuadrants(){
  const pilot=state.lens==='influence';
  $('#quadrant-context').textContent=pilot?`Four equal regions, not four definitive labels. Wealth divider ${money(wealthDivider(state.scale)*1e9)}; editorial spectrum midpoint 50. The gradient is continuous. Read confidence, historical scope and counterevidence in every file.`:'Four equal regions. The horizontal divider is 1% of annual national GDP; this economic comparison is not political influence.';
  $('#quadrant-cards').innerHTML=QUADRANTS[state.lens].map((q,i)=>`<article class="quadrant-card"><h3>${h(q.name)}</h3><p>${h(q.subtitle)}</p><small>${h(q.short.toLowerCase().replace(/^./,c=>c.toUpperCase()).replace(/ · /,', '))}</small></article>`).join('');
}
function renderRubric(a){
  if(a.score==null)return '<p class="case-scope">No numerical estimate: at least one dimension lacks enough reviewed evidence. Unknown is not zero.</p>';
  return `<div class="spectrum-meter" aria-label="Editorial estimate ${a.score} out of 100"><span style="left:${a.score}%"></span></div><p class="case-scope">Plausible editorial range: <strong>${a.range[0]}–${a.range[1]}</strong>. Not a statistical interval or probability of guilt.</p><details class="rubric-details"><summary>How this position was calculated</summary>${Object.entries(DIMENSIONS).map(([k,d])=>`<div class="rubric-row"><strong>${h(d.label)} · ${d.weight*100}%</strong><span>${a.rubric[k].level}/4</span><p>${h(a.rubric[k].rationale)}</p><small>Based on supporting receipt${a.rubric[k].sourceRefs.length===1?'':'s'} ${a.rubric[k].sourceRefs.map(i=>i+1).join(', ')} below; read the counterevidence too.</small></div>`).join('')}<p>Weighted mean × 25, rounded. Levels and range are authored judgments, not measurements or automatic search classifications.</p></details>`;
}
function renderResearchTrail(a){return `<div class="profile-section"><details class="receipt-item"><summary>Source-discovery trail · ${a.discovery.leads.length} candidate links</summary><p>Search performed ${h(a.discovery.searchedAt)}. These are unverified research leads, not evidence used to assign a score. Name matching can be wrong.</p><p class="quiet">Query: ${h(a.discovery.query)}</p>${a.discovery.leads.length?`<ul>${a.discovery.leads.map(l=>`<li><a href="${h(l.url)}" target="_blank" rel="noopener noreferrer">${h(l.title)}</a></li>`).join('')}</ul>`:'<p>No candidate link retained by the name-matching rule. This does not establish absence of influence.</p>'}</details></div>`;}
function toast(message){clearTimeout(toastTimer);$('#toast').textContent=message;$('#toast').hidden=false;toastTimer=setTimeout(()=>{$('#toast').hidden=true;},4200);}
async function share(){
  const hash=serializeState(state);
  history.replaceState(null,'',location.pathname+location.search+(hash?'#'+hash:''));
  try{await navigator.clipboard.writeText(location.href);toast('Your coordinates, copied. Filters and selected profile included.');}
  catch{openDialog('share');}
}
function openDialog(type){
  previousDialogFocus=document.activeElement;
  const cases=Object.values(evidence.profiles).filter(a=>a.fileState==='case-reviewed').length,placed=Object.values(evidence.profiles).filter(a=>a.score!=null).length;
  let content;
  if(type==='share')content=`<h2 id="dialog-title">Send a postcard.</h2><label>Copy this view’s link<input id="share-link" readonly style="width:100%;padding:12px" value="${h(location.href)}"></label>`;
  else if(type==='sources')content=`<h2 id="dialog-title">The receipts, please.</h2><h3>Forbes 2026 · ${data.people.length} launch entries</h3><p>First 200 entries in saved Forbes annual-list order; the full 500-entry source archive is retained. Wealth snapshot: 1 March 2026, not live prices. Family entries and tied ranks retained. <a href="${h(data.meta.forbesUrl)}">Source endpoint</a> · <a href="data/billionaires.json">Local factual extract</a></p><h3>World Bank · 2024</h3><p>GDP, GDP/person, PPP GDP and PPP/person share a common year. ${data.people.filter(p=>footprint(p,data.countries)===null).length} launch entries lack a GDP match; no proxy is invented. <a href="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD">World Development Indicators</a> · CC BY 4.0.</p><h3>Research coverage, honestly</h3><p>The archive contains 500 discovery queries and UK-list name checks. Within the 200-entry launch cohort: <strong>${cases} individually reviewed case files; ${placed} numerical estimates.</strong> Search titles and links are not individually verified. They are never scored automatically. <a href="data/assessments.json">All research records</a> · <a href="data/research-discovery.json">Discovery audit</a></p><p><a href="${h(screening.sourceUrl)}">UK FCDO CSV</a> · ${h(screening.reportDate)} · Crown copyright, Open Government Licence v3. A candidate match is not identity verification, sanctions clearance, or proof of oligarchy.</p><h3>Flag artwork</h3><p>50 local SVGs from <a href="https://github.com/lipis/flag-icons">flag-icons</a>, © Panayiotis Lipiridis, MIT licensed. <a href="assets/flags/LICENSE">License</a> · <a href="assets/flags/provenance.json">Pinned revision and hashes</a>. Citizenship follows Forbes, including territorial entries; it does not assign political allegiance.</p><div class="dialog-callout">Initial AI-assisted editorial research, not independently reviewed. Public launch still requires source-reuse review, independent editorial review and a corrections contact. No third-party rights are sublicensed.</div>`;
  else content=`<h2 id="dialog-title">A spectrum. With receipts.</h2><p><strong>Our definition:</strong> ${h(evidence.definition)}</p><h3>Position is not confidence</h3><p>The vertical axis is a continuous 0–100 editorial estimate of the documented wealth–power relationship. It is <strong>not a probability of guilt, an objective measurement, or a criminal classification</strong>. The background runs from “Just another billionaire” to “Oligarch.” These are directional labels, not certificates of innocence or guilt.</p><h3>Published rubric</h3><ul><li><strong>Political leverage — 25%:</strong> access, institutional power, or organized policy influence.</li><li><strong>Preferential economic benefit — 25%:</strong> a specific advantage linked to public power, not simply a public contract or business success.</li><li><strong>Wealth–power feedback — 50%:</strong> evidence that private resources and political advantage reinforce each other.</li></ul><p>Each dimension is authored on a 0–4 scale: 0 = reviewed evidence against the mechanism within the stated scope; 1 = contextual or weak connection; 2 = specific but contested or incomplete link; 3 = substantial institutional, scholarly or corroborated support; 4 = unusually strong direct or adjudicated support for that dimension. These are editorial anchors, not mechanically equivalent facts across countries.</p><code>Index = round(25 × (0.25 × leverage + 0.25 × benefit + 0.50 × feedback))</code><p>Every estimate exposes its three levels, rationale, supporting receipt references, qualitative confidence, plausible editorial range and counterevidence. The range is not statistical. Historical episodes are labeled and do not establish ongoing 2026 conduct. Small score differences should not be treated as meaningful ranks.</p><h3>Unknown never means ordinary</h3><p>If a dimension has not been adequately reviewed, its value is null and <strong>no position is assigned</strong>—not zero, not a random score, and not the midpoint. The launch cohort is the first 200 Forbes entries, not a handpicked set of scored people. Within it, ${cases} files have individual case reviews and ${placed} have estimates. The rest remain accessible in the unplaced list, table, search and profiles. A search or sanctions check is not a completed assessment.</p><h3>Equal quadrants, explicit scales</h3><p>Both dividers bisect the plotting rectangle exactly. The default wealth axis is logarithmic from $2.5B to $1T, putting $50B exactly at the center. Linear mode runs $0–$1T and changes the wealth divider to $500B; labels and quadrant assignment follow that mode. The spectrum midpoint is 50. Names describe regions, not four hard personal verdicts. Points use their exact values without jitter; overlapping entries are available in the profile and table.</p><h3>Economic lens</h3><p>Fortune in USD ÷ 2024 GDP in USD × 100. The log GDP axis runs 0.001%–1,000%, centered on 1%. This is a stock-to-flow comparison, not GDP owned or political power. PPP stays in international dollars; citizenship does not locate every asset. Missing GDP stays missing.</p><h3>What does not count automatically</h3><p>Nationality, inherited wealth, family relationships, company size, political donations, media ownership, public office, contracts or sanctions alone do not determine the estimate. Relatives do not inherit personal conduct. Company-level findings are not automatically personal liability.</p><h3>Origins, sources and corrections</h3><p>Self-made is Forbes’ flag, not a claim of no advantages. Non-self-made scores 1–2 are grouped as inherited, 3–5 as inherited-and-grown; absent detail stays family-linked, unspecified. Source availability and languages create uneven coverage. Before public launch, establish an independent editorial review and a corrections contact. A correction should identify the person, disputed claim, source and date. The old binary categories and four-signal point count are retired.</p>`;
  $('#dialog-content').innerHTML=content;$('#info-dialog').showModal();if(type==='share')$('#share-link').select();
}
function dotColor(p){return state.color==='flag'?`url(#flag-${p.iso})`:state.color==='continent'?CONTINENTS[p.continent]:ORIGINS[p.origin].color;}
function renderOverview(){
  const records=Object.values(evidence.profiles),reviewed=records.filter(a=>a.fileState==='case-reviewed').length,placed=records.filter(a=>a.score!=null).length;
  $('#assessment-overview').innerHTML=`<p>Height on the chart is a reviewed estimate of how a fortune and public power feed each other. ${placed} of ${data.people.length} have enough evidence to be placed. The other ${data.people.length-placed} are not scored, which does not mean they are clean. <button class="text-button" data-dialog="methodology">How the estimate works</button></p><div class="research-progress"><button data-assessment="all">All ${data.people.length}</button><button data-assessment="placed">Positioned (${placed})</button><button data-assessment="unplaced">Evidence needed (${data.people.length-placed})</button></div>`;
  for(const b of $$('#assessment-overview [data-assessment]'))b.setAttribute('aria-pressed',String(b.dataset.assessment===state.assessment));
  $('#likely-shortlist').innerHTML=`<span>Start with</span>${['elon-musk','charles-koch','aliko-dangote','jay-y-lee','gautam-adani-1','alisher-usmanov'].map(id=>{const p=data.people.find(p=>p.id===id);return `<button data-case="${h(id)}"><img src="assets/flags/${p.iso.toLowerCase()}.svg" width="16" height="16" alt=""> ${h(p.name.replace(' & family',''))}</button>`;}).join('')}`;
  for(const b of $$('[data-case]'))b.addEventListener('click',()=>{state={...DEFAULTS,selected:b.dataset.case};render();$('#profile').focus({preventScroll:true});$('#explorer').scrollIntoView({behavior:'auto'});});
}
boot();

function heroMap(){
  const svg=$('#hero-map');if(!svg)return;
  const ties=mergeTies(data.people,[]),L=layout(data.people,ties,'wealth'),b=L.bounds;
  const pad=24,w=b.x1-b.x0+pad*2,hh=b.y1-b.y0+pad*2;
  svg.setAttribute('viewBox',`${b.x0-pad} ${b.y0-pad} ${w} ${hh}`);
  const likely=id=>evidence.profiles[id]?.status==='likely';
  svg.innerHTML=data.people.map(p=>{const n=L.nodes[p.id];return `<path transform="translate(${n.x.toFixed(1)} ${n.y.toFixed(1)})" d="${coastline(p.id,isleRadius(p.wealth),.26)}" class="${likely(p.id)?'hero-isle hero-likely':'hero-isle'}"/>`;}).join('');
}
