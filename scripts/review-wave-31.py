"""Wave 31: narrow profile reviews; evidence supports no rubric for any entry."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review',levels=None,bounds=None,notes=None,refs=None):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; not exoneration',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if levels is not None: R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
LIM=' Searches were limited and several relevant outlets could not be retrieved; absence of findings here is not exoneration, and donations, lobbying, regulation and newer developments need further research.'
# Schaeffler
MC='https://www.moneycab.com/news/schaeffler-gewinnt-machtkampf-bei-conti-staat-soll-helfen/amp/'
VR='https://www.verkehrsrundschau.de/nachrichten/transport-logistik/staatshilfen-fuer-schaeffler-und-conti-3020251'
add('georg-schaeffler','mixed',
 'A 2009 episode reports state-level government discussions of aid for the family-owned Schaeffler group after its Continental takeover. The reviewed pages concern the company and Maria-Elisabeth Schaeffler as owner; they do not show Georg Schaeffler personally negotiating, and no outcome was verified.',
 'Corporate financing stress → reported state-aid discussions (outcome not verified)',
 'January 2009 Schaeffler–Continental episode; no current-period evidence reviewed',
 [r('Moneycab (26 Jan 2009) reports that Schaeffler had won the Continental power struggle; Handelsblatt reported that Bavaria would back Schaeffler and Lower Saxony Continental, with Seehofer and Wulff reportedly agreeing. Wulff mediated between the companies. Owner Maria-Elisabeth Schaeffler, not Georg, is the family member named.','Moneycab',MC,'2009-01-26','Contemporaneous press report of state-level discussions'),
  r('VerkehrsRundschau (26 Jan 2009) reports about EUR 500 million each from Bavaria and Lower Saxony as plans, with form (guarantee, direct stake) open and a condition from Wulff about separating Continental’s core business.','VerkehrsRundschau',VR,'2009-01-26','Reported plan, not a confirmed decision')],
 [r('The Bavarian state chancellery said there were talks but no agreement or commitments; Lower Saxony’s Wulff said no concept was concrete enough. The article labels the reports as unconfirmed.','Moneycab: government responses',MC,'2009-01-26','Contemporaneous denial of commitment'),
  r('The reviewed article states the aid was reported plans from newspaper and company sources, not confirmed decisions. No source read establishes final terms, or any personal role of Georg Schaeffler.','VerkehrsRundschau: status of reports',VR,'2009-01-26','Explicit limit of evidence')],
 'Georg Schaeffler is a family co-owner; the reviewed pages name Maria-Elisabeth Schaeffler. No assessment of donations, later lobbying or the final 2009 aid outcome was possible. A request for crisis aid by a large employer is not itself preferential treatment.'+LIM)
# Adcock
WB='https://en.wikipedia.org/wiki/Brett_Adcock'
add('brett-adcock','no-strong',
 'Searches found no reporting or filings in readable sources connecting Brett Adcock or Figure AI to political donations, lobbying or preferential government treatment. This is a narrow negative search, not a clearance.',
 'None established in reviewed sources','Searches in October 2026; no earlier period assessed',
 [r('Wikipedia identifies Adcock as founder of Figure AI, Archer Aviation (co-founder) and others and cites a Forbes estimate of about US$23 billion. Wealth from company valuations is the only documented link; no political activity is described.','Wikipedia: Brett Adcock',WB,'2026-10','Background only; secondary source','Page text reviewed; FEC and lobbying databases not queried')],
 [r('The page contains no mention of donations, lobbying, government contracts or political involvement. This is a limit of the source, not evidence the conduct never occurred.','Wikipedia: Brett Adcock',WB,'2026-10','Limitation, not exoneration')],
 'FEC contribution records, Senate lobbying disclosures and government contract databases were not accessible in this review. Not an investigation.'+LIM)
# Albrechts
WK='https://en.wikipedia.org/wiki/Karl_Albrecht_Jr.'
WH='https://en.wikipedia.org/wiki/Beate_Heister'
add('karl-albrecht-jr','no-strong',
 'Forbes lists Karl Albrecht Jr. with his family (his sister Beate Heister has a separate entry). The reviewed source describes joint control of the foundation that controls Aldi Süd and no political activity; the review found nothing on wealth–power mechanisms but is narrow.',
 'None established in reviewed sources','Searches in October 2026; mostly background',
 [r('Albrecht and his sister Beate Heister jointly control the Siepmann-Stiftung, which controls Aldi Süd; he retired from operations in 2004. The article lists no political involvement.','Wikipedia: Karl Albrecht Jr.',WK,'2026-10','Ownership background; secondary source')],
 [r('The article describes no political involvement or controversies (it cites a 2005 Süddeutsche Zeitung item about foundation tax problems that was not read). This is a limit of the source, not exoneration.','Wikipedia: Karl Albrecht Jr.',WK,'2026-10','Limitation, not exoneration')],
 'German party-donation reports (Bundestag), the lobby register and German press were not reviewed in detail. The Forbes family entry may include relatives; evidence here concerns Albrecht Jr. only. Not an investigation.'+LIM)
add('beate-heister','no-strong',
 'Beate Heister jointly controls the foundation behind Aldi Süd with her brother. The reviewed source describes her as reclusive and records no political involvement. Narrow review, not clearance.',
 'None established in reviewed sources','Searches in October 2026; mostly background',
 [r('Heister reportedly controls half of Aldi Süd, sits on its advisory board with her husband and son, and remained a Siepmann Foundation board member as of 2021.','Wikipedia: Beate Heister',WH,'2026-10','Ownership and governance background; secondary source')],
 [r('The article mentions no political involvement or controversies. This reflects the limits of the source and the search, not an affirmative finding.','Wikipedia: Beate Heister',WH,'2026-10','Limitation, not exoneration')],
 'No party-donation, lobbying or regulatory records were reviewed. Not an investigation.'+LIM)
# Hartono
FO='https://fortune.com/2026/03/19/indonesias-richest-man-tobacco-tycoon-michael-bambang-hartono-dies-at-86/'
WM='https://en.wikipedia.org/wiki/Michael_Bambang_Hartono'
JP='https://www.thejakartapost.com/news/2016/08/19/protobacco-lobby-intensifies'
add('michael-hartono','no-strong',
 'Michael Bambang Hartono died on 19 March 2026, after the wealth date used here. Reviewed sources describe industry-wide tobacco lobbying in Indonesia in which Djarum is named only as a consulted company, and a 2002 BCA acquisition; none establish a personal political exchange.',
 'Industry consultation and past privatization context; personal mechanism not established','Historical (2002–2016) context; subject died 2026-03-19',
 [r('Wikipedia notes the Hartono brothers’ vehicle took 51.15% of Bank Central Asia in 2002, defeating other bidders despite a lower offer, and that BCA shares moved to a holding company during a 2016 tax amnesty. It describes no political ties.','Wikipedia: Michael Bambang Hartono',WM,'2026-10','Historical transaction context; secondary source'),
  r('The Jakarta Post (2016) reports that the then industry minister consulted Djarum and Gudang Garam on a tobacco road map and that a minister opened a Djarum sports event; critics cited these as industry interference. It does not allege wrongdoing by Hartono personally.','The Jakarta Post: pro-tobacco lobby intensifies',JP,'2016-08-19','Industry-level reported interaction','Page text reviewed')],
 [r('Fortune’s obituary records his death on 19 March 2026 and mentions an honor at the presidential palace for the 2018 Asian Games; it describes no political bargain or preferential treatment.','Fortune: Hartono dies at 86',FO,'2026-03-19','Limitation, not exoneration')],
 'The family entry shares wealth with brother Robert Budi Hartono; evidence here is not transferred between them. The 2002 bank-sale context is not an allegation and its terms are not analyzed. Indonesian-language sources, Indonesian tobacco excise decisions and donations were not reviewed.'+LIM)
# Storonsky
NS='https://www.newstream.cz/money/sef-revolutu-nastval-briske-uredniky-protoze-bydli-v-arabii'
RT='https://www.realtid.se/bors-finans/bank-fintech/revolut-fornekar-koppling-till-kreml/'
LRT='https://www.lrt.lt/naujienos/lrt-tyrimai/46/242075/lrt-tyrimas-slaptose-pazymose-apie-revolut-rysiai-su-kremliumi'
add('nik-storonsky','no-strong',
 'Reviewed sources concern regulatory scrutiny of Revolut and reported Russian-link allegations (his father’s Gazprom institute role, an investor’s funding sources). They show friction with, not favor from, UK regulators; no political-power exchange was found. Narrow review.',
 'None established; reported regulatory friction and unproven link allegations','2019–2025 reports',
 [r('Newstream (1 Dec 2025) reports Revolut still lacked a full UK banking licence more than a year after applying, regulators reportedly worried about risk controls, and UK officials reportedly learned of his UAE residence change from the Financial Times. This reflects scrutiny, not preferential treatment.','Newstream.cz',NS,'2025-12-01','Regulatory context; secondary report','Page text reviewed (translated)'),
  r('LRT (22 Jan 2019) reported that his father is a deputy director at Gazprom’s Promgaz research centre, and that Lithuanian MP Stasys Jakeliūnas had requested intelligence reports; the agencies declined to comment. Revolut later confirmed the father’s role.','LRT investigation',LRT,'2019-01-22','Reported family-link allegation')],
 [r('Realtid (4 Mar 2022) reports Revolut says DST Global is a passive minority holder, that the father is an engineer at a research institute, and that Revolut is British and approved by many authorities. The article notes Storonsky renounced Russian citizenship in 2022 per other reports.','Realtid',RT,'2022-03-04','Company response and limits of the claims'),
  r('LRT states Revolut said it has no servers or services in Russia. A family member’s employment is not evidence of personal political leverage.','LRT investigation: company response',LRT,'2019-01-22','Subject response; limitation')],
 'Allegations about a family member and investors are not findings about Storonsky’s own conduct. UK political donations and lobbying were not located in the sources read. Not an investigation.'+LIM)
# Eric Li
LS='https://en.wikipedia.org/wiki/Li_Shufu'
add('eric-li','mixed',
 'Forbes lists Eric Li, identified as Li Shufu, Geely founder. Reviewed sources document political-consultative roles (CPPCC member, former independent NPC delegate) and a press question about state involvement in his Daimler stake. They do not establish a specific preferential exchange.',
 'Formal consultative roles and company expansion; benefit and exchange not established','2010–2023 sources',
 [r('Wikipedia records him as a member of the 14th CPPCC National Committee (Xinhua, March 2023) and an independent delegate to the 13th National People’s Congress (2018), and cites a 2018 Financial Times article asking whether the Chinese state was behind Geely’s Daimler stake.','Wikipedia: Li Shufu',LS,'2026-10','Roles and press question; secondary source')],
 [r('The same article does not document direct state financing of Geely, notes he criticized Beijing’s car-industry strategy in 2015, and cites a Reuters report that Geely corrected rumours of presidential-family ties. CPPCC and NPC membership alone is not evidence of favor.','Wikipedia: Li Shufu: limits',LS,'2026-10','Counterevidence and limitation')],
 'Claims of provincial-government or bank financing for the 2010 Volvo purchase appeared in search snippets but the pages could not be read, so they are not used. Subsidies, procurement lists and licensing were not analyzed. Political appointments are not misconduct.'+LIM)
# Zhong
WZ='https://en.wikipedia.org/wiki/Zhong_Huijuan'
add('zhong-huijuan','no-strong',
 'Searches found no readable sources documenting political office or preferential treatment for Zhong Huijuan. Hansoh’s exposure to Chinese drug-pricing and procurement policy is a sector condition, not shown here to be favoritism.',
 'None established in reviewed sources','Searches in October 2026; background only',
 [r('Wikipedia describes the 2019 Hansoh IPO, her 66% ownership via a trust, and that her husband managed a state-owned pharmaceutical factory earlier. It notes a 2007 women’s award and no political office.','Wikipedia: Zhong Huijuan',WZ,'2026-10','Background; secondary source')],
 [r('The article does not cover political roles, government relations or procurement policy; the lack of such content is a limit of the source, not an affirmative finding. A Fierce Pharma article on procurement could not be retrieved and is not relied upon.','Wikipedia: Zhong Huijuan: limits',WZ,'2026-10','Limitation, not exoneration')],
 'Chinese-language official membership lists and procurement records were not checked. Not an investigation.'+LIM)
# Hagen
SNL='https://snl.no/Torstein_Hagen'
add('torstein-hagen','mixed',
 'Norwegian reference text says Hagen was charged with gross corruption in 2015 over the Viking Star christening in Bergen, along with the then mayor and harbour chief, and that the case was later dropped for evidentiary reasons. Charged is not convicted; no wrongdoing is established.',
 'Alleged hospitality-for-favor in a port matter; case dropped','2015 allegation; later dropped',
 [r('Store norske leksikon says Hagen, Bergen mayor Trude Drevland and harbour chief Inge Tangerås were suspected and charged with gross corruption over the 17 May 2015 christening of the Viking Star; Drevland resigned as mayor.','Store norske leksikon: Torstein Hagen',SNL,'2025','Reference summary of a legal episode','Page text reviewed (Norwegian, translated)')],
 [r('The same entry says the case was later dropped because of the state of the evidence. It describes no party ties or political office for Hagen. Other outlets’ reports could not be retrieved and Viking’s response was not read.','Store norske leksikon: outcome',SNL,'2025','Legal outcome and limitation')],
 'Not a conviction; the details of the allegation and Viking’s denial were not read. Wider lobbying, including US shipping rules, was not reviewed.'+LIM)
# Wang Ning
TN='https://www.taiwannews.com.tw/news/6294109'
add('wang-ning','no-strong',
 'The only item found is a politician’s claim, reported 2 Feb 2026, that Pop Mart’s founder sits on the CPPCC National Committee, which was not verified against an official roster. Membership alone would not show favor. Family-entry attribution to the Pop Mart founder was not independently verified.',
 'Unverified claim of consultative membership; no exchange established','2026 report',
 [r('Taiwan News reports DPP legislator Lin Chu-yin saying Pop Mart’s founder is a CPPCC National Committee member and using it to argue the brand is part of China’s united front strategy.','Taiwan News',TN,'2026-02-02','Attributed political claim','Page text reviewed')],
 [r('Taipei officials rejected the framing and noted Pop Mart’s inclusion in the 2025 Macy’s parade; the article reports no response from Pop Mart or its founder, and the claim is not corroborated by an official source.','Taiwan News: responses',TN,'2026-02-02','Counterevidence and limitation')],
 'Many politicians share the name Wang Ning; only the Pop Mart founder entry was used. The Forbes entry is a family entry. Official CPPCC lists, procurement and local-government support were not reviewed.'+LIM)
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
(ROOT/'data/review-batches/031.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
