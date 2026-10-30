"""Wave 25: narrow profile-only reviews; evidence did not support all three rubric dimensions for any person."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def prof(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; no rubric assigned',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
NOEX=' This is a limited search and not an exoneration.'

# Abigail Johnson
BM='https://bettermarkets.org/newsroom/fidelity-fought-washington-over-money-market-funds-and-won'
LG='https://legis1.com/news/digital-asset-lobbying-fidelity'
prof('abigail-johnson','mixed',
 'Reviewed sources document Fidelity lobbying on financial regulation, including a 2012 meeting between Johnson and the SEC chair during the money-market-fund fight. They do not establish personal preferential benefit beyond ordinary industry advocacy, or an exchange.',
 'Corporate and executive lobbying on financial regulation',
 '2012 money-market-fund episode (reported 2014); Fidelity lobbying disclosures reported 2025',
 [r('A Better Markets repost of a Boston Globe story says Johnson met the SEC chair in June 2012 as part of a lobbying effort by Fidelity and other fund firms against tighter money market fund rules, and describes the effort as an unusually harsh lobbying battle.','Better Markets, republishing Boston Globe',BM,'2014-10-23','Reported individual participation in corporate lobbying','Repost reviewed; the page includes no Fidelity or Johnson response and the original Globe text was not read'),
  r('A third-party aggregator reports Fidelity in-house lobbying spending of $650,000 in Q3 2025, 77 in-house disclosures since 2003, and issues including digital-asset market structure, retirement and tax. It does not mention Johnson.','Legis1 (aggregator)',LG,'2025-10-23','Corporate lobbying activity (context)','Page text reviewed; aggregator figures not checked against official filings')],
 [r('Lobbying on regulation by a large asset manager is lawful and common to the industry; the reviewed pages do not show that Johnson received a special exemption, contract or personal favor. The aggregator article never names her.','Legis1 and Better Markets, limits of evidence',LG,'2025-10-23','Explicit limit of the evidence'),
  r('The Better Markets page carries no Fidelity or Johnson statement, so her side of the 2012 episode was not reviewed.','Better Markets, limits',BM,'2014-10-23','Absence of subject response','Page text reviewed')],
 'Narrow review of two secondary pages. No lobbying filings, donation records or outcome studies were read, and no finding is made about 2026 conduct. Corporate advocacy is not attributed to Johnson beyond what the sources say.'+NOEX)

# Zheng Shuliang
WK='https://en.wikipedia.org/wiki/China_Hongqiao_Group'
AL='https://alcircle.com/news/shandong-weiqiao-to-move-203-mt-aluminium-capacity-from-shandong-to-hydro-power-rich-yunnan-49505'
prof('zheng-shuliang','no-strong',
 'The Forbes entry is a family entry linked to China Hongqiao and Shandong Weiqiao. The pages reviewed describe corporate regulatory events, including a 2017 closure order and a government-notified 2019 capacity relocation, but none names Zheng Shuliang or shows personal political leverage, preferential benefit or an exchange.',
 'Corporate-level regulatory interaction only; no personal mechanism identified',
 'Corporate events 2017–2020',
 [r('Wikipedia summarizes the 2017 official order to close two million tonnes of unapproved smelting lines, regulatory scrutiny of coal use and 2017 short-seller allegations. It does not mention Zheng Shuliang.','Wikipedia: China Hongqiao Group',WK,'2026','Corporate regulatory context','Page text reviewed; secondary source'),
  r('A trade report says a Shandong provincial industry department notice confirmed relocation of 2.03 Mt of capacity from Binzhou to hydropower-rich Yunnan on 28 Nov 2019. It names no individual and does not mention the family.','alCircle',AL,'2019-11-29','Corporate regulatory process','Page text reviewed')],
 [r('The reported relocation is explained in the source by switching from coal to hydropower, an industrial rationale, and the source does not allege a favor.','alCircle: stated rationale',AL,'2019-11-29','Alternative explanation'),
  r('Neither page mentions Zheng Shuliang, so the evidence cannot be attributed to her personally.','Wikipedia and alCircle: attribution limit',WK,'2026','Explicit limit of the evidence')],
 'Identity: Zheng Shuliang is described in search results as widow of Hongqiao founder Zhang Shiping, but that and any political roles (e.g. NPC or CPPCC membership) were not confirmed from a reviewed page; Hong Kong exchange filings were fetched but were unreadable. Chinese-language sources were not searched. Not an exoneration.'+NOEX)

# Marilyn Simons
WS='https://en.wikipedia.org/wiki/Jim_Simons_(mathematician)'
WM='https://en.wikipedia.org/wiki/Marilyn_Simons'
prof('marilyn-simons','mixed',
 'Documented political giving, a 2014 Senate subcommittee condemnation of Renaissance basket options and a 2021 tax settlement concern Jim Simons and the firm. The pages reviewed do not attribute political or tax conduct to Marilyn Simons personally, so no rubric is assigned.',
 'Spousal and family-entry context: donor activity and a tax dispute attributed to Jim Simons and Renaissance',
 '2014–2021 (tax matter); donations by cycle through 2020',
 [r('Wikipedia reports Jim Simons ranked fifth among federal donors in the 2016 cycle, with gifts such as $7 million to Priorities USA Action, and about $30.6 million to federal campaigns from 2006. Marilyn is identified as his wife (1977) and co-founder of the Simons Foundation (1994).','Wikipedia: Jim Simons',WS,'2026','Spouse-level donor context','First 100,000 characters reviewed; secondary source'),
  r('The same page reports the July 2014 Senate subcommittee condemnation of basket options and the September 2021 settlement of back taxes and penalties by Simons and colleagues. Marilyn is not named in it.','Wikipedia: Jim Simons',WS,'2026','Corporate/spouse matter, not personal to Marilyn','First 100,000 characters reviewed; secondary source')],
 [r('The Marilyn Simons page attributes political donations and the tax dispute to Jim Simons and Renaissance, not to her, and gives no ownership or role at Renaissance.','Wikipedia: Marilyn Simons',WM,'2026','Explicit attribution limit','Page text reviewed; secondary source'),
  r('Simons gave to both parties and Wikipedia records a $25,000 super PAC gift supporting Republican Senator Lindsey Graham alongside largely Democratic giving. Donation records alone do not show an exchange.','Wikipedia: Jim Simons',WS,'2026','Context limiting inference','First 100,000 characters reviewed')],
 'Family entry: Jim Simons died 10 May 2024; the entry covers Marilyn and family, and the evidence concerns her late husband. Search surfaced a LittleSis page for "Marilyn Hawrys Simons" donors and a different "Simon, Marilyn" FEC record; neither was relied on and the FEC identity was not resolved. Primary FEC, Senate and IRS documents were not read. Not an exoneration.'+NOEX)

# Robert Pera
A5='https://www.actionnews5.com/story/37561387/memphis-grizzlies-owner-robert-pera-subpoenaed-by-sec/'
WP='https://en.wikipedia.org/wiki/Robert_Pera'
prof('robert-pera','no-strong',
 'Reviewed pages show corporate regulatory matters at Ubiquiti, including a reported 2018 SEC document request, but no reviewed page shows political leverage, public contracts or favorable policy treatment for Pera personally.',
 'No wealth-power mechanism identified in reviewed sources',
 'Ubiquiti SEC request reported February 2018; Grizzlies purchase 2012',
 [r('WMC Action News 5 reports an SEC subpoena asking for documents on accounting practices, financial information, international trade practices and distributor relationships. This is a regulatory inquiry, not evidence of political leverage or benefit.','WMC Action News 5',A5,'2018-02-21','Corporate regulatory context only','Page text reviewed'),
  r('Wikipedia records Pera founding Ubiquiti in 2005, its 2011 IPO and his 2012 NBA-approved Grizzlies purchase. No lobbying, donations or government contracts are described.','Wikipedia: Robert Pera',WP,'2026','Biographical context','Page text reviewed; secondary source')],
 [r('Ubiquiti said it was working to respond to the SEC request; the article reports no finding or outcome.','WMC Action News 5: company response',A5,'2018-02-21','Subject/company response'),
  r('The Wikipedia page contains nothing on political donations, lobbying or government contracts, so absence is an evidence limit.','Wikipedia: Robert Pera',WP,'2026','Explicit limit of the evidence')],
 'Search results also pointed to a 2014 OFAC settlement by Ubiquiti over exports to Iran and commentary about Russian military use of Ubiquiti gear; the OFAC document fetched was unreadable and the commentary is opinion, so neither is relied on and neither is attributed to Pera personally. No FEC or lobbying records were read. Not an exoneration.'+NOEX)

# Michal Strnad
E15='https://www.e15.cz/byznys/prumysl-a-energetika/babis-nesnasi-strnada-a-kritizuje-ceskou-municni-iniciativu-uz-pres-ni-proteklo-temer-sto-miliard-1428110'
SZ='https://www.seznamzpravy.cz/clanek/domaci-politika-zaskoceny-premier-americane-primeli-babise-zachranit-municni-iniciativu-298542'
LN='https://biz.liga.net/en/all/news/czech-billionaire-denies-clash-with-babis-over-weapons-supplies-to-ukraine'
prof('michal-strnad','mixed',
 'CSG is reported as the main supplier of the Czech ammunition initiative for Ukraine, which is mostly funded by foreign donors, and Prime Minister Babiš criticized then moderated his stance. Claims that US pressure or Strnad connections caused the reversal rest largely on anonymous sources. Documented state-linked revenue is not by itself leverage or exchange, so no rubric is assigned.',
 'State-linked defence procurement and public debate over profits; no proven personal influence',
 '2025–2026',
 [r('e15 reports about 2.1 of 3.7 million rounds planned for 2025–2026 are estimated to come from CSG, and that Babiš said he dislikes anyone profiting from the war and then called the initiative a principally good idea needing more transparency. An anonymous senior politician attributes his stance to envy of Strnad margins.','e15.cz (Pavel Otto)',E15,'2025-10-16','Reported scale of state-linked contracts and political reaction','Czech-language page read via tool summary'),
  r('Seznam Zprávy, relying mainly on Reportér, reports Babiš reversed course after meetings with US officials; it records a CSG subsidiary US Army contract of over $600 million and a CSG-linked fund investment in a round led by 1789 Capital. The causal claim about Strnad is inference backed by anonymous sources.','Seznam Zprávy (citing Reportér)',SZ,'2026-02-10','Allegation/inference, partly on-record meetings','Czech-language page read via tool summary')],
 [r('Strnad told Bloomberg he has no conflict with Babiš, that tensions eased after the election, and that CSG, a major employer and GDP contributor, should be treated with respect. CSG says its cooperation with Ukraine does not depend on the initiative.','Liga.net citing Bloomberg; e15',LN,'2025-12-12','Subject and company response'),
  r('e15 reports foreign donors fund 97.5% of the initiative per a government official and that margins are reportedly around 10%; an anonymous industry source says CSG share is a minority. Public funding is largely foreign, and margins are not documented as abnormal.','e15.cz',E15,'2025-10-16','Competing figures and alternative explanation','Czech-language page read via tool summary')],
 'Narrow review of Czech press only; no procurement contracts, audits or lobbying records were read. The dominant US-pressure narrative is anonymous and unverified. CSG began as a Strnad family business; Forbes lists Strnad individually. No finding of wrongdoing exists in the sources. Not an exoneration.'+NOEX)

# Elaine Marshall
DS='https://www.desmog.com/elaine-marshall/'
WE='https://en.wikipedia.org/wiki/Elaine_Tettemer_Marshall'
prof('elaine-marshall','no-strong',
 'Marshall is reported to hold, with her sons, a roughly 16 percent beneficial interest in Koch Industries and a board seat since 2006. Reviewed pages show modest personal political giving and attendance at a 2010 Koch network meeting; Koch Inc. policy influence is not attributed to her personally.',
 'Inherited stake in a politically active company; personal role unestablished',
 '2003–2022 donations; Koch board since 2006',
 [r('DeSmog, citing FEC data, reports an Elaine Marshall identified as a Koch board member gave $50,000 to KOCHPAC between 2011 and 2022 and $4,000 to Bush-Cheney 04; it reports she and two sons attended a June 2010 Koch network meeting in Aspen.','DeSmog Koch network profile',DS,'2026','Individual donations and event attendance (advocacy outlet citing FEC)','Page text reviewed; FEC records not checked'),
  r('Wikipedia says trusts for Marshall and her sons hold a 16% beneficial interest in Koch Industries, that she has been a director since 2006, and that Forbes valued her family at $30.9 billion in October 2025.','Wikipedia: Elaine Tettemer Marshall',WE,'2026','Ownership and role','Page text reviewed; secondary source')],
 [r('The Wikipedia page contains no political activity or policy-influence claim about her and the DeSmog profile has no statement from her about influence, so personal leverage is not evidenced.','Wikipedia and DeSmog: limits',WE,'2026','Explicit limit of the evidence'),
  r('The reviewed donations are small relative to her wealth and are reported through a company PAC and a past campaign, which are lawful and disclosed.','DeSmog: amounts',DS,'2026','Context limiting inference')],
 'Family entry: Marshall and family. Koch Inc. policy influence is a separate matter that belongs to Charles Koch and the company, not assumed here. Litigation over the J. Howard Marshall estate and a 2014 gift-tax case were seen but are not political evidence. Not an exoneration.'+NOEX)

# Shiv Nadar
WN='https://en.wikipedia.org/wiki/Shiv_Nadar'
WU='https://en.wikipedia.org/wiki/Shiv_Nadar_University'
prof('shiv-nadar','no-strong',
 'The reviewed pages describe HCL, the Shiv Nadar Foundation, a 2008 Padma Bhushan and the Institute of Eminence status of his university. None documents political leverage, preferential contracts or an exchange; an honor or regulatory recognition is not evidence of favoritism.',
 'No wealth-power mechanism identified in reviewed sources',
 '1976–2025 as described in profile pages',
 [r('Wikipedia records a Padma Bhushan (2008), his chairing of IIT Kharagpur board of governors until 2014 and philanthropic giving of Rs 2,708 crore in FY25 through the foundation. Its Shiv Nadar University page records an Institution of Eminence designation on 3 August 2022.','Wikipedia: Shiv Nadar; Shiv Nadar University',WN,'2026','Contextual recognition and institutional roles','Pages reviewed; secondary sources')],
 [r('The Shiv Nadar page, as read, mentions no political connections, ED/SEBI matters or other controversy; the university page describes the 2023 campus shooting as its only controversy and does not discuss land allocation.','Wikipedia: Shiv Nadar University',WU,'2026','Explicit limit of the evidence'),
  r('Public honors and Institution of Eminence designation come with formal criteria and are not shown here to be an exchange.','Wikipedia: Shiv Nadar University',WU,'2026','Alternative explanation','Page text reviewed')],
 'Searches for Uttar Pradesh land allotment and electoral-bond donations returned no relevant results about him, but only a few pages were read and no Indian primary sources, Election Commission data or HCL filings were reviewed. Not an exoneration.'+NOEX)

# Henry Samueli
OC='https://www.ocbj.com/news/samueli-appealing-judges-plea-bargain-rejection/'
AB='https://www.abajournal.com/news/article/despite_guilty_plea_broadcom_exec_didnt_lie_to_sec_federal_judge_finds'
prof('henry-samueli','no-strong',
 'The reviewed record concerns a Broadcom options-backdating case. Samueli pleaded guilty in June 2008 to a false statement to SEC investigators; a judge later set that plea aside in December 2009 after finding his answer was not a material false statement. This is not evidence of political leverage or preferential benefit.',
 'Historical regulatory/criminal matter; no wealth-power mechanism identified',
 '2008–2009',
 [r('OCBJ reports Samueli pleaded guilty in June 2008 to one felony count of lying to SEC investigators about options backdating; prosecutors proposed a $12 million payment, a $250,000 fine and probation, and Judge Carney rejected the deal as too lenient.','Orange County Business Journal',OC,'2008-10-13','Historical plea (since set aside)','Page text reviewed')],
 [r('On 9 December 2009 Judge Carney threw out the case and plea, finding Samueli did not make a significant false statement to the SEC, calling the answer ambiguous, evasive and arguably nonresponsive but not a material falsehood.','ABA Journal',AB,'2009-12-10','Court ruling vacating the plea; case dismissed')],
 'Searches found no political donation, lobbying or state-benefit evidence for him. No document was found supporting a pardon or any political-exchange claim; none is made. Political donations were not found in the searches (FEC data not checked). The Samueli Foundation and philanthropy were seen only in search listings. Not an exoneration.'+NOEX)

# Melinda French Gates
ST='https://www.statnews.com/2024/06/11/melinda-french-gates-pivotal-reproductive-rights-gates-foundation/'
prof('melinda-french-gates','no-strong',
 'Melinda French Gates is a prominent philanthropist whose Pivotal Ventures LLC can engage in political campaigns and advocacy. Reviewed reporting shows her advocacy for reproductive rights and political support, but no preferential economic benefit or exchange.',
 'Open political and philanthropic advocacy; no economic-benefit mechanism identified',
 '2024 reporting',
 [r('STAT reports that Pivotal Ventures, founded in 2015, is an LLC that can engage in political campaigns and direct advocacy, that she left the Gates Foundation in 2024 with $12.5 billion under separation terms, and that she wrote in a 28 May 2024 New York Times essay that she felt compelled to support reproductive rights domestically.','STAT News',ST,'2024-06-11','Advocacy and giving structure')],
 [r('The article describes charitable and advocacy intent and an expert expectation of future activity; it reports no contract, regulatory advantage or private economic benefit to her.','STAT News: limit',ST,'2024-06-11','Explicit limit of the evidence')],
 'Her wealth arises from a divorce settlement with Bill Gates; Bill Gates conduct is not attributed to her. A search snippet mentioned an undisclosed "substantial" Harris-Walz donation; that page was not read and is not relied on. No FEC data was read. Not an exoneration.'+NOEX)

# Reinhold Wuerth
TS='https://www.tagesspiegel.de/wirtschaft/steuerhinterziehung-ermittlungen-gegen-schraubenmillionar-wurth-1629604.html'
SZW='https://www.stuttgarter-zeitung.de/wirtschaft/schraubenmilliardaer-aus-kuenzelsau-wegen-afd-wuerth-will-lieber-im-ausland-investieren-79016546.html'
prof('reinhold-wuerth','no-strong',
 'Reviewed reporting covers a 2008 tax-evasion investigation reported by Tagesspiegel and Der Spiegel, with outcome not established, and Würth’s 2024 public advice against voting AfD. Neither shows preferential state treatment or an exchange; open political speech is not itself a rubric mechanism.',
 'Historical tax investigation and open political speech; no wealth-power exchange identified',
 '2006–2008 investigation; 2024 statements',
 [r('Tagesspiegel reports Stuttgart prosecutors were investigating Würth and five others for suspected tax evasion over millions of euros; lawyers were reportedly negotiating the amount and seeking a penalty order, with a fine of about 40 million euros discussed.','Tagesspiegel (citing Der Spiegel)',TS,'2008-03-29','Reported investigation, not a conviction','Page text reviewed'),
  r('Stuttgarter Zeitung (13 June 2024) reports Würth urged employees not to vote AfD in the European election and was weighing investing abroad.','Stuttgarter Zeitung',SZW,'2024-06-13','Public political statement','Article excerpt reviewed')],
 [r('Würth denied the allegations in 2006, saying at most there had been negligence in billing; the article says investigators and lawyers differed over tax rules and reports no completed conviction.','Tagesspiegel: subject response',TS,'2008-03-29','Subject response and legal-interpretation dispute'),
  r('An open voting recommendation to employees is public speech, not evidence of preferential benefit.','Stuttgarter Zeitung: nature of the evidence',SZW,'2024-06-13','Explicit limit of the evidence')],
 'Search results also listed a 2010 CDU donation of 100,000 euros from Adolf Würth GmbH in a Bundestag record, but the PDF was unreadable and it is not relied on. The outcome of the 2008 investigation was not found. Family entry (Reinhold Würth and family). Not an exoneration.'+NOEX)

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
(ROOT/'data/review-batches/025.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
