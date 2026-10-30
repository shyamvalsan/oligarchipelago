import {scoreRubric,wealthPosition,wealthDivider,plotGeometry} from '../lib/spectrum.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {DEFAULTS,ASSESSMENTS,assessment,coverage,filterPeople,footprint,influence,surprisePool,metric,quadrant,matchesRange,sortPeople,parseState,serializeState,money,percent,escapeHTML,csvCell,exportCsv} from '../lib/model.mjs';

const data=JSON.parse(await readFile(new URL('../data/billionaires.json',import.meta.url),'utf8'));
const evidence=JSON.parse(await readFile(new URL('../data/assessments.json',import.meta.url),'utf8'));
const {people,countries}=data;
const p=people[0];

test('Forbes snapshot has 500 unique ordered entries, ranks and snapshot date',()=>{
  assert.equal(people.length,500);assert.equal(new Set(people.map(p=>p.id)).size,500);
  assert.equal(data.meta.wealthDate,'2026-03-01');
  assert.equal(p.name,'Elon Musk');assert.equal(p.wealth,839);
  for(let i=0;i<499;i++)assert.ok(people[i].wealth>=people[i+1].wealth);
  for(const p of people){assert.ok(countries[p.country]);assert.ok(p.wealth>0);assert.ok(p.rank<=500);assert.ok(Number.isInteger(p.position));assert.ok(new URL(p.profileUrl).hostname==='www.forbes.com');}
});
test('GDP observations are positive, explicitly 2024, with sources',()=>{
  for(const c of Object.values(countries))for(const key of ['gdp','gdpPerCapita','gdpPpp','gdpPerCapitaPpp'])if(c[key]){
    assert.equal(c[key].year,2024);assert.ok(c[key].value>0);assert.ok(c[key].url.startsWith('https://data.worldbank.org/'));
  }
});
test('footprint converts billions to dollars exactly and never imputes missing GDP',()=>{
  assert.equal(footprint({country:'X',wealth:10},{X:{gdp:{value:1e12}}}),1);
  assert.equal(footprint(p,{}),null);
  assert.equal(footprint({country:'Taiwan',wealth:10},countries),null);
  assert.equal(footprint({country:'X',wealth:10},{X:{gdp:{value:0}}}),null);
});
test('influence unknowns do not turn into a zero score',()=>{
  assert.equal(influence({id:'not-researched'},evidence),null);
  assert.equal(influence(p,evidence),63);assert.equal(assessment({id:'not-researched'},evidence).status,'unassessed');
  assert.equal(metric({id:'not-researched'}, {...DEFAULTS,lens:'influence'},countries,evidence),null);
});
test('case files require support, counterevidence, confidence, dates and known people',()=>{
  for(const[id,r]of Object.entries(evidence.profiles).filter(([,r])=>r.fileState==='case-reviewed')){
    assert.ok(people.some(p=>p.id===id));assert.ok(r.status in ASSESSMENTS);
    assert.ok(r.confidence);assert.ok(r.period);assert.ok(r.limitations);assert.ok(['2026-10-08','2026-10-29','2026-10-30'].includes(r.reviewedAt));
    assert.ok(r.support.length);assert.ok(r.counter.length);
    for(const item of [...r.support,...r.counter]){assert.ok(item.text.length>30);assert.ok(item.date);assert.ok(item.kind);assert.ok(item.source);assert.equal(new URL(item.url).protocol,'https:');}
  }
});
test('500 discovery records remain distinct from 219 case reviews and 64 estimates',()=>{
  assert.equal(Object.keys(evidence.profiles).length,500);
  assert.equal(Object.values(evidence.profiles).filter(r=>r.fileState==='case-reviewed').length,219);
  assert.equal(Object.values(evidence.profiles).filter(r=>r.score!==null).length,64);
  const placed=filterPeople(people,{...DEFAULTS,assessment:'placed'},countries,evidence);
  const unplaced=filterPeople(people,{...DEFAULTS,assessment:'unplaced'},countries,evidence);
  assert.equal(placed.length,64);assert.equal(unplaced.length,436);
  assert.equal(new Set([...placed,...unplaced].map(p=>p.id)).size,500);
  for(const p of people){const a=assessment(p,evidence);assert.ok(a.discovery.query.includes(p.name.replace(' & family','')));assert.equal(a.discovery.status,'discovery-only-not-reviewed');
    if(a.fileState==='discovery-only'){assert.equal(a.reviewedAt,null);assert.equal(a.score,null);assert.equal(a.range,null);}
  }
});
test('every estimate matches the published rubric and includes an editorial range',()=>{
  for(const a of Object.values(evidence.profiles)){
    assert.equal(a.score,scoreRubric(a.rubric));
    if(a.score!==null){assert.ok(a.range[0]<=a.score&&a.range[1]>=a.score);assert.ok(a.range[0]>=0&&a.range[1]<=100);
      for(const d of Object.values(a.rubric)){assert.ok(d.rationale.length>20);assert.ok(d.sourceRefs.length);for(const ref of d.sourceRefs)assert.ok(a.support[ref]);}
    }
  }
  assert.equal(scoreRubric({}),null);assert.equal(scoreRubric({leverage:{level:0},benefit:{level:0},exchange:{level:0}}),0);
  assert.equal(scoreRubric({leverage:{level:null},benefit:{level:0},exchange:{level:0}}),null);
});
test('equal quadrants and centered dividers hold in every viewport and axis mode',()=>{
  for(const mobile of [false,true]){const g=plotGeometry(mobile);assert.equal(g.cx-g.L,g.R-g.cx);assert.equal(g.cy-g.T,g.B-g.cy);}
  assert.equal(wealthPosition(50),.5);assert.equal(wealthPosition(2.5),0);assert.equal(wealthPosition(1000),1);
  assert.equal(wealthPosition(500,'linear'),.5);assert.equal(wealthDivider('linear'),500);
  assert.equal(quadrant({wealth:500},50,'influence','linear').id,'high-high');
});
test('all citizenship flags exist locally with retained license and hashes',async()=>{
  const {createHash}=await import('node:crypto');const manifest=JSON.parse(await readFile(new URL('../assets/flags/provenance.json',import.meta.url),'utf8'));
  assert.equal(manifest.license,'MIT');
  for(const iso of new Set(people.map(p=>p.iso))){const name=iso.toLowerCase()+'.svg';const raw=await readFile(new URL('../assets/flags/'+name,import.meta.url));assert.ok(raw.toString().includes('<svg'));assert.equal(createHash('sha256').update(raw).digest('hex'),manifest.files[name]);}
  assert.ok((await readFile(new URL('../assets/flags/LICENSE',import.meta.url),'utf8')).includes('Permission'));
});
test('screening is separate from case classification and preserves ambiguity',async()=>{
  const screen=JSON.parse(await readFile(new URL('../data/screening.json',import.meta.url),'utf8'));
  assert.equal(screen.screenedCount,500);assert.equal(Object.keys(screen.profiles).length,500);
  assert.equal(screen.profiles['andrei-guryev-family'].matches.length,2);
  assert.equal(assessment({id:'andrei-guryev-family'},evidence).status,'unassessed');
  assert.equal(screen.profiles['jay-y-lee'].status,'no-name-match');assert.equal(assessment({id:'jay-y-lee'},evidence).status,'likely');
});
test('material case updates and narrow negative scope are retained',()=>{
  assert.ok(JSON.stringify(evidence.profiles['gautam-adani-1']).includes('2026-08-10'));
  assert.ok(JSON.stringify(evidence.profiles['jay-y-lee']).includes('pardoned'));
  assert.ok(JSON.stringify(evidence.profiles['mikhail-fridman']).includes('2022–March 2023'));
  for(const a of Object.values(evidence.profiles).filter(a=>a.status==='no-strong'))assert.match(a.limitations,/comprehensive|exoneration|absence/i);
});
test('quadrants use fixed thresholds, with equality in the higher category',()=>{
  assert.equal(quadrant({wealth:49},.99,'footprint').id,'low-low');
  assert.equal(quadrant({wealth:50},1,'footprint').id,'high-high');
  assert.equal(quadrant({wealth:20},50,'influence').id,'low-high');
  assert.equal(quadrant({wealth:50},49,'influence').id,'high-low');
  assert.equal(quadrant(p,null,'influence'),null);
});
test('range filters handle boundaries and missingness',()=>{
  assert.ok(matchesRange(undefined,'all',10,40));assert.ok(matchesRange(undefined,'missing',10,40));
  assert.ok(!matchesRange(undefined,'low',10,40));
  assert.ok(!matchesRange(10,'low',10,40));assert.ok(matchesRange(10,'middle',10,40));
  assert.ok(!matchesRange(40,'middle',10,40));assert.ok(matchesRange(40,'high',10,40));
});
test('all default entries and compound filters',()=>{
  assert.equal(filterPeople(people,DEFAULTS,countries).length,500);
  const us=filterPeople(people,{...DEFAULTS,country:'United States',origin:'self-made',industry:'Technology'},countries);
  assert.ok(us.length>5);assert.ok(us.every(p=>p.country==='United States'&&p.origin==='self-made'&&p.industry==='Technology'));
  assert.equal(filterPeople(people,{...DEFAULTS,search:'  MUSK '},countries)[0].id,'elon-musk');
  assert.equal(filterPeople(people,{...DEFAULTS,search:'no-such-billionaire'},countries).length,0);
  assert.ok(filterPeople(people,{...DEFAULTS,origin:'family'},countries).every(p=>['inherited','mixed','family-linked'].includes(p.origin)));
  assert.ok(filterPeople(people,{...DEFAULTS,gdp:'missing'},countries).every(p=>p.country==='Taiwan'));
  assert.equal(filterPeople(people,{...DEFAULTS,country:'India',continent:'Europe'},countries).length,0);
});
test('sorting preserves nulls at the end regardless of direction',()=>{
  for(const direction of ['asc','desc']){
    const sorted=sortPeople(people,{...DEFAULTS,sort:'metric',lens:'influence',direction},countries,evidence);
    assert.ok(influence(sorted[0],evidence));assert.equal(influence(sorted.at(-1),evidence),null);
  }
  assert.equal(sortPeople(people,{...DEFAULTS,sort:'wealth',direction:'desc'},countries,evidence)[0].id,'elon-musk');
});
test('URL state round-trips supported filters and rejects invalid values',()=>{
  const state={...DEFAULTS,country:'India',origin:'family',ppp:'middle',color:'origin',lens:'influence',view:'table',selected:'',page:2,search:'Ambani & family'};
  assert.deepEqual(parseState('#'+serializeState(state),people,countries),state);
  const bad=parseState('#lens=oops&country=nowhere&page=-1&selected=javascript:alert(1)&scale=oops',people,countries);
  assert.equal(bad.lens,'influence');assert.equal(bad.country,'all');assert.equal(bad.page,1);assert.equal(bad.selected,'');assert.equal(bad.scale,'log');
});
test('HTML and CSV escaping protect dataset and shared search inputs',()=>{
  assert.equal(escapeHTML('<img onerror="x">'), '&lt;img onerror=&quot;x&quot;&gt;');
  assert.equal(csvCell('=1+1'),'"\'=1+1"');assert.equal(csvCell('a"b'),'"a""b"');
  const csv=exportCsv([p],countries,evidence);assert.equal(csv.split('\r\n').length,2);assert.ok(csv.includes('wealth_date'));assert.ok(csv.includes('editorial_estimate_not_probability'));
});
test('formatting never renders missing values as money or zero',()=>{
  assert.equal(money(null),'Not available');assert.equal(percent(null),'Not available');
  assert.equal(money(839e9),'$839B');assert.equal(money(1.23e12),'$1.23T');assert.equal(percent(.005), '0.005%');
});

