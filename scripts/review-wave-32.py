"""Wave 32: narrow, profile-only reviews; thin evidence, no rubrics, not exoneration."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,status='no-strong'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed',confidence='Low / narrow review',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
LIM=' This is a narrow review, not an exoneration: it reflects only the sources listed and may have missed lobbying, donation, contract or regulatory records. No numerical estimate is made.'
WP='Wikipedia (secondary; page text reviewed)'
add('ludwig-merckle',
 'The reviewed sources describe Ludwig Merckle as sole heir to the Merckle group after the 2009 death of Adolf Merckle, with a corporate rescue negotiated with private creditor banks. They do not show political leverage, preferential state benefit or a wealth-to-power feedback loop.',
 'No supported mechanism identified',
 '2009 succession and group rescue',
 [r('dpa report: Ludwig Merckle to become sole heir of the Ulm group, whose estate includes stakes in HeidelbergCement, ratiopharm and Phoenix; banks required the ratiopharm sale as a bridge-loan condition.','Ärzte Zeitung (dpa)','https://www.aerztezeitung.de/Wirtschaft/Ludwig-Merckle-erbt-Firmenimperium-366886.html','2009-05-07','Inheritance and corporate context','Page text reviewed; German-language')],
 [r('The same report mentions only a rescue negotiated with private creditor banks; it describes no government guarantee, political action or state benefit.','Ärzte Zeitung (dpa): limit of evidence','https://www.aerztezeitung.de/Wirtschaft/Ludwig-Merckle-erbt-Firmenimperium-366886.html','2009-05-07','Explicit limit of the evidence','Page text reviewed; German-language')],
 'Searches for political activity or lobbying by Ludwig Merckle found only business-press material on the 2009 crisis and succession; the Heidelberg Materials CV PDF could not be retrieved (404). Inheritance and shareholding alone do not justify points.'+LIM)
add('sarath-ratanavadi',
 'Reviewed sources record family ties to the military and an early-regulation-era energy business. Reporting on LNG import licences notes a licence to Gulf alongside reported state-utility reversals, but the author questions whether Gulf can translate wealth into market power. No source reviewed establishes personal leverage, preferential benefit and exchange together.',
 'Possible access to energy licensing; not established',
 'Family background; 2020 LNG licensing; 2024 USC donor-influence reporting (unrelated to state power)',
 [r('Father reported as former Thai armed-forces chief of staff; received a royal order in 2021. The page describes no government concession, contract or political role.','Wikipedia: Sarath Ratanavadi','https://en.wikipedia.org/wiki/Sarath_Ratanavadi','2026-04-09',WP,'Page text reviewed; cited Nikkei and LA Times articles not opened'),
  r('Government granted Gulf an LNG import licence (1.7 mtpa) in 2020; the author describes PTT, not Gulf, as the dominant political and market power.','Asia Times (Tim Daiss)','https://asiatimes.com/?p=497642','2020-05-26','Licensing context','Page text reviewed')],
 [r('The Asia Times author calls Gulf\'s ability to turn wealth into market power an open question and says its LNG plans may never materialize.','Asia Times: limit of evidence','https://asiatimes.com/?p=497642','2020-05-26','Alternative reading and limit'),
  r('The Wikipedia page gives no response from Ratanavadi on the USC admissions matter and reports no outcome; that matter concerns university admissions, not state power.','Wikipedia: Sarath Ratanavadi (limits)','https://en.wikipedia.org/wiki/Sarath_Ratanavadi','2026-04-09','Explicit limit of the evidence')],
 'Family military ties, a royal honour and a licence in a liberalizing sector do not by themselves show political leverage or preferential treatment. Thai-language and procurement/regulatory records were not reviewed.'+LIM,'mixed')
add('theo-albrecht-jr',
 'The family entry reflects inherited Aldi Nord and Trader Joe\'s holdings. The reviewed sources contain no political donation, lobbying, contract or regulatory-benefit evidence. Which family member any later evidence concerns would need to be checked.',
 'No supported mechanism identified',
 'Inheritance after 2010; no political-activity record found',
 [r('Theo Albrecht died in 2010 and left Aldi Nord and Trader Joe\'s to sons Theo Jr. and Berthold; Berthold died in 2012 and his heirs share in the fortune.','Wikipedia: Theo Albrecht Jr.','https://en.wikipedia.org/wiki/Theo_Albrecht_Jr.','2021-07',WP,'Page text reviewed')],
 [r('The page covers no political activity, donations or controversies, and does not specify how the holdings are divided among family members.','Wikipedia: Theo Albrecht Jr. (limits)','https://en.wikipedia.org/wiki/Theo_Albrecht_Jr.','2021-07','Explicit limit of the evidence')],
 'Search for family political donations and lobbying returned only low-quality fact-check templates, which were not relied on. FEC, German lobby-register and Bundestag records were not searched.'+LIM)
add('edwin-chen',
 'Chen founded and controls Surge AI, a data-labelling firm with large private-sector customers. The reviewed material describes no government contracts, political donations, lobbying or regulatory benefit.',
 'No supported mechanism identified',
 'Company founded 2020; wealth reported 2025',
 [r('Founded Surge AI in 2020; remains CEO and majority owner; Forbes (Sept 2025) estimated net worth at $18 billion; clients included Google and OpenAI as of July 2025.','Wikipedia: Edwin Chen','https://en.wikipedia.org/wiki/Edwin_Chen','2025-12',WP,'Page text reviewed; cited Forbes and Inc. not opened')],
 [r('The page mentions no government or political ties, controversies or lawsuits.','Wikipedia: Edwin Chen (limits)','https://en.wikipedia.org/wiki/Edwin_Chen','2025-12','Explicit limit of the evidence')],
 'An English and Chinese-language search for government contracts found only profiles of wealth and valuation. Federal procurement and lobbying databases were not searched.'+LIM)
add('charlene-de-carvalho-heineken',
 'Reviewed sources describe controlling family ownership of Heineken through holding companies and a role in replacing the CEO in 2005. They contain no political role, donation, lobbying or state-benefit evidence. The family entry concerns Charlene de Carvalho-Heineken as controlling shareholder.',
 'No supported mechanism identified',
 'Corporate control, with 2005 CEO change',
 [r('Controls 51% of Heineken Holding NV, which owns 50.05% of Heineken NV; she and her husband helped replace the CEO in 2005.','Family Business Magazine (citing Fortune)','https://familybusinessmagazine.com/uncategorized/heinekens-controlling-shareholder-avoids-the-spotlight/','2014-09-17','Corporate control context')],
 [r('The article contains no political role or statements and describes her as private; she declined comment on the rejected SABMiller bid.','Family Business Magazine: limits','https://familybusinessmagazine.com/uncategorized/heinekens-controlling-shareholder-avoids-the-spotlight/','2014-09-17','Explicit limit of the evidence')],
 'The source is from 2014; Dutch lobbying and later records were not reviewed. Corporate governance control is not political power.'+LIM)
add('eric-smidt',
 'Smidt\'s reported political activity is mainly Democratic fundraising and local civic donations in Los Angeles, plus tool donations to schools. Nothing reviewed shows preferential economic benefit or an exchange; a search for tariff lobbying found nothing tied to him or Harbor Freight.',
 'Campaign and civic giving; no benefit established',
 '2007-2016 donations; 2020 PPE donation',
 [r('Reported co-chair of a 2007 Hillary Clinton fundraiser, $114,300 to Democratic campaigns in 2012, $350,000 toward a 2024 Olympics bid effort in 2016, and school tool donations.','Wikipedia: Eric Smidt','https://en.wikipedia.org/wiki/Eric_Smidt','2026',WP,'Page text reviewed; underlying LA Weekly and Daily News items not opened')],
 [r('The page mentions neither tariffs nor any government benefit. Donations and civic giving alone do not demonstrate leverage or exchange.','Wikipedia: Eric Smidt (limits)','https://en.wikipedia.org/wiki/Eric_Smidt','2026','Explicit limit of the evidence')],
 'Federal lobbying disclosures and tariff-exclusion dockets for Harbor Freight were not examined; a general tariff-lobbying search did not mention the company.'+LIM)
add('john-collison',
 'John Collison co-founded and jointly controls Stripe with his brother. The reviewed page attributes only a 2018 $1 million Stripe donation to a housing-lobbying group to both brothers; it records no government contract, office or preferential benefit specific to him.',
 'Corporate political giving; no benefit established',
 '2018 donation; 2021 Forbes dispute',
 [r('In 2018 Stripe, under the direction of the Collison brothers, gave $1 million to California YIMBY.','Wikipedia: John Collison','https://en.wikipedia.org/wiki/John_Collison','2026',WP,'Page text reviewed; cited SF Business Times not opened')],
 [r('The page lists no other political donations, lobbying or government dealings; the 2021 Forbes episode concerned Limerick, not state power.','Wikipedia: John Collison (limits)','https://en.wikipedia.org/wiki/John_Collison','2026','Explicit limit of the evidence')],
 'Evidence about Stripe\'s regulatory work is not attributed to John personally. Irish and US lobbying records were not searched.'+LIM)
add('patrick-collison',
 'Patrick Collison co-controls Stripe, joined Meta\'s board in 2025 and reportedly donated $7 million in 2026 to oppose a California billionaire wealth-tax measure. These show political expression and policy engagement, but the reviewed sources do not establish preferential benefit or an exchange.',
 'Policy-advocacy giving; no benefit established',
 '2018-2026 donations and advisory roles',
 [r('Per the page: 2018 Stripe $1 million to California YIMBY (attributed to both brothers); $7 million in 2026 to a group opposing Proposition 40, a California billionaire wealth-tax proposal (citing the Irish Times, 29 July 2026); joined the Meta board in April 2025.','Wikipedia: Patrick Collison','https://en.wikipedia.org/wiki/Patrick_Collison','2026',WP,'Page text reviewed; Irish Times and Irish Independent items not opened')],
 [r('The page reports no lobbying activity or government contracts. Opposing a tax by donation is lawful political expression, and no outcome or benefit is documented. A web search tying Stripe to stablecoin lobbying returned nothing about the Collisons.','Wikipedia: Patrick Collison (limits)','https://en.wikipedia.org/wiki/Patrick_Collison','2026','Explicit limit of the evidence')],
 'The 2026 donation was not verified from the original report. Stripe\'s regulatory dealings and the Rhine Group role (uncited on the page) were not examined.'+LIM,'mixed')
for pid,name in (('david-sun','David Sun'),('john-tu','John Tu')):
 add(pid,
 f'{name} co-founded privately held Kingston Technology. The reviewed page records ownership history and facilities but no political donations, government contracts, lobbying or controversies.',
 'No supported mechanism identified',
 'Company history 1987-2004',
 [r('Kingston was founded in 1987 by John Tu and David Sun; SoftBank bought 80% in 1996 and the founders repurchased it in 1999; plants in Taiwan and Shanghai.','Wikipedia: Kingston Technology','https://en.wikipedia.org/wiki/Kingston_Technology','2026',WP,'Page text reviewed; tagged as needing more citations')],
 [r('The page contains no information on government contracts, political donations or lawsuits for either founder; it is tagged as needing more citations.','Wikipedia: Kingston Technology (limits)','https://en.wikipedia.org/wiki/Kingston_Technology','2026','Explicit limit of the evidence')],
 'A search for donations, lobbying or tariff exemptions found only biographies. FEC, OpenSecrets and USTR exclusion records were not searched; individual biography pages for each founder were not opened.'+LIM)
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
(ROOT/'data/review-batches/032.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
