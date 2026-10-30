import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {layout,mergeTies,sharedCompanyTies,coastline,radius,MODES} from '../lib/archipelago.mjs';

const read=f=>JSON.parse(readFileSync(new URL(`../data/${f}`,import.meta.url)));
const people=read('billionaires.json').people.slice(0,200);
const documented=read('ties.json').ties;

test('every documented tie names two launch-cohort people, a source URL and a date field',()=>{
  const ids=new Set(people.map(p=>p.id));
  assert.ok(documented.length>=40);
  for(const t of documented){
    assert.ok(ids.has(t.a)&&ids.has(t.b)&&t.a!==t.b,`${t.a}/${t.b}`);
    assert.match(t.url,/^https:\/\//);
    assert.ok(t.label&&t.source&&t.kind&&'date' in t,`${t.a}/${t.b}`);
    assert.equal(t.opened,true,`${t.a}/${t.b} was not opened by the researcher`);
  }
});

test('shared-fortune ties come only from named companies, never sector words',()=>{
  const ties=sharedCompanyTies(people);
  assert.ok(ties.length>0);
  for(const t of ties){assert.ok(t.derived);assert.doesNotMatch(t.label,/Both list (Retail|Mining|Investments|Diversified|Real estate)\b/);}
  const pair=ties.find(t=>[t.a,t.b].sort().join()==='larry-page,sergey-brin');
  assert.ok(pair);
});

test('layout is deterministic and no two islands overlap, in every mode',()=>{
  const ties=mergeTies(people,documented);
  for(const mode of Object.keys(MODES)){
    const a=layout(people,ties,mode),b=layout(people,ties,mode);
    assert.deepEqual(a.nodes,b.nodes);
    const list=people.map(p=>({...a.nodes[p.id],id:p.id}));
    for(let i=0;i<list.length;i++)for(let j=i+1;j<list.length;j++){
      const d=Math.hypot(list[i].x-list[j].x,list[i].y-list[j].y);
      assert.ok(d>=list[i].r+list[j].r,`${mode}: ${list[i].id} overlaps ${list[j].id}`);
    }
  }
});

test('island size grows with wealth and coastlines are stable',()=>{
  assert.ok(radius(839)>radius(100)&&radius(100)>radius(10));
  assert.equal(coastline('elon-musk',80),coastline('elon-musk',80));
  assert.notEqual(coastline('elon-musk',80),coastline('larry-page',80));
});
