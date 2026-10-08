import {wealthDivider} from './spectrum.mjs';
export const CONTINENTS = {
  'North America': '#4e8b81', 'Europe': '#c99b55', 'Asia': '#b77f6c',
  'South America': '#879259', 'Africa': '#8f81a4', 'Oceania': '#739dac',
};
export const ORIGINS = {
  'self-made': {label:'Self-made', color:'#4e8b81'},
  inherited: {label:'Inherited', color:'#b284a2'},
  mixed: {label:'Inherited & grown', color:'#c69851'},
  'family-linked': {label:'Family-linked · unspecified', color:'#9a8a70'},
  unknown: {label:'Unknown', color:'#8d9990'},
};
export const ASSESSMENTS = {
  likely: {label:'Likely oligarch', short:'Likely', color:'#ad4a32', value:3},
  mixed: {label:'Mixed / disputed', short:'Mixed / disputed', color:'#aa7729', value:2},
  'no-strong': {label:'No strong evidence in reviewed sources', short:'No strong evidence*', color:'#357a74', value:1},
  unassessed: {label:'Not yet assessed', short:'Not assessed', color:'#8b959b', value:null},
};
export function assessment(person, evidence) {
  return evidence?.profiles?.[person.id] || {status:'unassessed'};
}
export function influence(person, evidence) {
  const a=assessment(person,evidence); return a.score ?? null;
}
export function surprisePool(people, lens, evidence) {
  const positioned=lens==='influence'?people.filter(p=>influence(p,evidence)!==null):people;
  return positioned.length?positioned:people;
}
export function coverage(people,evidence) {
  const counts=Object.fromEntries(Object.keys(ASSESSMENTS).map(k=>[k,0]));
  for(const p of people) counts[assessment(p,evidence).status]++;
  return counts;
}
export const DEFAULTS = Object.freeze({
  search:'', continent:'all', country:'all', origin:'all', industry:'all',
  gdp:'all', income:'all', ppp:'all', color:'flag', scale:'log',
  assessment:'all', lens:'influence', view:'chart', selected:'alisher-usmanov', sort:'rank', direction:'asc', page:1,
});
export const QUADRANTS = {
  footprint: [
    {id:'low-low', name:'First-Class Problems', subtitle:'Rich. Just not country-sized.', short:'LOWER WEALTH · LOWER FOOTPRINT', icon:'♧'},
    {id:'high-low', name:'Money Talks', subtitle:'A giant fortune in a bigger pond.', short:'HIGHER WEALTH · LOWER FOOTPRINT', icon:'≋'},
    {id:'low-high', name:'Big Fish, Small Pond', subtitle:'A fortune that looms large at home.', short:'LOWER WEALTH · HIGHER FOOTPRINT', icon:'◈'},
    {id:'high-high', name:'Whale Territory', subtitle:'Big money. Country-sized context.', short:'HIGHER WEALTH · HIGHER FOOTPRINT', icon:'✳'},
  ],
  influence: [
    {id:'low-low',name:'Billionaires',subtitle:'Lower wealth. Less oligarchic on the reviewed evidence.',short:'LESS WEALTH · LESS OLIGARCHIC',icon:'○'},
    {id:'high-low',name:'Mega-Billionaires',subtitle:'Greater wealth. Less oligarchic on the reviewed evidence.',short:'MORE WEALTH · LESS OLIGARCHIC',icon:'◉'},
    {id:'low-high',name:'Oligarchs',subtitle:'Lower wealth. Stronger wealth–power relationship.',short:'LESS WEALTH · MORE OLIGARCHIC',icon:'◈'},
    {id:'high-high',name:'Mega-Oligarchs',subtitle:'Greater wealth. Stronger wealth–power relationship.',short:'MORE WEALTH · MORE OLIGARCHIC',icon:'✳'},
  ],
};
export function footprint(person, countries) {
  const value = countries[person.country]?.gdp?.value;
  return Number.isFinite(value) && value > 0 ? person.wealth * 1e9 / value * 100 : null;
}
export function metric(person, state, countries, evidence) {
  return state.lens === 'influence' ? influence(person,evidence) : footprint(person,countries);
}
export function quadrant(person, value, lens, scale='log') {
  if (value === null) return null;
  const id = `${person.wealth >= wealthDivider(scale) ? 'high' : 'low'}-${value >= (lens==='influence'?50:1) ? 'high' : 'low'}`;
  return QUADRANTS[lens].find(q=>q.id===id);
}
export function matchesRange(value, choice, low, high) {
  if (choice === 'all') return true;
  if (choice === 'missing') return value == null;
  if (!Number.isFinite(value)) return false;
  if (choice === 'small' || choice === 'low') return value < low;
  if (choice === 'medium' || choice === 'middle') return value >= low && value < high;
  if (choice === 'large' || choice === 'high') return value >= high;
  return true;
}
export function filterPeople(people, state, countries, evidence) {
  const search = state.search.trim().toLocaleLowerCase();
  return people.filter(p => {
    const c = countries[p.country] || {};
    return (!search || `${p.name} ${p.sourceOfWealth}`.toLocaleLowerCase().includes(search))
      && (!state.assessment || state.assessment==='all' || (state.assessment==='placed'&&influence(p,evidence)!==null)||(state.assessment==='unplaced'&&influence(p,evidence)===null)||(state.assessment==='upper'&&influence(p,evidence)!==null&&influence(p,evidence)>=50)||(state.assessment==='lower'&&influence(p,evidence)!==null&&influence(p,evidence)<50))
      && (state.continent==='all' || state.continent===p.continent)
      && (state.country==='all' || state.country===p.country)
      && (state.industry==='all' || state.industry===p.industry)
      && (state.origin==='all' || state.origin===p.origin || (state.origin==='family' && ['inherited','mixed','family-linked'].includes(p.origin)))
      && matchesRange(c.gdp?.value,state.gdp,100e9,1e12)
      && matchesRange(c.gdpPerCapita?.value,state.income,1e4,4e4)
      && matchesRange(c.gdpPerCapitaPpp?.value,state.ppp,2e4,6e4);
  });
}
export function sortPeople(people, state, countries, evidence) {
  const direction = state.direction==='desc' ? -1 : 1;
  return [...people].sort((a,b) => {
    if (state.sort==='name') return direction * a.name.localeCompare(b.name);
    const av = state.sort==='metric' ? metric(a,state,countries,evidence) : a[state.sort];
    const bv = state.sort==='metric' ? metric(b,state,countries,evidence) : b[state.sort];
    if (av == null) return bv == null ? a.position-b.position : 1;
    if (bv == null) return -1;
    return direction * (av-bv) || a.position-b.position;
  });
}
export function parseState(hash, people, countries) {
  const params = new URLSearchParams(hash.replace(/^#/,''));
  const s = {...DEFAULTS};
  const valid = {
    continent:['all',...Object.keys(CONTINENTS)],country:['all',...Object.keys(countries)],
    origin:['all','family',...Object.keys(ORIGINS)],industry:['all',...new Set(people.map(p=>p.industry))],
    gdp:['all','small','medium','large','missing'],income:['all','low','middle','high','missing'],
    ppp:['all','low','middle','high','missing'],assessment:['all','placed','unplaced','upper','lower'],color:['flag','continent','origin'],scale:['log','linear'],
    lens:['footprint','influence'],view:['chart','table'],sort:['rank','name','wealth','metric'],direction:['asc','desc'],
  };
  for (const [key, values] of Object.entries(valid)) if(values.includes(params.get(key))) s[key]=params.get(key);
  s.search = (params.get('search') || '').slice(0,150);
  if(params.has('selected')) s.selected = people.some(p=>p.id===params.get('selected')) ? params.get('selected') : '';
  const page=Number(params.get('page'));
  if(Number.isInteger(page)&&page>0&&page<=100) s.page=page;
  return s;
}
export function serializeState(state) {
  const params = new URLSearchParams();
  for(const key of Object.keys(DEFAULTS)) if(state[key]!==DEFAULTS[key]) params.set(key,String(state[key]));
  return params.toString();
}
export function money(value, prefix='$') {
  if(value==null || !Number.isFinite(value)) return 'Not available';
  if(value>=1e12) return `${prefix}${(value/1e12).toLocaleString('en-US',{maximumFractionDigits:2})}T`;
  if(value>=1e9) return `${prefix}${(value/1e9).toLocaleString('en-US',{maximumFractionDigits:1})}B`;
  return `${prefix}${Math.round(value).toLocaleString('en-US')}`;
}
export function percent(value) {
  if(value==null) return 'Not available';
  return `${value.toLocaleString('en-US',{maximumFractionDigits:value<.1?3:2})}%`;
}
export function escapeHTML(value) {
  return String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
export function csvCell(value) {
  let text=String(value??'');
  if(/^[=+@\-\t\r]/.test(text)) text="'"+text;
  return '"'+text.replaceAll('"','""')+'"';
}
export function exportCsv(people,countries,evidence) {
  const rows=[['rank','name','country_citizenship','continent','wealth_usd_billions','wealth_date','origin','industry','gdp_usd','gdp_year','gdp_per_capita_usd','gdp_ppp_international_dollars','gdp_per_capita_ppp','economic_year','wealth_pct_annual_gdp','editorial_estimate_not_probability','editorial_range_low','editorial_range_high','assessment_confidence','assessment_period','assessment_reviewed_at','assessment_limitations','forbes_profile']];
  for(const p of people) {
    const c=countries[p.country]||{},i=assessment(p,evidence);
    rows.push([p.rank,p.name,p.country,p.continent,p.wealth,'2026-03-01',p.origin,p.industry,c.gdp?.value,c.gdp?.year,c.gdpPerCapita?.value,c.gdpPpp?.value,c.gdpPerCapitaPpp?.value,2024,footprint(p,countries),i.score,i.range?.[0],i.range?.[1],i.confidence,i.period,i.reviewedAt,i.limitations,p.profileUrl]);
  }
  return rows.map(r=>r.map(csvCell).join(',')).join('\r\n');
}
