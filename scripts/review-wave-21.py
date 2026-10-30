"""Wave 21: individual source-led reviews; mostly profile-only (no numerical estimate)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,confidence,summary,mechanism,period,support,counter,limitations,rubric=None):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; not exoneration where no estimate is given',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if rubric:
  levels,bounds,notes,refs=rubric
  R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
NARROW='Low / narrow review'

# ---- Larry Page
add('larry-page','no-strong',NARROW,
 'Searches found corporate-level Google political activity (a 2025 inauguration donation; an antitrust case with a 2025 remedies ruling) but no reviewed source attributing a personal political bargain, access episode or preferential benefit to Larry Page. This is not exoneration; it reflects a narrow search.',
 'Corporate political engagement and antitrust exposure; no personal mechanism identified',
 'Google corporate events, 2025',
 [r('Google gave $1 million to the 2025 Trump inaugural committee; a Google executive said this matched past inaugurations. The article names Sergey Brin and Sundar Pichai as having met Trump after the election and does not mention Larry Page.','NBC Washington / CNBC','https://www.nbcwashington.com/news/business/money-report/google-donates-1-million-to-trumps-inauguration-fund-joining-other-tech-giants/3809421/?amp=1','2025-01-09','Corporate donation; no Page-specific content')],
 [r('Judge Mehta’s September 2025 remedies ruling in the Google search case rejected Chrome and Android divestiture but imposed data-sharing and exclusivity limits. Continued enforcement and mixed remedies do not show a protective political bargain, and the ruling is not evidence about Page personally.','Hughes Hubbard & Reed (law firm summary)','https://www.hugheshubbard.com/news/court-issues-remedies-ruling-in-united-states-v-google-search-case','2025-09','Legal update / limit of evidence','Page text reviewed; secondary law-firm summary, not the opinion')],
 'Company conduct is not transferred to a co-founder. No personal donation, lobbying, access or contract evidence about Page was located in this review, and the search tool returned nothing on his political giving. Absence of findings is not a finding of absence.')

# ---- Sergey Brin
add('sergey-brin','mixed',NARROW,
 'Brin personally became a large political spender in 2026, reportedly funding a campaign against California’s proposed one-time billionaire tax and attending Trump-related events. This is open electoral activity directly tied to his own wealth interests; the reviewed material does not show a preferential benefit already obtained, and the ballot outcome (3 November 2026) is pending at review date.',
 'Large personal political spending on a measure affecting his wealth; access to officials; benefit not established',
 '2025–2026',
 [r('Il Post, citing New York Times reporting of April 2026, says Brin moved to Nevada before the end of 2025, gave $57 million over four months to Building a Better California, recruited other tech executives, backed a Republican candidate for governor, and has had repeated contact with Trump. Figures are from secondary reporting of the NYT.','Il Post (Italian; summarizing the New York Times)','https://www.ilpost.it/2026/05/08/sergey-brin-google-spostamento-destra/','2026-05-08','Secondary report of personal political spending and access','Page text reviewed in Italian; underlying NYT article not read'),
  r('NewsNation reports the Billionaire Tax Act (Prop 40) as a one-time 5% tax, that Prop 42 would bar retroactive taxes and is funded by Brin, and that Governor Newsom endorsed Prop 42 in October. It gives no dollar totals.','NewsNation (CalMatters reporting relayed)','https://www.newsnationnow.com/politics/gavin-newsom-california-ballot-measure-billionaire-tax/amp','2026-10','Current ballot-measure context','Page text reviewed; the article contains an apparent internal numbering error for the measure'),
  r('Brin and Pichai met Trump after the 2024 election; Google gave $1 million to the inaugural fund. The article does not tie the meeting to any request or outcome.','NBC Washington / CNBC','https://www.nbcwashington.com/news/business/money-report/google-donates-1-million-to-trumps-inauguration-fund-joining-other-tech-giants/3809421/?amp=1','2025-01-09','Access episode','Page text reviewed')],
 [r('The ballot spending is a public electoral process in which opponents also raise money; a pre-election poll cited by NewsNation had 45% supporting and 43% opposing Prop 40. Spending on a ballot measure is not by itself preferential treatment, and the vote is undecided.','NewsNation','https://www.newsnationnow.com/politics/gavin-newsom-california-ballot-measure-billionaire-tax/amp','2026-10','Alternative explanation / limit of evidence'),
  r('Il Post attributes Brin’s stated motive to his family’s Soviet-era history and concerns about California, and sources close to him credit his partner’s influence; these are his and others’ stated reasons, not an independent finding.','Il Post','https://www.ilpost.it/2026/05/08/sergey-brin-google-spostamento-destra/','2026-05-08','Subject response / alternative explanation','Page text reviewed in Italian')],
 'Review limited to secondary reports; amounts differ across outlets and some relied on search summaries not read. Open political spending to defeat a tax does not equal a preferential benefit, and the measure was undecided at review date. No score is assigned; not exoneration.')

# ---- Amancio Ortega
add('amancio-ortega','no-strong',NARROW,
 'Searches found large donations of medical equipment to Spanish public health systems and criticism of Inditex’s tax structures, but no reviewed evidence of political leverage, preferential state treatment or an exchange. Donations and tax planning alone do not justify points.',
 'Philanthropic agreements with regional governments; separate tax-avoidance allegations about Inditex',
 '2015–2017 donations; 2016 tax report',
 [r('The Amancio Ortega Foundation signed an agreement with Galicia’s Xunta/Sergas to fund about €17 million of oncology equipment, including 16 mammography units and 12 linear accelerators.','Redacción Médica','https://www.redaccionmedica.com/autonomias/galicia/20151022/fundacion-amancio-ortega-dona-millones-para-equipamiento-tecnologico-de-oncologia/342729_0.html','2015-10-22','Public-private donation agreement','Page text reviewed'),
  r('A Green group report in the European Parliament alleged Inditex avoided at least €585 million in tax in 2011–2014 using legal structures in the Netherlands, Ireland and Switzerland. This is an allegation about corporate planning, not a finding of unlawfulness or personal political favor.','Retail Gazette','https://www.retailgazette.co.uk/blog/2016/12/zara-accused-of-aggressive-tax-avoidance/','2016-12-09','Corporate allegation','Page text reviewed; sums vary by currency in reports')],
 [r('Inditex said the report was based on mistaken premises, and the report itself called the techniques legal. Critics of the donations, including Podemos and a public-health federation, argued about taxation and privatization; the foundation said the equipment would improve diagnosis and treatment. No source here alleges that the donations bought state favors.','Retail Gazette; Expansión (Mexico)','https://expansion.mx/empresas/2017/06/14/el-creador-de-zara-genera-polemica-en-espana-por-donacion','2017-06-14','Subject response / limit of evidence','Page text reviewed')],
 'Narrow review; Spanish-language political-influence reporting, procurement records and lobbying filings were not searched in depth. Not exoneration.')

# ---- Waltons
WALTON_US='https://united4respect.org/reports/walmart-political-spending-2024/'
WALTON_NWA='https://www.nwaonline.com/news/2020/oct/18/data-shows-some-walton-giving-leans-to-left/'
add('rob-walton','no-strong',NARROW,
 'The reviewed sources show Rob Walton as a Republican-leaning political donor, including near-total funding of a small super PAC in the 2024 cycle. They do not show a preferential benefit or exchange. The entry is a family record; evidence is attributed to Rob Walton personally only where stated.',
 'Personal political donations; no exchange identified',
 '1997–2024',
 [r('The advocacy report says Rob Walton provided nearly all of just over $1 million raised by Big Sky Action Fund, a super PAC that passed nearly all of it to Conservative Values for Utah.','United for Respect (advocacy group report)',WALTON_US,'c. 2024-10','Advocacy analysis of personal donation','Page text reviewed; undated, data through late 2024; author is a labor-aligned advocacy group'),
  r('Rob Walton gave mostly to Republicans since 1997, including recent gifts to Senators Sullivan and Portman.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Donation record')],
 [r('The Democrat-Gazette found Walton family giving split across parties (with several members, including Rob’s children, giving to Democrats) and no direct Walton donations to Trump campaigns in 2016 or 2020.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Alternative explanation / limit of evidence'),
  r('The advocacy report’s own methodology notes coding choices and undercounts; donations are not evidence of benefit.','United for Respect: methodology',WALTON_US,'c. 2024-10','Limit of evidence')],
 'Walmart corporate lobbying and policy interests were not reviewed individually. Donations do not establish benefit; not exoneration.')
add('jim-walton','no-strong',NARROW,
 'Reviewed sources show Jim Walton as the largest Walton political donor in the 2023–24 cycle (including $10 million to Americans for Prosperity per an advocacy report). Political spending is documented; no preferential benefit or exchange was found. The entry is a family record, and evidence is attributed to Jim personally only where stated.',
 'Personal political and issue-group donations; no exchange identified',
 '2019–2024',
 [r('The report says Jim Walton gave $10 million to Americans for Prosperity and over $2 million to pro-charter groups in the 2023–24 cycle, listing him at $14.7 million.','United for Respect (advocacy group report)',WALTON_US,'c. 2024-10','Advocacy analysis of personal donation','Page text reviewed; undated; advocacy source'),
  r('Jim Walton gave to Republican candidates and committees, including $143,000 to the NRSC in 2020.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Donation record')],
 [r('Report methodology codes issue PACs as nonpartisan and relies on address/occupation matching; donations to issue groups are lawful political expression and not evidence of benefit.','United for Respect: methodology',WALTON_US,'c. 2024-10','Limit of evidence'),
  r('The Democrat-Gazette found no direct Walton donations to Trump campaigns in 2016 or 2020.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Limit of evidence')],
 'No procurement, regulatory or policy-outcome evidence for Jim Walton was reviewed. Not exoneration.')
add('alice-walton','no-strong',NARROW,
 'Reviewed sources show Alice Walton as a donor who moved from Republican to mostly Democratic giving after 2013, with a $5 million gift to Americans for Prosperity reported in the 2023–24 cycle. No leverage, benefit or exchange evidence was found.',
 'Personal political donations; no exchange identified',
 '2013–2024',
 [r('The Democrat-Gazette says Alice Walton gave only to Republicans through 2012, then $25,000 to Ready for Hillary in 2013 and mostly Democrats since, while still backing Rep. Womack.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Donation record'),
  r('The advocacy report says Alice Walton donated $5 million to Americans for Prosperity in the 2023–24 cycle.','United for Respect (advocacy group report)',WALTON_US,'c. 2024-10','Advocacy analysis','Page text reviewed; undated; advocacy source')],
 [r('Her mixed-party giving and the absence of any identified exchange are limits on a partisan-capture reading.','Northwest Arkansas Democrat-Gazette',WALTON_NWA,'2020-10-18','Alternative explanation / limit of evidence')],
 'Museum and philanthropic activity were not examined for political leverage. Not exoneration.')

# ---- Ballmer
add('steve-ballmer','no-strong',NARROW,
 'The reviewed episode is the Clippers’ Inglewood arena: a negotiating agreement with the city, litigation by rivals and a neighborhood group, a 2019 ruling against one suit, and a $400 million purchase of the Forum to settle the dispute. Local approvals are documented; no reviewed source shows a preferential public benefit or improper influence by Ballmer.',
 'Local government approval of a private arena; no benefit or exchange established',
 '2017–2024',
 [r('MSG’s 2017 suit argued Inglewood violated state law by approving exclusive negotiations with Ballmer’s Clippers and withheld public records; the mayor was said to have promised no competing development.','Bisnow',
 'https://www.bisnow.com/news/los-angeles/neighborhood/forum-files-lawsuit-against-the-city-of-inglewood-77146','2017-07-31','Litigation allegation by a commercial rival','Page text reviewed; claims are MSG’s allegations')],
 [r('Wikipedia’s account says a judge ruled against Uplift Inglewood in November 2019, CARB approved the arena in December 2019, and the article does not mention public subsidies. MSG was itself accused of using litigation to block a competitor.','Wikipedia: Intuit Dome (secondary)','https://en.wikipedia.org/wiki/Intuit_Dome','2026','Alternative explanation / limit of evidence','First ~100,000 characters read; secondary, user-edited source')],
 'Narrow single-episode review; Microsoft-era history and personal political giving were not reviewed. Not exoneration.')

# ---- Gates
add('bill-gates','mixed',NARROW,
 'Two distinct strands: the Microsoft-era corporate political spending during the antitrust case, and the Gates Foundation’s role as a very large global-health funder, with experts and critics disagreeing on how much agenda-setting influence follows. A July 2026 external review of the foundation’s contacts with Jeffrey Epstein found no evidence of payment to Epstein. None of this establishes a personal preferential economic benefit or exchange, so no score is assigned.',
 'Corporate lobbying (historical); philanthropic agenda-setting influence (contested); no personal exchange established',
 '2000–2026',
 [r('During the antitrust fight Microsoft ran a broad lobbying and public-relations campaign and funded research groups and trade groups; the article does not mention Bill Gates.','New York Times News Service via Deseret News','https://www.deseret.com/2000/6/13/19545358/microsoft-shelling-out-dough-for-lobby-effort/','2000-06-13','Corporate lobbying report','Page text reviewed; Gates is not named'),
  r('Undark reports expert concern that the foundation concentrates unaccountable power and may set WHO and donor-government agendas; it also says the article documents no specific decision in which the foundation directed WHO or government policy.','Undark','https://undark.org/2025/07/02/gates-foundation-global-reach/','2025-07-02','Scholarly/expert concern with stated evidence limits','Page text reviewed'),
  r('A WilmerHale review found about 30 foundation meetings with Epstein in 2011–2014 and a related polio grant to an institute led by an Epstein associate; no evidence the foundation paid Epstein. Gates called the contact a grave error in judgment.','AP via ClickOnDetroit','https://www.clickondetroit.com/business/2026/07/21/the-gates-foundation-met-with-epstein-about-30-times-despite-staff-concerns-an-external-review-says/','2026-07-21','Independent review summary','Page text reviewed; only a three-page summary was released')],
 [r('Microsoft’s giving later shifted toward Democrats and its PAC was described as leaning Republican overall; the article does not mention Gates.','Redmond Magazine','https://rcpmag.com/articles/2004/10/01/following-microsofts-money.aspx','2004-10-01','Corporate context / limit of evidence'),
  r('Gates funding to WHO is mostly earmarked and WHO’s main budget comes from member-state contributions; the foundation says it informs rather than sets WHO’s agenda and publishes a grants database.','Undark','https://undark.org/2025/07/02/gates-foundation-global-reach/','2025-07-02','Foundation response / structural limit','Page text reviewed'),
  r('The Epstein review did not access Gates’s personal communications and found no claim that Epstein shaped foundation policy.','AP via ClickOnDetroit','https://www.clickondetroit.com/business/2026/07/21/the-gates-foundation-met-with-epstein-about-30-times-despite-staff-concerns-an-external-review-says/','2026-07-21','Limit of evidence')],
 'Philanthropic reach is not state patronage or a private economic benefit. Microsoft corporate conduct is not assigned to Gates personally, and the Epstein review is not evidence about policy. Not exoneration; narrow review.')

# ---- Bettencourt Meyers
add('francoise-bettencourt-meyers','no-strong',NARROW,
 'The well-documented political episode involving this family (the 2010 Bettencourt affair) concerns her late mother Liliane Bettencourt, not Francoise Bettencourt Meyers. The reviewed sources do not mention her, and no personal leverage, benefit or exchange evidence was found. The entry is a family record.',
 'Historical family-wealth political scandal concerning a different family member; no personal mechanism identified',
 '2010–2015 episode (Liliane Bettencourt)',
 [r('Reports in July 2010 described allegations by a former bookkeeper that Liliane Bettencourt made illegal cash donations to politicians, and a minister’s conflict of interest; Woerth and the wealth manager denied the allegations, and a tax inspectorate report found Woerth had not intervened in the family’s tax affairs. Francoise Bettencourt Meyers is not mentioned.','Al Jazeera','https://www.aljazeera.com/news/2010/7/12/sarkozy-backs-scandal-hit-minister','2010-07-12','Allegation concerning another family member','Page text reviewed'),
  r('The 2015 Bordeaux trial concerned abuse of weakness of Liliane Bettencourt; prosecutors requested Woerth’s acquittal. The final verdict was not confirmed in a page I could read.','RTBF','https://www.rtbf.be/article/france-proces-bettencourt-relaxe-requise-pour-l-ex-ministre-eric-woerth-8912081','2015-02-20','Trial context','Page text reviewed; verdict not on page')],
 [r('Wikipedia’s account notes Sarkozy was removed from the list of those to be charged in October 2013, Banier’s conviction was upheld in 2016, and Francoise Bettencourt Meyers is not mentioned. Allegations about her mother are not transferred to her.','Wikipedia: Bettencourt affair (secondary)','https://en.wikipedia.org/wiki/Bettencourt_affair','2026','Identity boundary / limit of evidence','Page text reviewed; secondary source')],
 'Identity: do not attribute Liliane Bettencourt’s episode to Francoise. L’Oreal lobbying, French tax policy and her own political activity were not reviewed. Not exoneration.')

# ---- Mukesh Ambani
add('mukesh-ambani','mixed',NARROW,
 'Reviewed reports document recurring accusations by rivals, opposition parties and a state government that Reliance benefited from favorable policy decisions, and one dated episode where an internal ministry objection to the Jio Institute designation was overridden. Each has an official or company explanation, and the 2014 gas-price FIR is an allegation, not a finding. The estimate is deliberately weak and wide.',
 'Contested policy and regulatory decisions favoring Reliance interests; allegations and procedural objections, not adjudicated exchange',
 '2014–2018 episodes; 2017 regulatory disputes',
 [r('Indian Express RTI records reported by Business Today show the Finance Ministry’s expenditure department called Institute of Eminence status for not-yet-established private institutions “beyond rationale”; the HRD Ministry nonetheless granted the tag, and the Jio Institute was among six selected.','Business Today (citing Indian Express RTI)','https://www.businesstoday.in/amp/latest/economy-politics/story/jio-institute-row-finance-ministry-warned-hrd-ministry-against-granting-institute-of-eminence-tag-non-existent-institutions-108990-2018-08-29','2018-08-29','Internal-record report of procedural objection'),
  r('Scroll reported that the designation exempts institutions from most regulation, that Jio had none of the required features yet, and that some academics suspected the selection favored Reliance.','Scroll.in','https://scroll.in/article/885897/reliances-jio-university-gets-governments-institute-of-eminence-status-but-its-yet-to-be-set-up','2018-07-09','Contemporaneous report and criticism'),
  r('Delhi’s chief minister alleged Reliance made windfall gains through KG-D6 gas pricing and ordered FIRs against Ambani, two oil ministers and a former regulator. Reliance has consistently denied price manipulation; Moily dismissed the claims.','Gulf News','https://gulfnews.com/amp/story/world%2Fasia%2Findia%2Faap-leader-arvind-kejriwal-takes-on-ambani-over-price-fixing-1.1289732','2014-02','Allegation by a state government','Page text reviewed; page metadata shows 2018, but content describes the 2014 FIR, so the date is approximate'),
  r('The Wire described Jio prevailing in three regulatory disputes in 2017 (free data offer, 2010 spectrum auction rules, test trials) under the attorney general’s advice and a Supreme Court dismissal; the article frames this as contested and still subject to CCI review.','The Wire','https://cms.thewire.in/106628/absolved-thrice-reliance-jio-now-faces-final-regulatory-challenge','2017-02-07','Regulatory outcomes favoring Jio; critical framing')],
 [r('The HRD Ministry said the designation was conditional on Jio meeting benchmarks within three years, was awarded in a greenfield category where 11 applications were received and only Jio met four criteria, and denied a reported government grant to Jio. The expert committee, led by a former chief election commissioner, chose only six of 20 planned places.','Gulf News; Newslaundry','https://gulfnews.com/world/asia/india/indian-officials-backtrack-on-jio-institute-honour-1.2249409','2018-11-05','Government response / alternative explanation','Page text reviewed'),
  r('Newslaundry reports the committee chair saying breaking into the top 500 is hard and only six institutions merited the designation, and the UGC defended Jio under the greenfield rules.','Newslaundry','https://www.newslaundry.com/2018/07/10/jio-institute-institutions-of-eminence-prakash-javadekar-mhrd','2018-07-10','Official justification','Page text reviewed; no Reliance statement on page'),
  r('Reliance denied KG-D6 manipulation; the Wire notes Jio argued it was not dominant and that regulators and the attorney general found no breach of the cited rules. A regulatory win is not itself proof of political favor.','Gulf News; The Wire','https://cms.thewire.in/106628/absolved-thrice-reliance-jio-now-faces-final-regulatory-challenge','2017-02-07','Subject response / alternative explanation')],
 'Evidence is mostly contemporaneous press reporting of 2014–2018 episodes; I did not read the CAG reports, the final status of the 2014 FIR, or any 2020s Reliance matters. Search snippets on the Radia tapes and telecom audits were not used because the underlying pages were not read. The estimate reflects allegation-heavy, historically bounded evidence and is not a finding of wrongdoing.',
 rubric=([2,2,1],[10,55],
  ['Accusations of access and influence come from rivals, opposition parties and a state government; one internal objection was overridden, but no adjudicated exchange.',
   'Jio Institute designation and favorable regulatory outcomes are documented, with official justifications and conditions; benefit is plausible but contested.',
   'A recurring pattern is alleged by critics, but no reviewed source shows wealth converted to power that in turn secured wealth; weakest dimension.'],
  [[2,0],[0,3],[2,3]]))

R.pop('mukesh-ambani',None)  # score withheld: 2014-2018 allegations only partly read; CAG reports, Radia tapes and FIR outcome not reviewed; exchange evidence weak
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
(ROOT/'data/review-batches/021.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
