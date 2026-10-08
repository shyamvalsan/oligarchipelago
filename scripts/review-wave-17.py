"""Public financing, contractual safeguards, and unresolved personal attribution."""
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
JONES='https://bobbyrossjr.com/2004/10/31/october-2004-the-associated-press/'
ARL='https://www.arlingtontx.gov/News-Articles/2025/August/Touchdown-City-of-Arlington-Pays-Off-ATT-Stadium-Debt-10-Years-Early'
add('jerry-jones',
 'Jones’s Cowboys financed a substantial campaign for voter-approved stadium support. Public construction funding is documented, but it was a shared-cost deal with private overruns, not a personal cash gift. The inference concerns a business-backed campaign securing favorable public investment.',
 'Team-financed referendum campaign → public stadium contribution',
 'Arlington stadium referendum in 2004 and construction financing; city repayment update in August 2025',
 [r('AP’s contemporaneous report says the Cowboys contributed nearly $5.1 million to the pro-stadium committee. Jones owned the team but stayed out of the public campaign spotlight; the reported donor was the Cowboys, not a separately identified personal check.','Bobby Ross Jr. / Associated Press, author’s republication',JONES,'2004-10-31','Contemporaneous political campaign and ownership attribution'),
  r('Arlington records voter approval of taxes supporting a $325 million city construction contribution. The stadium ultimately exceeded $1.2 billion, with the Cowboys responsible for expenses above the city’s contribution.','City of Arlington: stadium debt update',ARL,'2025-08-12','Primary public financing and private cost allocation')],
 [r('The 2004 report describes proposed team rent and youth-sports commitments, plus the mayor’s jobs-and-development defense. Competing commissioned studies disagreed on the economic outcome; anticipated benefits were not established facts.','Associated Press / Bobby Ross Jr.: public case and contested projections',JONES,'2004-10-31','Material public-benefit rationale and proposed consideration'),
  r('Arlington announced a final debt payment scheduled for 15 August 2025, a decade early. Its stated total of about $490.3 million includes principal, interest and fees, unlike the $325 million construction contribution.','City of Arlington: repayment accounting',ARL,'2025-08-12','Financing-cost distinction and dated outcome update')],
 'This is an editorial inference about the reviewed campaign and financing bargain, not bribery, illegitimate voting or a finding that the stadium made a net loss for taxpayers. Team spending is not automatically personal spending. No conduct is transferred to other relatives in the Forbes family entry.',
 rubric([3,2,2],[25,80],['Substantial team-funded electoral advocacy is documented; individual operational direction is less clear.','A specific public contribution benefits the team’s stadium project, with private financial obligations.','Advocacy and the requested financing outcome connect, but voter choice and public objectives remain real alternative explanations.'],[[0],[1],[0,1]]))
HOCHUL='https://www.governor.ny.gov/news/governor-hochul-announces-joint-public-private-agreement-ensure-buffalo-bills-remain-new-york'
ERIE='https://www4.erie.gov/caucus-rep/press/erie-county-legislature-approves-bills-stadium-deal-paving-way-construction-begin'
LEASE='https://www2.erie.gov/legislature/sites/www2.erie.gov.legislature/files/uploads/Misc_Uploards/10%20-%20Bills%20-%202023%20-%20Non-Relocation%20Agreement%20%5BExecuted%5D.pdf'
AP='https://apnews.com/article/8c56fad9d970f2b17429d3ae779f70ba'
add('terrence-pegula',
 'Pegula participated in the Bills’ public-private stadium bargain. It secured substantial public construction funding in return for a long-term team commitment, with public ownership and contractual safeguards. This is economic bargaining power, not proof of corruption or a personal subsidy equal to the project cost.',
 'Team retention and private investment ↔ public stadium financing',
 'New Buffalo Bills stadium agreement, 2022–2023; reported cost update in November 2024',
 [r('New York’s announcement quotes Terry and Kim Pegula welcoming the partnership and describes negotiations securing a 30-year team commitment alongside state, county, NFL and team financing.','Governor of New York: initial stadium agreement',HOCHUL,'2022-03-28','Primary owner-level participation and policy bargain'),
  r('The county legislature’s May 2023 release records a 10–0 approval and construction contributions of $600 million from the state and $250 million from the county.','Erie County Legislature, Republican Caucus: agreement approval',ERIE,'2023-05-04','Primary approval and public construction financing'),
  r('Section 5 of the executed non-relocation agreement also identifies public maintenance and capital-improvement funding. The $850 million construction figure is not the full lifecycle public commitment.','Erie County: executed Bills non-relocation agreement, section 5',LEASE,'2023','Primary distinction between construction and ongoing support','Relevant PDF text reviewed, especially sections 2 and 5; not every related agreement')],
 [r('The county release says the state will own the complex and lease it to the team; the Bills must bear construction overruns.','Erie County: ownership and overrun allocation',ERIE,'2023-05-04','Contractual safeguards'),
  r('AP reports the construction projection rising above $2.1 billion while the state/county share remained $850 million. Team owners were responsible for more than $560 million in overruns. These were reported projections, not a completed-project audit.','Associated Press / John Wawrow: cost update',AP,'2024-11-15','Independent dated cost update','AP article passages reviewed'),
  r('The agreement prioritizes court enforcement of the non-relocation promise. Fallback damages apply if that relief is unavailable or denied, and the percentage declines from year 15. It is not an unconditional right to leave by paying a fee.','Erie County: executed agreement, section 5',LEASE,'2023','Material enforcement terms','Relevant PDF text reviewed, especially sections 2 and 5; not every related agreement')],
 'Episode-limited assessment of financing leverage. Public ownership, private costs and retention obligations qualify the benefit. The receipts do not prove a purchased official decision, and forecasts of community returns are not audited outcomes. No claim is made that construction funding equals Pegula’s personal income or that all public costs end with construction.',
 rubric([2,2,2],[20,75],['Direct participation in a specific government bargain is documented, not control of the state.','Public financing supports the team’s facility, with meaningful counter-obligations.','The retention-for-financing exchange is explicit; public-interest explanations limit an oligarchic interpretation.'],[[0,1],[1,2],[0,1]]))
