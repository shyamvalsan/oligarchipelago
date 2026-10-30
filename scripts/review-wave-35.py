"""Wave 35: narrow profile-only reviews; evidence thin for a three-dimension rubric, so no rubrics added."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,status='no-strong'):
 P[id]=dict(status=status,reviewedAt='2026-10-29',reviewDepth='Narrow source-led review; not independently editorially reviewed',confidence='Low / narrow review',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
NOTE=' This is a narrow review, not exoneration: absence of a documented mechanism in the sources read does not mean none exists.'
WIKI='Wikipedia (secondary source)'
PAGE='Page summary reviewed via fetch tool; secondary summary, not a primary record'

# Ray Dalio
NBC_D='https://www.nbcnews.com/politics/politics-news/investor-predicted-2008-financial-crisis-says-worried-something-worse-rcna201040'
WP_D='https://en.wikipedia.org/wiki/Ray_Dalio'
add('ray-dalio',
 'No documented preferential state benefit or political-exchange mechanism was found for Dalio in the pages read. The reviewed material shows a public commentator who criticised US tariff policy in 2025, and a 2023 press investigation about investment-method claims that Dalio and Bridgewater dispute.',
 'None established; policy commentary and press controversy only',
 'Public statements in 2025; press controversy reported 2023',
 [r('Wikipedia summarises a November 2023 New York Times investigation (Rob Copeland) as reporting that Bridgewater investments were largely based on Dalio’s own picks and informed by legally obtained information from government-linked associations. This is a press characterisation, not a regulatory finding, and the article lists no enforcement action against Bridgewater.','Wikipedia: Ray Dalio',WP_D,'2026-10-29','Secondary summary of a press allegation',PAGE)],
 [r('Dalio called the book The Fund “fiction, created as fact” and Bridgewater called it a “false and misleading depiction”. Copeland said no substantive factual critique was raised. The summary notes no regulatory action against Bridgewater.','Wikipedia: Ray Dalio (responses)',WP_D,'2026-10-29','Subject response',PAGE),
  r('On Meet the Press Dalio said the US was “very close to a recession” and called the tariff rollout disruptive. The article does not report any political tie to the administration. Criticism of a policy is not evidence of a preferential benefit.','NBC News',NBC_D,'2025-04-13','Limit of evidence / alternative reading')],
 'Searched for political access, donations, government-linked benefit and Bridgewater-specific state dealings; only the items above were read. Wikipedia lists him as independent and records no donations; that is not a donations search of FEC records. No claim is made about China-related dealings beyond the article’s statement of a 2020 foundation gift.'+NOTE)

# Wang Liping
FB_W='https://www.forbes.com/profile/wang-liping/'
TG='https://www.itiger.com/news/1152241994'
add('wang-liping',
 'Wang Liping is the self-made founder and chairman of Jiangsu Hengli Hydraulic, a listed Changzhou manufacturer. The pages read describe business and wealth only; no preferential state benefit, political office or exchange was documented, and the review could not search Chinese-language sources.',
 'None established',
 'Company and wealth data to 2025–2026',
 [r('Forbes lists Wang as founder (1990) and chairman of Shanghai-listed Hengli, with factories in China, Germany, the US, Japan and Mexico; it records no political content and does not give his ownership stake or name family members in the entry.','Forbes profile: Wang Liping & family',FB_W,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool; real-time net worth as of 2026-10-29')],
 [r('A Hurun-based report puts Wang and family at 86 billion yuan in 2025 (headline mislabels the currency as dollars) and describes revenue and profit growth driven by cylinders for construction and agricultural machinery. No political tie is mentioned.','itiger news report on Hurun list',TG,'2025-10-29','Alternative explanation (commercial growth) and limit of evidence',PAGE)],
 'Identity note: a different Wang Liping (the late Shanghai CPPCC chairman, born 1940) appears in search results and must not be confused with the Hengli chairman (born c. 1966). No search of Chinese-language sources, CPPCC or party-congress membership rosters, subsidy or land records was possible in this session (search budget exhausted), so CPPCC or other political roles are untested.'+NOTE)

# Donald Newhouse
FB_N='https://www.forbes.com/profile/donald-newhouse/'
WP_N='https://en.wikipedia.org/wiki/Donald_Newhouse'
add('donald-newhouse',
 'Donald Newhouse (1929–2026) was president of the family-owned Advance Publications and inherited it with his brother. The pages read contain no political activity or state-benefit mechanism for him personally. Reported donations by other Advance-linked people are not attributed to him.',
 'None established for Donald Newhouse personally',
 'Inherited media holdings; death reported May 2026',
 [r('Forbes records that Donald and his late brother Si inherited Advance Publications from their father in 1979 and that Donald long oversaw the newspaper business; it records no political content. The same page reports his death in May 2026 although its net-worth figure is dated March 2026.','Forbes profile: Donald Newhouse',FB_N,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool')],
 [r('The Wikipedia entry reports no political donations or controversies for him. Search-result snippets about political giving named other people (a younger family member and Advance executives) and are not read as evidence about Donald Newhouse.','Wikipedia: Donald Newhouse',WP_N,'2026-10-29','Explicit limit of evidence / attribution boundary',PAGE)],
 'Identity: Forbes entry is Donald Newhouse (not Steven or other family members). Forbes and Wikipedia report his death in May 2026 while the Forbes net-worth figure is dated March 2026; the maintainer should check how the entry should be treated. Donations by Ben Newhouse and Advance executives surfaced only as search-result snippets and were not fetched, so they are not used. No FEC search was possible.'+NOTE)

# Hussain Sajwani
AP_S='https://www.clickondetroit.com/business/2025/01/07/trump-announces-20b-us-investment-by-emirati-businessman/'
NBC_S='https://www.nbcnews.com/news/us-news/trump-i-turned-down-2-billion-deal-dubai-friend-n705836'
WP_S='https://en.wikipedia.org/wiki/Hussain_Sajwani'
add('hussain-sajwani',
 'Sajwani is a long-time business partner of the Trump Organization and was publicly presented by Trump with a $20 billion US data-centre pledge in January 2025. The pages read document access and a licensing relationship, but not a state benefit or favour in return; the earlier promised deals did not materialise.',
 'Trump-brand licensing partnership and presidential-level access; no preferential benefit established',
 'Trump Organization partnership from 2010s; US pledge announced 2025-01-07',
 [r('AP reports Trump announcing DAMAC’s $20 billion US data-centre investment and notes that DAMAC built a Trump-branded golf club in Dubai and paid a multimillion-dollar licensing fee to the Trump Organization. AP says Sajwani was seen at Mar-a-Lago after the election and that the pledge suggests investors close to Trump can profit from the relationship. Trump said he wants investments of $1 billion or more to move quickly through environmental review.','Associated Press via WDIV ClickOnDetroit',AP_S,'2025-01-07','Reported access and business relationship'),
  r('In January 2017 Trump said he had turned down a $2 billion Dubai deal offered by Sajwani. DAMAC said that several property proposals had been discussed and rejected. Ethics experts quoted by NBC raised conflict-of-interest concerns about presidential family business ties.','NBC News',NBC_S,'2017-01-11','Reported access and ethics concern')],
 [r('AP says the promised $2 billion in deals after the 2016 election never materialised and a planned Trump-named course was dropped; DAMAC’s data-centre arm had no US sites at the time. The article reports no regulatory favour and no critic responses, so it supports the commercial relationship but not a state benefit.','Associated Press via WDIV ClickOnDetroit: limits',AP_S,'2025-01-07','Material limit of evidence'),
  r('Sajwani said after his 2016 discussions that he is not involved in political issues, according to NBC.','NBC News: subject statement',NBC_S,'2017-01-11','Subject response')],
 'Historical Egypt matter (a 2011 in-absentia sentence over a land purchase, suspended after a 2013 settlement) appears only in a Wikipedia summary and was not verified against primary or news sources, so it is not used as support. The review did not locate evidence on Dubai or Emirati state benefits, or on any US policy outcome favouring DAMAC after 2025. A licensing fee paid to the Trump Organization is a corporate commercial arrangement; it is not by itself a benefit to Sajwani from the state.'+NOTE)

# Shahid Khan
JT='https://jaxtoday.org/2024/06/25/city-council-oks-1-4b-stadium-of-the-future-deal/'
PFT='https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/jaguars-city-of-jacksonville-agree-to-1-4-billion-stadium-deal'
BB='https://www.bondbuyer.com/news/stadium-funds-part-of-jacksonvilles-355-million-bond-sale'
SI='https://www.si.com/nfl/2017/04/19/donald-trump-inaugural-committee-donors-nfl-mlb-donors'
WP_K='https://en.wikipedia.org/wiki/Shahid_Khan'
add('shahid-khan',
 'The Jacksonville stadium agreement commits large city funds to a team-owned franchise, a conventional local public subsidy for which the council gave public approval; Khan separately gave $1 million to a 2017 presidential inaugural committee. Nothing read links the donation to the stadium deal or shows leverage beyond ordinary stadium-subsidy negotiation.',
 'Public stadium financing for team lease; separate 2017 inaugural donation; no linkage established',
 'Jacksonville stadium agreement 2024–2025; inaugural donation reported 2017',
 [r('PFT reports the city and Jaguars each commit $625 million to a $1.25 billion project, plus $150 million from the city for preparation, a new 30-year lease, and Khan covering cost overruns and day-to-day operations. The city funds its share from a capital-plan shift and an existing half-penny sales tax.','NBC Sports ProFootballTalk',PFT,'2024-05-14','Reported public financing terms'),
  r('The council approved 14-1 on 25 June 2024. The lone no vote cited city finances, construction practice and the sales-tax plan; residents criticised separating the community-benefits agreement from the stadium deal.','Jacksonville Today',JT,'2024-06-25','Local criticism of the public share'),
  r('Bond Buyer reports a $355 million city bond sale in 2025 with $145 million for stadium reconstruction, repaid mainly from sales tax, state revenue sharing and utilities service taxes.','The Bond Buyer',BB,'2025-07-31','Reported financing mechanism'),
  r('Sports Illustrated, citing an FEC disclosure, reports Khan donated $1 million to the Trump inaugural committee, alongside several other NFL owners.','Sports Illustrated',SI,'2017-04-19','Reported political donation','Page summary reviewed via fetch tool')],
 [r('The stadium terms make Khan responsible for overruns and operations, and the council vote was public and near-unanimous. The articles do not connect the Jacksonville deal to any donation or private favour; stadium subsidies are common and contested across the league.','NBC Sports ProFootballTalk: obligations',PFT,'2024-05-14','Alternative explanation / limit of evidence'),
  r('Wikipedia records Khan publicly criticising Trump’s 2017 immigration ban and backing some economic policies while opposing social ones. Inauguration donations by many owners are not alone evidence of influence.','Wikipedia: Shahid Khan',WP_K,'2026-10-29','Subject position and limit',PAGE)],
 'Jaxdailyrecord pages on the 2021 hotel incentives package were not readable (HTTP 403), so no claim about that package is made. Not read: lobbying disclosures, council member donations from Khan or his companies, and any state-level benefits. The public-subsidy evidence is good on facts but is a standard local-policy transaction; it was not enough, with the thin political evidence, to assign a rubric.'+NOTE)

# Antonia Ax:son Johnson
FB_A='https://www.forbes.com/profile/antonia-axson-johnson/'
WP_A='https://en.wikipedia.org/wiki/Antonia_Ax:son_Johnson'
add('antonia-axson-johnson',
 'Antonia Ax:son Johnson is a fourth-generation owner of the Swedish Axel Johnson group, with wealth that is largely inherited. The pages read show no political office, donations or state-benefit mechanism for her; the review is too narrow to say more.',
 'None established',
 'Inherited conglomerate; chair 1982–2015',
 [r('Forbes describes her fortune as coming from the Axel Johnson conglomerate, founded in 1873 by her great-grandfather, which includes a 50% stake in Axfood. She chaired it from 1982 until 2015 and hands the role to her daughter Caroline Berg, keeping a board seat. The page has no political content.','Forbes profile: Antonia Ax:son Johnson & family',FB_A,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool; Forbes entry is for the family, with her as the named individual')],
 [r('The Wikipedia entry describes no political positions or controversies (it carries only an unexplained category tag for Swedish Liberals), and the extracted text does not contain any state-benefit episode.','Wikipedia: Antonia Ax:son Johnson',WP_A,'2026-10-29','Explicit limit of evidence',PAGE)],
 'Forbes “& family” entry: the evidence concerns Antonia only; other family members and group companies (Axfood, Axel Johnson Inc.) were not individually reviewed. No Swedish-language search, lobbying, procurement or regulatory search was possible (search budget exhausted).'+NOTE)

# Jaime Gilinski Bacal
LSV='https://www.lasillavacia.com/quien-es-quien/jaime-gilinski-bacal/'
RT='https://www.riotimesonline.com/de-la-espriella-gilinski-group-documented-2026/'
EH='https://www.elheraldo.co/economia/2022/02/09/jaime-y-gabriel-gilinski-renunciaron-a-junta-de-gnb-sudameris-886219/'
add('jaime-gilinski-bacal',
 'A Colombian investigative profile reports that Gilinski’s bank lent a presidential candidate roughly COP 5,000 million, and a 2026 report says GNB Sudameris lent about COP 17,500 million to a runoff campaign. Bank lending to campaigns is regulated rather than prohibited, no electoral authority has been reported to have examined the 2026 loan, and neither source establishes a state benefit in return.',
 'Bank lending to campaigns; reported but undocumented political proximity; no benefit established',
 'Campaign loans reported (earlier cycle undated; 2026 runoff); GEA takeover 2021–2024',
 [r('La Silla Vacía’s profile states that the bank financed almost all of Gustavo Petro’s second-round campaign with a COP 5,000 million loan, and that it also financed him in 2010. The profile does not clearly state the election year, and says rumours of closeness to Petro run through an associate, Álex Vernot. The reporting is the outlet’s own and is not sourced further.','La Silla Vacía: Quién es quién, Jaime Gilinski Bacal',LSV,'2023-09','Reported campaign financing','Page read via fetch summary; update date September 2023; loan year ambiguous'),
  r('Rio Times, citing La Silla Vacía, reports a GNB Sudameris loan of COP 17,500 million (about US$4.4 million) to Abelardo de la Espriella’s runoff campaign. The campaign declined to answer questions; the Gilinski group had made no public statement.','The Rio Times (citing La Silla Vacía)',RT,'2026','Reported campaign loan; attributed to the bank group','Secondary report of another outlet’s reporting; loan date not stated')],
 [r('The Rio Times article says bank lending to campaigns is lawful in Colombia and regulated, that no electoral authority had examined this loan, and that it attributes the loan to the bank, not to Jaime Gilinski personally; it frames the concern as political proximity, not legality.','The Rio Times: limits of evidence',RT,'2026','Explicit limit of evidence'),
  r('The family’s multi-company takeover bids for Grupo Sura and Grupo Nutresa were regulated tender offers; Jaime and Gabriel Gilinski resigned from the GNB Sudameris board in February 2022 to join those companies’ boards and avoid a conflict of interest. No political favour is alleged in the page.','El Heraldo',EH,'2022-02-09','Alternative explanation (ordinary regulated corporate activity)')],
 'The two campaign-loan reports point to different candidates and cycles and the earlier one has an unclear year; the maintainer should not attribute both to the same race. Superintendencia and Petro-era regulatory decisions affecting his banks were searched but nothing was read about them. Personal versus bank-group conduct is not separated in the reporting. No finding, allegation of wrongdoing or sanction is reported in any page read.'+NOTE)

# Ann Walton Kroenke
FB_AK='https://www.forbes.com/profile/ann-walton-kroenke/'
WP_AK='https://en.wikipedia.org/wiki/Ann_Walton_Kroenke'
add('ann-walton-kroenke',
 'Ann Walton Kroenke’s wealth derives from Walmart stock inherited from her father; she holds no Walmart board or executive role and owns the Denver Nuggets and Colorado Avalanche. The pages read contain no political activity of hers, and her husband’s separate sports and real-estate interests are not attributed to her.',
 'None established',
 'Inherited Walmart stake since 1995; franchise ownership from 2015–2016',
 [r('Forbes says she inherited part of her father Bud Walton’s Walmart stake after his 1995 death, has no board or executive role at the company, and that her husband Stan Kroenke owns the Nuggets, Avalanche, Rams, Rapids and Arsenal. The profile has no political information.','Forbes profile: Ann Walton Kroenke',FB_AK,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool; as of 2026-10-29')],
 [r('Wikipedia lists her as principal owner of the Nuggets and Avalanche (after a transfer from her husband), mentions no political donations or controversies, and has inconsistent birth dates, so it is a weak source.','Wikipedia: Ann Walton Kroenke',WP_AK,'2026-10-29','Explicit limit of evidence',PAGE)],
 'Identity and attribution: Walmart corporate lobbying and Stan Kroenke’s stadium and franchise-relocation matters are not hers and were not used. No donations (FEC), arena-subsidy or lobbying records were searched for her specifically (search budget exhausted).'+NOTE)

# Xavier Niel
CB='https://www.cbnews.fr/medias/image-avec-cession-ses-parts-xavier-niel-sanctuarise-capital-du-groupe-monde-84093'
WP_X='https://en.wikipedia.org/wiki/Xavier_Niel'
FB_X='https://www.forbes.com/profile/xavier-niel/'
add('xavier-niel',
 'Niel is a self-made telecom and media investor with documented ties to French public figures, including Macron’s attendance at his Station F inauguration. The pages read show a state-adjacent episode in his early years and a media-independence step, but no preferential benefit or exchange mechanism for his wealth.',
 'Public-figure ties and media ownership; no preferential benefit established',
 'Station F 2017; Légion d’honneur 2022; Le Monde stake transfer 2024',
 [r('Wikipedia’s summary says President Macron attended the 2017 inauguration of Niel’s Station F incubator and that Niel was made a Knight of the Legion of Honour in 2022. It also reports that as a teenager he was summoned to the Interior Ministry over decoder hacking and, per a 2016 biography, worked with the DST, and that in 2006 he received a two-year suspended sentence for misuse of company assets. These are historical or reputational ties, not evidence of a benefit.','Wikipedia: Xavier Niel',WP_X,'2026-10-29','Secondary summary of historical ties and legal history',PAGE),
  r('Forbes lists him as self-made, owner of the Iliad telecom group and holder of stakes in Le Monde and Vodafone, with no political content on the profile.','Forbes profile: Xavier Niel & family',FB_X,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool')],
 [r('CB News reports that on 23 April 2024 Niel transferred nearly all of his Le Monde group stake to a non-profit press-independence fund for €1, keeping one share, to lock in the group’s independence of any one investor. This reduces, rather than increases, a media-control concern.','CB News',CB,'2024-04-23','Subject action / alternative explanation')],
 'A fourth-mobile-licence award to his Iliad subsidiary in 2009 (single bidder, contested by rivals and upheld by the Conseil d’État in 2010 per search-result snippets) was not readable in any fetched page (lsa-conso and Concurrences returned HTTP 403), so it is not used as evidence. No Free/Iliad regulatory or lobbying records were read. Forbes entry is “& family”; evidence concerns Xavier Niel only. Wikipedia is secondary.'+NOTE)

# David Velez
FB_V='https://www.forbes.com/profile/david-velez/'
WP_V='https://en.wikipedia.org/wiki/David_V%C3%A9lez'
add('david-velez',
 'Vélez is the self-made founder and CEO of Nubank, a licensed digital bank listed in New York in 2021. The pages read show a Colombian state honour in 2024 but no preferential benefit, patronage or political exchange; regulatory licences and Brazilian policy were not documented in any page read.',
 'None established',
 'Nubank founding 2013; IPO 2021; Colombian congressional honour 2024',
 [r('Forbes describes him as cofounder and CEO of Nubank, with a stake in Nu Holdings, which listed on the NYSE in December 2021, and records no political content.','Forbes profile: David Velez & family',FB_V,'2026-10-29','Identity and wealth-source context','Page summary reviewed via fetch tool'),
  r('Wikipedia says Colombia’s Congress awarded him the Simón Bolívar Order of Democracy in September 2024 for entrepreneurial achievement. An honour is not a financial benefit or evidence of influence.','Wikipedia: David Vélez',WP_V,'2024-09','Contextual honour',PAGE)],
 [r('The same Wikipedia page describes a competitive product story (a no-fee card, app-based accounts and growth to over 100 million customers) and does not mention regulatory licences or controversies; it is a secondary summary and does not establish absence of favourable treatment.','Wikipedia: David Vélez',WP_V,'2026-10-29','Alternative explanation and limit of evidence',PAGE)],
 'Forbes “& family” entry; evidence concerns David Vélez only. Brazilian, Mexican and Colombian licensing decisions, campaign donations and lobbying were not read (search budget exhausted); their absence here is not a finding.'+NOTE)

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
(ROOT/'data/review-batches/035.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
