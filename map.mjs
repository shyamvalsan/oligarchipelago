import {launchUniverse} from './lib/universe.mjs';
import {ASSESSMENTS,CONTINENTS,assessment,money,escapeHTML as h} from './lib/model.mjs';
import {MODES,radius,layout,mergeTies,coastline,hills,hash,rng,neighbours} from './lib/archipelago.mjs';

const $=s=>document.querySelector(s);
const SVGNS='http://www.w3.org/2000/svg';
const el=(tag,attrs={},parent)=>{const n=document.createElementNS(SVGNS,tag);for(const [k,v] of Object.entries(attrs))n.setAttribute(k,v);if(parent)parent.append(n);return n;};
const KIND={
  family:{label:'Family',color:'#a8432d'},
  'marriage-or-divorce':{label:'Marriage / divorce',color:'#bf5f94'},
  'co-founder':{label:'Co-founders',color:'#c28a1b'},
  'business-partner':{label:'Business partners',color:'#2d7775'},
  'co-owner':{label:'Co-owners',color:'#2d7775'},
  investor:{label:'Investor',color:'#6a5aa8'},
  board:{label:'Board / governance',color:'#6a5aa8'},
  'shared-fortune':{label:'Same named company in Forbes’ source of wealth',color:'#7d7360'},
};
const kindOf=t=>KIND[t.kind]||{label:t.kind,color:'#7d7360'};
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;

let people,evidence,ties,byId,rank,layouts={},pos={},mode='wealth',selected='',view,home,bounds;
let nodes={},labelEls={},routeEls=[],regionLayer,flagsOn=true,tiesOn=true,labelsOn=true,anim=0;
const svg=$('#map');

