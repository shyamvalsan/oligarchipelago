"""Direct access is not proof of a purchased policy: three historical reviews."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Moderate / episode limited' if decision else 'Low / attribution unresolved',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
def rubric(levels,bounds,notes,refs):return dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
GOV='https://www.gov.uk/government/news/information-relating-to-the-ventilator-challenge-and-the-statutory-residence-test'
VENT='https://www.dyson.com/discover/news/press-releases/ventilator-update1'
BBC='https://www.dyson.co.uk/discover/archive/2021/bbc-james-dyson-apology'
add('james-dyson',
 'Dyson had direct prime-ministerial access during the emergency ventilator effort. The associated staff-tax clarification was a temporary, generally applicable measure, not a personal tax waiver. This episode supports access much more strongly than private enrichment.',
 'Emergency manufacturing request → direct access and staff-tax clarification',
 'UK ventilator initiative in March–May 2020; government explanation and BBC correction in 2021',
 [r('Downing Street confirms Dyson exchanged texts with Boris Johnson about internationally based staff returning to help make ventilators. The government subsequently announced a temporary change to the residence test.','Prime Minister’s Office: chronology and policy explanation',GOV,'2021-04-23','Primary acknowledgment of access and policy response'),
  r('The published BBC apology, reproduced by Dyson, acknowledges that the prime minister directly requested his assistance during the ventilator emergency.','BBC apology reproduced on Dyson’s website',BBC,'2021-05-12','Correction and emergency context','Text of the BBC apology reviewed on the subject’s website')],
 [r('The government says the change covered qualifying COVID-response workers across specified critical sectors from March to June 2020, not only Dyson staff. It did not exempt UK earnings from UK tax and went through parliamentary scrutiny.','Prime Minister’s Office: scope and safeguards',GOV,'2021-04-23','Material policy qualification; government’s own account'),
  r('Dyson’s May statement says the new ventilators were no longer needed in the UK and that he would fund the approximately £20 million project without accepting public money. This is his account, not an independent spending audit.','James Dyson: ventilator update',VENT,'2020-05-26','Subject’s explanation and reported project outcome'),
  r('The BBC apology withdraws the characterization of Dyson as a prominent Conservative supporter: a foundation gift for a school engineering festival did not establish party affiliation.','BBC apology reproduced by Dyson',BBC,'2021-05-12','Material correction to political attribution','Text of the BBC apology reviewed on the subject’s website')],
 'A narrow pandemic-era assessment, not a judgment on all Dyson business or tax affairs. The evidence for personalized political access is stronger than the evidence for a preferential economic exchange. Government and company statements are interested-party accounts; neither proves the absence of other influence. The range reflects that uncertainty.',
 rubric([3,1,1],[5,60],['Direct contact is acknowledged by government and contextualized in the published correction.','General staff relief is weak evidence of an exclusive private advantage.','The documented public-health purpose and reported self-funding substantially limit a private-benefit inference.'],[[0,1],[0],[0,1]]))
CAREER='https://members.parliament.uk/member/4305/career'
REGISTER='https://publications.parliament.uk/pa/cm/cmregmem/230530/johnson_boris.htm'
add('anthony-bamford',
 'Bamford’s formal political role and declared support for Boris Johnson are documented. They establish political connection, not by themselves a government concession to his business or a purchased peerage. Economic reciprocity remains unresolved in this review.',
 'Former parliamentary role and declared political hospitality; reciprocal benefit unresolved',
 'Lords membership 2013–2024 and declared wedding hospitality in July 2022',
 [r('Parliament records Bamford’s Conservative affiliation and Lords membership from 3 October 2013 to 1 March 2024.','UK Parliament: parliamentary career',CAREER,'Accessed 2026-10-08','Primary historical political role'),
  r('Johnson’s register names Lord Anthony and Lady Carole Bamford jointly as donors of wedding-celebration services valued at £23,853 on 30 July 2022. This is a declared joint gift, not an amount attributed solely to Anthony.','House of Commons: Johnson’s financial interests',REGISTER,'2023-05-30','Primary declaration of political hospitality')],
 [r('The career record ends his House membership in March 2024; this review does not describe him as a sitting member in 2026.','UK Parliament: end of membership',CAREER,'Accessed 2026-10-08','Material role update'),
  r('Other accommodation entries name Lady Carole alone. Those are not automatically Anthony’s donations, and disclosure does not establish a policy favor in return.','House of Commons: donor attribution',REGISTER,'2023-05-30','Individual attribution boundary')],
 'No numerical estimate: these records do not establish the preferential economic-benefit and feedback dimensions. The peerage predates the reviewed wedding gift by years; no causal claim linking that gift to the peerage is made. The Forbes family entry is retained, but the political role belongs to Anthony and jointly reported gifts remain joint. No inference of wrongdoing follows from lawful political activity.')
STOKES='https://www.abc.net.au/listen/programs/worldtoday/stokes-denies-impropriety-in-ski-slopes-meeting/339582'
TREASURY='https://treasury.gov.au/publication/tax-expenditures-statement-2010/tax-expenditures-statement-2010/chapter-3-tax-expenditures/chapter-3-tax-expenditures-6'
add('kerry-stokes',
 'Stokes’s ministerial holiday contact preceded broadcaster relief, but he denied discussing industry issues. The evidence establishes access and sector benefit, not a private bargain.',
 'Ministerial access alongside broadcaster relief; causal exchange unproven',
 'Australian broadcaster licence-fee rebates and holiday-contact controversy, 2010–2011',
 [r('ABC identifies Stokes as Seven’s chairman and majority shareholder, reporting holiday contact with minister Stephen Conroy roughly a month before fee cuts.','ABC / Peter Ryan: The World Today interview',STOKES,'2010-02','Contemporaneous person-level contact and company attribution'),
  r('Treasury’s 2010 Tax Expenditures Statement, item B50, records television broadcaster licence-fee rebates of 33% in 2010 and 50% in 2011. It identifies the implementing regulations.','Australian Treasury: Tax Expenditures Statement 2010, B50',TREASURY,'2010 statement','Primary confirmation of sector-specific economic relief')],
 [r('Stokes denies discussing industry issues, describing a social encounter. ABC identifies Seven, Nine and Ten as beneficiaries, not a personal payment.','ABC: Stokes’s response and breadth of relief',STOKES,'2010-02','Direct denial and alternative explanation')],
 'Historical, episode-limited estimate. Timing does not establish causation, an editorial quid pro quo or corruption. The feedback inference is weak, and no current ownership or policy claim is made.',
 rubric([2,2,1],[10,65],['A specific ministerial encounter is documented, but its policy content is expressly denied.','Official records establish targeted industry relief, not a personal cash transfer.','Temporal proximity is circumstantial; the reviewed record does not prove a bargain.'],[[0],[1],[0,1]]))
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/016.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