test('research batches preserve authored decisions and source-access limitations',async()=>{
  const {readdir}=await import('node:fs/promises');
  const dir=new URL('../data/review-batches/',import.meta.url);
  const seen=new Set();
  const names=(await readdir(dir)).filter(n=>n.endsWith('.json')).sort();
  const last=new Map();
  for(const n of names){const b=JSON.parse(await readFile(new URL(n,dir),'utf8'));for(const id of Object.keys(b.profiles))last.set(id,n);}
  for(const name of await readdir(dir)){
    if(!name.endsWith('.json'))continue;
    const batch=JSON.parse(await readFile(new URL(name,dir),'utf8'));
    for(const id of batch.supersedes||[])seen.delete(id);
    for(const [id,c]of Object.entries(batch.profiles)){
      assert.ok(!seen.has(id));seen.add(id);
      const output=evidence.profiles[id];assert.equal(output.fileState,'case-reviewed');
      if(last.get(id)!==name)continue;  // superseded by a later, deeper review
      assert.deepEqual(output.support,c.support);assert.deepEqual(output.counter,c.counter);
      for(const r of [...c.support,...c.counter])assert.ok(r.access.length>10);
    }
    for(const[id,r]of Object.entries(batch.rubrics)){
      if(last.get(id)!==name)continue;
      const output=evidence.profiles[id];
      assert.deepEqual(Object.values(output.rubric).map(d=>d.level),r.levels);
      assert.deepEqual(Object.values(output.rubric).map(d=>d.sourceRefs),r.sourceRefs);
      assert.deepEqual(output.range,r.range);
    }
  }
  assert.equal(seen.size,200);
});
test('a reviewed civic or political role does not force a numerical estimate',()=>{
  for(const id of ['bill-gates','steve-ballmer','zhang-yiming','savitri-jindal','li-ka-shing']){
    const a=evidence.profiles[id];assert.equal(a.fileState,'case-reviewed');assert.ok(a.support.length);assert.equal(a.score,null);
    assert.ok(filterPeople(people,{...DEFAULTS,assessment:'unplaced'},countries,evidence).some(p=>p.id===id));
  }
});

