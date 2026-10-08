"""Estate-tax advocacy, corporate lobbying, and a crypto-policy partnership."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Low to moderate / episode limited' if decision else 'Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
PC='https://www.citizen.org/sites/default/files/estatetaxfinal.pdf'
MARS='https://www.mars.com/about/policies-and-practices/public-policy-advocacy'
add('jacqueline-mars',
 'Historical estate-tax research implicates family-company advocacy, but does not establish Jacqueline’s individual direction or return.',
 'Family-company resources → estate-tax advocacy; individual direction unresolved','Estate-tax campaign in the 1990s–2000s; report published April 2006',
 [r('Public Citizen and United for a Fair Economy identify Jacqueline among the Mars siblings and describe company-funded efforts to repeal estate tax. The authors advocate retaining the tax.','Public Citizen / United for a Fair Economy, report p. 36',PC,'2006-04','Advocacy research','PDF text reviewed')],
 [r('The report’s projected tax savings are conditional estimates, not money shown to have been received by Jacqueline. Its spending evidence is predominantly company- and family-level.','Public Citizen / UFE: attribution and estimate limits',PC,'2006-04','Scope limitation','PDF text reviewed'),
  r('Mars currently says it discloses lobbying but makes no corporate candidate or party contributions. That company policy does not establish Jacqueline’s personal giving or disprove historical lobbying.','Mars: public policy and advocacy',MARS,'Accessed 2026-10-08','Subject policy statement','Indexed company policy text reviewed')],
 'No numerical estimate: the source identifies an economically relevant lobbying mechanism without assigning Jacqueline individual control of it. Historical corporate roles, inheritance and projected tax savings are not enough to fill every person-level dimension. The underlying lobbying filings were not independently reconstructed.')
add('john-mars',
 'John’s family-company political activity is documented; his personal decisions and resulting gains remain unresolved.',
 'Family-company estate-tax lobbying; person-level control and realized return unresolved','Estate-tax campaign in the 1990s–2000s; report published April 2006',
 [r('The report identifies John among the siblings with senior corporate roles and describes payments by Mars Inc. to an estate-tax lobbying group. It does not itemize his personal instructions.','Public Citizen / United for a Fair Economy, report p. 36',PC,'2006-04','Advocacy research','PDF text reviewed')],
 [r('Company payments are not automatically John’s personal payments. The report’s estimated family benefit is contingent on repeal, not a demonstrated individual windfall.','Public Citizen / UFE: person-versus-company scope',PC,'2006-04','Attribution limit','PDF text reviewed'),
  r('Mars distinguishes disclosed lobbying from corporate campaign contributions, which its policy prohibits. Neither statement amounts to a record of John’s individual political activity.','Mars: public policy and advocacy',MARS,'Accessed 2026-10-08','Subject policy statement','Indexed company policy text reviewed')],
 'No numerical estimate. Family-level research is retained as evidence to investigate, not transferred wholesale to John. More direct evidence of his decisions and policy outcomes is required; lack of a score is not a clean bill of health.')
GOV='https://www.ferrero.com/int/en/news-stories/news/the-ferrero-group-announces-new-governance-and-leadership-roles-reporting-into-president-giovanni-ferrero'
MEP='https://www.mepoftheweek.com/org/ferrero-international/'
CODE='https://www.static.ferrero.com/globalcms/documenti/1303.pdf'
add('giovanni-ferrero',
 'Ferrero International’s policy access is visible in a lobbying-record compilation. Giovanni’s strategic leadership is separately documented, but those facts do not establish that he attended the meetings or obtained a personal preferential decision.',
 'Corporate policy access and strategic control; individual action and outcome unresolved','European lobbying declarations through 2026; governance announcement, March 2026',
 [r('Ferrero’s March 2026 announcement identifies Giovanni as president of its holding company, with new leadership roles reporting to him and a continuing group strategy remit.','Ferrero: governance announcement',GOV,'2026-03-03','Subject governance statement','Indexed company announcement reviewed'),
  r('MEP of the Week compiles Ferrero International’s declared meetings on issues including deforestation and packaging. It is an independent aggregation of disclosure records, not evidence Giovanni personally attended.','MEP of the Week: Ferrero International record',MEP,'Accessed 2026-10-08','Secondary disclosure compilation')],
 [r('Ferrero’s published business-conduct code prohibits bribes and political-party or candidate contributions. A stated rule is not independent evidence of compliance, nor does it rule out lawful lobbying.','Ferrero: Code of Business Conduct, p. 5',CODE,'Undated; accessed 2026-10-08','Subject policy statement','Indexed PDF passage reviewed')],
 'No score: a corporate meeting log does not establish an individual favor or reciprocal bargain. The EU register page did not expose usable record text during this review, so the compilation is explicitly secondary. Private tax arrangements and business leadership alone do not establish oligarchy.')
TETHER='https://tether.io/news/tether-licensed-in-el-salvador-strengthening-focus-on-emerging-markets-and-innovation/'
VOLCANO='https://tether.to/en/tether-participates-in-1-billion-investment-to-build-the-worlds-largest-bitcoin-mining-farm-in-el-salvador/'
REUTERS='https://finance.yahoo.com/news/el-salvador-partnership-build-1-180726216.html'
TRADE='https://www.trade.gov/market-intelligence/el-salvador-ict-digital-assets-law'
add('paolo-ardoino',
 'Ardoino publicly links Tether’s investment and relocation to El Salvador’s crypto strategy. The record supports a commercial-policy partnership, but the reviewed licensing and tax framework is broader than Tether and does not establish a bespoke political favor.',
 'Executive-led investment and jurisdiction choice ↔ public crypto strategy and sector incentives','Volcano Energy announcement, June 2023; licensing and headquarters move, January 2025',
 [r('Tether’s January 2025 announcement quotes CEO Ardoino explaining its planned relocation after obtaining a digital-asset license and presents the move as aligned with El Salvador’s policy direction.','Tether: licensing and relocation announcement',TETHER,'2025-01-13','Subject statement'),
  r('Tether’s June 2023 announcement quotes then-CTO Ardoino supporting its participation in Volcano Energy. The project’s billion-dollar ambition is not a statement that Tether alone paid that amount.','Tether: Volcano Energy investment announcement',VOLCANO,'2023-06-05','Subject investment statement','Indexed company announcement reviewed'),
  r('Reuters describes a public-private mining project with a government revenue participation and Tether among initial investors; Tether’s contribution was not specified.','Reuters: El Salvador mining partnership',REUTERS,'2023-06-05','Reported partnership terms','Indexed Reuters article passage reviewed; direct retrieval unavailable'),
  r('The US International Trade Administration describes tax exemptions for registered issuers, certifiers and service providers, alongside licensing, fees and regulatory oversight.','US International Trade Administration',TRADE,'2024-06-25','Official description of sector framework')],
 [r('The tax framework applies to defined classes of registered participants, not just Tether. The same account describes the regulator’s power to suspend or cancel registrations.','US International Trade Administration: scope and safeguards',TRADE,'2024-06-25','Alternative explanation / constraints')],
 'Historical, episode-limited estimate of a policy partnership, not corruption. It does not establish that Ardoino wrote the law, personally received all company benefits, or paid for a license. Investment announcements are not completed-spending audits. Other executives’ alleged political channels are not assigned to him.',
 dict(levels=[2,1,2],range=[15,70],rationales=['A personally articulated executive role in investments aligned with a public policy project.','A registered business can benefit from broad sector incentives; a bespoke personal favor is not established.','Investment, a state-linked project and a policy-aligned relocation form a specific but non-exclusive commercial-policy relationship.'],sourceRefs=[[0,1,2],[0,3],[0,1,2]]))
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/009.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
