"""Regulatory roles, broad incentives and tax controversies are not personal capture."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Low / personal reciprocal influence unresolved',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
APPOINT='https://tether.io/news/tether-appoints-paolo-ardoino-as-ceo/'
AG='https://ag.ny.gov/press-release/2021/attorney-general-james-ends-virtual-currency-trading-platform-bitfinexs-illegal'
SETTLE='https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf'
RESPONSE='https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/'
DEFENSE='https://tether.io/news/tether-and-bitfinex-denounce-baseless-lawsuit-designed-to-undermine-the-cryptocurrency-community/'
RETIRE='https://www.theblock.co/news/markets/2025-01-02-tethers-general-counsel-retires-in-wake-of-mica-stablecoin-regulations-coming-into-effect-332986'
add('jean-louis-van-der-velde',
 'Van der Velde’s regulatory-facing executive role is documented. The reviewed sources establish company representation and a negotiated enforcement settlement, not a preferential political bargain benefiting him personally. Other Tether executives’ relationships are not automatically his.',
 'Executive regulatory relationships; personal political-economic exchange unresolved',
 'New York settlement in February 2021 and announced Tether leadership transition in October 2023',
 [r('Tether credits van der Velde with managing relationships with regulators internationally. This is a corporate description of his executive work, not proof that regulators granted him political favors.','Tether: CEO succession announcement',APPOINT,'2023-10','Primary description of individual regulatory role'),
  r('The official settlement identifies van der Velde as the director signing for the Tether entities. It requires the respondent companies to pay $18.5 million and cease trading with New York persons and entities.','New York Attorney General: settlement agreement',SETTLE,'2021-02-18','Primary personal signatory and corporate obligations','Relevant PDF text reviewed, including paragraphs 5, 55–57, 79 and signature page')],
 [r('The agreement says the companies neither admit nor deny the OAG findings. Its obligations and agency findings are not an individual criminal conviction of van der Velde.','New York Attorney General: settlement scope',SETTLE,'2021-02-18','Material legal and attribution distinction','Relevant PDF text reviewed, including paragraphs 5, 55–57, 79 and signature page'),
  r('The 2023 announcement says Ardoino would take over as Tether CEO in December, with van der Velde becoming an adviser while retaining the Bitfinex CEO role. The two companies and roles are distinct.','Tether: announced role change',APPOINT,'2023-10','Material historical role update')],
 'No numerical estimate: regulatory contact and settlement participation do not establish the preferential-benefit or feedback dimensions. This is not a comprehensive review of his investments, informal access or later activities. The 2023 announcement is a dated role update, not verification of every position held in 2026. Neither enforcement nor a change of title proves the absence of influence.')
add('stuart-hoegner',
 'Hoegner publicly defended Tether as its lawyer. That establishes personal involvement in legal advocacy, not control of government policy. The company enforcement outcome and his later retirement must be distinguished from a personal political-benefit mechanism.',
 'Legal advocacy and regulatory exposure; political reciprocity not established',
 'Public legal defense in 2020, company settlement in 2021 and reported retirement in January 2025',
 [r('Tether’s June 2020 statement identifies Hoegner as general counsel and quotes his rejection of market-manipulation claims in private litigation. These are counsel’s denials, not court findings.','Tether: response to amended class-action complaint',DEFENSE,'2020-06-04','Primary person-level legal advocacy'),
  r('The New York Attorney General’s separate 2021 announcement describes corporate reserve-disclosure findings and a settlement requiring $18.5 million, reporting and restrictions on New York trading. It is not a finding that Hoegner bought political protection.','New York Attorney General: company settlement announcement',AG,'2021-02-23','Primary enforcement context; separate proceeding')],
 [r('Tether’s settlement response disputes the attorney general’s characterization and emphasizes no admission of wrongdoing. This is the company’s response, not independent exoneration or the resolution of every private lawsuit.','Tether and Bitfinex: settlement response',RESPONSE,'2021-02-23','Subject response and proceeding boundary'),
  r('The Block reports the companies announcing Hoegner’s retirement and Michael Hilliard taking charge of legal affairs in January 2025. Earlier counsel responsibilities should not be presented as unchanged current duties.','The Block / RT Watson: legal leadership transition',RETIRE,'2025-01-02','Material role update')],
 'No numerical estimate. Representing a regulated business, contesting allegations and helping it navigate rules do not establish preferential governmental treatment. This review does not adjudicate the private litigation or infer a personal conviction from corporate findings. No colleagues’ political relationships or later corporate policy partnerships are transferred to Hoegner.')
PDD='https://www.sec.gov/Archives/edgar/data/1737806/000110465922049283/pdd-20211231x20f.htm'
TRANSITION='https://investor.pddholdings.com/static-files/9f447dfc-af0a-4f30-a023-21710fd23673'
add('colin-huang',
 'Pinduoduo disclosed preferential corporate tax treatment, but the reviewed filing ties it to enterprise and location-based programs rather than a demonstrated personal favor to Huang. His departure and changed voting rights also limit attribution of later company conduct.',
 'Company-level tax incentives; founder-level policy influence unresolved',
 'Tax treatment described for 2018–2021 and founder leadership transition in 2020–2021',
 [r('The 2021 annual report describes 15% corporate rates for specified operating entities, compared with a general 25% rate. It identifies high-technology status and qualifying Qianhai industries as the bases. These are historical company disclosures, not Huang’s personal tax rate.','Pinduoduo: 2021 Form 20-F, income-tax note 17',PDD,'2022-04-25','Primary company-level economic benefit'),
  r('The March 2021 announcement records Huang leaving the board after previously handing over the CEO role in July 2020. It links the founder personally to the company while dating the end of those responsibilities.','Pinduoduo: leadership transition announcement',TRANSITION,'2021-03-17','Primary founder role and chronology','Relevant PDF text reviewed, exhibits 99.2 and 99.3')],
 [r('The filing describes eligibility-based programs and possible withdrawal of preferential treatment. Eligibility and government discretion do not establish that Huang personally secured an exception.','Pinduoduo: tax eligibility and risk disclosure',PDD,'2022-04-25','Alternative program-based explanation'),
  r('The announcement says Huang’s ten-vote shares would lose their special voting rights and that he entrusted voting to the board. It attributes his departure to new research interests and leadership succession, not a stated finding of political coercion.','Pinduoduo: announcement and Huang’s shareholder letter',TRANSITION,'2021-03-17','Control change and founder’s explanation','Relevant PDF text reviewed, exhibits 99.2 and 99.3')],
 'No numerical estimate: a documented corporate benefit is not enough to fill the missing personal-leverage and exchange dimensions. These records do not prove that all informal influence ended, that every later incentive was ordinary, or that the disclosed historical rates still apply. The company’s explanation is not independent verification of his motives.')
REUTERS='https://www.uol.com.br/tilt/noticias/reuters/2012/05/17/senadores-dos-eua-acusam-saverindo-facebook-de-evitar-impostos.htm'
BILL='https://www.govinfo.gov/app/details/BILLS-112s3205is'
add('eduardo-saverin',
 'Saverin’s citizenship decision drew political criticism and proposed legislation. That controversy is not evidence that he controlled the tax rules or received a private exemption. His explanation and the distinction between a proposal and an adjudicated violation are essential.',
 'Citizenship and tax controversy; preferential rule-making not established',
 'US political response to citizenship renunciation before Facebook’s May 2012 IPO',
 [r('Reuters reports senators Schumer and Casey accusing Saverin of renouncing citizenship to avoid tax. Those are attributed political accusations, not a tax authority’s determination or a court finding.','Reuters / Kevin Drawbaugh, Portuguese edition republished by UOL',REUTERS,'2012-05-17','Contemporaneous attributed political criticism','Portuguese article passages reviewed'),
  r('GovInfo preserves S.3205 of the 112th Congress as introduced on May 17, 2012 and referred to the Finance Committee. The document is proposed legislation, not an order assessing Saverin’s tax or barring him from entry.','US Government Publishing Office: introduced Ex-PATRIOT bill',BILL,'2012-05-17','Primary legislative record and document type')],
 [r('Saverin told Reuters through a spokesman that he would pay hundreds of millions in US taxes and that living and working in Singapore motivated the decision. These are his stated reasons and commitments, not independently verified tax-payment records.','Reuters / UOL: Saverin’s response',REUTERS,'2012-05-17','Direct subject response','Portuguese article passages reviewed')],
 'No numerical estimate. Choosing a jurisdiction or being criticized by lawmakers does not establish influence over them. The reviewed record does not show him obtaining a bespoke tax concession or purchasing a legislative outcome. No current tax advice, verified tax liability, criminal finding or present-day travel status is inferred from this historical controversy.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/018.json').write_text(json.dumps(dict(profiles=P,rubrics={}),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews; 0 rubrics (personal reciprocal influence unresolved)')
