"""Individual donations, shared policy benefits and historical role attribution."""
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
DONATION='https://www.bundestag.de/webarchiv/presse/hib/2013_10/02-260006'
REUTERS='https://www.voanews.com/a/reu-bmw-family-donation-to-merkel-party-stokes-lobbying-row/1770441.html'
BMW='https://www.press.bmwgroup.com/global/article/detail/T0171788EN/bmw-group-remains-firmly-on-track-in-2013'
EU='https://climate.ec.europa.eu/news-other-reads/news/ende-gut-alles-gut-commissioner-hedegaard-welcomes-agreement-car-emissions-target-2014-02-25_en'
# The parliamentary record names each donor separately; neither is scored from
# kinship or from attributing the whole family donation to one person.
for id,name in [('stefan-quandt','Stefan Quandt'),('susanne-klatten','Susanne Klatten')]:
 add(id,
  f'{name} personally made a disclosed CDU donation. This review examines it alongside a favorable industry-policy outcome, while retaining the denial of a connection. The evidence supports a limited influence assessment, not a finding that policy was bought.',
  'Personal party funding alongside industry-wide regulatory relief; causal exchange unproved',
  'October 2013 donation and emissions negotiations; February 2014 legislative outcome',
  [r(f'The Bundestag identifies {name} individually as donating €230,000 to the CDU on 9 October 2013. The €690,000 total covered three separate donors, not this person alone.','German Bundestag: donation disclosure',DONATION,'2013-10-24','Primary person-level political finance record'),
   r('Reuters links BMW’s shareholder donations with Germany’s successful intervention to postpone an emissions deal affecting premium carmakers.','Reuters: donation and policy chronology',REUTERS,'2013-10-15','Contemporaneous reporting; not a causal finding'),
   r(f'BMW’s report on 2013 identifies {name} as an existing supervisory-board member proposed for reelection. The company relationship is not inferred merely from a surname.','BMW: 2013 results and board statement',BMW,'2014','Primary corporate-role attribution')],
  [r('The CDU denied a policy connection. The family’s spokesman said the gifts were decided in January and transferred after the election to avoid campaign involvement.','Reuters: party denial and family response',REUTERS,'2013-10-15','Material response and alternative chronology'),
   r('The Commission records Parliament endorsing a 95g CO₂/km fleet target for 2021 in February 2014. The delay was not permanent abolition of emissions regulation or a BMW-only exemption.','European Commission: subsequent legislative outcome',EU,'2014-02-25','Primary outcome qualification')],
  'Narrow historical estimate, not a present-day corruption allegation. A lawful donation is not itself evidence of improper conduct. The company could benefit from industry-wide relief; individual monetary gains and a donation-for-policy bargain are not established. Other relatives’ conduct and ancestral wrongdoing are not transferred to this donor.',
  rubric([2,2,1],[10,65],['An individually documented large party contribution, not proof of control over government.','Concrete industry relief plausibly benefits the linked company, without an exclusive concession.','Temporal association supports scrutiny, but the reviewed evidence does not establish causation.'],[[0],[1,2],[0,1]]))
MONITOR='https://media-ownership.eu/2025-edition/country-reports/austria/'
TREND='https://www.trend.at/unternehmen/dietrich-mateschitz-red-bull-nachfolge'
add('mark-mateschitz',
 'Mateschitz holds a major ownership interest behind an Austrian broadcaster, a potential channel of influence. But the reviewed ownership and succession records do not establish his personal political interventions or a preferential state benefit. His father’s actions cannot simply become his score.',
 'Inherited media ownership; personal political direction and reciprocal benefit unresolved',
 'Red Bull succession in November 2022; Austrian media ownership research in 2025',
 [r('The Euromedia Ownership Monitor identifies Mark Mateschitz’s 49% interest behind Red Bull Media and Servus TV. It also warns that complex ownership structures make practical decision-making influence difficult to infer.','Euromedia Ownership Monitor: Austria, 2025 edition',MONITOR,'2025','Research-based ownership mapping'),
  r('Trend reports Mark announcing Red Bull’s three-person management team and choosing a shareholder role rather than an operational management job in November 2022.','Trend / Bernhard Ecker: succession report',TREND,'2022-11-04','Personal statement and governance context')],
 [r('The succession report distinguishes Dietrich’s unusual operational authority from the rights passed to Mark, and records the other ownership bloc’s approval of the new leadership.','Trend: limits of inherited control',TREND,'2022-11-04','Material attribution limit'),
  r('The media monitor describes opaque ownership and difficulty verifying political ties. That is a research limitation, not evidence that Mark ordered particular coverage or received government favors.','Euromedia Ownership Monitor: transparency limits',MONITOR,'2025','Evidence-quality qualification')],
 'No numerical estimate: substantial media ownership is not equivalent to demonstrated policy capture. The succession account is historical, not a verified complete 2026 ownership register. No claim about his father’s political views, other shareholders’ relatives or broadcaster employees is treated as Mark’s own conduct.')
PROPOSAL='https://www.ecns.cn/m/news/politics/2021-03-06/detail-ihaihrwe3348059.shtml'
DEPARTURE='https://www.scmp.com/tech/big-tech/article/3207284/big-tech-cppcc-baidus-robin-li-neteases-ding-lei-no-longer-delegates-chinas-top-political-advisory'
FREEZE='https://www.marketscreener.com/quote/stock/37-INTERACTIVE-ENTERTAINM-11367211/news/China-ends-gaming-approval-freeze-grants-first-licenses-since-July-last-year-40022642/'
add('william-ding',
 'Ding had a documented national political-advisory role and made industry-related proposals. That demonstrates access, not that his proposals became law or secured special treatment for NetEase. His absence from the next delegate list and the company’s exposure to licensing restrictions qualify stronger claims.',
 'Political-advisory participation and industry proposals; preferential reward unresolved',
 'CPPCC proposals in March 2021, licensing freeze in 2021–2022 and delegate-list change in January 2023',
 [r('China Daily’s report, republished by ECNS, identifies Ding Lei as NetEase CEO and a 13th CPPCC National Committee member. It describes proposals concerning digital culture, music and vehicle-battery standards.','China Daily / ECNS: two-sessions proposals',PROPOSAL,'2021-03-06','State-media report of personal advisory activity'),
  r('SCMP reports William Ding Lei absent from the newly announced 14th CPPCC delegate list. This prevents presenting the earlier membership as an unchanged current role.','South China Morning Post / Coco Feng: delegate-list change',DEPARTURE,'2023-01-18','Dated role update','Indexed article passages reviewed; direct page retrieval failed')],
 [r('Reuters reports that the nine-month game-approval freeze heavily affected NetEase as well as Tencent. The April 2022 resumption covered a list of other publishers; this account does not establish preferential protection for Ding.','Reuters: Josh Ye and Brenda Goh, licensing freeze',FREEZE,'2022-04-11','Material constraint on claims of regulatory protection')],
 'No numerical estimate: advisory membership and a proposal are not a granted concession or proof of personal policy control. The review identifies William Ding with Ding Lei, but does not generalize from all Chinese technology companies. Being subject to regulation is not proof of no influence; subsequent offices, proposal adoption and person-linked benefits require further evidence.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/014.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
