"""Wave 34: case reviews; two with rubrics, eight narrow profiles without estimates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
D='2026-10-29'
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,levels,bounds,notes,refs,status='mixed',confidence='Low / narrow review',depth='Source-led review of the stated episode; not independently editorially reviewed'):
 P[id]=dict(status=status,reviewedAt=D,reviewDepth=depth,confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if levels is not None:
  R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
def thin(id,summary,mechanism,period,support,counter,searched):
 add(id,summary,mechanism,period,support,counter,
  searched+' This is a narrow review and is not exoneration: absence of a documented link in the pages read does not show that none exists. Wealth, nationality, office-holding, honours and company size are not scored, so no estimate is assigned.',
  None,None,None,None,status='no-strong',depth='Narrow source-led screen; not independently editorially reviewed')

# Hamm
RG='https://www.bostonglobe.com/2025/12/13/business/oilman-pushed-trump-fossil-fuels'
HCN='https://www.hcn.org/articles/emails-show-interior-delivered-new-drilling-permits-for-burgums-billionaire-ally/'
add('harold-hamm',
 'Reporting describes a long-running political relationship between Harold Hamm and Donald Trump, large campaign giving, and federal permitting and regulatory actions that benefited Hamm’s company Continental Resources. Outlets and critics link these; the agency denies individual favoritism, and no exchange or wrongdoing has been established.',
 'Campaign giving and personal access to the president and Interior leadership → reported regulatory and permitting benefit; causation unproven',
 'Second Trump administration, 2025–2026 (reporting dated December 2025 and May 2026)',
 [r('The Boston Globe reports that Hamm gave more than $2 million to Trump campaigns, helped organize a 2024 Mar-a-Lago oil-executive dinner, and that Energy Secretary Chris Wright is a former director of an industry lobbying group Hamm co-founded. It lists federal actions benefiting Continental, including new Converse County drilling permits, shorter permit reviews and a delayed Biden-era methane fee. Hamm called the Wright and Burgum appointments a “dream team.”','The Boston Globe: oilman who pushed Trump on fossil fuels',RG,'2025-12-13','Major newspaper investigation','Page text reviewed via fetch summary; Hamm and Continental declined comment'),
  r('High Country News, with Public Domain and Fieldnotes, reports records showing a Continental request to BLM for Converse County permits that avoided an enjoined environmental analysis, pushed by an Interior official, and an April 2025 Hamm meeting with an aide to Secretary Burgum. Continental donated $250,000 to Burgum’s 2024 run. BLM approved 71 new Continental wells. Hamm said regulatory hurdles being removed “does lower our cost of doing business.”','High Country News / Public Domain: Interior delivered permits for Burgum ally',HCN,'2026-05-07','Public-records investigation','Page text reviewed; domain advocacy-oriented outlet, records not independently examined')],
 [r('An Interior spokesperson said permitting is “based on agency policy — not on any individual or company,” and the White House described Hamm as one of several executives who advise the president. Hamm and Continental did not respond to the Globe.','The Boston Globe: agency and White House responses',RG,'2025-12-13','Agency response / alternative explanation'),
  r('The reporters say it is unclear what Hamm and Burgum discussed in April 2025, so the article does not establish that the meeting affected permitting. The 2020 environmental analysis was vacated in February 2026 and the ruling is under appeal; Interior’s only reported statement was that Burgum complied with ethics requirements and did not address the emails.','High Country News: stated limits of the evidence',HCN,'2026-05-07','Explicit evidential limit')],
 'Scoped to the 2025–2026 oil-and-gas policy and Converse County episode, not Hamm’s whole career. Policies such as permit streamlining and methane-fee changes apply industry-wide; lawful advocacy and donations are not bribery, and no investigation or finding of an improper exchange was found. Both main sources report on, and quote, critics; the WyoFile coverage and company filings were not read. The family entry is scored on Harold Hamm’s personal conduct only.',
 [3,3,2],[35,80],
 ['Documented personal access, large giving, and a co-founded lobbying group whose former director now heads Energy.','Reported agency actions that Hamm himself said lowered Continental’s costs; the agency attributes them to policy.','Giving, access and favorable action coexist, but the sources do not show an exchange; benefits are also available to other producers.'],
 [[0,1],[0,1],[0,1]])

# Ergen
YA='https://finance.yahoo.com/news/fcc-end-echostar-probe-5g-115227512.html'
BEN='https://www.benton.org/headlines/charlie-ergen-spacex-and-trump'
add('charles-ergen',
 'In 2025 the FCC chair closed an inquiry into EchoStar’s spectrum buildout and confirmed its exclusive rights to a valuable block while EchoStar was selling spectrum to AT&T and SpaceX. A Wall Street Journal editorial reports Ergen met President Trump beforehand. The record shows an unusually favorable regulatory outcome, not a documented payment or bargain.',
 'Personal access to the president → reported regulatory relief enabling large spectrum sales; exchange undocumented',
 'FCC inquiry and spectrum sales, May 2025–March 2026',
 [r('Reuters reports FCC Chair Carr’s letter to Ergen asking staff to close the investigation, conclude EchoStar met its 5G buildout obligations, and confirm exclusive rights to the AWS-4 spectrum being sold to SpaceX for $17 billion; EchoStar had also agreed to sell spectrum to AT&T for $23 billion. The investigation began in May 2025 after concerns about slow deployment and a SpaceX “warehousing” complaint.','Reuters via Yahoo Finance: FCC to end EchoStar probe',YA,'2025-09-09','Wire report','Page text reviewed'),
  r('A Wall Street Journal editorial, reposted by the Benton Institute, states Ergen met Trump in June 2025 to try to stop the FCC reclaiming EchoStar’s licenses and that Trump “prodded Chairman Carr to let Ergen sell his licenses.” This is opinion-page characterization, not an official record.','Wall Street Journal editorial board via Benton Institute',BEN,'2026-03-31','Editorial; attributed account','Repost text reviewed; original not read')],
 [r('Carr said the deals could be a “potential game changer for the American consumer,” that the status quo “wasn’t working,” and noted Boost Mobile had lost about 2 million subscribers. That is a competition and consumer-benefit rationale for the outcome.','Reuters via Yahoo Finance: Carr’s stated rationale',YA,'2025-09-09','Official explanation / alternative explanation','Page text reviewed'),
  r('The same editorial says the public interest lies in getting scarce spectrum to those who can use it, and notes that the 2019 merger conditions that created Dish as a fourth carrier also came from a Trump administration. It does not allege payments to officials.','Wall Street Journal editorial board via Benton Institute: policy framing',BEN,'2026-03-31','Alternative explanation and limit','Repost text reviewed')],
 'Scoped to the 2025 EchoStar spectrum episode. No campaign giving, payment or private benefit to officials was found in the pages read, so the feedback dimension is weak. EchoStar’s own statements and the FCC letter itself were not obtained (one trade-press page returned 403). Sale proceeds accrue to the company, in which Ergen is a controlling holder; the personal share was not examined.',
 [2,3,1],[15,65],
 ['A reported presidential meeting, sourced to an editorial, plus the chair’s later decision; direct personal leverage is only partly corroborated.','Probe closure and confirmed exclusivity enabled roughly $40 billion of announced sales, a documented regulatory benefit to the company he chairs.','No documented donation, payment or reciprocal favor; the public-interest explanation is plausible.'],
 [[0,1],[0],[0,1]])

# Rupert
CIT='https://www.citizen.co.za/business/ramaphosa-denies-tycoon-ties'
N24='https://www.news24.com/business/johann-rupert-radical-economic-transformation-just-a-code-word-for-theft-20170913'
thin('johann-rupert',
 'The reviewed pages show Rupert as an outspoken critic of the Zuma-era government and the target of allegations that he influenced a December 2015 finance-minister reversal. Both he and Ramaphosa denied the meeting. No page read documents state patronage or preferential state benefit. The entry concerns Johann Rupert, not other family members.',
 'Alleged business influence on Treasury leadership (denied); no benefit mechanism shown',
 '2015–2017 South African political controversies',
 [r('Moneyweb reports claims that Deputy President Ramaphosa met senior business people including Rupert after Nene was fired in December 2015, and that this may have influenced Gordhan’s appointment. These are reported claims, not findings.','Moneyweb via The Citizen: Ramaphosa denies tycoon ties',CIT,'2016-03-29','Reported allegation')],
 [r('The Presidency said Ramaphosa “categorically denies ever having such a meeting” with Rupert, and Rupert also denied meeting him.','Moneyweb via The Citizen: denials',CIT,'2016-03-29','Subject response'),
  r('At Richemont’s 2017 AGM Rupert said “radical economic transformation is just a code word for theft”; context includes the state-capture reports and a Bell Pottinger campaign against him. This shows political opposition to the government, not state patronage.','Bloomberg via News24: Rupert at Richemont AGM',N24,'2017-09-13','Direct statement and context')],
 'Searched Rupert with Zuma, Ramaphosa, Richemont and Remgro; found 2016–2017 controversy coverage only. Nothing current, and no review of Remgro or Richemont state contracts, tax, or party funding.')

# Damani
WIKI_D='https://en.wikipedia.org/wiki/Radhakishan_Damani'
thin('radhakishan-damani-1',
 'No political-leverage or preferential-benefit evidence was found for Damani. His wealth is described as coming from stock investing and the DMart retail chain, which listed in 2017.',
 'No wealth–power mechanism identified',
 'Career to 2026 (secondary summary)',
 [r('Describes him as a former stock-market investor who founded DMart in 2002 and took it public in 2017, with large listed stakes. Context for wealth origin only; a tertiary source.','Wikipedia: Radhakishan Damani',WIKI_D,'2026-09','Context only','Page text reviewed; tertiary source, citations not verified')],
 [r('The same page reports no political ties, SEBI enforcement actions or controversies. This reflects one tertiary page and a search that surfaced none, not a full regulatory or press review.','Wikipedia: Radhakishan Damani (absence of reported ties)',WIKI_D,'2026-09','Explicit limit of evidence','Page text reviewed')],
 'Searched Damani with DMart, Modi and political ties; results held Adani–Modi coverage that does not concern Damani. Not checked: SEBI orders, land or tax disputes, party donations or electoral-bond data.')

# Woo
WIKI_W='https://en.wikipedia.org/wiki/Peter_Woo'
thin('peter-woo',
 'Public-role information shows Woo held Hong Kong government-appointed posts and is reported to be on the CPPCC Standing Committee, but no page read documents policy influence over, or preferential benefit to, his property business.',
 'Official and advisory roles; no benefit mechanism shown',
 'Roles from 1990s to 2012; chairman of Wheelock and Wharf to 2015',
 [r('Lists Woo as HKTDC chairman (2000–2007), Hospital Authority chairman, a 1996 Chief Executive candidate, a Gold Bauhinia Star (1998) and Grand Bauhinia Medal (2012, cited to a government honours list), and CPPCC Standing Committee member (uncited, no date). Appointments and honours are not scored.','Wikipedia: Peter Woo',WIKI_W,'2026','Context only','Page text reviewed; many entries marked citation needed')],
 [r('The page describes no controversies, land deals or regulatory findings; this is an explicit limit of one tertiary page, not an assessment of his companies’ dealings.','Wikipedia: Peter Woo (absence of reported controversies)',WIKI_W,'2026','Explicit limit of evidence','Page text reviewed')],
 'Searched Woo with Wheelock, Wharf, CPPCC and land. A Hong Kong government press-release page fetched empty. Not checked: Wheelock/Wharf land grants, Harbour City or cable/franchise matters, his current (post-2015) role.')

# Zhang
TEN='https://www.tencent.com/team/zhang-zhidong-tony-zhang/'
thin('zhang-zhidong',
 'Zhang Zhidong is a Tencent co-founder (CTO until 2014, now advisor emeritus). No evidence of his personal political role, state patronage or influence over gaming policy was found. Tencent-level regulatory matters are not attributed to him.',
 'No personal wealth–power mechanism identified',
 'Tencent role 1998–2014; later advisory title',
 [r('Tencent’s profile states he co-founded the company in 1998, served as CTO until 2014, and is now advisor emeritus and honorary dean of Tencent Academy. This documents wealth origin and role only.','Tencent: Zhang Zhidong (Tony Zhang)',TEN,'2026','Primary company profile')],
 [r('Neither this profile nor the Wikipedia summary read mentions any NPC/CPPCC seat or controversy. He left executive office in 2014, so Tencent’s later regulatory interactions are not evidence about him.','Tencent profile; Wikipedia: Tony Zhang',TEN,'2026','Explicit limit of evidence','Tencent page and a Wikipedia summary reviewed')],
 'Searched Zhang with Tencent, online games and Chinese government; nothing personal found. Chinese-language sources, shareholding filings and any political advisory seats were not checked. Forbes’s “Online games” label differs from his Tencent description; identity as Tony Zhang is by name match.')

# Zou
K36='https://eu.36kr.com/de/p/3614932106740996'
thin('zou-zhinong',
 'Zou Zhinong is reported as founder of Tianfu Communication (Suzhou TFC Optical Communication), an optical-component maker listed in 2015. No page read documents political leverage, state preference or wealth–power feedback for him.',
 'No wealth–power mechanism identified',
 'Company founding 2005; reporting December 2025',
 [r('36Kr reports Zou co-founded Tianfu Communication in 2005 and is its founder, that it listed on the Growth Enterprise Market in 2015, and that it plans a Hong Kong H-share listing; Hurun 2025 named him richest in Yichun. Wealth origin only; market value is not his personal wealth.','36Kr: Tianfu Communication report',K36,'2025-12-28','Business press, context only','Page text reviewed; secondary outlet, filings not read')],
 [r('The article describes market performance and ownership and mentions no state role, subsidy, political post or controversy; this is a limit of one article, not a review of filings or Chinese-language sources.','36Kr: Tianfu Communication report (absence of reported links)',K36,'2025-12-28','Explicit limit of evidence','Page text reviewed')],
 'Forbes labels him “Telecom equipment”; identity is matched by name and company only. Bloomberg profile returned 403. Not checked: exchange filings, government subsidies, political advisory seats, family members.')

# Foroughi
MS='https://www.marketscreener.com/news/applovin-plunges-after-the-sec-opens-investigation-into-its-advertising-practices-ce7d5bdddd8df727'
thin('adam-foroughi',
 'The reviewed record on Foroughi’s AppLovin concerns a regulatory inquiry, not political favor. A preliminary SEC examination of its ad practices was reported in October 2025; no charges were reported. No political leverage or preferential benefit was found.',
 'No wealth–power mechanism identified; regulatory scrutiny only',
 'SEC inquiry reported October 2025',
 [r('Reports that the SEC was preliminarily examining whether AppLovin broke platform-partner rules in targeting ads, reportedly after a whistleblower complaint and short-seller reports; stock fell about 14%. This is corporate regulatory scrutiny, not evidence of a political mechanism.','MarketScreener (Bloomberg report): AppLovin SEC probe',MS,'2025-10-07','Reported regulatory inquiry','Page text reviewed; article summarises Bloomberg')],
 [r('Foroughi defended the practices and accused short sellers of manipulating the market; no charges were filed. The allegations are unproven and are not about political power.','MarketScreener (Bloomberg report): response and status',MS,'2025-10-07','Subject response')],
 'Searched Foroughi with SEC, Trump; no political tie surfaced. A second search for donations or lobbying could not run (search budget exhausted). Not checked: FEC or lobbying records, later developments in the inquiry.')

# Loh
BZ='https://www.boersen-zeitung.de/personen/friedhelm-loh-70'
thin('friedhelm-loh',
 'Loh led the electrical-industry federation ZVEI and sits in business-association and institutional roles, which are ordinary industry representation. No page read documents preferential state benefit or wealth–power feedback.',
 'Industry-association roles; no benefit mechanism shown',
 'Profile dated August 2016',
 [r('Börsen-Zeitung’s 70th-birthday profile reports he led Rittal since 1974, was long-time ZVEI president (now honorary), and is a Fraunhofer senator and Deutsche Messe supervisory board member. Industry-association roles are not scored.','Börsen-Zeitung: Friedhelm Loh 70',BZ,'2016-08-13','Business-press profile')],
 [r('The profile reports no party-political role. It notes Berlin government concerns about a Midea deal but does not link Loh to them.','Börsen-Zeitung: Friedhelm Loh 70 (limits)',BZ,'2016-08-13','Explicit limit of evidence','Page text reviewed')],
 'The source is a decade old. Other fetches (a Hessian order of merit item, an industry page) were unavailable or not read. Not checked: Lobbyregister entries, party donations, subsidy or contract records, current activity.')

# Mallouk
ING='https://ingrams.com/article/new-ranking-peter-mallouk-of-creative-planning-is-a-top-financial-power-player/'
thin('peter-mallouk',
 'Mallouk is described as president of Creative Planning, a wealth-management firm he bought in 2004. No evidence of a political role, state benefit or influence was found in the page read.',
 'No wealth–power mechanism identified',
 'Undated profile, apparently around 2018',
 [r('A trade-press ranking item describes him as president of Creative Planning, purchased in 2004 when it managed about $34 million, now $37 billion, and ranked 99th on Worth’s power list. Business-success context only.','Ingram’s: Mallouk ranked a financial power player',ING,'2018','Trade press, context only','Page text reviewed; no explicit date on page')],
 [r('The page mentions no political office or role for Mallouk; a power-list ranking is not political leverage. This reflects one dated page and a search finding no political-donation reporting.','Ingram’s: Mallouk (absence of political role)',ING,'2018','Explicit limit of evidence','Page text reviewed')],
 'Searched Mallouk with Trump and donations; returned only generic advisor-donation data. Bloomberg page returned 403. Not checked: FEC records, regulatory actions against Creative Planning, current coverage.')

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
(ROOT/'data/review-batches/034.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