async function boot(){
  try{
    const urls=['data/billionaires.json','data/assessments.json'];
    const rs=await Promise.all([...urls.map(u=>fetch(u)),fetch('data/ties.json').catch(()=>null)]);
    if(!rs[0].ok||!rs[1].ok)throw new Error('data');
    let data,ev;[data,ev]=await Promise.all([rs[0].json(),rs[1].json()]);
    ({data,evidence}=launchUniverse(data,ev));
    people=data.people;
    const documented=rs[2]&&rs[2].ok?(await rs[2].json()).ties||[]:[];
    ties=mergeTies(people,documented);
    byId=Object.fromEntries(people.map(p=>[p.id,p]));
    rank=Object.fromEntries(people.map((p,i)=>[p.id,i]));
    const params=new URLSearchParams(location.hash.replace(/^#/,''));
    if(MODES[params.get('mode')])mode=params.get('mode');
    layouts[mode]=layout(people,ties,mode);
    pos=Object.fromEntries(Object.entries(layouts[mode].nodes).map(([id,n])=>[id,{x:n.x,y:n.y}]));
    bounds=layouts[mode].bounds;
    draw();buildControls();
    fit(false);
    const sel=params.get('id');
    if(sel&&byId[sel])select(sel,true);else renderPanel();
    $('#loading').hidden=true;
  }catch(e){
    console.error(e);
    $('#loading').innerHTML='The chart could not load its data. Try reloading, or open the <a href="./">atlas</a>.';
  }
}

// ---------- drawing ----------
function draw(){
  svg.replaceChildren();
  const defs=el('defs',{},svg);
  const paper=el('filter',{id:'paper',x:'0',y:'0',width:'100%',height:'100%'},defs);
  el('feTurbulence',{type:'fractalNoise',baseFrequency:'.9',numOctaves:'2',seed:'7',result:'n'},paper);
  el('feColorMatrix',{in:'n',type:'matrix',values:'0 0 0 0 .35  0 0 0 0 .26  0 0 0 0 .14  0 0 0 .09 0'},paper);
  const vg=el('radialGradient',{id:'vig',cx:'50%',cy:'50%',r:'75%'},defs);
  el('stop',{offset:'55%','stop-color':'#efe2c0'},vg);el('stop',{offset:'100%','stop-color':'#d6bf8a'},vg);
  const X0=-5000,Y0=-3500,W=13000,H=9000;
  el('rect',{x:X0,y:Y0,width:W,height:H,fill:'url(#vig)'},svg);
  el('rect',{x:X0,y:Y0,width:W,height:H,filter:'url(#paper)'},svg);
  const gWaves=el('g',{'aria-hidden':'true'},svg);
  regionLayer=el('g',{'aria-hidden':'true'},svg);
  const gDeco=el('g',{'aria-hidden':'true'},svg);
  const gRoutes=el('g',{},svg),gIsles=el('g',{},svg),gLabels=el('g',{'aria-hidden':'true'},svg);

  const rand=rng(hash('waves'));
  for(let i=0;i<1100;i++){
    const x=-1300+rand()*5200,y=-900+rand()*3600;
    if(people.some(p=>{const q=pos[p.id];return Math.hypot(q.x-x,q.y-y)<radius(p.wealth)*1.5+34;}))continue;
    const s=9+rand()*10;
    el('path',{class:'sea-wave',d:`M${x-s} ${y}q${s/2} ${-s/1.6} ${s} 0t${s} 0`},gWaves);
  }
  decorate(gDeco);

  routeEls=ties.map((t,i)=>{
    const g=el('g',{},gRoutes),c=kindOf(t).color;
    const p=el('path',{class:'route'+(t.derived?' derived':''),stroke:c},g);
    const hit=el('path',{class:'route-hit'},g);
    hit.addEventListener('pointerenter',e=>tip(e,`${nameOf(t.a)} ↔ ${nameOf(t.b)}: ${t.label}`));
    hit.addEventListener('pointermove',e=>tip(e));
    hit.addEventListener('pointerleave',()=>tip());
    return {t,p,hit,g,bulge:(hash(t.a+t.b)%2?1:-1)*(.1+(hash(t.b+t.a)%7)/70)};
  });

  for(const p of people){
    const r=radius(p.wealth),a=assessment(p,evidence),c=CONTINENTS[p.continent]||'#8d9990';
    const g=el('g',{class:'isle',tabindex:'0',role:'button','aria-label':`${p.name}, ${money(p.wealth*1e9)}, ${p.country}${a.status&&a.status!=='unassessed'?`, ${ASSESSMENTS[a.status].short}`:''}`,'data-id':p.id},gIsles);
    el('path',{class:'shallows',d:coastline(p.id,r*1.3,.2)},g);
    el('path',{class:'shore',d:coastline(p.id,r*1.1,.24)},g);
    el('path',{class:'land',d:coastline(p.id,r,.26),style:`fill:color-mix(in srgb,${c} 52%,#e9dcae)`},g);
    for(const hl of hills(p.id,r))el('path',{class:'hill',d:`M${hl.x-hl.s} ${hl.y+hl.s*.6}L${hl.x} ${hl.y-hl.s}L${hl.x+hl.s} ${hl.y+hl.s*.6}`},g);
    const fl=el('g',{class:'flag'},g),k=Math.min(1.7,.8+r/60),st=ASSESSMENTS[a.status]||ASSESSMENTS.unassessed;
    const fy=-r*.25;
    el('path',{d:`M0 ${fy}V${fy-30*k}`,stroke:'#3a2d20','stroke-width':1.8,fill:'none'},fl);
    el('path',{d:`M0 ${fy-30*k}l${20*k} ${6*k}-${20*k} ${7*k}z`,fill:a.status==='unassessed'||!a.status?'#efe2c0':st.color,stroke:'#3a2d20','stroke-width':1.1},fl);
    g.addEventListener('click',()=>select(p.id));
    g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();select(p.id);}});
    g.addEventListener('pointerenter',e=>{tip(e,`${p.name} · ${money(p.wealth*1e9)} · ${p.country}`);hover(p.id);});
    g.addEventListener('pointermove',e=>tip(e));
    g.addEventListener('pointerleave',()=>{tip();hover('');});
    g.addEventListener('focus',()=>hover(p.id));g.addEventListener('blur',()=>hover(''));
    const lab=el('text',{class:'label'},gLabels);lab.textContent=p.name.replace(/ & family$/,'');
    nodes[p.id]=g;labelEls[p.id]=lab;
  }
  placeAll();
  svg.addEventListener('click',e=>{if(!e.target.closest('.isle')&&!moved)select('');});
}

