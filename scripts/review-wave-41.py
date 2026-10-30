"""Wave 41: narrow source-led, profile-only reviews; supersedes earlier authored profiles. No rubric: no person has all three dimensions supported by opened receipts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-30',reviewDepth='Narrow source-led review under a limited search budget; not independently editorially reviewed; no rubric assigned',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
WIKI='Page text reviewed; tertiary source via fetch tool, cited links not verified'
SNIP='Search-result summary only; page not opened directly'

# Walton
HO='https://oversight.house.gov/wp-content/uploads/2022/01/First-Solar-Letter_final-draft.pdf'
HOR='https://oversight.house.gov/release/comer-norman-probe-biden-administrations-taxpayer-funded-solar-loan-to-political-donor'
DFC='https://www.dfc.gov/media/press-releases/dfc-announces-approval-provide-500-million-debt-financing-first-solars'
add('lukas-walton','mixed',
 'The documented episode is a $500 million DFC debt-financing approval (7 December 2021) for First Solar\'s Tamil Nadu plant, followed by a January 2022 letter from two House Oversight Republicans asking whether Walton\'s 2020 Democratic donations played a role. The letter is a records request and an allegation of possible influence; the pages read contain no finding that donations affected the decision.',
 'Political donations and a First Solar ownership link, questioned in congressional oversight in relation to a government loan; no causal link established',
 'Donations 2020; DFC approval December 2021; House letter January 2022',
 [r('House Oversight letter of 18 January 2022 (Comer and Norman to DFC acting CEO) states that DFC approved the loan on 7 December 2021, that First Solar is "owned by Lukas Walton" (the letter\'s wording), that Walton gave $300,000 to the Biden campaign and over $100,000 to the DNC in 2020, and that the lawmakers are "concerned" the relationship "may have played a role". It requests DFC-White House and DFC-Walton communications. This is an allegation of possible influence, not a finding.','House Oversight Republicans: letter to DFC',HO,'2022-01-18','Political donations; allegation by lawmakers','PDF text extracted and read'),
  r('DFC announcement: up to $500 million of debt financing, "the largest single debt financing transaction for DFC", for a 3.3 GW thin-film module plant in Tamil Nadu, India; quotes DFC acting CEO and First Solar CEO. The page does not mention Walton.','DFC press release',DFC,'2021-12-07','Government financing','Page text reviewed'),
  r('Committee press release repeats the request and describes the concerns as questions; reports no DFC reply, documents produced or later findings.','House Oversight Committee release',HOR,'2022-01-18','Allegation status','Page text reviewed')],
 [r('The DFC press release records the loan as support for a manufacturing facility under a stated development initiative and does not mention Walton; the loan itself is an ordinary stated-purpose financing. The letter\'s Obama-era and Solyndra comparisons concern other administrations and are not evidence about Walton.','DFC press release; House letter',DFC,'2021-12-07','Scope limit; alternative explanation','Page text reviewed'),
  r('A web search summary reported that DFC denied any political considerations and that a DFC Inspector General inspection of the First Solar and Bio E loans exists; its findings and date could not be retrieved, so it is not relied on.','Search results (oversight.gov listing)','https://www.oversight.gov/reports/inspection-dfcs-first-solar-and-bio-e-projects','n/a','Possible exculpatory/neutral review, unread',SNIP)],
 'Not obtained: the DFC OIG report text (HTTP 406 on fetch), DFC board records, FEC filings, First Solar filings showing Walton\'s actual ownership (the letter\'s "owned by" wording is not verified; an earlier profile in this repo cited 4.9%). Ordinary donations and a loan to a company do not establish the mechanism. Narrow review, not exoneration and not a finding of influence.')

# Frist
DOJ='https://www.justice.gov/archive/opa/pr/2003/June/03_civ_386.htm'
WFR='https://en.wikipedia.org/wiki/Thomas_F._Frist_Jr.'
add('thomas-frist-jr','no-strong',
 'The documented matter is corporate: HCA subsidiaries pleaded guilty in 2000-2001 and HCA settled civil and administrative claims in 2003 (US$1.7 billion combined recovery). The DOJ release read does not describe any charge against Frist Jr. personally. No pages read show a personal political-benefit mechanism. His brother Bill Frist\'s Senate career is a relative\'s conduct and is not attributed to him.',
 'Corporate fraud enforcement against a company he led; no individual wealth-power exchange evidenced',
 'HCA leadership 1987-2002; settlements 2000-2003',
 [r('Frist Jr. co-founded HCA (1968), was chairman/president/CEO from 1987, left in the 1995 HealthTrust merger period as vice chairman, and returned as chairman and CEO in 1997 after Rick Scott resigned; CEO until January 2001, chairman until January 2002; HCA went private in a $21 billion deal in 2006.','Wikipedia: Thomas F. Frist Jr.',WFR,'2026','Role only (tertiary)',WIKI),
  r('DOJ, 26 June 2003: HCA agreed to $631 million civil and $250 million administrative payments, adding to over $840 million from the December 2000 subsidiary guilty pleas, for about $1.7 billion total; allegations included cost-report fraud, physician kickbacks and improper transfers dating to the late 1980s; a Corporate Integrity Agreement ran to 2009. Relates to the company, not to a named charge against Frist Jr.','US Department of Justice press release',DOJ,'2003-06-26','Corporate enforcement (company-level)','Page text reviewed')],
 [r('The DOJ release does not state that any individual executive was charged and does not name Frist Jr.; the conduct is described as that of HCA and subsidiaries, with the whistleblower cases covering schemes from the late 1980s, partly before and partly outside his 1997-2002 return.','US Department of Justice press release',DOJ,'2003-06-26','Scope limit on individual attribution','Page text reviewed'),
  r('The Wikipedia page does not mention political donations or the federal investigation, and lists Bill Frist only as his brother.','Wikipedia: Thomas F. Frist Jr.',WFR,'2026','Absence on this page (not exoneration)',WIKI)],
 'Not read: OpenSecrets/FEC records for Frist Jr. and family, HCA lobbying disclosures, any court record on individual liability. The "& family" entry here is evidenced only for Thomas Frist Jr.\'s executive role. Narrow review, not exoneration.')

# Mars
PC='https://www.citizen.org/sites/default/files/estatetaxfinal.pdf'
WM='https://en.wikipedia.org/wiki/Mars,_Incorporated'
mars_support=lambda who,role:[
 r('Public Citizen / United for a Fair Economy (April 2006, p. 36): the Mars family owns all of Mars Inc.; Jacqueline, Forrest Jr. and John have served as vice president, CEO and chairman; the family joined others to hire Patton Boggs to lobby for estate-tax repeal in 1992; Mars Inc. reported lobbying on the estate tax each year since 1998 and (p. 18-19) reported about $9.5 million of lobbying spending over eight reporting periods (all issues, not estate tax alone). The authors are advocates for retaining the estate tax and estimate the siblings\' tax saving from repeal in aggregate. The report does not itemise '+who+'\'s personal instructions.','Public Citizen / United for a Fair Economy: Spending Millions to Save Billions',PC,'2006-04','Advocacy research on lobbying','PDF text extracted and read'),
 r('Wikipedia notes Mars Inc. lobbying spend of over $1.8 million in 2008 and $1.655 million in 2009 (tax issues) and that Mars is entirely family owned; '+role,'Wikipedia: Mars, Incorporated',WM,'2026','Company lobbying and ownership (tertiary)',WIKI+'; first 100,000 characters only')]
mars_counter=[r('Estate-tax repeal did not happen: the report itself records that early Mars-involved efforts in the 1990s were described by a Washington Post reporter as "fruitless". Lobbying on a general tax policy is open advocacy and disclosed under federal law; the report does not show a specific preferential benefit to Mars Inc. or any sibling.','Public Citizen report, p. 36 (quoting Washington Post, 2005)',PC,'2006-04','Counter-evidence: outcome and legality','PDF text extracted and read')]
mars_lim='Not read: Mars Inc. LDA filings and OpenSecrets/FEC data for the individual siblings (political giving would be a separate dimension), sugar-policy lobbying, any post-2006 period. Company lobbying is not transferred to an individual without evidence of direction. Narrow review, not exoneration.'
add('jacqueline-mars','mixed','Documented activity is company-level lobbying and a family-funded effort on estate-tax repeal in the 1990s-2000s, reported by an advocacy group. Jacqueline is named only as a sibling with a corporate role; her personal direction, political giving and any realised benefit are not shown in the pages read. The repeal did not succeed in the period covered.','Family-company lobbying on a general tax rule; individual direction and preferential benefit not evidenced','1992-2006 (report published April 2006)',
 mars_support('Jacqueline','Jacqueline Mars is not described there.'),mars_counter,mars_lim)
add('john-mars','mixed','Documented activity is company-level lobbying and a family-funded effort on estate-tax repeal in the 1990s-2000s, reported by an advocacy group. John Mars is named as a sibling and a chairman of Mars Inc.; his personal direction, political giving and any realised benefit are not shown in the pages read. The repeal did not succeed in the period covered.','Family-company lobbying on a general tax rule; individual direction and preferential benefit not evidenced','1992-2006 (report published April 2006)',
 mars_support('John','Wikipedia lists John Franklyn Mars as chairman.'),mars_counter,mars_lim)

# Son
SNP='https://newschannel9.com/news/nation-world/president-elect-donald-trump-japanese-technology-group-softbank-ceo-masayoshi-son-to-announce-100b-us-investment-plan-mar-a-lago-florida-election-policies'
WS='https://en.wikipedia.org/wiki/Masayoshi_Son'
add('masayoshi-son','mixed',
 'Son has documented high-level access: in December 2024 he joined then President-elect Trump at Mar-a-Lago to announce a SoftBank pledge of $100 billion of US investment over four years. A pledge by a company is not a government benefit, and the pages read show no preferential public-sector benefit, subsidy or regulatory favour to Son. His other regulatory episode on the page read (Nvidia-Arm, 2022) was a government block that cut against SoftBank.',
 'Political access via investment announcement; no specific preferential benefit evidenced',
 'December 2024; Arm/Nvidia 2022',
 [r('AP coverage (syndicated copy, December 2024): Son joined Trump at Mar-a-Lago to announce $100 billion US investment over four years, 50,000 jobs and $50 billion into startups; Trump said it doubled a 2016 pledge; Commerce nominee Howard Lutnick was present; AP noted WeWork\'s bankruptcy and past unfulfilled Trump-era pledges. Only a search-result summary was seen, not the full page.','Associated Press (syndicated local-station copy, via search summary)',SNP,'2024-12','Political access',SNIP),
  r('Wikipedia: SoftBank held a 29.5% Alibaba stake worth about $108.7 billion (October 2018); Alibaba board exit June 2020; personal debt to SoftBank of $5.1 billion by February 2023 (Bloomberg, via the page), which Son said involved no conflict; listed in the Pandora Papers category without detail.','Wikipedia: Masayoshi Son',WS,'2026','Wealth origin, governance context (tertiary)',WIKI)],
 [r('Nvidia-Arm deal failed in February 2022 after US and EU antitrust objections, and Chinese regulatory crackdowns in 2021 hurt the Vision Fund (per Wikipedia): evidence of regulators acting against SoftBank interests.','Wikipedia: Masayoshi Son',WS,'2022-02','Counter-evidence: adverse state action',WIKI),
  r('AP (via search summary) noted that some companies failed to deliver on past investment promises; no follow-up on how much of the $100 billion was deployed was found. The announcement is a private pledge, not a state award.','Associated Press (search summary)',SNP,'2024-12','Scope limit',SNIP)],
 'Not read in full: the AP page (blocked), Stargate government documents, SoftBank filings, Saudi PIF-Vision Fund material, Japanese government dealings, FEC/LDA records. Wikipedia had nothing on Trump meetings or PIF. Narrow review, not exoneration; no rubric dimension is fully supported.')

# Li
WL='https://en.wikipedia.org/wiki/Li_Ka-shing'
WCK='https://en.wikipedia.org/wiki/CK_Hutchison_Holdings'
add('li-ka-shing','mixed',
 'Pages read show a business family operating in tense relations with the Chinese state at points: state media criticism in 2015 over asset sales that then stopped, and in 2025-26 a ports sale linked to US politics followed by a Panama Supreme Court ruling that voided CK Hutchison\'s Panama concessions. These are company-level and exposure-to-state-pressure facts; they do not show personal preferential benefit to Li Ka-shing. Li\'s son Victor Li leads the group; relatives\' conduct is not attributed to him.',
 'Strategic-infrastructure exposure to state pressure; no preferential-benefit mechanism evidenced',
 '2011-2026 (sources dated within)',
 [r('Wikipedia: Li endorsed Henry Tang in 2011; Xinhua criticised him over the 2014 protests; in early 2015 Global Times and others attacked him over reported property sales, calling them "an act of ingratitude"; the attacks stopped after several weeks; his companies said the sales were ordinary business.','Wikipedia: Li Ka-shing',WL,'2011-2015','Relations with state (tertiary)',WIKI),
  r('Wikipedia: March 2025 reports of CK Hutchison selling its port holdings to a consortium including BlackRock and MSC-linked TiL, framed against Trump\'s criticism of Chinese influence at the Panama Canal; Panama sued in July 2025 and its Supreme Court on 29 January 2026 ruled the Balboa and Cristobal concession unconstitutional.','Wikipedia: CK Hutchison Holdings',WCK,'2025-2026','Company exposure (tertiary)',WIKI)],
 [r('The Panama ruling went against CK Hutchison, and the 2015 episode shows state criticism rather than favour; neither shows a concession or benefit granted to Li personally. The page does not say whether CK Hutchison\'s own statements dispute the Panama accusations.','Wikipedia: CK Hutchison Holdings; Li Ka-shing',WCK,'2026','Counter-evidence: adverse outcomes',WIKI)],
 'Not read: Hong Kong land-sale or government-contract records, Basic Law/advisory role details (the page only lists categories), Reuters/Panama court documents, CK Hutchison filings, historical Hong Kong property episodes. Wikipedia only; narrow review, not exoneration.')

# Pignataro
WP='https://en.wikipedia.org/wiki/Andrea_Pignataro'
add('andrea-pignataro','no-strong',
 'The only government-facing matter in the page read is an Italian tax matter: in 2025 the revenue agency reportedly investigated alleged evasion of about EUR 500 million (2013-2023) and he reportedly agreed to pay EUR 280 million in instalments. That is an enforcement/settlement episode, not evidence of political benefit. Acquisitions of Italian firms (Cedacri, Cerved, Prelios) are ordinary investments in the pages read. No political-power mechanism was found; this is a scoped statement.',
 'No wealth-power mechanism identified in sources read; tax settlement is enforcement',
 '1997-2026 as described',
 [r('Wikipedia: founded ION in 1997; invested over EUR 3 billion in 2021 to acquire Cedacri and Cerved and EUR 1.35 billion for control of Prelios (July 2024); in 2025 reportedly investigated by Agenzia delle Entrate for alleged evasion of about EUR 500 million (about EUR 1.2 billion with interest) and reportedly agreed to pay EUR 280 million in five instalments (citing Il Post, 9 June 2025).','Wikipedia: Andrea Pignataro',WP,'2025','Business and tax enforcement (tertiary; figures reported)',WIKI)],
 [r('The page does not mention political ties, donations or state benefits, and the tax outcome was a payment by Pignataro. A separate earlier search-result summary (Reuters via MarketScreener, Cedacri golden-power case, Council of State voiding a 2023 decree in December 2025) was not reopened here (page returned 404), so it is not relied on.','Wikipedia: Andrea Pignataro',WP,'2025','Scope limit; absence not exoneration',WIKI)],
 'Not read: the Reuters Cedacri article (404), Italian golden-power decrees, Il Post/Il Sole 24 Ore tax reports, UK/Italy donation or lobbying records. Allegations of tax evasion are reported allegations; the settlement terms are reported by a tertiary source. Narrow review, not exoneration.')

ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
out=dict(supersedes=list(P),profiles=P,rubrics=R)
(ROOT/'data/review-batches/041.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
