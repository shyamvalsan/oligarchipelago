"""Family attribution, philanthropy, and documented policy-access episodes."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Moderate / episode limited' if decision else 'Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
BOE='https://boe.es/diario_boe/txt.php?id=BOE-A-2021-18259'
add('amancio-ortega',
 'Ortega’s foundation participates in a major public-health funding agreement. That gives a private donor a role in public provision, but this agreement does not establish a commercial return or preferential treatment for Ortega.',
 'Private philanthropy and public-health provision; private benefit unresolved','Spanish proton-therapy funding agreement, October 2021',
 [r('Spain’s official gazette publishes an agreement under which the Amancio Ortega Foundation commits up to €280 million for ten proton-therapy systems in public healthcare.','Boletín Oficial del Estado',BOE,'2021-11-08','Official agreement')],
 [r('The agreement assigns equipment purchasing to the Ministry of Health and earmarks the donation for the stated medical purpose. It is not an award of €280 million to Ortega.','BOE: allocation of responsibilities',BOE,'2021-11-08','Official safeguards / scope')],
 'No score follows from philanthropy alone. Foundation influence, commercial interests and an individual reciprocal benefit require separate evidence. This file does not evaluate Inditex’s full regulatory history or equate charitable giving with political capture.')
BR='https://www.denverbroncos.com/team/front-office-roster/rob-walton'
BR2='https://www.denverbroncos.com/news/read-owners-greg-penner-carrie-walton-penner-announce-preferred-stadium-site-in-joint-letter-with-mayor-mike-johnston-gov-jared-polis'
add('rob-walton',
 'Rob Walton is an owner in a group pursuing a stadium project with public authorities. The reviewed announcement is signed by other family-group leaders and does not establish his personal negotiations or a delivered preferential benefit.',
 'Sports ownership and public infrastructure partnership; individual attribution unresolved','Broncos stadium announcement, September 2025; ownership biography in 2026',
 [r('The team identifies Rob Walton as an owner and dates his former Walmart chairmanship to 1992–2015. These are distinct roles and periods.','Denver Broncos official biography',BR,'2026','Subject institutional record'),r('The stadium letter by Greg Penner, Carrie Walton Penner, the mayor and governor proposes private funding alongside shared public improvements.','Denver Broncos joint announcement',BR2,'2025-09-09','Project / government partnership')],
 [r('The announcement promises private investment and no new taxes, but public improvements still require scrutiny. It does not show Rob personally directing the agreement or establish the final public cost.','Broncos letter: financing and attribution limits',BR2,'2025-09-09','Subject statement / scope')],
 'No numeric estimate: do not transfer his daughter’s or son-in-law’s actions to him. An announced funding plan is not a completed transaction or independently audited cost; older Walmart policy activity remains outside this review.')
TU='https://www.timesunion.com/capitol/article/bloomberg-walmart-heir-give-charter-school-fight-19369658.php'
WF='https://www.waltonfamilyfoundation.org/our-work/education-program/systems'
add('jim-walton',
 'The reviewed evidence establishes Jim Walton’s own education-policy financing, rather than merely a family association. It does not establish a private business return from that advocacy.',
 'Personal campaign financing for education policy; private economic return unresolved','New York charter-school advocacy, March 2024',
 [r('The Times Union reports Jim Walton contributing $750,000 to a pro-charter election fund.','Albany Times Union',TU,'2024-03-26','Individual campaign contribution'),r('The family foundation describes its support for national organizations, research and leadership intended to shape education policy. That is institutional context, not proof Jim directed every grant.','Walton Family Foundation',WF,'Accessed 2026-10-08','Subject policy statement')],
 [r('The foundation presents its aim as improved education systems. This explanation neither proves selfless motives nor supplies the missing evidence of Jim’s private economic gain.','Walton Family Foundation: stated purpose',WF,'Accessed 2026-10-08','Alternative explanation')],
 'No numerical estimate: policy influence and personal enrichment are different dimensions. Family and Walmart political activities require individual attribution; no whole-career clearance is implied.')
add('alice-walton',
 'Alice Walton’s own education-related campaign funding is documented. That establishes participation in policy advocacy, not a personal entitlement to favors or an economic exchange.',
 'Personal education-policy giving; reciprocal business advantage unresolved','New York education campaign contributions, 2020; reported March 2024',
 [r('The Times Union identifies Alice Walton’s $1.6 million in 2020 contributions to the education campaign group, separately from Jim’s later giving.','Albany Times Union',TU,'2024-03-26','Individual campaign contribution')],
 [r('The source identifies different donors and dates. Their contributions cannot be combined and assigned to Alice as if she alone made or controlled them.','Times Union: attribution limit',TU,'2024-03-26','Scope limitation')],
 'No score is assigned from a donation alone. Broader philanthropy, corporate policy, personal access and preferential economic outcomes need separate evidence; sharing a surname does not share conduct.')
JDD='https://www.lejdd.fr/Societe/cette-fois-laffaire-bettencourt-est-definitivement-terminee-3896665'
add('francoise-bettencourt-meyers',
 'The family name appears in a major political and legal controversy, but the reviewed personal proceeding against Françoise ended in dismissal. Her mother’s alleged relationships cannot serve as her own oligarchy assessment.',
 'Family litigation and attribution limits; personal political mechanism unresolved','Witness-influence proceeding, 2016–2019; dismissal reported May 2019',
 [r('Le JDD reports the investigating judge issuing a dismissal in the witness-influence proceeding against Françoise Meyers, which had begun in 2016.','Le Journal du Dimanche',JDD,'2019-05-05','Legal-status reporting')],
 [r('The reported order rejected a suspected improper link with a witness. The existence of the earlier proceeding is not a conviction or proof of an oligarchic bargain.','Le JDD: dismissal and scope',JDD,'2019-05-05','Counterevidence')],
 'No score: a family scandal does not establish this individual’s three rubric dimensions. This narrow legal-status review is not a review of all L’Oréal policy activity, and the underlying court order was not independently inspected.')
JK='https://www.insidephilanthropy.com/home/2022-10-31-a-new-koch-in-town-4-things-to-note-about-the-philanthropy-of-americas-richest-woman'
add('julia-koch',
 'The reviewed account distinguishes Julia’s own giving from the much larger political network associated with her late husband and brother-in-law. Inheritance cannot transfer their political conduct to her.',
 'Personal giving versus family-network attribution; private benefit unresolved','Philanthropic and political giving described in October 2022',
 [r('Inside Philanthropy describes Julia’s charitable activity and some Republican political donations, while distinguishing her from an established political megadonor at that time.','Inside Philanthropy',JK,'2022-10-31','Individual profile','Indexed source passage reviewed; page retrieval unavailable')],
 [r('The article discusses an emerging philanthropic role, not evidence that Julia personally directs every Koch network campaign. A family ownership stake is not proof of those instructions.','Inside Philanthropy: attribution limit',JK,'2022-10-31','Scope limitation','Indexed source passage reviewed; page retrieval unavailable')],
 'No score: the reviewed source is dated and limited. It cannot establish the current scale of giving or a reciprocal commercial favor, and it cannot justify importing Charles or David Koch’s assessment.')
WSJ='https://www.livemint.com/technology/the-kill-or-be-killed-fight-for-crypto-s-future/amp-11741055797869.html'
WH='https://www.whitehouse.gov/fact-sheets/2025/01/fact-sheet-executive-order-to-establish-united-states-leadership-in-digital-financial-technology/'
add('giancarlo-devasini',
 'Reporting links Devasini personally to an attempted political-protection channel. The reported expectation of help is not proof that an investigation was stopped or a law privately purchased.',
 'Financial relationship and access → attempted regulatory protection','Tether–Cantor relationship and policy debate, 2024–March 2025',
 [r('The Journal reports associates describing Devasini’s expectation that Lutnick would oppose harmful legislation, alongside Cantor’s financial relationship with Tether. The account relies on reported conversations.','The Wall Street Journal via Mint',WSJ,'2025-03-04','Reported private discussions'),r('The January executive-order fact sheet establishes a government digital-assets working group and a broad regulatory initiative, not an exemption naming Devasini.','White House',WH,'2025-01-23','Official policy context')],
 [r('Lutnick told senators he had not suggested improper action for Tether. An expectation attributed to Devasini is not an adjudicated quid pro quo.','WSJ: Lutnick response',WSJ,'2025-03-04','Subject response')],
 'Historical episode only. Financial alignment warrants scrutiny, but a specific delivered exception is not established. This estimate does not assign colleagues’ conduct to Devasini or assert current enforcement status.',
 dict(levels=[3,1,2],range=[20,70],rationales=['A personally reported channel to senior political access.','Broad policy alignment, not a demonstrated bespoke exemption.','Reported expectations and financial alignment support an attempted-protection inference, not a proven bargain.'],sourceRefs=[[0],[1],[0]]))
HC='https://oversight.house.gov/wp-content/uploads/2022/04/Norman-Letter-to-OMB-042122.pdf'
DFC='https://www.dfc.gov/media/press-releases/dfc-ceo-marks-us-500-million-loan-strategic-supply-chain-diversification'
OIG='https://www.oversight.gov/reports/inspection-dfcs-first-solar-and-bio-e-projects'
add('lukas-walton',
 'Lawmakers questioned whether Walton’s political giving influenced a loan to a company in which he held a minority stake. The loan is documented; the alleged donor-to-award connection is not established by the reviewed inspection.',
 'Political donations and minority investment ↔ questioned development-finance award','First Solar DFC financing, 2021–2024; inspector-general review, September 2025',
 [r('A 2022 Republican oversight letter describes Walton holding 4.9% of First Solar and questions his political donations in relation to DFC financing. This is an allegation and records request, not a finding.','House Oversight member letter',HC,'2022-04-21','Congressional concern','Indexed PDF passage reviewed'),r('DFC confirms a $500 million loan for First Solar’s Indian facility and describes supply-chain diversification, jobs and development objectives. This is corporate debt financing, not a personal grant to Walton.','US International Development Finance Corporation',DFC,'2024-01-11','Official financing record','Indexed source passage reviewed')],
 [r('The 2025 inspector-general summary identifies monitoring weaknesses and mixed impact progress. Its stated scope is project compliance and impact, not establishing that Walton bought the loan decision.','DFC Office of Inspector General via Oversight.gov',OIG,'2025-09-30','Independent inspection / scope')],
 'No score: personal political leverage in the award and preferential terms remain unresolved. A minority stake is not sole ownership, and neither an oversight allegation nor this differently scoped inspection proves or clears a donor-related bargain.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/006.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