function decorate(g){
  const b=bounds,cx=b.x1+120,cy=b.y1-70;
  // compass rose
  const c=el('g',{transform:`translate(${cx} ${cy})`},g);
  const pts=[];for(let i=0;i<16;i++){const a=i*Math.PI/8-Math.PI/2,r=i%4===0?120:i%2===0?72:38;pts.push([Math.cos(a)*r,Math.sin(a)*r]);pts.push([Math.cos(a+Math.PI/16)*18,Math.sin(a+Math.PI/16)*18]);}
  el('circle',{class:'deco',r:92,'stroke-dasharray':'2 5'},c);el('circle',{class:'deco',r:132},c);
  el('polygon',{class:'deco deco-fill',points:pts.map(p=>p.join(',')).join(' ')},c);
  const n=el('text',{x:0,y:-146,'text-anchor':'middle','font-family':'Georgia,serif','font-size':36,'font-style':'italic','font-weight':700,fill:'#3a2d20'},c);n.textContent='N';
  const ct=el('text',{x:0,y:178,'text-anchor':'middle','font-family':'Georgia,serif','font-size':17,'font-style':'italic',fill:'#6b5841'},c);ct.textContent='Magnetic north of money';
  // sea serpent
  const s=el('g',{transform:`translate(${b.x0-60} ${b.y1+30}) scale(1.6)`},g);
  el('path',{class:'deco deco-fill',d:'M0 0q10-34 22 0t22 0t22 0t22 0'},s);
  el('path',{class:'deco deco-fill',d:'M88 0q0-26 14-30q8-3 12 4l-7 4q-6-2-10 4q-3 8-1 18z'},s);
  el('circle',{cx:105,cy:-25,r:1.8,fill:'#3a2d20'},s);
  el('path',{class:'deco',d:'M-12 8q8-6 14 0t14 0t14 0t14 0t14 0t14 0t14 0'},s);
  // ship
  const sh=el('g',{transform:`translate(${b.x1-40} ${b.y0-90}) scale(1.7)`},g);
  el('path',{class:'deco deco-fill',d:'M-34 0h68l-12 17h-44z'},sh);el('path',{class:'deco',d:'M0 0V-52M0 -50l26 36h-26M0 -46l-20 30h20M0 -52l14 5-14 5'},sh);
  el('path',{class:'deco',d:'M-44 24q8-6 15 0t15 0t15 0t15 0t15 0t15 0'},sh);
  // hand-lettered legend line
  const t=el('text',{x:b.x0-20,y:b.y0-60,'font-family':'Georgia,serif','font-style':'italic','font-size':30,fill:'#6b5841',opacity:.8},g);
  t.textContent='Here be dragons — and dividends.';
}

// ---------- layout / animation ----------
function placeAll(){
  for(const p of people){
    const q=pos[p.id],r=radius(p.wealth);
    nodes[p.id].setAttribute('transform',`translate(${q.x.toFixed(1)} ${q.y.toFixed(1)})`);
    labelEls[p.id].setAttribute('x',q.x.toFixed(1));labelEls[p.id].setAttribute('y',(q.y+r*.86+15).toFixed(1));
  }
  for(const r of routeEls){
    const a=pos[r.t.a],b=pos[r.t.b],ra=radius(byId[r.t.a].wealth),rb=radius(byId[r.t.b].wealth);
    const dx=b.x-a.x,dy=b.y-a.y,d=Math.hypot(dx,dy)||1,ux=dx/d,uy=dy/d;
    const sx=a.x+ux*ra*.95,sy=a.y+uy*ra*.95,ex=b.x-ux*rb*.95,ey=b.y-uy*rb*.95;
    const mx=(sx+ex)/2-uy*d*r.bulge,my=(sy+ey)/2+ux*d*r.bulge;
    const dstr=`M${sx.toFixed(1)} ${sy.toFixed(1)}Q${mx.toFixed(1)} ${my.toFixed(1)} ${ex.toFixed(1)} ${ey.toFixed(1)}`;
    r.p.setAttribute('d',dstr);r.hit.setAttribute('d',dstr);
  }
  drawRegions();updateLabels();
}

function drawRegions(){
  regionLayer.replaceChildren();
  if(mode==='wealth')return;
  const key=mode==='country'?p=>p.country:p=>p.industry,groups=new Map();
  for(const p of people){const k=key(p);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(p);}
  for(const [k,list] of groups){
    if(list.length<(mode==='country'?3:4))continue;
    let x=0,top=Infinity;for(const p of list){x+=pos[p.id].x;top=Math.min(top,pos[p.id].y-radius(p.wealth));}
    const t=el('text',{class:'region',x:x/list.length,y:top-46},regionLayer);t.textContent=k;
  }
}

