"""Wave 30: narrow source-led reviews; most entries are profile-only (no rubric) because evidence is thin or not person-specific."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,status='mixed',levels=None,bounds=None,notes=None,refs=None,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; absence of evidence found is not exoneration',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if levels:
  R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
WP='Encyclopedia summary page read; its cited sources were not independently checked'

# 1 Alwaleed
UPI='https://www.upi.com/Top_News/World-News/2018/01/27/Saudi-billionaire-prince-freed-after-paying-settlement/6571517068907/'
CYP='https://archive.cyprus-mail.com/2018/01/27/saudi-billionaire-prince-alwaleed-released/'
MM='https://www.malaymail.com/news/money/2022/05/22/saudi-billionaire-prince-to-sell-1687pc-of-firm-to-sovereign-fund/8233'
add('prince-alwaleed-bin-talal-alsaud',
 'The reviewed record concerns state power exercised over Alwaleed: his November 2017 detention in a crown-prince-led anti-corruption campaign, a financial settlement with no disclosed terms, and a 2022 sale of a Kingdom Holding stake to the Public Investment Fund. It does not document him obtaining a specific preferential benefit from officials, so no estimate is made.',
 'State leverage over a royal-family businessman → undisclosed settlement; later sale to a state fund (direction of influence unresolved)',
 'Detention November 2017 to January 2018; Kingdom Holding stake sale announced May 2022',
 [r('UPI reports that Alwaleed was arrested in November 2017 at the Riyadh Ritz-Carlton, that the state prosecutor approved an unspecified financial settlement, and that the amount was not disclosed. The crackdown was led by Crown Prince Mohammed bin Salman and was seen as consolidating his power.','UPI',UPI,'2018-01-27','Release and settlement report'),
  r('Malay Mail reports Alwaleed selling a 16.87% stake (625 million shares, roughly US$1.5 billion per a Tadawul filing) in Kingdom Holding to the Public Investment Fund, which the crown prince chairs, and describes the earlier detention as seen by critics as a power grab.','Malay Mail (news agency report)',MM,'2022-05-22','Transaction with state fund; terms beyond the filing not reviewed')],
 [r('Reuters, via Cyprus Mail, quotes Alwaleed saying "There are no charges", "I have nothing to hide at all" and that he maintained his innocence. A senior Saudi official would neither confirm nor negate that the attorney general was convinced of his innocence. The allegations (money laundering, bribery, extorting officials) were reported as allegations only.','Reuters via Cyprus Mail',CYP,'2018-01-27','Subject response and limit of evidence'),
  r('Neither the UPI nor the Malay Mail report states that the settlement terms or the 2022 sale price were preferential; the filing reports a price but the pages reviewed do not assess whether it was above or below market.','Limit of reviewed pages',MM,'2022-05-22','Explicit limit of the evidence','Reviewed pages: UPI and Malay Mail; no valuation analysis read')],
 'Only wire and news reports were read; no court record exists because no charges were reported. This is not exoneration and not a finding of wrongdoing. Coercion by a state is different from the wealthy-to-power influence the scale measures, and royal status, nationality, a detention or a settlement alone do not justify points. Alwaleed’s earlier decades and Kingdom Holding’s dealings with the state were not reviewed.')

# 2 Chearavanont
AT='https://asiatimes.com/2020/10/a-monopoly-moment-of-truth-for-thailand/'
VIBES='https://www.thevibes.com/articles/business/5244/tesco-gets-nod-to-sell-thai-supermarket-business'
add('dhanin-chearavanont',
 'Commentators quoted in the press say Thailand’s large conglomerates, including CP Group, have political connections that could blunt competition enforcement. The one concrete test reviewed, the 2020 Tesco Lotus acquisition, ended with the regulator finding market dominance possible but not a monopoly and imposing a three-year bar on further retail mergers. That is mixed evidence at group level and says nothing specific about Dhanin personally, so no estimate is made.',
 'Corporate scale and alleged political connections → competition-regulator treatment (outcome mixed)',
 '2020 Tesco Thailand acquisition and OTCC decision; background commentary only',
 [r('Asia Times reports that a historian (Chris Baker) said close connections between monopoly holders and the government made a tough ruling unlikely, and that the regulator might seek a compromise given the "politically powerful CP Group". These are quoted opinions, not findings.','Peter Janssen / Asia Times',AT,'2020-10-12','Attributed expert commentary'),
  r('The Vibes reports the OTCC majority agreed the US$10.6 billion Tesco Thailand/Malaysia deal could create market dominance but was not a monopoly, and that CP Group may not pursue other retail merger deals for three years.','The Vibes',VIBES,'2020-11-07','Regulatory outcome report')],
 [r('The regulator imposed a three-year restriction on further retail mergers, and a member of its vetting committee publicly argued the deal would create a monopoly, which cuts against a claim of unconditional protection; the outcome nevertheless permitted the deal.','The Vibes',VIBES,'2020-11-07','Mixed outcome / alternative explanation'),
  r('CP Group did not comment on the regulator’s decision, so the reviewed record contains no company response to the political-connection claims. The Asia Times piece presents them as source opinion.','Asia Times; The Vibes',AT,'2020-10-12','Limit of evidence')],
 'Narrow review: two news pages. The group’s decisions are not attributed to Dhanin personally. Earlier-era claims about relationships with former prime ministers appeared only in an unreliable search snippet and were not used. No sanction, conviction or preferential contract was reviewed. Not exoneration.')

# 3 Doerr
PI='https://publicintegrity.org/politics/green-bundler-with-the-golden-touch/'
add('john-doerr',
 'John Doerr has documented political access: he served on President Obama’s Economic Recovery Advisory Board, he and Kleiner Perkins executives gave over $1 million to federal causes (mostly Democratic) across two decades, and he hosted Obama at a 2011 fundraising dinner, while Kleiner-backed green-energy companies received federal Energy Department funding. The reviewed article presents these as questions about access and does not allege improper conduct, so no estimate is made.',
 'Political giving and advisory role → access; portfolio-company federal funding (link unproven)',
 '2009–2011 Obama administration clean-energy funding period',
 [r('The Center for Public Integrity reports Doerr and Kleiner Perkins executives gave more than $1 million to federal political causes over two decades, mostly to Democrats; that Doerr served on the Economic Recovery Advisory Board; that he hosted Obama at his estate in February 2011; and that several Kleiner-backed green-tech firms received Energy Department funding.','Ronnie Greene and Matthew Mosk / Center for Public Integrity',PI,'2011-03-30','Investigative report','First 100,000 of about 117,000 characters read')],
 [r('The same article says public records show no indication that the GAO or Energy Department inspector general inquiries focus on Doerr or his firm, does not claim his giving or advisory role was improper, and reports that Doerr did not respond to interview requests about the Obama dinner.','Center for Public Integrity: limits and response',PI,'2011-03-30','Explicit limit of the evidence')],
 'The principal source is 2011 and the later years, Doerr’s later climate advocacy and any other policy episodes were not reviewed. Funding of portfolio companies is not personal benefit; no award was shown to be influenced. Not exoneration, not an allegation of wrongdoing.')

# 4 Lemann
SUNO='https://www.suno.com.br/noticias/americanas-amer3-lemann-sicupira-telles-cvm/amp/'
WL='https://en.wikipedia.org/wiki/Jorge_Paulo_Lemann'
add('jorge-paulo-lemann',
 'No specific, reliable evidence of political leverage, preferential state benefit or an exchange was found in this narrow review of the Forbes family entry, which concerns Jorge Paulo Lemann. The one regulatory matter reviewed, the CVM proceeding over the 2023 Americanas accounting scandal, concerns disclosure by reference shareholders, not political power.',
 'Not established: no political-power mechanism found in sources read',
 '2023 CVM proceeding on Americanas; background profile',
 [r('The CVM said on 19 January 2023 it created a task force on the Americanas accounting scandal, and that one of seven administrative proceedings examines the possible responsibility of reference shareholders Lemann, Sicupira and Telles regarding information given to the market. If infractions are formally established, those responsible could be held accountable.','Suno Notícias (Portuguese)',SUNO,'2023-01-19','Regulatory proceeding report; no finding')],
 [r('No findings or charges are reported in that article, and it carries no response from the three shareholders. The matter concerns market disclosure by a company, not a political exchange.','Suno Notícias: limit of evidence',SUNO,'2023-01-19','Explicit limit of the evidence'),
  r('The Wikipedia profile does not mention political ties, CADE’s Ambev approval, BNDES financing or donations; claims about those from search snippets (a Portuguese advocacy blog on CADE’s 1999 approval) were not read or used.','Wikipedia: Jorge Paulo Lemann',WL,'2026-10-29','Gap in coverage',WP)],
 'Very narrow review; the family entry means other members were not separately reviewed. The 1999 Ambev merger approval, any public-bank financing and Brazilian political donations were searched but not verified from reliable pages, and a search limit prevented further queries. Not exoneration.',
 status='no-strong')

# 5 Hartono
CAP='https://www.caproasia.com/?p=69377'
add('r-budi-hartono',
 'No reliable evidence on political leverage, state preference or an exchange involving Budi Hartono was found. The only item surfaced, an unsourced investment-newsletter line about a son’s travel ban in a tax investigation, is unverified and concerns a different person.',
 'Not established',
 '2025–2026 unverified report; background profile',
 [r('A newsletter obituary page for his brother Michael Hartono says Budi’s eldest son Victor, Djarum Group CEO, was issued a six-month travel ban in a tax-reduction corruption investigation and mentions his relationships with Presidents Prabowo and Widodo. The page cites no sources or official statements, and the year is given only in a summary line.','Caproasia (unsourced newsletter)',CAP,'2026-03-21','Unverified lead only','Page read partly; claim not corroborated in mainstream outlets I could read')],
 [r('The claim is unsourced, concerns Victor Hartono, not Budi, and does not explain what the presidential relationships involve or link them to the investigation; it should not be treated as evidence.','Caproasia: limit',CAP,'2026-03-21','Explicit limit of the evidence'),
  r('The Wikipedia articles on Budi Hartono and Djarum describe business activities (Djarum, a Bank Central Asia stake) and contain no political ties, excise or regulatory matters involving him; they report only a 2016 Human Rights Watch child-labor finding on Indonesian tobacco firms.','Wikipedia: Robert Budi Hartono (and Djarum page, both read)','https://en.wikipedia.org/wiki/Robert_Budi_Hartono','2026-10-29','Gap in coverage',WP)],
 'Search limits prevented a corroborating query on the travel-ban report and on tobacco excise policy. Nothing here accuses Budi Hartono or establishes the claim about his son. Not exoneration.',
 status='no-strong')

# 6 Bailleres
ELCEO='https://elceo.com/negocios/palacio-de-hierro-penoles-y-gnp-las-empresas-detras-de-la-fortuna-de-13500-mdd-de-alejandro-bailleres/'
add('alejandro-bailleres-gual',
 'No evidence of political leverage, preferential state benefit or an exchange was found for Alejandro Baillères Gual in this narrow review. The family entry spans Grupo Bal (Peñoles, Fresnillo, Palacio de Hierro, GNP, Profuturo), a mining-and-financial group; attribution between family members was not resolved.',
 'Not established',
 'Current ownership profile, 2026',
 [r('El CEO (18 July 2026) describes Alejandro Baillères as chairman of Grupo Bal and heir of Alberto Baillères, who died in 2022, with a 44% Peñoles stake held through a control trust, and Peñoles owning almost 75% of Fresnillo. It reports business holdings, nothing about government or political ties.','El CEO (Spanish)',ELCEO,'2026-07-18','Ownership profile only')],
 [r('The page mentions no government or political ties, so it provides no support for a wealth-power mechanism; it is a gap in what was reviewed.','El CEO: limit',ELCEO,'2026-07-18','Explicit limit of the evidence')],
 'Mining concessions, government contracts and Mexican political ties were not verified because the search budget was exhausted. Alberto Baillères’ own history is a different person’s record and was not scored. Not exoneration.',
 status='no-strong')

# 7 Anschutz
UD='https://www.utilitydive.com/news/largest-planned-wind-farm-in-us-gets-key-federal-approval/565795'
WA='https://en.wikipedia.org/wiki/Philip_Anschutz'
add('philip-anschutz',
 'Anschutz is a documented Republican and conservative-institution donor, and an Anschutz-owned developer received federal land-use approvals for the Chokecherry and Sierra Madre wind project. The reviewed material does not link donations to those approvals, which proceeded through public environmental review, so no estimate is made.',
 'Political giving (context) and federal permitting (separate)',
 'Donations 2016–2017; BLM approvals 2017 and 2019; 2001 drilling decision',
 [r('The Wikipedia summary reports Anschutz giving $1 million to conservatives in the 2016 elections and $200,000 in 2017, funding conservative think tanks through his foundation, and a 2006 letter from his lawyer to the White House counsel recommending Neil Gorsuch for a Tenth Circuit seat. It also reports the Bush administration upholding his right to drill at Weatherman Draw in 2001.','Wikipedia: Philip Anschutz',WA,'2026-10-29','Secondary summary',WP+'; first 100,000 of about 136,000 characters read'),
  r('Utility Dive reports that Power Company of Wyoming, an Anschutz Corporation affiliate, received a BLM environmental assessment (October 2019, draft for public comment) for the second phase of the Chokecherry and Sierra Madre wind project, up to 1,000 turbines, with the first phase assessed in January 2017.','Utility Dive',UD,'2019-10-25','Permitting report')],
 [r('Utility Dive notes the approval came despite President Trump’s opposition to wind power and a 2018 BLM rejection of another large wind project, and that the assessment was a draft open to comment. The project’s completion slipped from 2020 to 2026 owing to permitting delays, which cuts against a claim of smooth political access.','Utility Dive: context',UD,'2019-10-25','Counterevidence / alternative explanation'),
  r('On Qwest, the Wikipedia summary reports the company paid a $250 million SEC penalty without admitting or denying and that Anschutz was not charged criminally; the SEC and DOJ found no justification for action against any Qwest board member. That is corporate conduct and not a political-power finding.','Wikipedia: Philip Anschutz (Qwest, Spitzer matters)',WA,'2026-10-29','Legal limit',WP)],
 'Wikipedia is a secondary summary and its sources were not checked. The Spitzer settlement (no wrongdoing admitted) and Qwest matters are not political power. Donations, land permits and company size alone earn no points; later policy episodes were not reviewed. Not exoneration.')

# 8 Menard
YAH='https://www.yahoo.com/news/wisconsin-gov-scott-walker-photo-charlie-114429739886.html'
WPR='https://wpr.org/economy/menards-president-gave-1-5m-wisconsin-club-growth-yahoo-news-reports'
MPR='https://www.mprnews.org/story/2015/07/16/npr-scott-walker'
add('john-menard-jr',
 'Yahoo News reported in 2015, from documents seized in the Wisconsin "John Doe" probe and three sources, that Menard gave more than $1.5 million in 2011-2012 to the Wisconsin Club for Growth, which backed Governor Walker’s recall defense, and that his company later received up to $1.8 million in state tax credits from an economic-development body Walker chaired. The governor’s office denied any special favors. Evidence of causation is circumstantial and the 2015 reporting is the latest reviewed.',
 'Large undisclosed political giving → access; later state tax credits (link unproven)',
 'Donations 2011–2012; tax credits 2013–2014 as reported; reporting March 2015',
 [r('Michael Isikoff reports Menard wrote checks totaling more than $1.5 million in 2011 and 2012 to the Wisconsin Club for Growth, found in documents seized in the John Doe 2 probe and confirmed by three sources, and that Menards was awarded up to $1.8 million in tax credits by the Wisconsin Economic Development Corporation. It also reports Walker’s appointees scaling back DNR enforcement, described as a Menard priority; environmental referrals fell from an average of 68 to 34 a year.','Michael Isikoff / Yahoo News',YAH,'2015-03-24','Investigative report relying on seized documents and unnamed sources'),
  r('WPR summarizes the Yahoo report, notes court documents suggested Walker encouraged donations to the Club, and that Yahoo suggested Menard received WEDC grants after the donations.','Shawn Johnson / Wisconsin Public Radio',WPR,'2015-03-24','Secondary report')],
 [r('Walker’s spokeswoman denied special favors, said he was not involved in the tax-credit decision, noted that Menards received $1.5 million in credits in 2006 under Democratic Governor Doyle (later reduced to $1 million for missing job targets), and that the DNR drop reflected a policy of working with businesses early. Menard did not respond to requests for comment.','Yahoo News: responses',YAH,'2015-03-24','Subject response'),
  r('The Wisconsin Supreme Court ruled 4-2 on 16 July 2015 that no laws were broken in the Walker recall-campaign coordination inquiry and closed the John Doe investigation. The report does not mention Menard; the ruling concerns the campaign, not Menard’s donations or credits. The donations themselves were legal and undisclosed.','Minnesota Public Radio / NPR',MPR,'2015-07-16','Legal outcome / limit of evidence'),
  r('Per Yahoo, the 2006 credits had been reduced for missed job targets, WPR notes Walker’s office said WEDC also granted funds to companies run by prominent Democrats, and no source reviewed shows an agreement between Menard and Walker.','Yahoo News and WPR: Walker office response',YAH,'2015-03-24','Alternative explanation')],
 'A single 2015 investigative story with unnamed sources underpins the leverage and benefit dimensions; the estimate is deliberately low and wide. The donation and credit sequence is not proof of an exchange, and no wrongdoing finding exists. Menard’s later giving, other states and later years were not reviewed. Not a verdict.',
 levels=[2,2,1],bounds=[10,60],
 notes=['Large documented donations to a group allied with the governor give specific but indirect political leverage.','State tax credits of up to $1.8 million are documented, but Walker’s office said they followed job-performance criteria, with a 2006 precedent under another governor and a reduction then for missed job targets.','A donation-then-benefit sequence is reported but denied; no evidence of a bargain or of policy reshaped for him.'],
 refs=[[0,1],[0],[0,1]])

# 9 Chen Jianhua
TR='https://home.treasury.gov/news/press-releases/sb0472'
WH='https://en.wikipedia.org/wiki/Hengli_Group'
add('chen-jianhua',
 'Chen Jianhua co-founded and chairs Hengli Group with his wife Fan Hongwei. The reviewed record shows a 2010 partnership between Hengli and the Dalian municipal government and, in April 2026, a US Treasury designation of Hengli’s Dalian refinery over Iranian oil purchases, which the company denies. No evidence about political leverage, preferential benefit or an exchange attributable to Chen personally was found, so no estimate is made.',
 'Not established; entity-level sanctions and local-government partnership only',
 '2010 Dalian partnership; April 2026 OFAC action',
 [r('Treasury’s release dated 24 April 2026 sanctions Hengli Petrochemical (Dalian) Refinery, alleging it bought billions of dollars of Iranian petroleum including shipments overseen by Sepehr Energy. It names no individuals, so Chen is not mentioned.','US Department of the Treasury',TR,'2026-04-24','Government designation; allegation against a company','Page read; legal-basis list could not be confirmed'),
  r('A Wikipedia summary reports Hengli partnered with Dalian’s municipal government in 2010 to build a petrochemical park, that Chen and Fan are the actual controllers of the listed company (75.73% with concert parties), and Reuters reports China’s commerce ministry issued a May 2026 blocking order against US sanctions on five refiners including Hengli.','Wikipedia: Hengli Group',WH,'2026-10-29','Secondary summary',WP)],
 [r('Hengli Petrochemical said it complied with laws and has never traded with Iran. The Treasury page is a US government allegation against a company, not a finding against Chen, and OFAC action is not proof of Chinese political leverage.','Wikipedia: Hengli Group (company response and Treasury allegation)',WH,'2026-04-24','Subject response and entity limit'),
  r('The Wikipedia summary mentions no NPC or CPPCC membership, party roles or subsidies for Chen or Fan.','Wikipedia: Hengli Group',WH,'2026-10-29','Gap in coverage',WP)],
 'Identity: Forbes lists Chen Jianhua; the evidence read mostly concerns the company and his wife Fan Hongwei and is not attributed to him. Chinese party or legislative roles, subsidies and the 2015 refinery approval were not verified. Sanctions and local-government partnership alone earn no points. Not exoneration.',
 status='no-strong')

# 10 Bren
WB='https://en.wikipedia.org/wiki/Donald_Bren'
add('donald-bren',
 'Donald Bren is a long-time political donor and the owner of the Irvine Company, whose land holdings depend on local development approvals; newspapers have described him as exceptionally influential in Orange County. The reviewed material does not document a specific approval, subsidy or exchange tied to his giving, so no estimate is made.',
 'Land-owner influence over local development and political giving (specific exchange not shown)',
 'Long-running; references from 2005–2016',
 [r('The Wikipedia summary reports Bren giving to Republican causes including Pete Wilson’s campaigns and at least $135,000 to the California Republican Party, as well as Democrat Dianne Feinstein, and cites OC Weekly (2005) and the Los Angeles Times (2006) calling him more powerful than Howard Hughes and the most powerful person in Southern California.','Wikipedia: Donald Bren',WB,'2026-10-29','Secondary summary of press characterizations',WP)],
 [r('The same page documents no land-use controversy or specific approval, and reports land donations: about 55,000 acres over 30 years and preserved Irvine Ranch land reaching 60%. Press characterizations of influence are opinion, not evidence of an exchange.','Wikipedia: Donald Bren',WB,'2026-10-29','Explicit limit and alternative context',WP)],
 'Search limits prevented review of campaign-finance records, local council minutes or Great Park reporting. A bipartisan donor pattern and press descriptions of influence do not establish preferential treatment. Not exoneration.')

R.pop('john-menard-jr',None)  # score withheld: single 2015 investigation relying on unnamed sources; Walker investigation closed without findings on Menard
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
(ROOT/'data/review-batches/030.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