test('new episode reviews retain unsuccessful influence, legal closure and attribution limits',()=>{
  const e=evidence.profiles;
  assert.equal(e['miriam-adelson'].score,44);
  assert.equal(e['harry-triguboff'].score,38);
  assert.equal(e['michael-dell'].score,31);
  assert.equal(e['stephen-schwarzman'].score,56);
  assert.equal(e['daniel-gilbert'].score,56);
  for(const id of ['miriam-adelson','harry-triguboff']){
    assert.equal(e[id].rubric.benefit.level,0);
    assert.match(e[id].rubric.benefit.rationale,/episode/);
  }
  assert.match(e['dieter-schwarz'].counter[0].text,/closed/);
  assert.match(e['daniel-gilbert'].counter[1].text,/not the amount already paid/);
  assert.match(e['masayoshi-son'].counter[0].text,/not a \$500 billion US appropriation/);
  for(const id of ['thomas-peterffy','german-larrea-mota-velasco','masayoshi-son','dieter-schwarz','ma-huateng','robin-zeng','andrea-pignataro']){
    assert.equal(e[id].fileState,'case-reviewed');assert.equal(e[id].score,null);
  }
});

test('family ties, minority ownership and advocacy do not transfer conduct or force scores',()=>{
  const e=evidence.profiles;
  for(const id of ['amancio-ortega','rob-walton','jim-walton','alice-walton','francoise-bettencourt-meyers','julia-koch','lukas-walton','tadashi-yanai','iris-fontbona','zhong-shanshan']){
    assert.equal(e[id].fileState,'case-reviewed');assert.equal(e[id].score,null);
  }
  assert.match(e['lukas-walton'].support[0].text,/4\.9%/);
  assert.match(e['lukas-walton'].limitations,/minority stake is not sole ownership/);
  assert.match(e['francoise-bettencourt-meyers'].support[0].text,/dismissal/);
  assert.match(e['iris-fontbona'].counter[0].text,/does not remove ownership power/);
  assert.match(e['zhong-shanshan'].counter[0].text,/outside the park boundary/);
  // Mordashov: scored in wave 47 from the full text of General Court T-248/22; the judgment finds no specific preferential benefit.
  assert.equal(e['alexey-mordashov'].score,69);assert.deepEqual(e['alexey-mordashov'].range,[45,85]);
  assert.match(e['alexey-mordashov'].counter[0].text,/contains no finding of a specific preferential contract/);
  assert.match(e['alexey-mordashov'].limitations,/not a finding of criminal guilt/);
  assert.equal(e['giancarlo-devasini'].score,50);
  assert.match(e['giancarlo-devasini'].limitations,/not established/);
});