function go(next){
  if(next===mode)return;
  mode=next;
  layouts[mode]??=layout(people,ties,mode);
  const from={...Object.fromEntries(Object.entries(pos).map(([k,v])=>[k,{...v}]))},to=layouts[mode].nodes;
  const t0=performance.now(),dur=reduceMotion?1:1100;
  cancelAnimationFrame(anim);
  const step=now=>{
    const t=Math.min(1,(now-t0)/dur),e=t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;
    for(const id in to)pos[id]={x:from[id].x+(to[id].x-from[id].x)*e,y:from[id].y+(to[id].y-from[id].y)*e};
    placeAll();
    if(t<1)anim=requestAnimationFrame(step);else{bounds=layouts[mode].bounds;fit(!selected);if(selected)select(selected);}
  };
  anim=requestAnimationFrame(step);
  syncHash();
  document.querySelectorAll('#modes button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===mode)));
}

// ---------- view (pan / zoom) ----------
function size(){return {w:svg.clientWidth||innerWidth,h:svg.clientHeight||innerHeight};}
function applyView(){
  const {w,h:hh}=size(),vw=view.w,vh=vw*hh/w;
  svg.setAttribute('viewBox',`${view.cx-vw/2} ${view.cy-vh/2} ${vw} ${vh}`);
  updateLabels();
}
function fit(animate){
  const {w,h:hh}=size(),pad=330,bw=bounds.x1-bounds.x0+pad*2,bh=bounds.y1-bounds.y0+pad*2;
  const target={cx:(bounds.x0+bounds.x1)/2,cy:(bounds.y0+bounds.y1)/2,w:Math.max(bw,bh*w/hh)};
  home=target;
  if(animate&&view)flyTo(target);else{view={...target};applyView();}
}
let flight=0;
function flyTo(t,dur=650){
  cancelAnimationFrame(flight);
  const f={...view},t0=performance.now(),d=reduceMotion?1:dur;
  const step=now=>{const k=Math.min(1,(now-t0)/d),e=1-Math.pow(1-k,3);view={cx:f.cx+(t.cx-f.cx)*e,cy:f.cy+(t.cy-f.cy)*e,w:f.w+(t.w-f.w)*e};applyView();if(k<1)flight=requestAnimationFrame(step);};
  flight=requestAnimationFrame(step);
}
function zoomAt(factor,clientX,clientY){
  const r=svg.getBoundingClientRect(),{w,h:hh}=size(),vw=view.w,vh=vw*hh/w;
  const fx=(clientX-r.left)/r.width,fy=(clientY-r.top)/r.height;
  const px=view.cx-vw/2+fx*vw,py=view.cy-vh/2+fy*vh;
  const nw=Math.min(home.w*1.6,Math.max(260,vw*factor)),nh=nw*hh/w;
  view={w:nw,cx:px-fx*nw+nw/2,cy:py-fy*nh+nh/2};applyView();
}
let moved=false;
function wirePanZoom(){
  const pts=new Map();let last=null,pinch=0;
  svg.addEventListener('pointerdown',e=>{pts.set(e.pointerId,{x:e.clientX,y:e.clientY});last={x:e.clientX,y:e.clientY};moved=false;if(pts.size===2)pinch=dist();});
  const dist=()=>{const [a,b]=[...pts.values()];return Math.hypot(a.x-b.x,a.y-b.y);};
  svg.addEventListener('pointermove',e=>{
    if(!pts.has(e.pointerId))return;
    pts.set(e.pointerId,{x:e.clientX,y:e.clientY});
    if(pts.size===2){const d=dist(),[a,b]=[...pts.values()];if(pinch)zoomAt(pinch/d,(a.x+b.x)/2,(a.y+b.y)/2);pinch=d;moved=true;return;}
    const dx=e.clientX-last.x,dy=e.clientY-last.y;
    if(!moved&&Math.hypot(dx,dy)<4)return;
    if(!moved){moved=true;svg.classList.add('drag');}
    const scale=view.w/size().w;view.cx-=dx*scale;view.cy-=dy*scale;last={x:e.clientX,y:e.clientY};applyView();
  });
  const up=e=>{pts.delete(e.pointerId);pinch=0;svg.classList.remove('drag');last=pts.size?[...pts.values()][0]:null;setTimeout(()=>moved=false,0);};
  svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);
  svg.addEventListener('wheel',e=>{e.preventDefault();zoomAt(Math.exp(e.deltaY*.0015),e.clientX,e.clientY);},{passive:false});
  $('#zin').onclick=()=>zoomAt(.7,innerWidth/2,innerHeight/2);
  $('#zout').onclick=()=>zoomAt(1.4,innerWidth/2,innerHeight/2);
  $('#zreset').onclick=()=>flyTo(home);
  addEventListener('resize',()=>{fit(false);});
}

