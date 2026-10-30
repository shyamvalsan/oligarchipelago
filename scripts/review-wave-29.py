"""Wave 29: narrow-evidence case reviews (profiles only; no rubric where evidence does not support all three dimensions)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed; not exoneration',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)

# 1 Chen Tianshi
AS='https://www.asianscientist.com/2017/08/tech/cambricon-series-a-funding-unicorn/'
FR='https://www.govinfo.gov/content/pkg/FR-2022-12-19/html/2022-27151.htm'
add('chen-tianshi','mixed',
 'Cambricon was spun out of a Chinese Academy of Sciences institute and its early financing included state-linked investors; the US later listed Cambricon entities for supporting Chinese military modernization. These are corporate and institutional facts. The review found no evidence about Chen Tianshi personally exercising political leverage or securing a preferential exemption, so no estimate is made.',
 'State-linked research and investment backing for a chip startup (corporate level)',
 '2016-2017 founding and Series A; US Entity List action in December 2022',
 [r('Cambricon’s August 2017 Series A was led by SDIC Chuangye, described as a subsidiary of China’s State Development and Investment Corporation, with the CAS investment arm also participating. The company spun off from the CAS Institute of Computing Technology and received US$1.4 million from CAS in April 2017.','Asian Scientist: Cambricon raises US$100 million',AS,'2017-08-23','Reported state-linked financing of the company','Page summary reviewed; fetched text was a condensed extraction'),
  r('The US Bureau of Industry and Security added Cambricon entities to the Entity List for acquiring and attempting to acquire US-origin items in support of China’s military modernization, describing them as major AI chip R&D, manufacturing and sales entities.','Federal Register / GovInfo, 87 FR 77505 (rule 2022-27151)',FR,'2022-12-19','Primary regulatory action against corporate entities','Page text reviewed (extract of Cambricon entries)')],
 [r('The Entity List action names companies, not Chen Tianshi, and is a US export-control determination, not a finding of preferential treatment or misconduct by him.','Federal Register / GovInfo (scope of the listing)',FR,'2022-12-19','Explicit limit of the evidence'),
  r('State venture and academy funding of a university spin-out is a common innovation-policy arrangement in China; the article does not allege any improper favor.','Asian Scientist (framing of the financing)',AS,'2017-08-23','Alternative explanation')],
 'Not exoneration. Did not locate documents on his personal political roles, procurement or subsidy terms, or the share-price-driven wealth rise, and Chinese-language sources were not searched exhaustively. Public investors and a state-affiliated institute holding stakes does not by itself show wealth-power feedback.')

# 2 Dang Yanbao
WD='https://en.wikipedia.org/wiki/Dang_Yanbao'
add('dang-yanbao','no-strong',
 'Dang Yanbao chairs Ningxia Baofeng Energy Group, a coal and chemicals company. Searches did not surface reporting on political office, concession terms, subsidies or other state preferences tied to him personally. This is a gap in what was found, not a finding of absence.',
 'None established in reviewed sources','Searches in October 2026; wealth figures from 2022 and later listings',
 [r('A reference summary describes him as chairman of Ningxia Baofeng Energy Group, with a Forbes 2022 listing at US$14.8 billion, and notes his Ningxia Yanbao Charity Foundation (RMB 302 million donated in 2019). It mentions no political roles or government ties; the page is a stub and one of its cited sources is a dead link.','Wikipedia: Dang Yanbao',WD,'accessed 2026-10-29','Background only; no mechanism evidence','Page text reviewed; stub with weak sourcing')],
 [r('The page lists no political office, state contract or regulatory favor; philanthropy is not evidence of political leverage.','Wikipedia: Dang Yanbao (absence of political detail)',WD,'accessed 2026-10-29','Explicit limit of the evidence','Page text reviewed')],
 'Not exoneration. A Bloomberg profile could not be fetched (access blocked), and Chinese-language sources on resource allocation, local-government support or political advisory roles were not reviewed. Coal-linked wealth in Ningxia may involve state licensing; no evidence about this was found.')

# 3 Kwong Siu-hing
ICAC='https://www.icac.org.hk/en/p/press-archive/by-year/index_id_4952.html'
SHKP='https://en.wikipedia.org/wiki/Sun_Hung_Kai_Properties'
add('kwong-siu-hing','mixed',
 'Kwong Siu-hing is the matriarch of the family controlling Sun Hung Kai Properties. Her son Thomas Kwok was convicted in 2014 of conspiracy involving misconduct in public office by Hong Kong’s former Chief Secretary; her son Raymond Kwok was acquitted. The reviewed sources do not name Kwong Siu-hing in the case, and no guilt is transferred to her. Evidence about her own conduct was not found.',
 'Family-company executive payments to a senior official (convicted individual: Thomas Kwok, not Kwong Siu-hing)',
 'Case 2012-2017; her chairmanship 2008-2011',
 [r('On 23 December 2014 the Court of First Instance sentenced former Chief Secretary Rafael Hui to 7.5 years and SHKP co-chairman Thomas Kwok to 5 years (plus fine and director disqualification) in a case of bribery-related conspiracy and misconduct in public office.','Hong Kong ICAC press release',ICAC,'2014-12-23','Primary court-outcome summary regarding a family member','Page text reviewed; the summary of which defendant was convicted on which count was internally inconsistent'),
  r('Wikipedia lists Kwong Siu-hing as SHKP chairman 2008-2011 and, citing The Standard, as controlling shareholder who removed Walter Kwok from his post in 2008; the company is controlled by the Kwok family trust.','Wikipedia: Sun Hung Kai Properties',SHKP,'accessed 2026-10-29','Background on family control (secondary source)','Page text reviewed')],
 [r('Raymond Kwok was acquitted of all charges and the ICAC release does not mention Kwong Siu-hing, so the conviction cannot be attributed to her.','Hong Kong ICAC press release',ICAC,'2014-12-23','Counterevidence and explicit limit','Page text reviewed')],
 'Not exoneration, and no assessment of her personal conduct. The case concerned a son and a public official; policy influence of the Kwok property business on Hong Kong land policy was not researched here. Forbes entry is for the widow of the founder, not Thomas, Raymond or Walter Kwok.')

# 4 Henry Nicholas
SEC='https://www.sec.gov/litigation/litreleases/lr-21409'
FOX='https://www.foxnews.com/us/federal-prosecutors-wont-appeal-dismissal-of-criminal-charges-against-broadcom-co-founders.amp'
add('henry-nicholas-iii','no-strong',
 'Henry Nicholas, Broadcom co-founder, faced criminal and SEC stock-option backdating allegations and separate drug charges. The criminal backdating indictment was dismissed with prejudice in December 2009, the drug charges were later dismissed, and the SEC did not pursue its case. Those matters concern corporate-governance and personal-conduct allegations, not a documented wealth-political power exchange; no political-power evidence was found.',
 'None established (legal allegations were dismissed; not a political mechanism)','Allegations 2008; dismissals 2009-2010',
 [r('The SEC sued Nicholas and others in May 2008 for allegedly backdating options from 1998 to 2003; the SEC later stated it did not intend to proceed after the criminal indictment against Nicholas was dismissed with prejudice on 15 December 2009 and the court found the evidence likely insufficient.','SEC Litigation Release 21409',SEC,'2010-02-04','Primary regulatory record','Page text reviewed')],
 [r('Fox News reported on 28 May 2010 that prosecutors would not appeal dismissal of the backdating and narcotics charges against Nicholas, after Judge Carney criticized prosecutorial misconduct.','Fox News: prosecutors will not appeal dismissals',FOX,'2010-05-28','Outcome of the proceedings','Page text reviewed (extract)')],
 'Not exoneration of anything beyond these case outcomes; no pardon claims were verified. Political donations, lobbying or policy influence were not found in this narrow search.')

# 5 Melnichenko
EUC='https://eucrim.eu/news/cjeu-rulings-on-eus-restrictive-measures-against-russia-january-april-2025/'
BAR='https://www.thebarentsobserver.com/industry-and-energy/owner-of-murmansk-seaport-is-now-russias-richest/151680'
add('andrey-melnichenko','mixed',
 'Melnichenko, with family, is a fertilizer and coal magnate who was EU-sanctioned in March 2022; the General Court upheld the listing in January 2025 on the basis of his leading role in sectors generating significant revenue for the Russian government and his attendance at a 24 February 2022 meeting with Putin. A sector-based sanction and a meeting attendance do not establish a preferential-benefit exchange; no rubric is assigned.',
 'Sector-based sanctions rationale (not an adjudicated exchange)','Wealth formation 1990s-2010s; EU listing 2022; General Court ruling 22 January 2025',
 [r('The EU Council listed him on 9 March 2022, citing a 24 February 2022 meeting with Putin and 36 other businesspeople.','The Barents Observer',BAR,'2023-04-05','Reported ground of EU listing','Page text reviewed'),
  r('In T-271/22 the General Court (22 January 2025) upheld the listing, found he retained economic benefits and influence despite transferring assets to a trust and his wife, and said no personal link to the Russian government need be shown for leading businesspersons in key sectors.','eucrim: CJEU rulings on restrictive measures',EUC,'2025-01-22','Judicial finding on sanctions criteria','Page text reviewed (summary report, not the judgment)')],
 [r('Melnichenko told Forbes his stakes in EuroChem and SUEK were reduced to zero after the sanctions, and neither company was itself sanctioned at that time. This is his own account; the court found he retained benefits.','The Barents Observer (quoting Forbes interview)',BAR,'2023-04-05','Subject response','Page text reviewed'),
  r('The Court’s test did not require proof of a personal link to the government, so the ruling is not a finding of a corrupt exchange or special state treatment.','eucrim summary (scope of ruling)',EUC,'2025-01-22','Explicit limit of the evidence','Page text reviewed')],
 'Not exoneration and not a finding of misconduct. Forbes entry covers Melnichenko and family; the court case also concerns his wife’s separate listing, not examined here. The UK EuroChem ruling mentioned in search snippets was not fetched and is not used. Privatization-era wealth formation and Russian state dealings were not reviewed.')

# 6 Takizaki
add('takemitsu-takizaki','no-strong',
 'Takemitsu Takizaki founded Keyence, an industrial sensors company. A narrow search found no reporting of political leverage, state benefits or policy influence connected to him. Absence in this search is not exoneration.',
 'None established','Searches in October 2026',
 [r('A reference page describes him as Keyence founder, honorary chairman since 2015, with a wealth figure from 2022; it mentions no political involvement or government ties, and is a short stub.','Wikipedia: Takemitsu Takizaki','https://en.wikipedia.org/wiki/Takemitsu_Takizaki','accessed 2026-10-29','Background only; no mechanism evidence','Page text reviewed; stub')],
 [r('The reviewed page records no political involvement, government ties or controversies; this is a limit of the available evidence, not an affirmative finding.','Wikipedia: Takemitsu Takizaki','https://en.wikipedia.org/wiki/Takemitsu_Takizaki','accessed 2026-10-29','Explicit limit of the evidence','Page text reviewed')],
 'Japanese political-funds disclosure records were not searched, and Japanese-language reporting was not reviewed. Low-quality secondary pages mention philanthropy; none was used.')

# 7 Esteves
BL='https://news.bloomberglaw.com/securities-law/btg-founder-esteves-acquitted-in-brazil-witness-tampering-1'
add('andre-esteves','mixed',
 'André Esteves, BTG Pactual founder, was arrested in November 2015 in the Lava Jato investigation on obstruction allegations tied to a plan to influence the testimony of a former Petrobras executive, and was acquitted in July 2018 for lack of valid proof. This is an allegation without a conviction; no rubric is assigned and no wider finding is made about his dealings with the state.',
 'Alleged obstruction connected to a senator (allegation; acquitted)','Arrest 2015; acquittal 12 July 2018',
 [r('Bloomberg Law reports Esteves was arrested in 2015, spent about three weeks in Bangu prison and was held on obstruction charges linked to efforts to tamper with a former Petrobras executive’s testimony.','Bloomberg Law: BTG founder Esteves acquitted',BL,'2018-07-12','Reported allegation and detention','Page text reviewed (extract)')],
 [r('Federal Judge Ricardo Leite acquitted him, saying there was no valid proof to support conviction; the prosecutor had earlier recommended dropping the charges.','Bloomberg Law: BTG founder Esteves acquitted',BL,'2018-07-12','Judicial acquittal','Page text reviewed (extract)')],
 'Not exoneration of other conduct. Searches did not review BTG’s relationships with BNDES, pension funds or privatizations, nor any appeal of the acquittal. Brazilian-Portuguese sources appeared in search results but only the Bloomberg Law page was read.')

# 8 Kellnerova
E15='https://www.e15.cz/byznys/finance-a-bankovnictvi/kellnerovy-namluvy-s-ruskou-bankou-vtb-se-komplikuji-695960'
add('renata-kellnerova','no-strong',
 'Renata Kellnerova inherited control of PPF Group after the 2021 death of her husband Petr Kellner. Attribution matters: the only political-economy source read concerned Petr Kellner’s historical Russian business and shows an attempted partnership with a state bank in 2011, which is business and not evidence of leverage by Renata Kellnerova. No evidence about her personally was found.',
 'None established for her personally','PPF in 2011 (Petr Kellner era); searches October 2026',
 [r('E15 reported on 1 September 2011 that PPF, led by Petr Kellner, treated Home Credit Russia as its most valuable foreign asset and considered a partnership with state-owned VTB, which stalled. It also notes unconfirmed speculation about a state-controlled partner.','E15: Kellner’s talks with VTB',E15,'2011-09-01','Historical business context (about Petr Kellner)','Page text reviewed (extract)')],
 [r('The article describes commercial negotiations that did not complete and does not allege any political favor; it concerns Petr Kellner, not Renata Kellnerova.','E15: Kellner’s talks with VTB',E15,'2011-09-01','Limit of the evidence and attribution caveat','Page text reviewed (extract)')],
 'Not exoneration. A Forbes Czech page and an OSW analysis could not be read (empty or blocked), so succession, Czech government dealings, and post-2022 Russia exit were not verified. No inference is made from Petr Kellner’s business onto Renata Kellnerova.')

# 9 Low Tuck Kwong
KITCO='https://www.kitco.com/news/off-the-wire/2026-09-21/indonesia-grants-bayan-resources-15-20-mln-tons-additional-coal-mining'
add('low-tuck-kwong','mixed',
 'Low Tuck Kwong controls Bayan Resources, an Indonesian coal miner. In September 2026 the energy ministry granted Bayan subsidiaries an additional quota of about 15-20 million tonnes, after a force majeure declaration and the announced conditional sale of 10 billion shares to a company owned by tycoon Haji Isam. An official said the quota had nothing to do with the share sale. Only an unexplained timing coincidence appears in the sources read; no wrongdoing is alleged.',
 'Regulatory quota decision (timing noted; no alleged exchange)','September 2026 (recent); earlier history not reviewed',
 [r('Reuters via Kitco reports the ministry issued an additional quota to three Bayan subsidiaries on 21 September 2026, the week after Bayan declared force majeure and announced the conditional sale of shares held by Low Tuck Kwong and Elaine Low to Jhonlin Baratama, owned by Haji Isam.','Reuters via Kitco: Indonesia grants Bayan additional coal quota',KITCO,'2026-09-21','Dated report of a government decision and transaction timing','Page text reviewed')],
 [r('Energy ministry official Tri Winarno said the approval of the additional quotas has nothing to do with the share purchase agreement; the article does not explicitly link the quota to the force majeure approval.','Reuters via Kitco (official’s statement)',KITCO,'2026-09-21','Official response and explicit limit of the evidence','Page text reviewed')],
 'Not exoneration and not a finding of favor. The Haji Isam relationship to the government appears in search snippets only and was not verified from fetched pages (two Engineering News pages were blocked). Prior concession history, the 2022 export ban and any political ties of Low were not documented here.')

# 10 Nancy Walton Laurie
WIKI='https://en.wikipedia.org/wiki/Nancy_Walton_Laurie'
NWA='https://www.nwaonline.com/news/2020/oct/18/data-shows-some-walton-giving-leans-to-left/'
add('nancy-walton-laurie','no-strong',
 'Nancy Walton Laurie inherited a Walmart stake from her father James “Bud” Walton, Sam Walton’s brother. Walton-family political giving is documented for other members; the pages reviewed do not mention her political donations or policy activity. Family and corporate (Walmart) political activity is not attributed to her.',
 'None established for her personally','Inherited wealth; reviews dated 2020 and 2026 pages',
 [r('A reference page describes her as an heir to the Walmart fortune, with philanthropy and controversies (a university arena naming episode, a yacht protest), and states no political donations or involvement.','Wikipedia: Nancy Walton Laurie',WIKI,'accessed 2026-10-29','Background only','Page text reviewed')],
 [r('An Arkansas Democrat-Gazette analysis of FEC data on Walton family giving does not mention Nancy Walton Laurie; it covers Rob, Jim, Alice, and other relatives with mixed partisan patterns.','NWA Democrat-Gazette: Walton giving data',NWA,'2020-10-18','Attribution limit: family evidence is not about her','Page text reviewed (extract)')],
 'Not exoneration. FEC records for her individually were not searched. Advocacy reports on Walmart/Walton political spending appeared in results but were not read and are not used.')

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
(ROOT/'data/review-batches/029.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