test('shipping reviews preserve unsuccessful bids, witness status and dated ownership',()=>{
  const e=evidence.profiles;
  assert.equal(e['klaus-michael-kuehne'].score,25);
  assert.equal(e['klaus-michael-kuehne'].rubric.benefit.level,0);
  assert.match(e['klaus-michael-kuehne'].limitations,/does not mean no benefit from any government/);
  assert.equal(e['gianluigi-aponte'].score,56);
  assert.match(e['gianluigi-aponte'].counter[0].text,/witness.*not under investigation/);
  assert.match(e['gianluigi-aponte'].counter[1].text,/late 2025.*executive chairman/);
  assert.equal(e['rafaela-aponte-diamant'].score,null);
  assert.match(e['rafaela-aponte-diamant'].support[1].text,/20 February 2026/);
  assert.match(e['rafaela-aponte-diamant'].limitations,/do not copy Gianluigi/);
});

test('corporate advocacy is not personal direction and broad tax incentives are not bespoke favors',()=>{
  const e=evidence.profiles;
  for(const id of ['jacqueline-mars','john-mars','giovanni-ferrero']){
    assert.equal(e[id].fileState,'case-reviewed');assert.equal(e[id].score,null);
  }
  assert.match(e['jacqueline-mars'].counter[0].text,/conditional estimates/);
  assert.match(e['john-mars'].counter[0].text,/not automatically John/);
  assert.match(e['giovanni-ferrero'].limitations,/explicitly secondary/);
  assert.equal(e['paolo-ardoino'].score,44);
  assert.match(e['paolo-ardoino'].support[1].text,/not a statement that Tether alone paid/);
  assert.match(e['paolo-ardoino'].counter[0].text,/not just Tether/);
});

