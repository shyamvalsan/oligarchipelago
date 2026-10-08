import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {launchUniverse,LAUNCH_COUNT} from '../lib/universe.mjs';
import {researchReadiness} from '../lib/readiness.mjs';
import {parseState,DEFAULTS,filterPeople,footprint} from '../lib/model.mjs';
const data=JSON.parse(await readFile(new URL('../data/billionaires.json',import.meta.url),'utf8'));
const evidence=JSON.parse(await readFile(new URL('../data/assessments.json',import.meta.url),'utf8'));

test('launch is the first 200 Forbes entries, not the easiest 200 to score',()=>{
  const before=JSON.stringify({data,evidence});
  const launch=launchUniverse(data,evidence);
  assert.equal(launch.data.people.length,LAUNCH_COUNT);
  assert.deepEqual(launch.data.people.map(p=>p.id),data.people.slice(0,200).map(p=>p.id));
  assert.equal(launch.data.people.at(-1).id,'david-velez');
  assert.deepEqual(Object.keys(launch.evidence.profiles),launch.data.people.map(p=>p.id));
  assert.equal(JSON.stringify({data,evidence}),before);
  assert.deepEqual(Object.keys(launch.data.countries).sort(),[...new Set(launch.data.people.map(p=>p.country))].sort());
  assert.equal(filterPeople(launch.data.people,DEFAULTS,launch.data.countries,launch.evidence).length,200);
  assert.equal(launch.data.people.filter(p=>footprint(p,launch.data.countries)!==null).length,199);
});

test('top-200 readiness retains missing evidence instead of treating reduced scope as complete',()=>{
  const launch=launchUniverse(data,evidence);
  const report=researchReadiness(launch.data.people,launch.evidence,{expectedCount:200});
  assert.deepEqual(report.counts,{total:200,reviewed:94,scored:50,discoveryOnly:106,reviewedUnplaced:44});
  assert.deepEqual(report.structuralErrors,[]);
  assert.equal(report.researchGatePassed,false);
  assert.equal(report.blockers.length,2);
  assert.equal(researchReadiness(launch.data.people,launch.evidence).researchGatePassed,false);
});

test('launch fails closed on a truncated archive or missing profile; old out-of-scope links do not select strangers',()=>{
  assert.throws(()=>launchUniverse({...data,people:data.people.slice(0,200)},evidence));
  const copy=structuredClone(evidence);delete copy.profiles[data.people[0].id];
  assert.throws(()=>launchUniverse(data,copy));
  const launch=launchUniverse(data,evidence);
  assert.equal(parseState('#selected='+data.people[200].id,launch.data.people,launch.data.countries).selected,'');
});