RAMS='https://www.therams.com/team/front-office-roster/e-stanley-kroenke'
LAIST='https://laist.com/news/the-deal-that-helped-bring-sofi-stadium-to-inglewood-isnt-legally-valid-judge-rules'
RULING='https://www.decisiondepot.legal/cases/279259'
add('stanley-kroenke',
 'Kroenke’s stadium development involved a city reimbursement agreement as well as private construction funding. The agreement’s validity was rejected in a September 2026 ruling. Disputed claims, payments and legal outcomes must not be collapsed into a single subsidy figure.',
 'Private development and disputed public infrastructure reimbursement',
 'Inglewood’s 2015 development agreement and September 2026 litigation update',
 [r('The Rams identify Kroenke as owner/chairman and describe him financing SoFi’s construction. This establishes his project role, not an independent audit of every public contribution.','Los Angeles Rams: owner biography',RAMS,'Accessed 2026-10-08','Primary corporate role and financing account'),
  r('LAist reports that Kroenke-linked companies claimed roughly $400 million in infrastructure/service reimbursement under the 2015 agreement. That is a disputed demand, not money established as received.','The LA Local, republished by LAist',LAIST,'2026-09-12','Reported public-private arrangement and disputed claim')],
 [r('LAist reports the September 1 ruling against the agreement’s validity. Hollywood Park disagreed, defended its performance and said it could appeal; Inglewood defended the ruling while expressing interest in further talks.','LAist / The LA Local: ruling and both sides’ responses',LAIST,'2026-09-12','Material adverse ruling and developer response'),
  r('A third-party reproduction of the ruling identifies the challenged counts as two breach-of-contract claims. It does not establish final disposition of every claim or an appeal outcome.','DecisionDepot: Pincay RE v. City of Inglewood, 25TRCV04256',RULING,'2026-09-01','Procedural-scope qualification','Relevant reproduced ruling section reviewed; not the official docket. The page also contains unrelated preceding case text.')],
 'No numerical estimate. This review does not resolve the net economic concession, individualized policy influence or ultimate litigation outcome. Privately financed construction does not rule out other public support, and invalidity of a development agreement is not a corruption conviction. The latest substantive update reviewed is dated September 12, 2026.')
AEC='https://transparency.aec.gov.au/AnnualDonor/ReturnDetail?returnId=69575'
SBS='https://www.sbs.com.au/news/article/who-are-the-biggest-donors-to-australias-political-parties/ojow9dhy3'
VISY='https://frrr.org.au/?p=72312'
NSW='https://www.parliament.nsw.gov.au/lcdocs/other/14296/Answers%20to%20QONs%20-%20Hon.%20John%20Barilaro%20MP%2C%20Deputy%20Premier%20-%20Received%209%20March%202021.pdf'
add('anthony-pratt',
 'A company connected to Pratt reported political giving, and Visy received a contested bushfire-recovery grant. These are relevant leads, but the reviewed record does not establish that his personal intervention secured the grant or that a donation purchased it.',
 'Corporate political giving and recovery grant; personal reciprocal influence unresolved',
 'Tumut recovery activity and grant in 2020–2021; separate 2023–2024 donor disclosure',
 [r('FRRR’s April 2020 announcement identifies Anthony Pratt as Visy executive chairman and quotes him about the company’s Tumut recovery involvement. The foundation grants described there are distinct from the later government grant.','Foundation for Rural & Regional Renewal: Tumut recovery announcement',VISY,'2020-04-03','Primary person-level company role','Indexed announcement passages reviewed; direct page retrieval failed'),
  r('The AEC’s 2023–24 return identifies Pratt Holdings Pty Ltd as the donor and reports A$1 million given to political parties. It is a company return, not a personal Anthony Pratt filing.','Australian Electoral Commission: annual donor return 69575',AEC,'2023–2024 financial year','Primary corporate political-finance disclosure'),
  r('SBS identifies Pratt Holdings as Pratt’s company and reports federal Labor as the recipient of the A$1 million. This supplements the AEC summary, whose detailed recipient table was not exposed by the page extraction.','SBS News: annual political-finance disclosures',SBS,'2025-02-03','Reported ownership and recipient attribution'),
  r('Answers to a NSW parliamentary inquiry acknowledge A$10 million in public support for the Visy project and describe an equal company contribution.','NSW Parliament: Deputy Premier’s answers on notice',NSW,'2021-03-09','Primary acknowledgment of company-level grant','Indexed PDF passages reviewed; direct document retrieval failed')],
 [r('The Deputy Premier’s answers defend independent, merit-based assessment and anticipated forestry jobs. Those are the government’s explanations, not independent verification that every claimed job materialized.','NSW Parliament: grant assessment and employment defense',NSW,'2021-03-09','Material alternative explanation','Indexed PDF passages reviewed; direct document retrieval failed'),
  r('The reviewed donor return concerns 2023–24, after the 2020–21 grant episode. It cannot by itself establish a prior inducement for that grant.','Australian Electoral Commission: disclosure period',AEC,'2023–2024 financial year','Chronology and attribution boundary')],
 'No numerical estimate: receipt of a grant plus political giving does not establish an exchange. Company and individual attribution remain distinct. This is not a comprehensive review of earlier Australian giving, US political activity, or every Visy assistance program; no conclusion is inferred from the missing evidence.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/017.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
