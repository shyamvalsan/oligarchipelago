import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {researchReadiness} from '../lib/readiness.mjs';
const data=JSON.parse(await readFile(new URL('../data/billionaires.json',import.meta.url),'utf8'));
const evidence=JSON.parse(await readFile(new URL('../data/assessments.json',import.meta.url),'utf8'));

test('current coverage cannot pass the all-500 research gate',()=>{
  const report=researchReadiness(data.people,evidence);
  assert.deepEqual(report.counts,{total:500,reviewed:108,scored:61,discoveryOnly:392,reviewedUnplaced:47});
  assert.deepEqual(report.structuralErrors,[]);assert.equal(report.researchGatePassed,false);
  assert.equal(report.blockers.length,2);
});
test('readiness detects unmatched identities and fabricated discovery scores',()=>{
  const copy=structuredClone(evidence);
  const [id,a]=Object.entries(copy.profiles).find(([,a])=>a.fileState==='discovery-only');
  a.score=0;
  copy.profiles['unrecognized-person']=structuredClone(a);
  const report=researchReadiness(data.people,copy);
  assert.ok(report.structuralErrors.some(e=>e.includes('identities')));
  assert.ok(report.structuralErrors.some(e=>e.includes(id)));
  assert.equal(report.researchGatePassed,false);
});
test('readiness treats a reviewed zero as a score but never a missing score',()=>{
  const copy=structuredClone(evidence);
  const a=copy.profiles['tadashi-yanai'];
  a.rubric={leverage:{level:0},benefit:{level:0},exchange:{level:0}};
  a.score=0;a.range=[0,10];
  const report=researchReadiness(data.people,copy);
  assert.equal(report.counts.scored,62);assert.equal(report.counts.reviewedUnplaced,46);
  assert.equal(report.researchGatePassed,false);
});
