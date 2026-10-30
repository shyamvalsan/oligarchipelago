"""Wave 47: primary-document upgrades from files a human fetched into data/inbox/ (not published; cited by URL).
- Alexey Mordashov: full text of General Court judgment T-248/22 (20 Sept 2023), French original, OCR'd locally; translations are ours.
- Lukas Walton: adds the DFC Inspector General's inspection report (DFC-25-001-IE, 30 Sept 2025) as a scope-limiting receipt."""
import json,glob
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
J='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62022TJ0248'
OCR='Full judgment printed to PDF by a human from EUR-Lex (French original); text read by OCR; quoted paragraphs paraphrased and translated by us'
P['alexey-mordashov']=dict(status='mixed',reviewedAt='2026-10-30',
 reviewDepth='Primary-document review of one judgment; not independently editorially reviewed; not a finding of criminal guilt',
 confidence='Moderate for the sanctions-law findings; low for any benefit mechanism',
 period='EU listing 2022 to 20 September 2023 (General Court judgment T-248/22)',
 summary='The EU General Court dismissed Mordashov\'s challenge to his 2022-23 listing. It accepted the Council\'s evidence that he held a 5.9% voting stake in Bank Rossiya, described in the evidence file as a bank of senior Russian officials, and that a company he controlled took part in a joint venture whose gas turbines were installed in Crimea. It also treated his attendance at Kremlin meetings with Putin as corroboration that he is an influential businessman. These are findings about the lawfulness of EU sanctions listings, which are not criminal findings, and the Court did not find a specific preferential contract or favour.',
 mechanism='Strategic-sector holdings (steel, energy engineering, banking stake) ↔ material support to Russian decision-makers, as accepted under EU listing criteria',
 support=[
  r('Paras 93-94 and 108-110: the Court held the Council could treat Mordashov as supporting and benefiting from the Russian leadership because he controls an "economic empire" in steel (Severstal), energy engineering (JSC Power Machines) and finance (Bank Rossiya). Through Severgroup he held 5.9% of Bank Rossiya\'s voting rights (5.481% shareholding in the evidence), the fifth-largest shareholder, which the Court said implies some control or at least presence in its decision-making; the Council could find he knew the bank supported certain Russian decision-makers and, by letting that continue, supported them himself.','General Court, T-248/22, paras 93-94, 108-110',J,'2023-09-20','Court finding on sanctions-listing grounds',OCR),
  r('Paras 113-118: Mordashov controls 100% of JSC Power Machines through Severgroup; Power Machines held 35% of a Siemens gas-turbine joint venture that sold four turbines (over EUR 200 million) to OJSC TPE, a subsidiary of state company Rostec; the turbines were installed in Crimea. He did not dispute that installation there is material support to Russian decision-makers; the Court held a contract clause meant to bar installation in Crimea did not change that.','General Court, T-248/22, paras 113-118',J,'2023-09-20','Court finding on sanctions-listing grounds',OCR),
  r('Paras 133 and 136: the Court noted he attended a 24 February 2022 meeting convened by Putin with a small group of businesspeople (it says 37 were invited) and a 16 March 2023 meeting; this was "not in itself decisive" but corroborated that he is an influential businessman. It did not itself adopt the Council\'s wording that he belongs to Putin\'s "closest circle".','General Court, T-248/22, paras 133 and 136',J,'2023-09-20','Court finding on access',OCR)],
 counter=[
  r('The judgment reviews whether the Council made an error of assessment under EU restrictive-measures criteria, which are preventive and not criminal (para 108). Criterion (g) alone requires only that a person be an influential businessperson in a revenue-generating sector, with no link to the government (para 125). The judgment contains no finding of a specific preferential contract, licence or subsidy to Mordashov.','General Court, T-248/22, paras 108 and 125',J,'2023-09-20','Legal standard and scope',OCR),
  r('Mordashov said Severgroup sold its Bank Rossiya shares on 21 July 2022 and that the Siemens joint venture had been misled by its customer. The Court did not accept the divestment evidence, finding the documents did not identify the buyer or show an independent third party (paras 96-102), and noted that legality is assessed on the facts when each act was adopted (para 97). It rejected the claim that the clause or the customer\'s conduct removed his responsibility (paras 115-118).','General Court, T-248/22, paras 96-102 and 115-118',J,'2023-09-20','His arguments and their treatment',OCR),
  r('The judgment is dated 20 September 2023. Later EU listings, any appeal, and developments since were not reviewed.','Scope of this review',J,'2026-10-30','Explicit limit of evidence',OCR)],
 limitations='Reads one judgment, in OCR from a French original. The Court assessed the Council\'s evidence file, not the underlying facts at trial; many of the Council\'s sources are not public. No specific preferential benefit is shown. The Court\'s test for supporting and benefiting from decision-makers is broader than our rubric\'s benefit and exchange dimensions, so the estimate leans on judgment. Later events were not reviewed. This is not a finding of criminal guilt.')
R['alexey-mordashov']=dict(levels=[3,2,3],range=[45,85],
 rationales=['Attended Putin-convened meetings of a small group of businesspeople in February 2022 and March 2023; the Court treated this as corroborating influence, not as proof of a closest circle.',
  'The Court accepted that he benefited from Russian decision-makers through his strategic-sector position, but no specific preferential contract, licence or subsidy to him is identified.',
  'The Court upheld the Council\'s finding that he supported Russian decision-makers through a Bank Rossiya stake and the Crimea turbine joint venture; this is adjudicated on sanctions-law grounds, with his divestment evidence rejected.'],
 sourceRefs=[[2],[0,1],[0,1]])
# ---- Lukas Walton: keep the earlier authored review and add the DFC OIG scope receipt
old=None
for f in sorted(glob.glob(str(ROOT/'data/review-batches/*.json'))):
 b=json.loads(Path(f).read_text())
 if 'lukas-walton' in b.get('profiles',{}) and not f.endswith('047.json'): old=b['profiles']['lukas-walton']
assert old
new=json.loads(json.dumps(old))
new['reviewedAt']='2026-10-30'
new['counter'].append(r('The DFC Inspector General inspected the $500 million First Solar loan (and a separate $50 million Bio E loan) for compliance with agreement terms and progress on impact metrics. It found gaps in environmental and social oversight of the First Solar project. It does not examine how the loan was approved or any political process, and it does not mention Walton.','US DFC Office of Inspector General, Inspection Report DFC-25-001-IE','https://www.dfc.gov/sites/default/files/media/documents/Inspection%20of%20DFC%27s%20First%20Solar%20and%20Bio%20E%20Projects%20%28DFC-25-001-IE%29.pdf','2025-09-30','Scope of an official review','PDF text extracted and read (full report fetched by a human)'))
new['limitations']=old['limitations']+' The DFC Inspector General\'s 2025 inspection looked only at post-approval compliance and impact, so it neither supports nor rebuts the 2022 congressional questions about approval.'
P['lukas-walton']=new
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
out=dict(supersedes=['alexey-mordashov','lukas-walton'],profiles=P,rubrics=R)
(ROOT/'data/review-batches/047.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
