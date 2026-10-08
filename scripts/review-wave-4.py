"""Reviewed episodes: distinguish policy access, attempted influence and actual benefits."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Moderate / episode limited' if decision else 'Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
AP='https://apnews.com/article/7e2615d50a3fc0563109ed0eeb4c41e1'
BD='https://breakingdefense.com/2026/05/pentagon-awards-dell-9-7-billion-contract-to-consolidate-software-licenses/'
add('michael-dell',
 'Dell’s support for a presidential savings initiative sits alongside a major government software agreement. This warrants scrutiny, but the reviewed procurement account supplies an ordinary purchasing rationale rather than evidence of a personal exchange.',
 'Public philanthropy and government procurement; causal connection unproven','Trump Accounts pledge, December 2025; software procurement, May 2026',
 [r('Michael and Susan Dell pledged $6.25 billion toward children’s investment accounts using the Trump Accounts program. The announced beneficiaries were children, not the president personally.','Associated Press',AP,'2025-12-02','Philanthropy / policy access','Indexed source passage reviewed; article retrieval unavailable'),r('The Pentagon awarded Dell Federal Systems a five-year software-purchasing agreement valued at about $9.7 billion. It consolidated existing budgets rather than creating that amount of new funding.','Breaking Defense',BD,'2026-05-27','Procurement reporting')],
 [r('Officials described procurement consolidation and projected annual savings. A company contract is not evidence that Michael Dell personally traded his philanthropy for preferential treatment.','Breaking Defense: procurement rationale',BD,'2026-05-27','Alternative explanation')],
 'This is an episode-specific estimate, not a finding about procurement legality. Contract face value is neither Dell profit nor a personal payment. Broader political activity and award-selection records remain outside this review.',
 dict(levels=[2,1,1],range=[10,60],rationales=['Visible support for a presidential policy initiative.','Government sales are documented; exceptional preferential terms are not established here.','The timing warrants questions but does not establish a reciprocal favor.'],sourceRefs=[[0],[1],[0,1]]))
TT='https://www.texastribune.org/2025/11/11/texas-gambling-legalization-senate-election-huffman-wambganss-district-9/'
TT2='https://www.texastribune.org/2026/03/06/texas-primary-election-casino-gambling-candidates-sands-adelson/'
add('miriam-adelson',
 'Adelson’s Texas political financing pursues a clear commercial-policy objective. The reviewed campaign also shows substantial limits: spending did not deliver the desired legalization.',
 'Casino wealth → electoral financing → attempted market-opening policy','Texas casino campaign, 2023–March 2026',
 [r('The Tribune reports Adelson financing casino-aligned PACs and a broad set of legislative campaigns. In November 2025, the casino-backed Senate candidate failed to reach the runoff.','The Texas Tribune',TT,'2025-11-11','Campaign finance reporting'),r('March 2026 reporting records further defeats for casino-backed challengers and continuing legislative resistance. Sands defended supporting candidates who favor a business-friendly economy.','The Texas Tribune',TT2,'2026-03-06','Follow-up / subject response')],
 [r('Several anti-gambling candidates won despite opposing spending. Legalization also requires voter approval of a constitutional amendment: donor financing is not unilateral control.','The Texas Tribune: constraints',TT2,'2026-03-06','Counterevidence')],
 'The estimate covers this attempted economic-policy influence, not all US or Israeli activity. Miriam’s actions are separated from her late husband’s. Lawful advocacy is not bribery; an unsuccessful campaign is not a received concession.',
 dict(levels=[3,0,2],range=[20,65],rationales=['Sustained electoral financing directed toward a commercial-policy goal.','The reviewed Texas campaign had not delivered legalization; zero applies to this episode, not her entire business history.','A clear attempted wealth–policy link, constrained by electoral and legislative defeats.'],sourceRefs=[[0],[1],[0,1]]))
CNN='https://transcripts.cnn.com/show/ebo/date/2017-12-05/segment/01'
WSJ='https://www.livemint.com/market/stock-market-news/how-the-private-equity-lobby-wonagain-11659877538908.html'
add('stephen-schwarzman',
 'Schwarzman’s high-level political access and private-equity tax interests form a documented influence channel. The evidence is stronger for coordinated industry lobbying than for a personal quid pro quo.',
 'Political access and industry lobbying ↔ preservation of favorable tax treatment','US carried-interest debates, 2017 and 2022',
 [r('CNN reported Schwarzman hosting a Trump fundraiser and helping form the president’s business advisory council. It connected the carried-interest debate to his financial interests.','CNN transcript',CNN,'2017-12-05','Political access reporting'),r('The Journal describes Blackstone’s participation in the industry lobbying coalition and preservation of carried-interest treatment in 2022. It cites securities filings showing Schwarzman received substantial carry and incentive compensation.','The Wall Street Journal via Mint',WSJ,'2022-08-07','Lobbying / financial context')],
 [r('Blackstone told CNN the overall 2017 bill would increase Schwarzman’s personal taxes because of other provisions. That differs from the narrower benefit of retaining carried-interest treatment.','CNN: Blackstone response',CNN,'2017-12-05','Subject response'),r('The industry and Senator Sinema offered investment and growth reasons for the tax treatment. Many firms shared the benefit; the reporting does not prove Schwarzman personally determined the vote.','The Wall Street Journal via Mint: competing rationale',WSJ,'2022-08-07','Alternative explanation')],
 'This historical estimate does not assert the current tax code or a corruption finding. Industry coordination, individual access and financial exposure are distinguishable; legislative causation remains contested.',
 dict(levels=[3,2,2],range=[30,75],rationales=['Direct presidential access and fundraising are documented.','A favorable industry-wide tax provision benefits his compensation class.','Organized lobbying and preserved benefits support an influence inference, not proof of a personal bargain.'],sourceRefs=[[0],[1],[0,1]]))
PH='https://www.pressherald.com/2023/04/19/after-high-flying-start-desantis-hits-stumbling-blocks-on-road-to-2024/'
add('thomas-peterffy',
 'The reviewed donor episode demonstrates political participation and willingness to withhold support. It does not establish the business benefit needed for a defensible oligarchy estimate.',
 'Donor leverage; preferential economic exchange unresolved','Republican presidential donor debate, April 2023',
 [r('Reporting describes Peterffy putting prospective DeSantis support on hold, citing abortion and school-book policies. This identifies stated policy preferences, not a business concession.','The Washington Post via Portland Press Herald',PH,'2023-04-19','Donor statement')],
 [r('The same account presents disagreement between a donor and a politician. Withholding support does not show the politician obeyed, or that the donor received a private economic return.','Washington Post report: scope limit',PH,'2023-04-19','Scope limitation')],
 'No numeric score is assigned from campaign giving alone. Land, taxation and brokerage regulation require separate person-specific research; neither clearance nor wrongdoing is inferred from this narrow review.')
GM='https://www.marketscreener.com/news/latest/Mexico-Grupo-Mexico-reach-deal-over-occupation-of-railway-line-44006666/'
GM2='https://www.investing.com/news/stock-market-news/govt-compensation-to-grupo-mexico-over-railway-wont-include-cash--president-3089995'
add('german-larrea-mota-velasco',
 'The Ferrosur episode documents a state–company negotiation, but the concession change was compensation following state occupation. Treating that alone as a gift to Larrea would omit the loss on the other side of the transaction.',
 'Railway concession renegotiation following government occupation','Ferrosur dispute and settlement, May 2023',
 [r('Reuters reported an agreement to extend expiring concessions rather than pay cash after government forces occupied a railway section controlled by Grupo México’s transport business.','Reuters via MarketScreener',GM,'2023-05-31','Negotiated settlement'),r('Earlier Reuters reporting records the president proposing concession restructuring as compensation after the takeover. It does not establish Larrea’s personal control over the state.','Reuters via Investing.com',GM2,'2023-05-24','Policy context')],
 [r('The occupation itself and non-cash compensation are material constraints on the patronage interpretation. The transaction cannot be evaluated as a benefit without valuing what the company surrendered.','Reuters: settlement context',GM,'2023-05-31','Alternative explanation')],
 'No score: concession value, individual negotiating role and broader privatization history remain unresolved. Company and family assets are not automatically evidence of personal political favoritism.')
SB='https://group.softbank/en/news/press/20250122'
add('masayoshi-son',
 'Son’s Stargate role combines a very large investment ambition with presidential-stage access. The announcement is not evidence that the US government supplied the headline capital or granted Son a preferential private benefit.',
 'Investment pledge and political promotion; specific preferential return unresolved','Stargate launch, January 2025',
 [r('Son appeared with Trump at Stargate’s announcement.','Associated Press','https://apnews.com/article/be261f8a8ee07a0623d4170397348c41','2025-01-21','Political access','Indexed source passage reviewed'),r('SoftBank’s announcement names Son as chairman, identifies the initial equity funders and assigns financial responsibility to SoftBank. The $500 billion figure is an intended four-year investment.','SoftBank Group',SB,'2025-01-22','Company primary statement')],
 [r('The company identifies equity investors, not a $500 billion US appropriation, and warns that forward-looking plans may differ from outcomes. An announcement is not completed spending.','SoftBank Group: financing and cautions',SB,'2025-01-22','Subject statement / scope limit')],
 'No score is assigned from an investment pledge and access alone. Actual incentives, financing terms, regulatory decisions and other countries require separate review; this is not a whole-career assessment.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/004.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