function updateLabels(){
  if(!view)return;
  const px=size().w/view.w;
  for(const p of people){
    const r=radius(p.wealth),show=p.id===selected||(labelsOn&&(rank[p.id]<14||r*px>=19||px>.9));
    labelEls[p.id].style.display=show?'':'none';
    labelEls[p.id].style.fontSize=Math.max(9,Math.min(70,13.5/px))+'px';labelEls[p.id].style.strokeWidth=Math.max(3,4/px)+'px';
  }
}

// ---------- interaction ----------
function nameOf(id){return byId[id].name.replace(/ & family$/,'');}
function tip(e,text){
  const t=$('#tip');
  if(!e||(!text&&t.hidden)){t.hidden=true;return;}
  if(text){t.textContent=text;t.hidden=false;}
  t.style.left=Math.min(innerWidth-280,e.clientX+14)+'px';t.style.top=(e.clientY+16)+'px';
}
function hover(id){
  if(selected)return;
  highlight(id);
}
function highlight(id){
  const linked=new Set([id]);
  if(id)for(const n of neighbours(ties,id))linked.add(n.other);
  for(const p of people)nodes[p.id].classList.toggle('dim',!!id&&!linked.has(p.id));
  for(const r of routeEls){const on=!id||r.t.a===id||r.t.b===id;r.p.classList.toggle('dim',!on);r.p.classList.toggle('hot',!!id&&on);}
}
function select(id,instant){
  selected=id;
  for(const [k,n] of Object.entries(nodes))n.classList.toggle('sel',k===id);
  highlight(id);syncHash();renderPanel();updateLabels();
  if(id){
    const q=pos[id],near=[id,...neighbours(ties,id).map(n=>n.other)];
    const xs=near.map(k=>pos[k].x),ys=near.map(k=>pos[k].y);
    const w=Math.max(900,(Math.max(...xs)-Math.min(...xs))+520);
    const t={cx:near.length>1?(Math.max(...xs)+Math.min(...xs))/2:q.x,cy:near.length>1?(Math.max(...ys)+Math.min(...ys))/2:q.y,w:Math.min(w,home.w)};
    if(innerWidth>900)t.cx+=t.w*.12;else t.cy+=t.w*size().h/size().w*.2;
    instant?(view=t,applyView()):flyTo(t);
  }
}
function syncHash(){
  const p=new URLSearchParams();if(selected)p.set('id',selected);if(mode!=='wealth')p.set('mode',mode);
  history.replaceState(null,'',p.toString()?'#'+p:location.pathname+location.search);
}

