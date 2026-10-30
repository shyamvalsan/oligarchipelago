"""Wave 27: narrow profile-only reviews; evidence did not support all three rubric dimensions for any person."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def prof(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; no rubric assigned',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
NOEX=' This is a limited search and not an exoneration.'

# Rick Cohen & family
FORT='https://www.fortune.com/2024/02/29/kroger-albertsons-ftc-challenge-billionaire-rick-cohen/'
BG='https://www.bostonglobe.com/2024/01/03/business/rick-cohen-symbotic-cs-grocers-new-hampshire'
IJ='https://www.insurancejournal.com/news/national/2024/12/12/804501.htm'
prof('rick-cohen','no-strong',
 'Rick Cohen chairs C&S Wholesale Grocers and founded Symbotic, whose revenue is heavily concentrated in Walmart. The reviewed sources document commercial dependence and a proposed C&S store purchase that a federal court found inadequate as a divestiture remedy. They do not document political donations, lobbying or preferential state treatment of Cohen. The Forbes entry is a family entry; the evidence reviewed concerns Rick Cohen.',
 'Commercial concentration and merger role; no political mechanism established','Symbotic–Walmart relationship 2021–2024; Kroger–Albertsons divestiture litigation 2024',
 [r('The Boston Globe reports Walmart expanded a Symbotic automation plan to all 42 of its regional distribution centers in 2022, owned about 11% of Symbotic as of January 2023 and accounted for almost 90% of Symbotic revenue. Cohen credited a prior C&S supply relationship with helping win the deal. This is a private commercial dependence, not a government relationship.','The Boston Globe',BG,'2024-01-03','Company-structure and customer-concentration context'),
  r('Fortune reports Cohen chairs C&S, which agreed to buy 413 stores from the Kroger–Albertsons merger, and that Walmart, a grocery competitor, owns about 13% of and is a customer of Symbotic. The FTC and states sued to block the merger in February 2024. The article does not say Cohen was personally named in the suit.','Fortune',FORT,'2024-02-29','Corporate role and commercial context')],
 [r('Neither the Boston Globe profile nor the Fortune article (cited above) reports political activity, donations or lobbying by Cohen. Absence from these two articles is not a search of FEC or lobbying records.','The Boston Globe: scope of coverage',BG,'2024-01-03','Explicit limit of the evidence'),
  r('Insurance Journal reports Judge Adrienne Nelson blocked the Kroger–Albertsons merger and found the planned divestiture to C&S insufficient in scale. A court ruling against the structure in which C&S would benefit weighs against a claim of government favoritism toward Cohen\'s company.','Insurance Journal (reporting the federal court ruling)',IJ,'2024-12-12','Counterevidence: adverse court outcome')],
 'Customer concentration, a strategic shareholder and a merger divestiture are commercial facts, not evidence of political leverage. No FEC, lobbying, procurement-with-government or regulatory-preference records were reviewed. Family members were not separately researched.'+NOEX)

# Israel Englander
LAW='https://www.law.com/almID/900005546556/'
WIKIE='https://en.wikipedia.org/wiki/Israel_Englander'
prof('israel-englander','no-strong',
 'Englander founded Millennium Management. The reviewed sources document a 2005 market-timing settlement in which the firm and he paid penalties, and his philanthropy. No source reviewed documents political donations, lobbying, government contracts or preferential regulatory treatment. Searches on his political giving returned nothing about him.',
 'No wealth–power mechanism identified in reviewed sources','2005 enforcement settlement; no current political mechanism found',
 [r('Law.com reports a 2005 settlement with New York Attorney General Eliot Spitzer and the SEC over market-timing: Millennium Partners $121.4 million, Englander $30 million in civil penalties and two management companies $26.6 million. This is an enforcement outcome against a business and him, not evidence of political leverage.','Law.com',LAW,'2005-12-01','Historical enforcement context (excerpt; rest paywalled)','Excerpt only; article paywalled')],
 [r('The Wikipedia entry reviewed describes philanthropy and the unrelated 1980s Jamie Securities episode (stating he was never implicated), and contains no political donations or government ties. It is a tertiary page and not a record search.','Wikipedia: Israel Englander',WIKIE,'2026','Explicit limit of the evidence; tertiary source','Page text reviewed; tertiary source'),
  r('The 2005 settlement is a regulator holding him and his firm to account, which cuts against a reading of unusual regulatory shelter in that episode. It is historical and says nothing about 2026.','Law.com: enforcement outcome',LAW,'2005-12-01','Alternative explanation','Excerpt only; article paywalled')],
 'No FEC, lobbying or SEC-current-matter records were reviewed; two web searches for his political giving and 2025-26 regulatory contact returned nothing about him. Millennium\'s November 2025 stake sale was seen only in a search snippet, not a fetched page.'+NOEX)

# Suleiman Kerimov & family
TRE='https://home.treasury.gov/news/press-releases/jy0841'
MT18='https://www.themoscowtimes.com/2018/04/06/us-targets-oligarchs-in-new-wave-of-anti-russia-sanctions-a61079'
WK='https://en.wikipedia.org/wiki/Suleiman_Kerimov'
prof('suleiman-kerimov-family','mixed',
 'Kerimov has held public office (Duma 1999-2007, Federation Council seat from Dagestan since 2008, per a tertiary source) and is designated by the US, UK and EU. The reviewed material documents office-holding, designations and a blocked Delaware trust, but not a court finding of preferential benefit from office. This file separates government designations and unresolved allegations from adjudicated findings.',
 'Public office and strategic investments; extent of preferential protection unresolved','Political roles 1999-present; US designation 2018; Treasury trust action 2022',
 [r('Treasury says OFAC designated Kerimov on April 6, 2018 under E.O. 13661 as an official of the Russian government, that he is a Federation Council member, and on June 30, 2022 notified Heritage Trust (over $1 billion in assets, formed July 2017) that its assets were blocked because he kept a property interest. Treasury also says he used layered structures and front persons. These are government positions, not court findings.','US Treasury: Heritage Trust blocking notification',TRE,'2022-06-30','Official designation and administrative action'),
  r('The Moscow Times describes him as a lawmaker whose family controls Polyus among oligarchs whose US assets were frozen on April 6, 2018 and quotes Treasury\'s general rationale on Russian government malign activity. It gives no individual rationale for him.','The Moscow Times',MT18,'2018-04-06','Contemporaneous reporting on the designation'),
  r('Wikipedia, citing press reports, states Kerimov moved assets into trusts in 2013 after a law barring officials from foreign accounts, and that Sberbank lent him $3.2 billion in 2004 for equities he later sold. These are tertiary summaries and not individually verified here.','Wikipedia: Suleiman Kerimov',WK,'2026','Tertiary summary of historical episodes','First 100,000 of about 141,000 characters read; tertiary source')],
 [r('Per the same Wikipedia summary, French tax-evasion charges were dismissed in June 2018 and he was placed under formal investigation in March 2019 with no final conviction reported; Belarus withdrew a 2013 criminal case that Interpol called political; and a Cypriot freeze was lifted without deciding the merits. None is a finding of misconduct.','Wikipedia: Suleiman Kerimov (legal outcomes)',WK,'2026','Material limit: no adjudicated finding','First 100,000 of about 141,000 characters read; tertiary source'),
  r('The Moscow Times article gives no Kerimov-specific rationale, and the Treasury action rests on his official status. A designation of an officeholder is not evidence that he obtained a specific preferential economic benefit.','The Moscow Times; US Treasury',MT18,'2018-04-06','Explicit limit of the evidence')],
 'This is a narrow review: web search capacity ran out before primary EU, UK or French court documents or the Amadea forfeiture record could be read, so those matters are not assessed. Family wealth is not assigned identical conduct. Designation, office-holding and nationality do not themselves justify a score.'+NOEX,'Low / unresolved attribution')

# Dilip Shanghvi
WKS='https://en.wikipedia.org/wiki/Dilip_Shanghvi'
prof('dilip-shanghvi','no-strong',
 'Shanghvi is founder of Sun Pharmaceutical. The only page read documents honours and advisory appointments, not political leverage or preferential benefit. Search snippets mentioned US FDA warning letters about Sun Pharma\'s Halol plant, but those pages could not be fetched and are not relied on.',
 'No wealth–power mechanism identified in reviewed sources','Padma Shri 2016; RBI central board appointment 2018 (per tertiary source)',
 [r('Wikipedia reports he received the Padma Shri in 2016, was appointed to the Reserve Bank of India central board in January 2018 and chairs the IIT Bombay board of governors. Honours and advisory appointments are office-holding context, not evidence of preferential treatment.','Wikipedia: Dilip Shanghvi',WKS,'2026','Appointments context; tertiary source','Page text reviewed; tertiary source, some cited links dead')],
 [r('The page lists no donations, lobbying, legal problems or policy-influence claims. It is a stub with weak citations, so this is an evidence limit, not clearance.','Wikipedia: Dilip Shanghvi (scope)',WKS,'2026','Explicit limit of the evidence','Page text reviewed; tertiary source')],
 'Electoral-bond, lobbying, Indian regulatory or Ranbaxy-era records were not reviewed. Search capacity for further queries was exhausted.'+NOEX)

# Yu Yong
K36='https://eu.36kr.com/en/p/3834170186213251'
WKY='https://en.wikipedia.org/wiki/Yu_Yong'
prof('yu-yong','no-strong',
 'Yu Yong (Cathay Fortune / Hongshang Group, Shanghai) is described as CMOC\'s actual controller since 2014 and holds a CATL stake. The reviewed sources describe business acquisitions and a 2012 Australian bid, but contain no documented political roles, state patronage or policy influence. Identity is the Shanghai-based Yu Yong (于泳, b. 1961), not other people named Yu.',
 'No wealth–power mechanism identified in reviewed sources','CMOC control from 2014; CATL pre-IPO stake 2016-2018; 2012 Discovery Metals bid',
 [r('China Entrepreneur via 36Kr (June 2026) says he became CMOC\'s actual controller in 2014 through Hongshang Group, holds no CMOC position and is little known; Hongshang bought 49% of CMOC in 2004 for 178 million yuan and CATL later acquired Luoyang Mining\'s CMOC stake. It does not discuss political connections.','China Entrepreneur / 36Kr',K36,'2026-06-01','Business-structure context','Page text reviewed; one outlet'),
  r('Wikipedia says Cathay Fortune\'s 2012 hostile bid for Discovery Metals was reportedly financed with China-Africa Development Fund loans. The claim is tagged citation-needed there; it would only show state-linked financing for an overseas bid, not preferential treatment of him.','Wikipedia: Yu Yong',WKY,'2026','Weakly sourced lead','Page text reviewed; stub, claim tagged citation needed')],
 [r('The Wikipedia page does not mention CPPCC, NPC or party positions or government relations beyond Australian resistance to the bid. The 36Kr piece says he holds no position at CMOC. These are evidence limits.','Wikipedia: Yu Yong; 36Kr',WKY,'2026','Explicit limit of the evidence','Page text reviewed; stub')],
 'Chinese-language sources, regulatory filings and political-advisory-body membership lists were not reviewed. Wealth figures differ across aggregators and are not used. His brother Yu Bo is Hongshang\'s public representative; conduct is not transferred between them.'+NOEX)

# Stuart Hoegner
BLAW='https://news.bloomberglaw.com/crypto/tether-gc-hoegner-stepping-down-hilliard-to-lead-legal-affairs'
BLOCK='https://www.theblock.co/news/markets/2025-01-02-tethers-general-counsel-retires-in-wake-of-mica-stablecoin-regulations-coming-into-effect-332986'
NYAG='https://ag.ny.gov/press-release/2021/attorney-general-james-ends-virtual-currency-trading-platform-bitfinexs-illegal'
FARG='https://www.forbesargentina.com/millonarios/el-nuevo-valor-mercado-tether-haria-su-principal-accionista-mas-rico-warren-buffett-n86924'
prof('stuart-hoegner','no-strong',
 'Hoegner was general counsel of Tether and Bitfinex until his January 2025 retirement, and Forbes (via Forbes Argentina, February 2026) estimates a 12% Tether stake. The reviewed sources document a corporate enforcement settlement and his role as a lawyer, not personal political leverage or preferential government treatment.',
 'Legal role and company regulatory exposure; political reciprocity not established','Company settlement 2021; retirement January 2025; Forbes estimate February 2026',
 [r('Forbes Argentina (dated 2026-02-27) says Forbes estimates Hoegner holds about 12% of Tether, worth about $25 billion at a roughly $200 billion valuation based on conversations with investors and executives; it lists Devasini (44-45%), Ardoino and van der Velde (about 19% each) and Cantor Fitzgerald (about 5%) as other holders. The valuation is an estimate.','Forbes Argentina',FARG,'2026-02-27','Wealth-source context','Page text reviewed; secondary outlet republishing Forbes estimate'),
  r('The New York Attorney General\'s February 2021 release says Tether falsely claimed one-to-one dollar backing and Bitfinex concealed about $850 million of losses; the settlement required $18.5 million and ending trading with New Yorkers. It is a company enforcement matter; the page does not state whether admissions were made.','New York Attorney General',NYAG,'2021-02-23','Corporate enforcement context; not personal finding')],
 [r('The Block reports he retired as general counsel, announced January 2, 2025, with Michael Hilliard leading legal affairs; it gives no reason and mentions no equity stake. Later Tether developments are not attributed to him.','The Block',BLOCK,'2025-01-02','Material role update','Page text reviewed'),
  r('Bloomberg Law confirms the retirement announcement of January 3, 2025.','Bloomberg Law',BLAW,'2025-01-03','Corroboration of role change','Short page text reviewed')],
 'The corporate findings are not findings against him personally. No political donations, lobbying, or government relationships attributable to him were found. The earlier wave-18 review is superseded here only in framing; it also found no personal mechanism.'+NOEX,'Low / personal reciprocal influence unresolved')

# Huang Shilin
WKH='https://en.wikipedia.org/wiki/Huang_Shilin'
YAH='https://finance.yahoo.com/news/co-founder-chinese-ev-battery-093000854.html'
prof('huang-shilin','no-strong',
 'Huang Shilin is a CATL co-founder and former vice chairman who, per SCMP via Yahoo (November 2025), has left his company role and still holds over 9% of CATL. The reviewed sources document his shareholding and a 1% stake sale, and contain nothing on political roles, state patronage or policy influence. Identity: Huang Shilin of CATL, not other Huangs in the sector.',
 'No wealth–power mechanism identified in reviewed sources','Co-founder of CATL; stake sale November 2025',
 [r('SCMP via Yahoo Finance (2025-11-21) reports he sold about 1% of CATL (45.6 million A shares at 376.12 yuan, about 1.7 billion yuan) to 16 institutions, was formerly general manager and vice chairman and led R&D, and that CATL said he relinquished his role and is no longer an employee. He retains over 9%.','South China Morning Post via Yahoo Finance',YAH,'2025-11-21','Stake and role context','Page text reviewed; syndicated copy'),
  r('Wikipedia identifies him as CATL vice chairman, notes a 12% stake as of 2018 (Forbes) and a 2026 Forbes/Bloomberg listing. It is a stub that does not mention political roles or controversies.','Wikipedia: Huang Shilin',WKH,'2026','Identity and wealth context','Page text reviewed; stub, partly outdated')],
 [r('Neither source reviewed mentions NPC/CPPCC membership, subsidies attributable to him, or controversies. Chinese battery-industry policy support is a sector matter and is not attributed to a co-founder without person-level evidence.','Wikipedia; SCMP via Yahoo (scope)',WKH,'2026','Explicit limit of the evidence','Page text reviewed')],
 'Bloomberg, mining.com and CATL filings could not be fetched (HTTP 403/404). Chinese-language sources and company disclosures on political positions were not reviewed. Search capacity ended before further queries.'+NOEX)

# Christy Walton
U4R='https://united4respect.org/reports/walmart-political-spending-2024/'
SNO='https://www.yahoo.com/news/fact-check-walmart-heiress-christy-224200768.html'
FA2='https://www.forbesargentina.com/today/la-heredera-walmart-christy-walton-financia-republicanos-anti-trump-n1740'
prof('christy-walton','no-strong',
 'Christy Walton inherited a Walmart stake (about 1.9% per Snopes via Yahoo) on John T. Walton\'s death in 2005 and has no Walmart board or decision-making role. Her documented political activity is personal giving, including to Democratic-aligned causes and a 2025 newspaper advertisement. The advocacy report on Walton-family spending mentions her only briefly. No policy-benefit mechanism attributable to her was found.',
 'Personal political giving; no preferential benefit or Walmart policy role shown','Giving 2020-2025; inheritance 2005',
 [r('Forbes Argentina (May 2020) reports she gave $20,000 to The Lincoln Project in January 2020 and previously donated to Democratic pre-candidates Bennet and Hickenlooper; she declined to comment on the latter. Giving is context, not a preferential-benefit exchange.','Forbes Argentina',FA2,'2020-05','Personal donation record','Page text reviewed; secondary outlet'),
  r('Snopes (via Yahoo, 2025-06-11) confirms she paid for a June 8, 2025 New York Times ad promoting the "No Kings" protest, cites FEC records of donations to Planned Parenthood, the Lincoln Project and Kamala Harris\'s campaign, and quotes Walmart saying the ads are not connected to or endorsed by it.','Snopes via Yahoo News',SNO,'2025-06-11','Personal political activity; company disclaimer')],
 [r('United for Respect\'s report puts Walmart-and-Walton political spending at about $32 million in the 2023-24 cycle, mostly Republican-directed, from other family members; it mentions Christy Walton once, in about $300,000 of smaller giving to reproductive-health causes. The group is an advocacy organisation critical of the family; its figures are not attributed to her.','United for Respect: Walmart political spending 2024',U4R,'2024','Evidence limit; family giving not attributable to her','Page text reviewed; advocacy source'),
  r('The Walmart statement quoted by Snopes says she has no board or decision-making role at the company, so a mechanism running through Walmart policy is not shown for her.','Snopes via Yahoo News: Walmart statement',SNO,'2025-06-11','Subject/company response')],
 'Family-level spending belongs to other members and is not transferred to her. Walmart lobbying, tax-subsidy and wage-policy interactions were not reviewed at person level. Her stake and its political significance are indirect.'+NOEX)

# Stefan Persson
RT='https://www.realtid.se/sa-banade-stefan-persson-vag-svenska-miljardarer'
TV4='https://www.tv4.se/artikel/tt-260310-miljardarslista1-aed56158/han-ar-rikast-i-sverige'
prof('stefan-persson','mixed',
 'A popular-history book excerpt describes how, in 1996-97, Persson publicly objected to a proposed Swedish wealth tax, suggested H&M or his own residence might move abroad, and the final law exempted owners of more than 25% of votes in companies listed before 1992, which the book says covered his family. The account is single-source and historical (the tax was abolished in 2007); no current mechanism was found.',
 'Public lobbying and relocation signals → wealth-tax design exempting closely held large owners (historical, single source)','Wealth tax proposal and law, 1996-1997; EU referendum statement 1994',
 [r('Realtid.se republishes an excerpt of Erik Palm and Jonas Alsgren\'s book The Big Boss (Norstedts) dated 2020-01-30. It says Persson argued in 1996-97 that the new wealth tax could take near 100% of his income, said he might move H&M abroad, that H&M moved to the O-list in June 1997, and that the resulting law exempted owners with over 25% of votes in firms on the A-list before 1992, which the authors say covered his family. Dagens Industri is reported as saying only one of eighteen Swedish stock-market billionaires paid the tax. The book authors argue he effectively rewrote the tax law on this point.','Realtid.se, excerpt of The Big Boss (Palm and Alsgren)',RT,'2020-01-30','Historical episode; authors\' interpretation','Page text reviewed; book excerpt, single source'),
  r('The same excerpt describes a statement with Gudrun Sjoden in Dagens Industri twelve days before the 1994 EU referendum supporting membership, and calls it his debut as a political lobbyist; it notes he had not been contacted by the Yes campaign. Public advocacy for membership is ordinary political expression.','Realtid.se, excerpt of The Big Boss',RT,'2020-01-30','Public advocacy context','Page text reviewed; book excerpt')],
 [r('According to the excerpt, Persson said the move to the O-list was reluctant and for shareholders\' benefit, and the proposal was changed by the Social Democratic government. A public policy change to a general threshold is not proof of a private bargain, and the excerpt gives interpretation by the authors.','Realtid.se, excerpt of The Big Boss',RT,'2020-01-30','Subject response and alternative explanation','Page text reviewed; book excerpt'),
  r('TT/TV4 (March 2026) reports Affärsvärlden\'s estimate of his wealth at SEK 223.6 billion, first in Sweden and 107th globally. The article reports nothing about current political leverage. Swedish Wikipedia states the wealth tax was abolished in January 2007.','TT via TV4 Nyheterna',TV4,'2026-03-10','Current-status limit','Page text reviewed')],
 'Single-source historical episode; the exemption text, Riksdag record and contemporaneous Dagens Industri articles were not read. Current Swedish policy influence, donations or lobbying were not found. The text in the excerpt is the authors\' account and is not adopted as established fact.'+NOEX,'Low / single-source historical episode')

# Steve Cohen
CO='https://commercialobserver.com/2025/08/mets-steve-cohen-casino-queens/'
QE='https://queenseagle.com/all/2025/5/29/cohens-casino-gets-green-light-in-albany'
QL='https://queenseagle.com/all/2025/4/9/queens-casino-bidders-topped-state-lobbying-spending-last-year'
NY1='https://ny1.com/nyc/all-boroughs/news/2023/05/16/casino-applicants-spend-millions-on-campaign-contributions-and-lobbying'
CV='https://www.covers.com/industry/new-york-gov-could-reportedly-revive-queens-casino-project-oct-10-2024'
FOS='https://www.frontofficesports.com/mets-owner-steve-cohen-clears-final-hurdle-for-8b-casino-project/'
FOX='https://www.fox5ny.com/news/new-york-casino-licenses-latest'
AICIO='https://www.ai-cio.com/news/sac-capital-starts-anew-as-point72/'
prof('steve-cohen','mixed',
 'Cohen and his wife are large New York political donors, entities tied to his Metropolitan Park casino bid were among the top lobbying spenders in 2023-2024, the legislature passed a parkland bill the project needed, and the state Gaming Commission approved the license in December 2025. The reviewed sources do not show that donations or lobbying produced an exemption or discount: the licence carries a $500 million fee and went through a multi-bidder state process, and the bill drew opposition. Separate: SAC Capital pleaded guilty in 2013; Cohen was not criminally charged.',
 'Political giving and lobbying plus a legislative and licensing process; causal preferential benefit not shown','Casino bid and approvals 2023-2025; SAC Capital plea 2013',
 [r('NY1 (2023-05-16) reports Steve Cohen and his wife anted up more than $5 million in political donations in five years, the top donors in the casino-applicant group; Cohen\'s team declined to discuss.','NY1',NY1,'2023-05-16','Donation record as reported','Page text reviewed; article gives no lobbying figure for Cohen'),
  r('Queens Daily Eagle (2025-04-09) reports Queens Future, the Cohen/Hard Rock venture, spent about $2.6 million lobbying in Albany in 2024, fifth in the state, and that Cohen led city casino lobbying with more than $2 million aimed at the mayor and city lawmakers; the state figure is for the venture, not Cohen personally.','Queens Daily Eagle',QL,'2025-04-09','Lobbying records as reported'),
  r('Queens Daily Eagle reports the State Senate passed the parkland-alienation bill 54-5 on May 27, 2025, with Senator John Liu sponsoring (Commercial Observer separately says Governor Hochul signed it). Cohen agreed to explore a Flushing Skypark and pledged $100 million to park improvements if it was not built. Senator Jessica Ramos opposed, calling it about power.','Queens Daily Eagle; Commercial Observer',QE,'2025-05-29','Legislative outcome and opposition','Page text reviewed'),
  r('Front Office Sports reports the Gaming Commission granted Metropolitan Park its license on December 15, 2025, with a $500 million upfront fee and $500 million capital commitment per licensee.','Front Office Sports',FOS,'2025-12-15','Licensing outcome','Page text reviewed'),
  r('Covers reports that on October 10, 2024 Hochul denied a New York Post report that she planned to put legislation helping the project in her executive budget, saying she had no intention of doing so.','Covers',CV,'2024-10-10','Official denial of a related report','Page text reviewed')],
 [r('Fox5 reports the Gaming Facility Location Board recommended licenses for all three remaining bidders on December 1, 2025, with each paying $500 million, and that the city reached an agreement on the project. The licence was one of three awarded under a state process in which the bids were evaluated by the board, which weighs against a claim that it was a unique favor.','Fox5 New York',FOX,'2025-12-01','Alternative explanation: structured state process','Page text reviewed; scoring criteria and vote count not given'),
  r('Commercial Observer reports Queens Chamber of Commerce praise for the outreach and added housing, transit and green-space commitments; igamingbusiness (https://igamingbusiness.com/legal-compliance/licensing/met-park-new-york-casino-cac/) reports approval by all six community boards, the borough president, the city council and both chambers. Broad institutional support is an alternative explanation to donor-driven access.','Commercial Observer',CO,'2025-08','Alternative explanation','Page text reviewed'),
  r('Covers reports a Cohen spokesperson saying one person should not be able to stop or approve a project, responding to Senator Ramos\'s position.','Covers',CV,'2024-10-10','Subject response','Page text reviewed'),
  r('On SAC Capital, ai-CIO reports the firm pleaded guilty in November 2013 with a $1.2 billion fine; Cohen was personally not charged criminally and the SEC action against him concerned supervision; an SEC administrative action against him was pending at that time. The episode is historical and not part of the casino mechanism.','ai-CIO',AICIO,'2014','Historical and corporate versus personal conduct','Page text reviewed; SEC order not read')],
 'No rubric: leverage is partly documented, but preferential benefit is not distinguished from a competitive licence at a $500 million fee, and the feedback link from casino profits to future power is not evidenced. Donation totals are as reported in 2023 and not updated; Cohen-specific 2025-26 contributions, the USTA lawsuit and later developments were not reviewed. Donations, lobbying, licences and wealth are not themselves points.'+NOEX)

_prev=set()  # entries already authored in waves 1-20 keep their existing review
for _f in sorted((ROOT/'data/review-batches').glob('0[01]*.json')):
 _prev|=set(json.loads(_f.read_text())['profiles'])
for _k in list(P):
 if _k in _prev:P.pop(_k);R.pop(_k,None)
import re as _re
for _v in P.values():  # every narrow no-strong review must say it is not an exoneration
 if _v['status']=='no-strong' and not _re.search('comprehensive|exoneration|absence',_v['limitations'],_re.I):_v['limitations']=_v['limitations'].rstrip()+' This is a narrow review, not an exoneration.'
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/027.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
