// Mechanical coverage checks only. These cannot certify editorial fairness,
// source-reuse rights, accessibility, or permission to publish.
import {scoreRubric} from './spectrum.mjs';

export function researchReadiness(people, evidence, {expectedCount=500}={}) {
  const ids=new Set(people.map(p=>p.id));
  const profiles=evidence?.profiles||{};
  const counts={total:people.length,reviewed:0,scored:0,discoveryOnly:0,reviewedUnplaced:0};
  const errors=[];
  if(!Number.isInteger(expectedCount)||expectedCount<1)errors.push('Expected count must be a positive integer.');
  if(people.length!==expectedCount||ids.size!==expectedCount)errors.push(`Expected exactly ${expectedCount} unique Forbes entries.`);
  if(Object.keys(profiles).length!==ids.size||Object.keys(profiles).some(id=>!ids.has(id)))errors.push('Assessment identities do not match the Forbes universe.');
  for(const p of people){
    const a=profiles[p.id];
    if(!a){errors.push(`Missing assessment record: ${p.id}`);continue;}
    const reviewed=a.fileState==='case-reviewed';
    if(reviewed)counts.reviewed++;
    else if(a.fileState==='discovery-only')counts.discoveryOnly++;
    else errors.push(`Unknown review state: ${p.id}`);
    if(a.score!=null){
      counts.scored++;
      if(!reviewed||a.score!==scoreRubric(a.rubric))errors.push(`Unreviewed or inconsistent score: ${p.id}`);
      if(!Array.isArray(a.range)||a.range.length!==2||!a.range.every(Number.isFinite)||a.range[0]<0||a.range[1]>100||a.range[0]>a.score||a.range[1]<a.score)errors.push(`Invalid editorial range: ${p.id}`);
    }else if(reviewed)counts.reviewedUnplaced++;
    if(reviewed&&(!a.reviewedAt||!a.period||!a.limitations||!a.support?.length||!a.counter?.length))errors.push(`Incomplete review fields: ${p.id}`);
  }
  const blockers=[...errors];
  if(counts.reviewed!==expectedCount)blockers.push(`${expectedCount-counts.reviewed} entries still lack an individual case review.`);
  if(counts.scored!==expectedCount)blockers.push(`${expectedCount-counts.scored} entries lack a numerical placement under the current model. Do not invent scores to pass this check.`);
  return {counts,structuralErrors:errors,blockers,researchGatePassed:blockers.length===0};
}
