"""Build the spectrum from authored case decisions, never from search hits."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/'data'/name).read_text())
cases=read('cases.json');people=read('billionaires.json')['people']
# Hand-authored dimension levels: political leverage, preferential economic benefit,
# and strength of the wealth/power feedback mechanism. Unknown is never zero.
R={
 'alisher-usmanov':([3,3,3],[50,90],['Specific high-level patronage attributed by authorities.','Material benefit specifically attributed, not just sector exposure.','Support and benefit described together; contested authority accounts.']),
 'mikhail-gutseriev':([3,3,3],[50,90],['Longstanding ruler access described by FCDO.','Government economic benefit attributed in the designation.','Business-backed regime support and benefit linked in the accounts.']),
 'jay-y-lee':([3,4,4],[75,100],['A specific route to presidential support was established historically.','The historical case concerned government support for corporate control.','Separate bribery conviction established the exchange; pardon and later acquittal included.']),
 'prajogo-pangestu':([3,4,3],[60,95],['Named as a politically connected concession beneficiary.','Discretionary concessions and privileged credit are concrete benefits.','Institutional research links allocation to regime objectives; historical scope.']),
 'vladimir-potanin':([3,3,3],[55,95],['Privatization policy access and a later executive role are documented.','Acquisition through the program is documented; extent of underpricing debated.','The policy-design / acquisition relationship supports the historical inference.']),
 'roman-abramovich':([3,3,3],[50,90],['Specific high-level access is attributed by the UK.','Specific concessions alleged, rather than sanctions alone.','Authority describes preferential political-economic treatment; not a criminal finding.']),
 'mikhail-fridman':([2,1,1],[5,65],['Proximity attributed, but challenged in court.','Sector exposure is contextual, not proof of a private favor.','Court annulment materially weakens earlier reciprocal-benefit claims.']),
 'elon-musk':([4,2,2],[35,90],['Formal government access in the stated historical period.','Starlink trade-access benefit specifically alleged, not adjudicated.','Specific public-role/private-benefit allegation, with unresolved causation.']),
 'gautam-adani-1':([2,2,2],[20,85],['Specific official-access mechanism alleged by SEC.','Specific above-market purchase benefits alleged.','The alleged exchange is specific; dismissal and no-admission settlement limit inference.']),
 'rupert-murdoch':([3,1,1],[10,70],['Regulator describes political agenda influence.','Business-facing access is contextual, not a proven favor.','Regulator cautions that access does not establish an exchange.']),
 'jeff-bezos':([2,1,1],[5,65],['Media decision and political-business access create a plausible channel.','Overlapping business interests are contextual; no specific reward established.','Circumstantial linkage explicitly denied; low confidence.']),
 'aliko-dangote':([3,3,3],[50,95],['Institutional industrial-policy access documented.','Protection and incentives tied to business interests in research.','Academic account links political networks and protective policy.']),
 'carlos-slim-helu':([3,3,3],[50,90],['Historical presidential access and backing described in scholarship.','Privatized monopoly and political protection described.','Historical support/access/business protection mechanism; later reforms constrain it.']),
 'charles-koch':([4,3,3],[50,95],['Sustained organized policy-shaping network documented in research.','Academic account links regulatory agenda to business interests.','Wealth-funded policy work and commercial interests reinforce one another; ideology also matters.']),
 'gina-rinehart':([3,2,2],[25,80],['Prominent role in a coordinated policy campaign documented.','Tax exposure is concrete; individual benefit attribution is less certain.','Campaign and policy outcome linked; individual causal contribution unresolved.']),
 'andrew-forrest':([3,2,2],[25,80],['Prominent role in a coordinated policy campaign documented.','Tax exposure is concrete; firm-specific outcomes differ.','Sector-wide policy campaign, not proof of exclusive political reward.']),
 'peter-thiel':([3,1,1],[15,75],['Specific political relationships reported.','Government business is documented, preferential procurement is not.','Business and political ties overlap without an established exchange.']),
 'jeff-yass':([2,2,1],[10,75],['A relevant political meeting is documented.','A specific investment could benefit from the policy position.','Causation explicitly denied; temporal association is weak evidence.']),
 'vincent-bollore':([2,2,2],[20,90],['Specific political-campaign assistance alleged.','Specific port-concession benefit alleged.','An alleged exchange awaits the individual trial; no conviction assumed.']),
 'bernard-arnault':([3,1,1],[10,70],['Extensive political access is reported.','General tax relief is not independently proof of preferential treatment.','Influence is clearer than an individualized exchange.']),
}
specific_refs={}
for path in sorted((ROOT/'data/review-batches').glob('*.json')):
 batch=json.loads(path.read_text())
 for id in batch.get('supersedes',[]):  # drop the replaced review's rubric; the new batch supplies its own, if any
  R.pop(id,None);specific_refs.pop(id,None)
 for id,decision in batch['rubrics'].items():
  assert id not in specific_refs, f'Duplicate rubric: {id}'
  assert id in cases['profiles'], f'Rubric without case: {id}'
  R[id]=(decision['levels'],decision['range'],decision['rationales'])
  specific_refs[id]=decision['sourceRefs']
discovery={}
for f in sorted((ROOT/'data/research-batches').glob('*.json')):
 batch=json.loads(f.read_text())
 for id,record in batch['profiles'].items():
  assert id not in discovery, f'Duplicate discovery record: {id}'
  discovery[id]=record
assert len(discovery)==500 and set(discovery)=={p['id'] for p in people}
profiles={}
for p in people:
 id=p['id'];c=cases['profiles'].get(id)
 if c:
  c=dict(c);c['fileState']='case-reviewed';c['score']=None;c['range']=None
  if c['summary'].startswith('Mixed / disputed: '):c['summary']=c['summary'][18:19].upper()+c['summary'][19:]
  if id in R:
   levels,bounds,notes=R[id]
   refs=specific_refs.get(id,[list(range(len(c['support'])))]*3)
   assert len(levels)==len(notes)==len(refs)==3
   assert all(type(v) is int and 0<=v<=4 for v in levels)
   assert all(ref and all(type(i) is int and 0<=i<len(c['support']) for i in ref) for ref in refs)
   c['rubric']={k:dict(level=v,rationale=n,sourceRefs=ref) for k,v,n,ref in zip(['leverage','benefit','exchange'],levels,notes,refs)}
   c['score']=math.floor((levels[0]*.25+levels[1]*.25+levels[2]*.5)*25+.5);c['range']=bounds
  else:
   c['rubric']={k:dict(level=None,rationale='The narrow source review is not sufficient to estimate this dimension.',sourceRefs=[]) for k in ['leverage','benefit','exchange']}
 else:
  c=dict(status='unassessed',fileState='discovery-only',reviewedAt=None,confidence='Not established',period='Individual evidence review not completed',score=None,range=None,
   summary=f"Forbes attributes {p['name']}’s fortune to {p['sourceOfWealth']}. Those business facts do not establish political leverage or a preferential economic exchange. Sources have been sought, but this individual assessment is unfinished.",
   limitations='A targeted search and a sanctions-name screen are only discovery. Search hits may concern a namesake or contain disputed claims. No oligarchy estimate is inferred from nationality, industry, wealth origin, a non-match, or a missing result.',
   support=[],counter=[],reviewDepth='Source discovery only, not a completed assessment',rubric={k:dict(level=None,rationale='Individual source review still required.',sourceRefs=[]) for k in ['leverage','benefit','exchange']})
 c['discovery']=discovery[id];profiles[id]=c
out=dict(version='0.3-spectrum',reviewedAt='2026-10-08',definition=cases['definition'],method='Editorial evidence spectrum: 25% political leverage + 25% preferential economic benefit + 50% wealth–power feedback. Each component 0–4; total scaled to 100. Missing components prevent a score. No automated scoring from searches or sanctions.',limitations='Research incomplete. Discovery covers 500 names, but only the explicitly authored cases are individually reviewed. Estimates and ranges are editorial, not probabilities, confidence intervals or criminal findings. Historical cases are not assertions of current conduct.',profiles=profiles)
(ROOT/'data/assessments.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
# Single compact, reproducible audit index; no shell argument proportional to dataset size.
(ROOT/'data/research-discovery.json').write_text(json.dumps(dict(searchedCount=500,method='Source discovery only; not verified identity, evidence or a completed assessment.',profiles=discovery),ensure_ascii=False,indent=2)+'\n')
print('500 research files;',len(cases['profiles']),'case reviews;',sum(c['score'] is not None for c in profiles.values()),'editorial estimates')
