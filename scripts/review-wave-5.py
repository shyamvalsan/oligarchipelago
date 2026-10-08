"""Additional source-led reviews; institutional influence is not automatically private patronage."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Moderate / episode limited' if decision else 'Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
MP='https://www.michiganpublic.org/politics-government/2017-09-12/quicken-loans-spends-big-on-lobbying-reaps-legislative-reward'
MP2='https://www.michiganpublic.org/politics-government/2017-06-08/governor-signs-new-tax-incentives-into-law-to-boost-development-of-blighted-sites'
MSF='https://www.michiganbusiness.org/globalassets/documents/msf-board/msf-board-packets/february-2025-msf-board-packet_final---web-upload.pdf'
add('daniel-gilbert',
 'Gilbert supported legislation that enabled major incentives for his development business. The policy campaign and subsequent award support an influence estimate, while public redevelopment objectives and program conditions limit a patronage interpretation.',
 'Development interests → lobbying and legislation → conditional project incentives','Michigan brownfield legislation, 2017; award documented in 2025 board packet',
 [r('Michigan Public identifies Gilbert as a prominent supporter of the 2017 brownfield tax-incentive law.','Michigan Public',MP2,'2017-06-08','Individual policy role'),r('Reporting records increased Quicken Loans lobbying and donations by employees around passage. Employee donations are not automatically Gilbert’s personal donations or instructions.','Michigan Public',MP,'2017-09-12','Corporate lobbying context'),r('The February 2025 MSF packet records a 2018 award of up to $618 million in reimbursements to Bedrock for four projects. A proposed financing-mix amendment would not increase the overall cap.','Michigan Strategic Fund, packet pp. 119–120',MSF,'2025-02-25','Official program record','PDF text reviewed')],
 [r('Lawmakers told reporters they supported the legislation to help their districts. The law was not confined to Gilbert’s projects, and the account does not establish a vote-for-payment bargain.','Michigan Public: legislative response',MP,'2017-09-12','Alternative explanation'),r('The board material describes eligible-cost reimbursement and third-party analysis, not an unconditional personal grant to Gilbert. The award ceiling is not the amount already paid.','Michigan Strategic Fund: award constraints',MSF,'2025-02-25','Official program conditions','PDF text reviewed')],
 'Scope is Michigan’s brownfield program, not all projects or the separate federal Opportunity Zones debate. Correlation between giving and votes is not causation. Later proposals are not treated as approved awards.',
 dict(levels=[3,2,2],range=[30,75],rationales=['Personal advocacy plus a documented corporate policy campaign.','Large, conditional project-specific reimbursements under a wider program.','Policy advocacy and business benefit are linked, but public-purpose explanations remain substantial.'],sourceRefs=[[0,1],[2],[0,1,2]]))
ABC='https://www.abc.net.au/news/2023-06-25/meritons-plans-to-redevelop-sydney-eastern-precinct/102515194'
NSW='https://www.planningportal.nsw.gov.au/rezoning-reviews/planning-panel-or-commission-decision/1406-1408-anzac-parade-little-bay-little-bay-cove'
add('harry-triguboff',
 'Triguboff’s own correspondence links a rezoning request to private development and promised public revenue. The reviewed record also shows that planning bodies refused an earlier proposal: access and pressure did not equal automatic approval.',
 'Direct policy lobbying for higher-density development','Little Bay correspondence, 2022–2023; prior decision in 2021',
 [r('ABC reviewed correspondence in which Triguboff urged senior NSW officials to accelerate rezoning and highlighted revenue for government alongside Meriton’s development interest.','ABC News',ABC,'2023-06-25','FOI-based reporting'),r('The official portal records the earlier Little Bay review as refused, with a decision not to proceed dated 17 June 2021. This is that application’s status, not a verdict on every later proposal.','NSW Planning Portal',NSW,'2021-06-17','Official planning decision')],
 [r('Meriton told ABC that housing supply, affordable homes and transport contributions supported its proposal. The prior refusal is evidence of institutional resistance, not a received rezoning favor.','ABC News: company response',ABC,'2023-06-25','Subject response / counterevidence')],
 'This estimate concerns the documented lobbying episode only. It does not assert the current status of every application or infer corruption from a public-benefit offer. Other donations and developments need separate assessment.',
 dict(levels=[2,0,2],range=[15,60],rationales=['Direct correspondence with senior officials seeking a policy change.','The reviewed earlier proposal was refused; no delivered preferential rezoning is established within this episode.','An explicit attempted link between development value and government revenue, not proof of a private favor.'],sourceRefs=[[0],[1],[0,1]]))
TI='https://www.transparency.de/aktuelles/detail/article/neue-enthuellungen-im-fall-reinhold-geilsdoerfer-geheimvertrag-mit-lidl-gruender'
K='https://www.kontextwochenzeitung.de/gesellschaft/302/lidl-lohnt-sich-fuer-einen-4130.html'
add('dieter-schwarz',
 'The reviewed education-foundation episode raises governance questions but does not establish a personal corrupt exchange by Schwarz. Crucially, later reporting says the associated criminal investigation was closed for lack of supporting evidence.',
 'Private education funding and public-university governance; personal benefit unresolved','Foundation / university staffing controversy, 2016–2017',
 [r('Transparency International’s press digest described allegations involving a foundation contract for then-university president Reinhold Geilsdörfer. These were allegations, not a conviction of Schwarz.','Transparency International Deutschland press digest',TI,'2016-08-09','Reported allegations')],
 [r('Kontext subsequently reported that the investigation had been closed because evidence of bribery was not found. The initial allegation must not be presented as a proven or still-pending case.','Kontext Wochenzeitung',K,'2017-01-11','Legal-status follow-up')],
 'The reviewed materials concern foundation governance and an official’s role, not a verified person-level enrichment mechanism for Schwarz. No score is assigned. The legal status comes from reporting, not a reviewed prosecutor’s decision.')
MA='https://uk.investing.com/news/stock-market-news/at-china-political-meeting-internet-bosses-are-out-chip-execs-are-in-2937309'
add('ma-huateng',
 'Ma’s former parliamentary membership is documented, as is his absence from the 2023 delegate list. That role establishes access in a particular period, not personal control of the state or a specific economic favor.',
 'Former legislative access under significant state oversight','NPC representation change, March 2023',
 [r('Reuters reports Ma having served two five-year NPC terms before being absent from the 2023 list. The article describes shifting state priorities toward hardware rather than internet businesses.','Reuters via Investing.com',MA,'2023-03-03','Political role and change')],
 [r('Reuters places the change in the context of state scrutiny of internet businesses. A former seat cannot be carried forward as a current role or equated with freedom from regulation.','Reuters: limits of access',MA,'2023-03-03','Counterevidence / scope')],
 'No score: this review does not establish the preferential-benefit and reciprocal-exchange dimensions. Nationality, market share, censorship exposure and compliance with state direction do not automatically establish personal oligarchic leverage.')
CP='https://en.cppcc.gov.cn/2024-03/07/c_968760.htm'
EU='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2754'
add('robin-zeng',
 'Zeng’s policy-advisory role and CATL’s place in a state-supported industry merit examination. These sources alone cannot determine whether Zeng personally obtained exceptional favors through political leverage.',
 'Policy advisory role and battery industrial policy; personal reciprocal mechanism unresolved','CPPCC proposal and EU battery-policy findings, 2024',
 [r('The CPPCC website identifies CATL founder Zeng Yuqun as a national committee member and records his vehicle-to-grid policy proposals. Robin Zeng and Zeng Yuqun refer to the same founder.','CPPCC / China Daily',CP,'2024-03-07','Official institutional reporting','Indexed source passage reviewed; page retrieval unavailable'),r('The European Commission’s definitive BEV regulation discusses state support and pricing policies across China’s battery industry, including CATL-related transactions. This is a trade investigation, not a personal corruption finding.','European Commission, Regulation 2024/2754',EU,'2024-10-29','Official sector-level findings')],
 [r('The regulation records objections by China and industry parties to the Commission’s pricing and subsidy analysis. Sector-wide government policy is distinct from a benefit negotiated personally by Zeng.','European Commission: objections and scope',EU,'2024-10-29','Competing arguments')],
 'No numeric estimate: advisory membership and sector subsidies cannot fill the missing person-specific exchange evidence. This file does not estimate personal subsidy receipts or assert the current status of later trade litigation.')
ION='https://uk.marketscreener.com/news/italy-court-voids-government-s-golden-power-decision-on-ion-owned-cedacri-s-loan-ce7d51dcde8df126'
add('andrea-pignataro',
 'The reviewed Cedacri episode shows a company challenging government restrictions through the courts. A successful appeal does not itself establish political favoritism toward Pignataro.',
 'Strategic-asset regulation and judicial review; preferential political exchange unresolved','Cedacri loan conditions, 2023; appeal decision, December 2025',
 [r('Reuters reports Italy imposing conditions on an ION-owned Cedacri loan, followed by the Council of State voiding that 2023 decree in December 2025. ION is identified as Pignataro-owned.','Reuters via MarketScreener',ION,'2025-12-05','Court reporting')],
 [r('The court’s reported reasoning concerned the pledge structure and limits on government intervention. A legal remedy is not evidence of a privately arranged favor or captured court.','Reuters: judicial reasoning',ION,'2025-12-05','Alternative explanation')],
 'No score is assigned from regulatory exposure or business concentration. Broader political relationships and other proceedings are outside this narrow review; this is not a legal clearance.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/005.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
