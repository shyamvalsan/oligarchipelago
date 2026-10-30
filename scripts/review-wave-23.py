"""Wave 23: narrow profile-only reviews; evidence thin for a three-dimension rubric, so no rubrics added."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,status='no-strong'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed',confidence='Low / narrow review',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
NOTE=' This is a narrow review, not exoneration: absence of a documented mechanism in the sources read does not mean none exists.'

WBUR='https://www.wbur.org/onpoint/2025/03/24/masayoshi-son-tech-billionaire-artificial-intelligence-trump'
add('masayoshi-son',
 'Son has had public, high-level access to President Trump, including investment pledges announced alongside him and the Stargate AI venture. The reviewed sources document access and announcements, not a specific preferential government benefit to Son or a documented exchange.',
 'Large US investment pledge → White House access and announcement platform',
 'Investment pledges announced 2016 and 2024–2025; Stargate announcement January 2025',
 [r('WBUR’s interview-based discussion reports Son appearing in the Oval Office with Altman and Ellison on Trump’s first full day of his second term. It reports that Son said he had promised $100 billion at an earlier meeting and that Trump told him to aim for $200 billion, and that he returned with a $500 billion pledge. It also records a $50 billion, 50,000-job pledge after Trump’s 2016 win.','WBUR On Point: Masayoshi Son, Trump and AI',WBUR,'2025-03-24','Access and announcement evidence')],
 [r('The same program reports commentators calling the $500 billion four-year goal a stretch, questioning whether Son has the money, saying he tends to embellish, and noting that the 2016 pledge was hard to verify. Elon Musk also publicly doubted SoftBank’s funding, which Altman disputed. These are doubts about delivery, not evidence about a government favor.','WBUR On Point: caveats on funding and track record',WBUR,'2025-03-24','Counterevidence and limit of the evidence')],
 'No specific regulatory decision, contract, subsidy or other preferential benefit to Son or SoftBank was found in the pages read, and a private investment venture is not a government benefit. The CNN and CNBC pages that would give more primary detail on the announcements could not be retrieved (HTTP 451 and 403). No Japanese-side evidence was reviewed.'+NOTE)

NWA='https://www.nwaonline.com/news/2020/oct/18/data-shows-some-walton-giving-leans-to-left/'
add('lukas-walton',
 'The one dated source read reports Lukas Walton’s 2020 federal giving as Democratic-leaning and identifies him as a Walton Family Foundation board member. Broader reporting on Walton-family education and political spending concerns the family or foundation, not documented personal conduct by Lukas.',
 'Political donations and philanthropy → possible policy influence (not established for this person)',
 '2020 federal giving; foundation roles',
 [r('The Democrat-Gazette, citing FEC figures as of 21 September 2020, reports Lukas Walton, 34, gave $5,600 to Joe Biden’s campaign and $142,000 to the Democratic National Committee, sits on the Walton Family Foundation board and chairs its Environment Program Committee.','Northwest Arkansas Democrat-Gazette: Walton giving',NWA,'2020-10-18','Individual donation record (reported)')],
 [r('The same article says the broader Walton family has long backed mostly conservative candidates, with some shift left, so his giving cannot be assumed to match family patterns. Donations alone are not evidence of preferential treatment.','Northwest Arkansas Democrat-Gazette: family contrast',NWA,'2020-10-18','Limit of the evidence and context')],
 'Only one dated article was fully read. Search results about the foundation’s charter-school funding and a Georgia official’s remarks were not fetched and are not relied on; they concern the foundation or family. No policy benefit linked to Lukas personally was found, and no more recent cycle was verified against FEC data.'+NOTE)

IL='https://www.ilpost.it/2025/10/22/antonio-pignataro-archiviata-indagine-evasione-fiscale/'
BT='https://news.bloombergtax.com/daily-tax-report/ion-founder-to-pay-280-million-to-settle-tax-probe-carlino-2'
add('andrea-pignataro',
 'The reviewed record concerns an Italian tax-residency probe of Pignataro that ended in a €280 million settlement with the tax agency and, per Il Post, dismissal of the tax-evasion investigation. It is a tax dispute, not evidence of political leverage or a preferential state benefit.',
 'None established; tax-residency dispute with Italian authorities',
 'Tax probe 2013–2023 period; settlement June 2025; archiving October 2025',
 [r('Bloomberg Tax, citing Il Resto del Carlino, reports Pignataro agreed to pay €280 million over five years to end a probe; Bologna prosecutors had sought up to €1.2 billion and a criminal case remained open at that time.','Bloomberg Tax: ION founder settlement',BT,'2025-06','Reported settlement','Page partly readable (excerpt cut off)'),
  r('Il Post reports a Bologna investigating judge archived the tax-evasion investigation, finding his centre of interests was abroad and noting unclear residency rules before a 2023 amendment. It also describes the June 2025 €280 million agreement. The URL slug says Antonio but the text refers to Andrea.','Il Post: tax investigation archived',IL,'2025-10-22','Judicial outcome (reported)')],
 [r('Il Post reports the judge rejected the prosecutors’ residency theory, so there is no finding of evasion; the settlement is not an admission in the sources read.','Il Post: judge’s reasoning',IL,'2025-10-22','Outcome and limit of the evidence')],
 'Searches for Russia-sanctions, ransomware or political-donation links produced nothing about Pignataro in the pages read. Nothing shows wealth being translated into political influence or benefit. A tax dispute with the state is not itself a political-power mechanism.'+NOTE)

IS='https://en.ilsole24ore.com/art/case-toti-l-shipowner-aponte-genoa-prosecutors-office-AGN06PX'
add('rafaela-aponte-diamant',
 'No evidence about Rafaela Aponte-Diamant personally was found. The only relevant item concerns her husband, Gianluigi Aponte, heard as a person with information in a Genoa port-corruption probe in which he was not a suspect. That is his episode and is not attributed to her.',
 'None established for this person',
 '2024 Genoa probe (husband, as witness)',
 [r('Il Sole 24 Ore reports Gianluigi Aponte of MSC was questioned on 11 June 2024 as a person with information on the Toti/Spinelli investigation (Liguria president, ex-port authority head, logistics entrepreneur), and is not under investigation. He co-owns a terminal with Spinelli and competes with him for port space; a wiretapped 2022 call has him criticizing the port authority for favoring Spinelli.','Il Sole 24 Ore: Aponte heard by Genoa prosecutors',IS,'2024-06-12','Adjacent family-member episode; not her conduct')],
 [r('The same report states he is not under investigation and was a witness whose recorded remarks criticize, rather than benefit from, an allegedly favored rival.','Il Sole 24 Ore: witness status',IS,'2024-06-12','Explicit limit of the evidence')],
 'Forbes lists her individually, but company-level MSC subsidy, port-concession or political-donation questions were not substantiated for her in the search; none are attributed to her. No MSC corporate pages beyond this one article were read.'+NOTE)

FN='https://www.foodnavigator.com/Article/2012/10/31/Mars-sugar-reform/'
FN16='https://www.foodnavigator.com/Article/2016/11/10/How-candy-lobbying-dollars-were-spent-in-election-year/'
mars_support=[r('Mars Inc. concentrated lobbying on reforming the US sugar program in 2012, spending about $1.36 million that year to date versus $2.31 million in 2011, through the Coalition for Sugar Reform. In June 2012 the Senate voted 50-46 to shelve an amendment to repeal the program.','FoodNavigator-USA: Mars pumps bucks into sugar reform',FN,'2012-10-31','Company-level lobbying record (reported)')]
mars_counter=[r('Mars made no corporate political contributions in 2016. The $36,166 given came from employees or family members and leaned Democratic; the top recipient was Hillary Clinton. Lobbying that cycle was $1.7 million. Individual family giving is not identified by person.','FoodNavigator: How candy lobbying dollars were spent',FN16,'2016-11-10','Counterevidence and limit of attribution'),
 r('The reporting says the lobbying outcome was claimed as at least partly a win by both candy-industry and grower sides, and Mars did not comment. Ordinary trade lobbying on a public policy is not evidence of improper benefit.','FoodNavigator-USA: outcome and response',FN,'2012-10-31','Alternative explanation')]
mars_lim='The evidence is company-level lobbying against a sugar-price support program, which would, if successful, lower input costs for a broad industry. It is not attributed to the individual and does not show a preferential benefit. No donation or political activity by this person individually was verified. Mars Inc. is privately held by family members; the roles of individuals in lobbying decisions are not documented in the sources read.'+NOTE
add('jacqueline-mars','Only company-level Mars lobbying on US sugar policy was found; nothing was attributed to Jacqueline Mars personally. The 2012–2016 reporting shows no corporate donations and family or employee giving that leaned Democratic in 2016.','Company lobbying on commodity policy (not attributed to this person)','2012 and 2016 reporting',mars_support,mars_counter,mars_lim)
add('john-mars','Only company-level Mars lobbying on US sugar policy was found; nothing was attributed to John Mars personally. The 2012–2016 reporting shows no corporate donations and family or employee giving that leaned Democratic in 2016.','Company lobbying on commodity policy (not attributed to this person)','2012 and 2016 reporting',mars_support,mars_counter,mars_lim)

FA='https://ilfattoalimentare.it/nutella-ferrero-ministero.html'
add('giovanni-ferrero',
 'The one reviewed item is a 2016 trade-press piece noting an Italian deputy agriculture minister defending palm oil at a conference Ferrero hosted. The article itself calls any link to Ferrero’s plant location speculation. No lobbying, donation or preferential benefit was documented.',
 'Industry conference platform → public official statements (speculative)',
 'October 2016 conference',
 [r('Il Fatto Alimentare reports Deputy Minister Andrea Olivero unexpectedly defended palm oil at a Ferrero-organized Milan conference. The author suggests Olivero’s birthplace near Ferrero’s Cuneo plant may explain this, presented as speculation.','Il Fatto Alimentare: Nutella, Ferrero and the ministry (Roberto La Pira)',FA,'2016-10-27','Opinion-leaning trade press; speculation flagged as such')],
 [r('The same article states this is speculation, reports Ferrero says it uses more costly mitigated palm oil (10-50% more), and notes Greenpeace, a partner in a sustainability group, said Ferrero’s palm oil meets acceptable standards. A deputy minister defending a legal product is not evidence of an exchange.','Il Fatto Alimentare: company and NGO positions',FA,'2016-10-27','Counterevidence and limit of the evidence')],
 'This is a single 2016 item about company-level advocacy. Italian lobbying registers and campaign finance were not checked. Giovanni’s personal political activity was not found.'+NOTE)

AJ='https://www.aljazeera.com/news/2025/4/1/why-is-china-angry-about-a-plan-to-sell-two-ports-on-the-panama-canal'
HS='https://www.hellenicshippingnews.com/panama-ports-deal-delayed-under-chinese-pressure/'
add('li-ka-shing',
 'The reviewed 2025 episode shows the Chinese state pressuring a Li-family company (CK Hutchison) over a ports sale, which is state leverage over a tycoon, not tycoon leverage over the state. Whether Li Ka-shing personally directed the sale is not shown in the pages read, and his son Victor leads the group.',
 'State pressure on a business group (reverse direction)',
 'March–April 2025 Panama ports deal',
 [r('Al Jazeera reports CK Hutchison planned to sell its stake in two Panama Canal ports within a $22.8bn deal led by BlackRock; state-run Ta Kung Pao accused it of grovelling, Hong Kong’s leader said it deserved serious attention, China’s market regulator announced an antitrust review, and Bloomberg reported Beijing told state firms to hold off business with CK Hutchison. The WSJ reportedly said Xi was angered that approval was not sought.','Al Jazeera: why China is angry about Panama ports sale',AJ,'2025-04-01','Reported state pressure'),
  r('Hellenic Shipping News reports (27 March 2025) that Beijing reportedly told state firms to stop doing business with CK Hutchison and the Li family’s companies, and the signing was delayed; the company made no on-the-record statement.','Hellenic Shipping News: ports deal delayed',HS,'2025-04-01','Reported state pressure; unnamed sources')],
 [r('Al Jazeera notes the article carries no stated position from Li Ka-shing or the company, and that his son Richard was invited to a Beijing forum, read by markets as positive. The delay is described as speculation about yielding to pressure, not confirmed.','Al Jazeera: limits of the account',AJ,'2025-04-01','Explicit limit of the evidence')],
 'This does not show Li using wealth to obtain political favors. Historical Hong Kong property, utilities and port concessions were not reviewed; SCMP and Seatrade pages returned HTTP 403, and the deal status after April 2025 was not verified. Nothing here supports points for leverage, benefit or exchange.'+NOTE)

NE='https://www.neglobal.eu/late-red-bull-tycoon-left-an-indelible-mark-on-austrian-society-politics'
add('mark-mateschitz',
 'No evidence about Mark Mateschitz’s own political activity was found. Search results on political or media influence (Servus TV, public statements) concern his late father Dietrich Mateschitz and are not attributed to Mark.',
 'None established for this person',
 'Searches covering 2016–2022 reporting',
 [r('Search results (not fetched; the fetch returned HTTP 403) described Dietrich Mateschitz’s media holdings and political commentary. These pertain to the father, not Mark.','Search results summarized from neglobal.eu (page not retrievable)',NE,'2022','Adjacent family-member material; not relied on','Not read; search-result snippet only')],
 [r('The only checkable finding is a negative one: nothing located ties Mark Mateschitz to political leverage, contracts or policy benefit, and the wealth here is inherited. That is a limit of this review, not counterevidence about the family.','Reviewer note on search coverage',NE,'2026-10-29','Explicit limit of the evidence','Not read; reviewer statement')],
 'Page contents were not read, so this entry rests on the search summary only. Red Bull ownership is shared with the Thai Yoovidhya family; events involving that family must not be attributed to Mark. Dietrich Mateschitz’s influence is a separate subject.'+NOTE)

RC='https://rollcall.com/2005/10/26/frist-embraces-hca-on-stump'
PR='https://prospect.org/2005/09/28/frist-things-first/'
IN='https://www.inquirer.com/philly/news/nation_world/20070427_No_charges_as_Frist_stock_inquiry_ends.html'
add('thomas-frist-jr',
 'Thomas Frist Jr. is HCA’s co-founder and a long-time executive; his brother Bill Frist was Senate Majority Leader. Contemporary critics argued Bill Frist’s votes and stock sale favored the family firm, but those claims concern Bill, not Thomas Jr., and a federal inquiry into the stock sale closed without charges. No conduct by Thomas Jr. was documented in the pages read.',
 'Family tie to a senator → alleged favorable treatment of HCA (allegation about a different person)',
 '1990s–2007 reporting; mostly about his brother',
 [r('Roll Call reports that Bill Frist’s sale of HCA stock from blind trusts, completed by early July 2005 shortly before the share price fell nearly 10 percent, was under SEC and SDNY investigation. It identifies Thomas Frist Jr. as Bill’s brother who took over HCA and later became CEO emeritus.','Roll Call: Frist embraces HCA on stump (Paul Kane)',RC,'2005-10-26','Family-member episode; not his conduct'),
  r('The American Prospect article alleges HCA predecessors’ Medicare billing and that a Frist bill would have benefited Columbia/HCA, citing a 1997 Mother Jones piece and unnamed sources. It does not name Thomas Frist Jr.','American Prospect: Frist Things First (Robert Dreyfuss)',PR,'2005-09-28','Opinion and allegation about family company and brother')],
 [r('The Inquirer reports the SEC and SDNY closed their 18-month inquiry in April 2007 with letters effectively clearing Bill Frist; he said he sold to remove the appearance of a conflict.','Philadelphia Inquirer: No charges as Frist stock inquiry ends',IN,'2007-04-27','Outcome and subject response')],
 'Forbes lists Thomas Frist Jr. and family, but no evidence was found that he personally lobbied, donated to or received preferential treatment through his brother’s office. HCA’s settlements are corporate matters not analyzed here, and no campaign-finance records were checked. Evidence about Bill Frist is not attributed to Thomas Jr.'+NOTE,
 status='mixed')

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
(ROOT/'data/review-batches/023.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