function renderPanel(){
  const pn=$('#panel');
  if(!selected){
    pn.className='panel empty';
    pn.innerHTML='Click an island to read the receipts. Drag to sail, scroll to zoom.';
    return;
  }
  pn.className='panel';
  const p=byId[selected],a=assessment(p,evidence),st=ASSESSMENTS[a.status]||ASSESSMENTS.unassessed;
  const nb=neighbours(ties,selected).sort((x,y)=>(x.tie.derived?1:0)-(y.tie.derived?1:0)||rank[x.other]-rank[y.other]);
  const scored=Number.isFinite(a.score);
  pn.innerHTML=`<button class="close" aria-label="Close panel" data-close>×</button>
  <p class="meta">Forbes rank ${p.rank}, ${h(p.country)}</p>
  <h2>${h(p.name)}</h2><p class="meta">${h(p.sourceOfWealth)} · ${h(p.industry)}</p>
  <div class="big">${money(p.wealth*1e9)}</div>
  <dl><dt>Fortune</dt><dd>${h(({'self-made':'Self-made (Forbes)',inherited:'Inherited',mixed:'Inherited & grown','family-linked':'Family-linked'})[p.origin]||'Unknown')}</dd><dt>Age</dt><dd>${p.age??'—'}</dd>
  <dt>Flag</dt><dd><span class="badge" style="background:${st.color}">${h(st.short)}</span></dd>
  ${scored?`<dt>Spectrum</dt><dd>${a.score}/100 (plausible ${a.range[0]}–${a.range[1]})</dd>`:`<dt>Spectrum</dt><dd>Not placed — evidence still needed</dd>`}</dl>
  ${a.summary?`<p class="note" style="font-size:12px;color:inherit">${h(a.summary)}</p>`:''}
  <h3>Sea routes (${nb.length})</h3>
  ${nb.length?`<ul class="ties">${nb.map(({other,tie})=>`<li style="--c:${kindOf(tie).color}"><button data-id="${h(other)}">${h(nameOf(other))}</button><small>${h(kindOf(tie).label)}${tie.date&&!tie.derived?` · ${h(String(tie.date))}`:''}</small><small>${h(tie.label)}${tie.url?` — <a href="${h(tie.url)}" target="_blank" rel="noopener noreferrer">${h(tie.source||'source')}</a>`:''}</small></li>`).join('')}</ul>`:'<p class="note">No documented ties on file. That means none have been recorded here, not that none exist.</p>'}
  <a class="link" href="./#selected=${encodeURIComponent(p.id)}&lens=influence">Open the evidence in the atlas</a>
  <p class="note">Flags are editorial judgments, not legal findings. Island position is arranged for legibility; distance is not a measurement.</p>`;
  pn.querySelector('[data-close]').onclick=()=>{select('');svg.focus();};
  pn.querySelectorAll('button[data-id]').forEach(b=>b.onclick=()=>select(b.dataset.id));
}

function buildControls(){
  $('#modes').innerHTML=Object.entries(MODES).map(([k,m])=>`<button data-mode="${k}" aria-pressed="${k===mode}" title="${h(m.note)}">${h(m.label)}</button>`).join('');
  $('#modes').addEventListener('click',e=>{const b=e.target.closest('button');if(b)go(b.dataset.mode);});
  $('#names').innerHTML=people.map(p=>`<option value="${h(nameOf(p.id))}">`).join('');
  $('#find').addEventListener('change',e=>{
    const q=e.target.value.trim().toLowerCase();if(!q)return;
    const m=people.find(p=>nameOf(p.id).toLowerCase()===q)||people.find(p=>p.name.toLowerCase().includes(q));
    if(m){select(m.id);e.target.value='';}
  });
  $('#t-flags').onchange=e=>{flagsOn=e.target.checked;document.querySelectorAll('.flag').forEach(f=>f.style.display=flagsOn?'':'none');};
  $('#t-ties').onchange=e=>{tiesOn=e.target.checked;for(const r of routeEls)r.g.style.display=tiesOn?'':'none';};
  $('#t-labels').onchange=e=>{labelsOn=e.target.checked;updateLabels();};
  addEventListener('keydown',e=>{if(e.key==='Escape'&&selected){select('');}});
  const swatch=c=>`<svg width="26" height="6" aria-hidden="true"><path d="M0 3h26" stroke="${c}" stroke-width="2.4" stroke-dasharray="7 4"/></svg>`;
  const flag=c=>`<svg width="16" height="16" aria-hidden="true"><path d="M3 15V2" stroke="#3a2d20" stroke-width="1.6"/><path d="M3 2l11 3-11 4z" fill="${c}" stroke="#3a2d20"/></svg>`;
  $('#legend').innerHTML=`<h2>Key</h2><ul>
    <li>${flag(ASSESSMENTS.likely.color)} Likely oligarch</li><li>${flag(ASSESSMENTS.mixed.color)} Mixed / disputed</li><li>${flag(ASSESSMENTS['no-strong'].color)} No strong evidence found*</li></ul>
    <ul><li>${swatch('#a8432d')} Family, marriage</li><li>${swatch('#c28a1b')} Co-founders</li><li>${swatch('#2d7775')} Partners, co-owners</li><li>${swatch('#6a5aa8')} Investors, boards</li><li>${swatch('#7d7360')} Same company in Forbes’ field</li></ul>
    <p>Island size = net worth (Forbes, 1 Mar 2026). Colour = continent. *Not an exoneration. Routes show only ties we have recorded with a source.</p>`;
  wirePanZoom();
}

boot();
