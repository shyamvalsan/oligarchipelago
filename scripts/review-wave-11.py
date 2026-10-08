"""Public-private deals: separate political access, commitments and realized benefits."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={}; R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led episode review; not independently editorially reviewed',confidence='Moderate / episode limited' if decision else 'Low / unresolved attribution',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
def rubric(levels,bounds,notes,refs):return dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
GRANGEMOUTH='https://www.gov.uk/government/news/500-jobs-protected-at-grangemouth-as-uk-government-partners-with-ineos-to-save-vital-plants-future'
UKEF='https://www.gov.uk/government/publications/category-a-project-supported-ineos-project-one-belgium/category-a-project-supported-ineos-project-one-belgium'
ADVOCACY='https://www.lse.co.uk/news/ineos-founder-jim-ratcliffe-calls-on-britain-to-cut-environmental-costs-2kujqfm0cu9djdi.html'
add('james-ratcliffe',
 'Ratcliffe publicly sought policy relief for industry, while INEOS secured named government-backed investments. These are concrete state–business relationships, but the reviewed record also shows public-interest conditions rather than an unrestricted personal windfall.',
 'Industrial policy advocacy ↔ government-backed investment with public safeguards','Project One support, 2023; policy advocacy and Grangemouth agreement, 2025',
 [r('Reuters reports Ratcliffe personally urging Britain to reduce environmental costs on businesses, presenting high costs as a barrier to investment.','Reuters: industrial-policy appeal',ADVOCACY,'2025-04-29','Personal policy advocacy','Indexed Reuters passages reviewed'),
  r('The UK announced more than £120 million of government support within a £150 million joint Grangemouth investment. Its release quotes Ratcliffe welcoming the partnership. These are announced project amounts, not personal payments.','UK Government: Grangemouth partnership',GRANGEMOUTH,'2025-12-17','Official announcement'),
  r('UK Export Finance disclosed €700 million principal support for INEOS Project One and named the participating UK exporters. It is export-finance support, not a €700 million cash gift to Ratcliffe.','UK Export Finance: supported project notice',UKEF,'2023-04-14','Official financing notice')],
 [r('The Grangemouth announcement identifies jobs and critical supply chains as public objectives. It restricts funding to site improvements, requires an operational commitment, and gives government a right to share future profits.','UK Government: conditions and rationale',GRANGEMOUTH,'2025-12-17','Public safeguards'),
  r('UKEF required environmental and social performance monitoring. Its notice describes an export-support decision subject to standards, not a finding of political favoritism.','UK Export Finance: support conditions',UKEF,'2023-04-14','Constraints / alternative explanation')],
 'The estimate concerns documented industrial-policy bargaining, not corruption or a claim that lobbying caused these awards. Announced support is not audited disbursement or profit. The chemicals plant is distinct from the closed oil refinery. Broad industry relief is not exclusive personal privilege.',
 rubric([2,2,2],[20,75],['Direct public policy advocacy by the owner-executive.','Named corporate financing and investment support, qualified by conditions and public objectives.','Investment, policy advocacy and a negotiated public partnership overlap; a personal reciprocal bargain is not established.'],[[0,1],[1,2],[0,1]]))
CFB='https://www.nyccfb.info/PDF/2021_Post-Election_Report.pdf'
FORBES='https://www.forbes.com/sites/samanthasharf/2019/03/14/billionaire-stephen-ross-insists-hudson-yards-is-for-everyone-and-hes-unhappy-that-no-one-believes-him/'
IBO='https://ibo.nyc.ny.us/iboreports/as-hudson-yards-refinances-old-debt-need-for-nearly-100-million-in-additional-funding-emerges-as-costs-continue-to-exceed-plan.pdf'
MAYOR='https://www.nyc.gov/mayors-office/news/2025/06/mayor-adams-helps-negotiate-agreement-add-nearly-50-percent-more-affordable-housing-units-to'
add('stephen-ross',
 'Ross combined substantial electoral spending with a development business benefiting from public financing and tax incentives. That overlap supports an influence estimate, not a claim that his donations purchased a particular approval.',
 'Private electoral spending ↔ publicly enabled urban development','Hudson Yards reporting, 2017–2019; city elections, 2021; western-yard proposal, 2025',
 [r('The Campaign Finance Board lists Stephen M. Ross as Common Sense NYC’s largest contributor, at $1 million. The committee spent about $1.52 million in City Council races; its total spending is not all Ross’s personal expenditure.','NYC Campaign Finance Board: 2021 post-election report, p. 93',CFB,'2022','Official campaign-finance analysis','PDF text reviewed, PDF page 104'),
  r('Forbes interviews Ross about Hudson Yards and distinguishes an estimated $1.4 billion in tax breaks from $4 billion of other city investment. Those aggregate figures are not a direct payment of the entire sum to him.','Forbes: Samantha Sharf interview',FORBES,'2019-03-14','Reported business benefit and subject interview'),
  r('IBO explains that qualifying commercial developments receive discounted payments in lieu of property taxes, whereas residential and hotel developments generally pay full taxes. It separately identifies city infrastructure and interest support.','NYC Independent Budget Office: Hudson Yards fiscal brief',IBO,'2017','Public financing mechanism','Indexed PDF passages reviewed; direct URL now redirects')],
 [r('Ross defended the development as connected to the wider city rather than an exclusive enclave. Public infrastructure can benefit others as well as the developer; the full city investment is not his private gain.','Forbes: subject response and scope',FORBES,'2019-03-14','Subject response / attribution limit'),
  r('The city’s June 2025 western-yard announcement describes a tentative deal including affordable homes, public space and a school, using future project tax revenue for infrastructure. Proposed delivery is not proof of completed public benefits.','NYC Mayor’s Office: western-yard proposal',MAYOR,'2025-06','Government rationale / proposed public benefits')],
 'Historical episode estimate, not proof of vote buying, guaranteed election outcomes or a quid pro quo. The 2021 donations postdate the earlier Hudson Yards arrangements. District-wide costs, tax concessions and company receipts are different quantities. This review does not audit later financing or assign all Related activity to Ross.',
 rubric([3,2,2],[25,80],['A large individually attributed contribution to a city-election spending vehicle.','Specific tax incentives and public infrastructure support for the associated development, not all private proceeds.','Documented political spending and public-facing development interests coexist; chronology does not prove purchased favors.'],[[0],[1,2],[0,1,2]]))
GLOBES='https://en.globes.co.il/en/article-icl-pressuring-netanyahu-to-drop-sheshinski-ii-1001057141'
LAW='https://mayafiles.tase.co.il/RPdf/1002001-1003000/P1002648-00.pdf'
COMMENT='https://www.prnewswire.com/news-releases/icls-comment-to-sheshinski-interim-recommendation-the-commissions-interim-recommendations-might-force-icl-to-stop-investing-in-israel-and-focus-on-cost-cutting-259718231.html'
add('idan-ofer',
 'Ofer personally joined high-level lobbying over ICL’s resource-tax exposure. The narrow episode shows political access and investment leverage, but the company’s own subsequent filing confirms that the contested tax legislation passed.',
 'Prime-ministerial access and investment pressure → unsuccessful attempt to stop a tax reform','Sheshinski II tax-policy campaign, 2014–2015',
 [r('Globes reports Ofer, the controlling shareholder of Israel Corporation, meeting Netanyahu with ICL chairman Nir Gilad during the effort to remove the resource-tax recommendations from the budget bill.','Globes: Stella Korin-Lieber and Amiram Barkat',GLOBES,'2015-07-30','Individual policy access'),
  r('ICL’s response to the interim recommendations warned that the proposed regime would curtail investment in Israel. This documents the company’s bargaining position, not an independently verified economic forecast.','ICL: public response to interim recommendations',COMMENT,'2014-05-18','Subject policy statement','Indexed company statement reviewed'),
  r('ICL reported that the Knesset approved legislation implementing Sheshinski II on 18 November 2015 and anticipated an adverse effect on profits, dependent on potash prices.','ICL: stock-exchange disclosure',LAW,'2015-11-19','Documented outcome limiting the inference','PDF text reviewed')],
 [r('The Prime Minister’s Office characterized the meeting as normal dialogue and said no decisions had been taken; the finance minister supported the reform.','Globes: government responses',GLOBES,'2015-07-30','Contemporaneous response'),
  r('The company’s enactment notice contradicts a claim that the campaign prevented the reform. It does not measure whether lobbying affected any details.','ICL: legislation outcome',LAW,'2015-11-19','Material counterevidence','PDF text reviewed')],
 'The zero benefit level is confined to stopping this reform, not a finding of no concessions or political advantages anywhere in Ofer’s career. The score does not cover later Dead Sea arrangements, whose assets and compensation require separate valuation. Company conduct is attributed to him only where personal involvement is reported.',
 rubric([3,0,2],[15,70],['A named personal meeting about an economically relevant policy dispute.','The objective of stopping the tax reform was not achieved: enactment is documented, rather than assumed from silence.','Political access and investment pressure are linked within the campaign, but the law’s passage limits evidence of successful feedback.'],[[0],[2],[0,1,2]]))
CSG='https://csg.com/en/news/csg-sets-the-record-straight-in-response-to-short-seller-allegations'
IPO='https://czechoslovakgroup.com/itf/CZECHOSLOVAK_GROUP_ITF_FINAL.pdf'
RESULTS='https://rss.globenewswire.com/news-release/2026/03/26/3262734/0/en/csg-full-year-2025-results-statement.html'
add('michal-strnad',
 'Strnad’s leadership and CSG’s major government procurement framework are documented. The framework’s headline value is not booked revenue, and the reviewed material does not establish his personal influence over the award or preferential terms.',
 'Owner-led defense supplier → public procurement; individual political mechanism unresolved','Slovak framework, December 2025; IPO and company disclosures, 2026',
 [r('The IPO announcement identifies Michal Strnad as owner and chairman, and names him for the chair/CEO role after the proposed corporate conversion.','CSG: intention-to-float announcement',IPO,'2026-01','Subject governance disclosure','Indexed PDF passage reviewed; direct URL redirected to a generic page'),
  r('CSG’s annual results describe ZVS Holding’s seven-year Slovak Ministry of Defence framework for ammunition for Slovakia and other EU states, with a potential value up to €58 billion.','CSG: full-year 2025 results statement',RESULTS,'2026-03-26','Subject contract disclosure','Indexed company results passages reviewed')],
 [r('CSG explicitly says €58 billion is a potential framework value, not a committed order book. Individual orders are required, and approximately €1 billion was included in the pipeline at the results announcement. Pipeline is not recognized revenue.','CSG: response to short-seller allegations',CSG,'2026-05-05','Material accounting and procurement distinction')],
 'No numerical estimate from defense-sector exposure or contract size alone. The company’s response is an interested-party statement, not independent validation. Personal political intervention, award comparisons and realized preferential gains need further evidence. No claim that the framework funded his IPO is adopted.')
TREASURY='https://home.treasury.gov/news/press-releases/jy0841'
URALKALI='https://www.themoscowtimes.com/archive/uralkalieurtms-rybolovlev-sells-25-stake-to-kerimov'
SALE='https://www.lse.co.uk/news/reuters-summit-russian-foreign-investors-could-buy-uralkali-shuvalov-axkf6itz6gwuwlp.html'
add('suleiman-kerimov-family',
 'Kerimov’s parliamentary position and politically sensitive investments provide substantial reasons for scrutiny. This file nevertheless separates documented office-holding from unverified claims that political protection produced particular financial benefits.',
 'Public office and strategic investments; extent of preferential protection unresolved','Uralkali purchase and sale discussions, 2010–2013; Treasury action, 2022',
 [r('Treasury identifies Kerimov as a Federation Council member and states that his 2018 designation was for being a Russian government official. Its 2022 notice blocks a trust in which it says he retained an interest.','US Treasury: Heritage Trust action',TREASURY,'2022-06-30','Official position and administrative action'),
  r('Combined Reuters, Bloomberg and Moscow Times reporting records his 25% Uralkali purchase and describes investor expectations that a Kremlin-loyal buyer would reduce political risk. Expectations are not a demonstrated concession awarded to him.','The Moscow Times: combined reports on Uralkali sale',URALKALI,'2010-06-15','Transaction and reported political-risk interpretation')],
 [r('The same acquisition report cites a source saying the purchase price exceeded market value. It does not establish that Kerimov acquired the stake at a state-engineered discount.','The Moscow Times: transaction pricing qualification',URALKALI,'2010-06-15','Countervailing transaction evidence'),
  r('Reuters reports the Russian government ruling out a state purchase of his stake during the 2013 Belarus dispute, while leaving open a private trade sale. That limits a claim of an assured public bailout.','Reuters: Shuvalov at investment summit',SALE,'2013-09-23','Documented limit on state support')],
 'No numerical position yet: public office and designation are not substitutes for evaluating every dimension. This review does not resolve the causal effect of political protection or reconstruct financing terms. Family wealth is not assigned identical conduct. Separate French tax and yacht disputes are outside this file; no criminal finding is inferred from the designation.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/011.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