test('historical steel reviews retain government defenses and mixed judicial outcomes',()=>{
  const e=evidence.profiles;
  assert.equal(e['lakshmi-mittal'].score,56);
  assert.ok(e['lakshmi-mittal'].counter.some(c=>/award decision was made before the letter/.test(c.text)));
  assert.match(e['lakshmi-mittal'].limitations,/not a finding that any contract or letter was purchased/);
  assert.equal(e['rinat-akhmetov'].score,63);
  assert.match(e['rinat-akhmetov'].counter[0].text,/fair-hearing violation.*no property-rights violation/);
  assert.match(e['rinat-akhmetov'].limitations,/not ongoing possession/);
  assert.match(e['rinat-akhmetov'].counter[1].text,/licenses, not transfer of the entire business/);
});


test('public-private reviews distinguish commitments, public benefits and failed lobbying',()=>{
  const e=evidence.profiles;
  assert.equal(e['james-ratcliffe'].score,50);
  assert.match(e['james-ratcliffe'].counter[0].text,/right to share future profits/);
  assert.match(e['james-ratcliffe'].support[2].text,/not a €700 million cash gift/);
  assert.equal(e['stephen-ross'].score,56);
  assert.match(e['stephen-ross'].limitations,/donations postdate/);
  assert.match(e['stephen-ross'].support[1].text,/tax breaks from.*other city investment/);
  assert.equal(e['idan-ofer'].score,44);
  assert.equal(e['idan-ofer'].rubric.benefit.level,0);
  assert.match(e['idan-ofer'].limitations,/confined to stopping this reform/);
  assert.equal(e['michal-strnad'].score,null);
  assert.match(e['michal-strnad'].counter[0].text,/not a committed order book/);
  assert.equal(e['suleiman-kerimov-family'].score,null);
  assert.match(e['suleiman-kerimov-family'].counter[1].text,/ruling out a state purchase/);
});

test('Surprise me includes a reviewed zero and respects the current filtered universe',()=>{
  const sample=[{id:'zero'},{id:'high'},{id:'missing'}];
  const ratings={profiles:{zero:{score:0},high:{score:75},missing:{score:null}}};
  assert.deepEqual(surprisePool(sample,'influence',ratings).map(p=>p.id),['zero','high']);
  assert.deepEqual(surprisePool([sample[2]],'influence',ratings),[sample[2]]);
  assert.deepEqual(surprisePool(sample,'footprint',ratings),sample);
  assert.deepEqual(surprisePool([],'influence',ratings),[]);
});


test('patronage history, withdrawn bids and investor speculation retain their limits',()=>{
  const e=evidence.profiles;
  assert.equal(e['anthoni-salim-1'].score,75);
  assert.match(e['anthoni-salim-1'].limitations,/share an author and research base/);
  assert.match(e['anthoni-salim-1'].counter[1].text,/cannot be presented as current/);
  assert.equal(e['pham-nhat-vuong'].score,25);
  assert.equal(e['pham-nhat-vuong'].rubric.benefit.level,0);
  assert.match(e['pham-nhat-vuong'].limitations,/this withdrawn bid/);
  assert.match(e['pham-nhat-vuong'].counter[1].text,/not a loan disbursement/);
  assert.equal(e['enrique-razon-jr'].score,null);
  assert.match(e['enrique-razon-jr'].counter[0].text,/no clear ties to Duterte/);
});

