"""State-backed credit is distinct from a grant; sanctions reasons change."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Low / causal link limited' if decision else 'Low / personal mechanism unresolved',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
def rubric(levels,bounds,notes,refs):return dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
TREASURY='https://home.treasury.gov/news/press-releases/jy0650'
LOAN='https://www.investing.com/news/commodities-news/russias-renova-gets-credit-line-from-promsvyazbank-1446057'
APPOINT='https://www.interfax-russia.ru/main/medvedev-naznachil-vekselberga-koordinatorom-sozdaniya-centra-innovaciy-v-skolkovo-s-rossiyskoy-storony'
add('viktor-vekselberg',
 'Vekselberg’s presidential appointment and Renova’s later state-arranged credit support show institutional proximity and economic protection. They do not establish that the loan rewarded his political role. The estimate gives only weak weight to that unproven causal connection.',
 'Presidential innovation role and state-arranged credit protection; reciprocal bargain unproven',
 'Skolkovo appointment in 2010, Renova credit support in May 2018, and a dated US government account in March 2022',
 [r('Interfax reports Medvedev personally announcing Vekselberg’s appointment to lead the Russian part of the Skolkovo coordination structure. This is a specific state-development responsibility, not merely attendance at a meeting.','Interfax: presidential appointment announcement',APPOINT,'2010-03-23','Contemporaneous report of direct presidential appointment','Russian article text reviewed'),
  r('Reuters reports the Russian finance ministry confirming a repayable credit line for Vekselberg’s Renova after US sanctions. Promsvyazbank had been taken over by the central bank and earmarked to lend to sanctioned entities.','Reuters, republished by Investing.com: Renova credit support',LOAN,'2018-05-14','Specific state-arranged company financing'),
  r('Treasury’s 2022 account describes Vekselberg’s Skolkovo appointment and participation in Kremlin diplomatic activities. These are attributed government statements, not a criminal judgment.','US Treasury: Vekselberg designation narrative',TREASURY,'2022-03-11','Primary government attribution','Relevant Vekselberg section reviewed')],
 [r('The ministry said government funds were not used and the credit was repayable. Reuters also describes discussions of support for other sanctioned businesses. The article gives no loan amount or interest rate.','Reuters: terms and broader policy context',LOAN,'2018-05-14','Material financing and exclusivity limits'),
  r('Medvedev’s stated rationale was to involve Russian business in building an effective innovation system. A public development objective is an alternative to a private patronage interpretation.','Interfax: president’s stated rationale',APPOINT,'2010-03-23','Material public-purpose explanation','Russian article text reviewed'),
  r('The 2022 Treasury account says Vekselberg no longer held that Skolkovo position following his earlier designation. The historical appointment is not treated as a current 2026 office.','US Treasury: historical role limitation',TREASURY,'2022-03-11','Material role update','Relevant Vekselberg section reviewed')],
 'This is an episode-limited editorial inference, not proof of corruption or an overall lifetime ranking. State-arranged lending is not the same as a treasury cash grant or verified below-market financing. These sources do not establish a loan-for-service agreement, subsequent repayment, or every later role. The wide range reflects that uncertainty; nationality and sanctions do not themselves add points.',
 rubric([3,2,1],[10,70],['A direct presidential appointment and government-facing institutional role are specifically documented.','State-arranged credit access protected the company, but terms, subsidy value and exclusivity are not established.','Institutional proximity and credit protection provide contextual evidence only; no causal reward or reciprocal bargain is established.'],[[0,2],[1],[0,1]]))
UK='https://assets.publishing.service.gov.uk/media/69b8276ce2719934bb53a2e1/Sanctions_Notice__Russia__16_March_2026.pdf'
EU='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202500528'
APPEAL='https://eur-lex.europa.eu/eli/C/2025/2521/oj/eng/pdf'
add('viatcheslav-kantor',
 'Kantor’s sanctions history requires jurisdiction and date distinctions. The UK retained restrictions while replacing its reasons in March 2026; the EU deleted his entry in March 2025. Neither an old political-association label nor delisting establishes a personal wealth–power exchange or its absence.',
 'Sanctions-based business attribution; personal preferential exchange unresolved',
 'EU delisting and appeal in March 2025; UK reasons variation in March 2026',
 [r('The UK’s March 2026 variation retains the listed sanctions and bases its reasons on Kantor’s ownership, control or management of Acron in strategic chemicals and extractives sectors. It does not identify a particular concession he secured.','UK FCDO: variation notice, RUS1127',UK,'2026-03-16','Primary updated sanctions basis','PDF pages 1–2 visually reviewed to distinguish red deletions from highlighted additions')],
 [r('The marked-up notice deletes the earlier description associating Kantor with Putin. That deleted wording must not be presented as the reasons retained in this notice; the change is not itself a general exoneration.','UK FCDO: tracked changes to reasons',UK,'2026-03-16','Material change to political-association wording','PDF pages 1–2 visually reviewed to distinguish red deletions from highlighted additions'),
  r('The annex to Council Decision 2025/528 explicitly deletes entry 896, Viatcheslav Moshe Kantor. This is an EU Council action, not a judgment declaring that every earlier allegation was false or a removal of UK restrictions.','Council of the European Union: Decision 2025/528, annex point 2',EU,'2025-03-14','Primary jurisdiction-specific delisting','Relevant PDF text reviewed, pages 1–3'),
  r('The official notice of Kantor’s March 24, 2025 appeal records challenges to legal interpretation, proportionality and the treatment of evidence. Those are his grounds of appeal, not findings accepting them.','EU Official Journal: appeal C-231/25 P',APPEAL,'2025-05-12','Subject’s formally recorded legal challenge','Two-page appeal notice reviewed; not a later disposition')],
 'No numerical estimate. The reviewed sector-based designation does not supply all three dimensions of personal leverage, preferential benefit and feedback. Delisting does not prove their absence. This narrow review does not resolve the origin of Acron ownership, informal relationships or the later outcome of the cited appeal. The March 2026 variation is dated evidence, not comprehensive sanctions advice.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/019.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
