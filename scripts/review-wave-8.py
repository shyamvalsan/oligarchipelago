"""Shipping reviews: distinguish personal access, unsuccessful bids and ownership dates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Low to moderate / episode limited' if decision else 'Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
REUTERS='https://www.investing.com/news/stock-market-news/battle-heats-up-for-hamburg-port-operator-as-msc-makes-14-billion-offer-3173340'
MSC='https://www.msc.com/en/newsroom/press-releases/2024/msc-group-completes-acquisition-of-minority-stake-in-hhla'
OPERA='https://www.hamburg.de/politik-und-verwaltung/behoerden/behoerde-fuer-kultur-und-medien/oper/worauf-haben-sich-stiftung-und-stadt-vertraglich-geeinigt--1018726'
add('klaus-michael-kuehne',
 'Kuehne publicly sought a city privatization arrangement favoring his holding company or Hapag-Lloyd. Hamburg instead completed its partnership with MSC. The estimate covers this unsuccessful commercial-policy effort, not his whole career.',
 'Personal advocacy for port ownership → requested city deal, not an achieved award','HHLA privatization debate, September 2023–November 2024; separate opera agreement, 2025',
 [r('Reuters quotes Kuehne seeking an agreement with Hamburg to privatize HHLA toward his holding company or Hapag-Lloyd, in which he held a substantial stake. This identifies a personal request and a direct economic interest.','Reuters: Friederike Heine and Jan Schwartz',REUTERS,'2023-09-13','Personal statement / commercial interest','Indexed Reuters article passages reviewed'),
  r('MSC subsequently announced completion of its HHLA joint venture with Hamburg, with the city retaining 50.1% and MSC holding 49.9%. Kuehne was not the successful private partner in this transaction.','MSC transaction-completion announcement',MSC,'2024-11-28','Outcome / company announcement'),
  r('Hamburg separately describes a foundation-led opera project with public participation and a capped €147.5 million city contribution for site-specific costs. This is a different agreement, not a reward from the port deal.','City of Hamburg: opera agreement summary',OPERA,'2025; accessed 2026-10-08','Separate public-philanthropic partnership')],
 [r('Hamburg’s opera summary provides for the foundation’s shares to be donated to the city after completion and assigns additional construction risks to the foundation. Public spending on that project is not a personal cash grant to Kuehne.','City of Hamburg: ownership and risk terms',OPERA,'2025; accessed 2026-10-08','Terms / alternative explanation')],
 'The zero benefit component means the requested HHLA award did not go to him in this episode. It does not mean no benefit from any government anywhere. No causal exchange between opera philanthropy and shipping policy is established; the two projects are kept separate.',
 dict(levels=[2,0,1],range=[5,55],rationales=['An individually attributable attempt to shape a city privatization decision.','The requested HHLA award did not go to him in this reviewed episode.','Commercial interests motivated the request; a successful reciprocal political bargain is not established.'],sourceRefs=[[0],[1],[0,1]]))
REP='https://genova.repubblica.it/cronaca/2024/06/12/news/inchiesta_in_liguria_interrogato_larmatore_gianluigi_aponte-423219936/'
RAI='https://www.rainews.it/tgr/liguria/articoli/2024/06/aponte-in-procura-623ad003-09d2-436b-9d5c-34ca6ba18eab.html'
TRANSFER='https://www.marketscreener.com/news/msc-transfers-ownership-to-children-of-founder-gianluigi-aponte-ce7e50ded98ff226'
add('gianluigi-aponte',
 'Reporting on the Genoa port case describes Aponte personally contacting political leadership about a concession connected to his business interests. This supports a specific access–benefit relationship, while the reporting expressly identifies him as a witness, not a suspect.',
 'Personal mayoral access ↔ long-term port-concession interest','Genoa terminal-concession contacts in 2021, reported June 2024; ownership update announced April 2026',
 [r('La Repubblica reports an intercepted November 2021 call in which Aponte told Spinelli he had obtained reassurance from Genoa’s mayor about a thirty-year concession. It attributes a 45% interest in the terminal operator to Aponte.','La Repubblica: Genoa investigation reporting',REP,'2024-06-12','Reported investigation material','Indexed article passages reviewed; direct retrieval failed')],
 [r('Rai reports that Aponte was heard as a witness and was not under investigation in this proceeding at the time. An alleged payment by another businessman must not be attributed to him.','Rai regional news: Pietro Adami',RAI,'2024-06-12','Procedural status / attribution limit'),
  r('Reuters reports MSC’s April 2026 announcement that ownership had passed to Diego and Alexa in late 2025, while Gianluigi remained executive chairman. Historical ownership and present executive influence are not interchangeable.','Reuters: MSC succession announcement',TRANSFER,'2026-04-13','Ownership / role update','Indexed Reuters article passages reviewed')],
 'Historical, episode-limited estimate. The underlying intercept and concession contract were not independently inspected. A report of access is not proof of an unlawful personal bargain, and being a witness is not an accusation. The fixed Forbes annual wealth snapshot is retained rather than silently rewritten after the ownership announcement.',
 dict(levels=[3,2,2],range=[25,80],rationales=['A personally attributed conversation with the mayor is reported in investigation coverage.','A specific long-term concession and economic interest are identified; preferential terms are not independently established.','The reported access and concession interest form a concrete but incompletely corroborated feedback mechanism.'],sourceRefs=[[0],[0],[0]]))
FOUNDATION='https://mscfoundation.org/about-us/transparency/governance'
CH='https://find-and-update.company-information.service.gov.uk/company/02974020/persons-with-significant-control'
add('rafaela-aponte-diamant',
 'Rafaela’s foundation governance and historical company-control role are documented separately from her husband’s political contacts. The reviewed records do not establish that she directed those contacts or secured a preferential public decision.',
 'Foundation governance and historical corporate control; personal political mechanism unresolved','MSC Foundation governance reviewed October 2026; UK subsidiary control filing effective February 2026',
 [r('The MSC Foundation lists Rafaela Aponte as a board member in a governance structure that sets strategy and approves initiatives. This establishes her own institutional role, not the direction of every MSC business negotiation.','MSC Foundation: governance',FOUNDATION,'Accessed 2026-10-08','Subject institutional record'),
  r('Companies House records Rafaela’s former significant-control status at MSC Cruises Limited as ceased on 20 February 2026. This is a filing about the named UK entity, not a complete audit of the worldwide group or her personal wealth.','UK Companies House: company 02974020',CH,'2026-02-20 effective date','Company control filing')],
 [r('The foundation describes Swiss supervisory oversight, an independent advisory board and external financial audit. These are governance arrangements, not proof of no political influence or an audit of the shipping group’s concessions.','MSC Foundation: oversight scope',FOUNDATION,'Accessed 2026-10-08','Subject governance safeguards')],
 'No numerical estimate: do not copy Gianluigi’s contacts, scores or allegations onto Rafaela. A control filing is not evidence of misconduct, and its effective date does not authorize replacing the Forbes annual snapshot with an inferred new wealth figure. Broader person-specific research remains necessary.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/008.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