test('political giving, stadium funding and corporate disputes preserve attribution and safeguards',()=>{
  const e=evidence.profiles;
  assert.equal(e['phil-knight'].score,44);
  assert.match(e['phil-knight'].support[1].text,/did not cut current tax rates or freeze future rates/);
  assert.match(e['phil-knight'].counter[0].text,/2014 donation followed the 2012 agreement/);
  assert.equal(e['david-tepper'].score,50);
  assert.match(e['david-tepper'].support[0].text,/city would own the improvements/);
  assert.match(e['david-tepper'].counter[0].text,/fifteenth anniversary.*remaining city debt/);
  assert.match(e['david-tepper'].counter[1].text,/not an independent audit/);
  for(const id of ['len-blavatnik','thomas-frist-jr','abigail-johnson']){
    assert.equal(e[id].fileState,'case-reviewed');assert.equal(e[id].score,null);
  }
  assert.equal(e['len-blavatnik'].support[1].date,'2026-09-16');
  assert.match(e['len-blavatnik'].counter[1].text,/not proof of Blavatnik’s complete financial exit/);
  assert.match(e['thomas-frist-jr'].support[0].text,/not a new.*personal fine/);
  assert.match(e['abigail-johnson'].support[0].text,/Dave Gray/);
  assert.match(e['abigail-johnson'].counter[0].text,/neither a Fidelity-specific approval/);
});

test('individual gifts are not family totals and former roles are not current political control',()=>{
  const e=evidence.profiles;
  for(const id of ['stefan-quandt','susanne-klatten']){
    assert.equal(e[id].score,38);
    assert.match(e[id].support[0].text,/€230,000/);
    assert.match(e[id].support[0].text,/three separate donors/);
    assert.match(e[id].counter[0].text,/decided in January/);
    assert.match(e[id].counter[1].text,/not permanent abolition/);
    assert.equal(e[id].rubric.exchange.level,1);
  }
  assert.equal(e['mark-mateschitz'].score,null);
  assert.match(e['mark-mateschitz'].counter[0].text,/authority from the rights passed to Mark/);
  assert.equal(e['william-ding'].score,null);
  assert.match(e['william-ding'].support[1].text,/absent.*14th CPPCC/);
  assert.match(e['william-ding'].counter[0].text,/heavily affected NetEase/);
});

test('clemency, conditional incentives and changed voting rights retain material qualifications',()=>{
  const e=evidence.profiles;
  assert.equal(e['mong-koo-chung'].score,75);
  assert.match(e['mong-koo-chung'].support[1].text,/74 business figures/);
  assert.match(e['mong-koo-chung'].support[2].text,/not a reported acquittal/);
  assert.match(e['mong-koo-chung'].counter[0].text,/not treated here as separate adjudicated bribery/);
  assert.equal(e['euisun-chung'].score,50);
  assert.match(e['euisun-chung'].support[2].text,/projected \$2\.1 billion/);
  assert.match(e['euisun-chung'].counter[0].text,/below 80%/);
  assert.match(e['euisun-chung'].counter[1].text,/did not face trial/);
  assert.equal(e['jack-ma'].score,null);
  assert.match(e['jack-ma'].counter[0].text,/no longer controlled/);
  assert.match(e['jack-ma'].support[0].access,/Indexed/);
});


test('access reviews retain general relief, direct denials and joint-donor boundaries',()=>{
  const e=evidence.profiles;
  assert.equal(e['james-dyson'].score,38);
  assert.match(e['james-dyson'].counter[0].text,/did not exempt UK earnings/);
  assert.match(e['james-dyson'].counter[1].text,/not an independent spending audit/);
  assert.match(e['james-dyson'].counter[2].text,/withdraws the characterization/);
  assert.equal(e['anthony-bamford'].score,null);
  assert.match(e['anthony-bamford'].support[1].text,/£23,853/);
  assert.match(e['anthony-bamford'].support[1].text,/not an amount attributed solely/);
  assert.match(e['anthony-bamford'].counter[0].text,/ends his House membership/);
  assert.equal(e['kerry-stokes'].score,38);
  assert.equal(e['kerry-stokes'].rubric.exchange.level,1);
  assert.match(e['kerry-stokes'].counter[0].text,/denies discussing industry issues/);
});


test('stadium and recovery reviews distinguish paid support, claims and public safeguards',()=>{
  const e=evidence.profiles;
  assert.equal(e['jerry-jones'].score,56);
  assert.match(e['jerry-jones'].support[0].text,/reported donor was the Cowboys/);
  assert.match(e['jerry-jones'].counter[1].text,/principal, interest and fees/);
  assert.equal(e['terrence-pegula'].score,50);
  assert.match(e['terrence-pegula'].support[2].text,/not the full lifecycle public commitment/);
  assert.match(e['terrence-pegula'].counter[0].text,/must bear construction overruns/);
  assert.match(e['terrence-pegula'].counter[2].text,/not an unconditional right to leave/);
  assert.equal(e['stanley-kroenke'].score,null);
  assert.match(e['stanley-kroenke'].support[1].text,/disputed demand/);
  assert.equal(e['stanley-kroenke'].counter[0].date,'2026-09-12');
  assert.match(e['stanley-kroenke'].counter[1].text,/not establish final disposition of every claim/);
  assert.equal(e['anthony-pratt'].score,null);
  assert.match(e['anthony-pratt'].support[1].text,/company return, not a personal/);
  assert.match(e['anthony-pratt'].counter[1].text,/after the 2020–21 grant/);
});


test('legal representation, company incentives and political criticism do not invent personal scores',()=>{
  const e=evidence.profiles;
  for(const id of ['jean-louis-van-der-velde','stuart-hoegner','colin-huang','eduardo-saverin']){
    assert.equal(e[id].fileState,'case-reviewed');assert.equal(e[id].score,null);
    assert.equal(e[id].range,null);
    assert.ok(Object.values(e[id].rubric).every(d=>d.level===null));
  }
  assert.match(e['jean-louis-van-der-velde'].counter[0].text,/neither admit nor deny/);
  assert.match(e['jean-louis-van-der-velde'].counter[1].text,/two companies and roles are distinct/);
  assert.match(e['stuart-hoegner'].support[0].text,/counsel’s denials, not court findings/);
  assert.match(e['stuart-hoegner'].counter[1].text,/retirement/);
  assert.match(e['colin-huang'].support[0].text,/not Huang’s personal tax rate/);
  assert.match(e['colin-huang'].counter[1].text,/lose their special voting rights/);
  assert.match(e['eduardo-saverin'].support[1].text,/proposed legislation, not an order/);
  assert.match(e['eduardo-saverin'].counter[0].text,/not independently verified tax-payment/);
});

test('state-arranged lending and amended sanctions retain terms, chronology and jurisdiction',()=>{
  const v=evidence.profiles['viktor-vekselberg'];
  assert.equal(v.fileState,'case-reviewed');assert.equal(v.score,44);
  assert.equal(v.rubric.exchange.level,1);
  assert.match(v.rubric.exchange.rationale,/no causal reward or reciprocal bargain/);
  assert.match(v.counter[0].text,/government funds were not used/);
  assert.match(v.counter[0].text,/no loan amount or interest rate/);
  assert.match(v.counter[2].text,/not treated as a current 2026 office/);
  const k=evidence.profiles['viatcheslav-kantor'];
  assert.equal(k.fileState,'case-reviewed');assert.equal(k.score,null);
  assert.equal(k.support[0].date,'2026-03-16');
  assert.match(k.support[0].access,/visually reviewed/);
  assert.match(k.counter[0].text,/deletes the earlier description/);
  assert.match(k.counter[1].text,/not a judgment/);
  assert.match(k.counter[2].text,/grounds of appeal, not findings/);
});

test('privatization and import-policy reviews preserve partner attribution and public objectives',()=>{
  const p=evidence.profiles['mikhail-prokhorov'];
  assert.equal(p.score,69);assert.deepEqual(p.range,[40,85]);
  assert.match(p.support[2].text,/division of labor/);
  assert.match(p.counter[0].text,/later company valuation is not the price of the original stake/);
  assert.match(p.counter[1].text,/denied being a Kremlin instrument/);
  assert.match(p.limitations,/not evidence that the earlier acquisition was an election payment/);
  const l=evidence.profiles['vladimir-lisin'];
  assert.equal(l.score,38);assert.equal(l.rubric.exchange.level,1);
  assert.match(l.support[1].text,/each agreeing to invest/);
  assert.match(l.support[4].text,/progressively reduced volumes/);
  assert.match(l.counter[0].text,/not the same as an unconditional grant/);
  assert.match(l.counter[2].text,/could not establish which states/);
  assert.match(l.limitations,/not verification of the rules/);
});
