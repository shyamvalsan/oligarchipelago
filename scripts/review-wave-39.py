"""Wave 39: US/Spain mega-fortunes (Alphabet, Walmart, Microsoft, Inditex). Profile-only reviews; supersedes thin launch profiles 002/006/021."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
WIKI='Page text reviewed; tertiary source via fetch tool, cited links not verified'
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-30',reviewDepth='Narrow source-led review under a limited search budget; not independently editorially reviewed; no rubric assigned',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)

W='https://en.wikipedia.org/wiki/'
DOJ='https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google'
UG=W+'United_States_v._Google_LLC_(2020)'
SB=W+'Sergey_Brin'
add('larry-page','no-strong',
 'Page co-founded Google. The reviewed pages describe company-level antitrust litigation (US v. Google) and, per a Wikipedia summary of a 2026 press report, Page and Brin moving or closing 60 California LLCs in December 2025 around a proposed state billionaire tax. None of the pages read names Page personally in a political donation, appointment, or state benefit.',
 'No personal wealth-power mechanism identified; company-level antitrust case and a tax-residency/asset-structure episode only',
 '2020-2026 as described in reviewed pages',
 [r('Justice Department press release: court ordered remedies in US v. Google on 2 September 2025, barring exclusive contracts for Google Search, Chrome, Assistant and Gemini and requiring some index and interaction data sharing with rivals. The August 2024 opinion found Google maintained a monopoly in general search. This is a company case; Page is not mentioned in the release.','US Department of Justice press release',DOJ,'2025-09-02','Government release (company-level)','Page text reviewed'),
  r('Summary of the case: liability ruling 5 August 2024 (Judge Mehta), remedies September 2025 with no Chrome/Android divestiture, supplementary December 2025 order, appeals pending as of early 2026. The page does not name Page or Brin.','Wikipedia: United States v. Google LLC (2020)',UG,'2026','Case summary (tertiary)',WIKI),
  r('Role-only: article reports that in December 2025 Brin and Page (combined $520 billion per the page) moved or closed 60 California LLCs, which the article ties to the 2026 billionaire-tax initiative. Motive is the article\'s inference, not an adjudicated finding; Page-specific conduct is not separately detailed in the text read.','Wikipedia: Sergey Brin (citing NYT)',SB,'2026','Press report via tertiary summary',WIKI)],
 [r('The antitrust case is against the company and its outcome was a conduct remedy, not a state benefit to the founder. Restructuring assets in response to a tax proposal is lawful planning absent further facts, and no benefit linked to public power was found.','Reviewer scope note',UG,'2026','Explicit limit of evidence',WIKI)],
 'Not read: FEC, OpenSecrets or LDA records for Alphabet and Page personally; the NYT original; Alphabet proxy statements. Rubric dimensions (leverage, benefit, exchange) lack receipts specific to Page. A narrow review, not exoneration.')

add('sergey-brin','mixed',
 'Brin co-founded Google. A Wikipedia summary of an April 2026 New York Times report says he gave to Democrats in earlier years ($5,000 to Obama 2012; $30,800 to the DNC), later shifted toward Republican causes, reportedly spent $57 million trying to block California\'s proposed billionaire tax, attended Trump\'s second inauguration, and was appointed to PCAST in March 2026. These are personal political acts and an advisory appointment, but no preferential economic benefit was found.',
 'Personal political spending and an advisory appointment (PCAST, March 2026); no linked economic benefit shown',
 '2012-2026',
 [r('Brin\'s political giving: $5,000 to Obama 2012 reelection and $30,800 to the DNC; per an April 2026 NYT report cited by the page, a move to conservative causes and about $57 million spent trying to block the California billionaire tax; attended the 2025 inauguration; appointed to the President\'s Council of Advisors on Science and Technology in March 2026. Figures are the page\'s summary of press reporting and were not checked against FEC or California filings.','Wikipedia: Sergey Brin',SB,'2026','Press report via tertiary summary',WIKI),
  r('December 2025: Brin-linked entity moved or closed 15 California LLCs in the 10 days before Christmas, seven converted to Nevada entities; Brin and Page together moved or closed 60 LLCs, per the page.','Wikipedia: Sergey Brin (citing NYT)',SB,'2026','Press report via tertiary summary',WIKI),
  r('Company-level: remedies in US v. Google ordered 2 September 2025; Brin not named.','US Department of Justice press release',DOJ,'2025-09-02','Government release (company-level)','Page text reviewed')],
 [r('Spending to oppose a tax and holding an advisory seat are ordinary-looking political participation unless a specific preferential benefit is shown; none was found. PCAST seats are advisory.','Reviewer scope note',SB,'2026','Explicit limit of evidence',WIKI)],
 'Leverage may be non-trivial (advisory seat, access), but no benefit or feedback evidence was opened, so no rubric is assigned (benefit and exchange lack receipts). The primary filings and the NYT article were not read. Narrow review, not exoneration.')

BAL=W+'Intuit_Dome'
add('steve-ballmer','no-strong',
 'Ballmer (former Microsoft CEO) owns the LA Clippers. The reviewed Intuit Dome page describes the arena\'s approval by the City of Inglewood (exclusive negotiating agreement 2017; environmental review process 2018-2019; Surplus Land Act challenge dismissed November 2019) and the 2020 purchase of The Forum from MSG for $400 million. It reports no public subsidy and no personal political favour.',
 'Municipal approval of a private arena; no subsidy or preferential benefit found in the page read',
 '2017-2024',
 [r('Inglewood approved an exclusive negotiating agreement with the Clippers in 2017; a draft EIR notice was issued February 2018; a judge ruled against a Surplus Land Act suit (Uplift Inglewood) in November 2019; MSG-funded resident litigation and a December 2018 countersuit are recorded; Ballmer announced purchase of The Forum in March 2020 (closed May 2020) removing the last major hurdle; arena opened 15 August 2024. The page, as read, describes no public subsidy.','Wikipedia: Intuit Dome (first ~100,000 characters)',BAL,'2026','Case/project summary (tertiary)',WIKI)],
 [r('A municipal land-use approval of a private arena with a court challenge dismissed is a routine, contested process rather than evidence of a bargain; the page notes no public subsidy. The last ~30,000 characters of the page were not read.','Reviewer scope note',BAL,'2026','Explicit limit of evidence',WIKI)],
 'Not read: Inglewood council records, land transfer terms, CEQA documents, any city agreements, FEC/Washington-state disclosures, USAFacts funding. No evidence for leverage, benefit or exchange at rubric standard. Narrow review, not exoneration.')

USM=W+'United_States_v._Microsoft_Corp.'
add('bill-gates','no-strong',
 'Gates co-founded Microsoft. The reviewed page on US v. Microsoft (DOJ suit 1998; liability findings 1999-2000; D.C. Circuit 2001; settlement approved 2002 and 2004) concerns company conduct. Gates\' videotaped deposition was reported as evasive by a cited source; no personal finding against him is recorded. This is a historical episode in which a regulator was adverse to the company, the opposite of preferential treatment.',
 'Company-level antitrust litigation 1998-2004 (adverse, then settled); no personal benefit mechanism shown',
 '1998-2004 for this episode',
 [r('DOJ and 20 states and DC sued Microsoft 18 May 1998; Judge Jackson found monopolization 1999-2000 and ordered a breakup 7 June 2000; the D.C. Circuit on 28 June 2001 overturned the breakup and remanded; DOJ settled 1 November 2001; settlement accepted largely 1 November 2002 and approved 30 June 2004. The page records Gates\' deposition as described by BusinessWeek and a source; no personal findings about him.','Wikipedia: United States v. Microsoft Corp. (first ~100,000 characters)',USM,'2026','Case summary (tertiary)',WIKI)],
 [r('The government pursued the company adversely for years; the settlement outcome was a conduct decree. Corporate litigation does not show a personal wealth-power exchange, and Gates\' later philanthropic influence on health policy was not part of this review.','Reviewer scope note',USM,'2026','Explicit limit of evidence',WIKI)],
 'Gates\' foundation, global-health agenda and any post-2008 government relationships were not reviewed here, and no primary filings were opened. Rubric dimensions lack receipts. Narrow review, not exoneration.')

ORT=W+'Amancio_Ortega'
add('amancio-ortega','no-strong',
 'Ortega founded Inditex (Zara). The page read reports honours (Knight Grand Cross, Order of Civil Merit, 2009 decree) and foundation donations to Spanish public health (EUR 17 million 2015; EUR 320 million announced March 2017 for cancer equipment; the page also gives EUR 300 million, and gives inconsistent equipment counts of 440 and over 290), criticised by Podemos (2019 report cited). It describes no formal government agreement, tax, regulatory or commercial benefit.',
 'Philanthropic donations to public health and state honour; no commercial return or preferential benefit shown',
 '2009-2024',
 [r('Honour 2009 (Real Decreto 1976/2009); 2017 AEF philanthropy award; 2015 EUR 17 million to hospitals in Galicia and Andalusia; March 2017 largest donation (EUR 320 million per one paragraph, EUR 300 million per another) to public healthcare systems for cancer machines, radiotherapy machines at public hospitals rising from 20 to 70; criticised by Podemos; a cited May 2019 headline says nearly half the donated machines were idle (headline only). Also 2019 and 2021 stakes in grid companies Enagas, Red Electrica and REN via Pontegadea; November 2024 EUR 100 million fund for Valencia flood victims.','Wikipedia: Amancio Ortega',ORT,'2026','Biographical summary (tertiary)',WIKI)],
 [r('The page lists no Inditex tax, regulatory, labour or government-contract matters; donations to public health are philanthropy, and a government honour does not itself show favour. Grid-company stakes are market purchases in regulated utilities; no preferential terms were described.','Reviewer scope note',ORT,'2026','Explicit limit of evidence',WIKI)],
 'Not read: Spanish government/Ministry of Health donation agreement text, BOE, Inditex filings, tax rulings. Figures conflict within the page itself. Narrow review, not exoneration.')

WF=W+'Walton_family'; RW=W+'Rob_Walton'; AW=W+'Alice_Walton'; JW=W+'Jim_Walton'
add('rob-walton','no-strong',
 'Rob Walton (Walmart heir and former chairman) personally funds Republican political spending according to a Wikipedia summary: over $17.6 million supporting Republican candidates in the 2024 elections and $11 million in the 2026 cycle (as of August 2026). He led the group buying the Denver Broncos ($4.65 billion, agreed 7 June 2022). No public benefit, appointment or contract is linked to him in the page.',
 'Personal political giving; sports-franchise purchase; no preferential public benefit shown',
 '2022-2026',
 [r('Walton spent over $17.6 million supporting Republican candidates in 2024 and $11 million in 2026 (as of August 2026), per the page; ownership group led by Walton agreed to buy the Broncos on 7 June 2022 for $4.65 billion, approved by the NFL 9 August 2022; no government or ambassador role is listed. Figures are not checked against FEC filings.','Wikipedia: Rob Walton',RW,'2026','Biographical summary (tertiary)',WIKI)],
 [r('Political contributions alone do not establish a mechanism. The page shows no linkage between giving and policy outcomes; the stadium page connected the Broncos to Empower Field without linking him to public stadium negotiations. Criticism noted (2010 Democracy Now! video title; 2014 advocacy-site piece) is from advocacy sources.','Reviewer scope note',RW,'2026','Explicit limit of evidence',WIKI)],
 'Walmart lobbying (LDA) and FEC records were not opened (OpenSecrets was blocked). Walmart is a corporate lobbyer; relatives\' and company conduct are not attributed to him. Narrow review, not exoneration.')

add('jim-walton','no-strong',
 'Jim Walton personally gave political money per a Wikipedia summary: 2012 (over $102,500 to Huntsman, then over $202,500 to Romney), 2015-2018 $543,800 to two Illinois charter-school PACs, 2024 $500,000 to oppose an Arkansas school-standards amendment, and $10.7 million supporting Republicans in the 2026 cycle (as of August 2026). A 2008 complaint to the FEC alleged contributions above limits; the page reports no outcome (an allegation).',
 'Personal political and education-policy giving; allegation (2008 FEC complaint) with no recorded outcome',
 '2008-2026',
 [r('2008: about $111,600 mostly to Republicans, and an FEC complaint by Making Change at Walmart alleging exceeding individual limits (outcome not reported on the page); 2012 Huntsman and Romney giving; 2015-2018 $543,800 to charter-school PACs; 2024 $500,000 against the Arkansas Educational Rights Amendment; 2026 $10.7 million (as of August 2026).','Wikipedia: Jim Walton',JW,'2026','Biographical summary (tertiary)',WIKI)],
 [r('Political and education-advocacy donations are lawful participation unless linked to a specific benefit; the page does not describe any such benefit, and the FEC complaint is an unadjudicated allegation in the text read.','Reviewer scope note',JW,'2026','Explicit limit of evidence',WIKI)],
 'FEC, OpenSecrets and LDA records were not opened. Education-policy advocacy was characterised only as political giving, not as a business return. Narrow review, not exoneration.')

add('alice-walton','no-strong',
 'Alice Walton is a Walmart heir and art and health philanthropist. The page reports political giving ($2.6 million to Progress for America in 2004; $200,000 to Restore Our Future by January 2012; $1.4 million to Illinois charter-school PACs 2015-2018 as summarised; $353,400 to the Hillary Victory Fund in 2016) and local public-private projects (airport terminal funding in 1998, Crystal Bridges 2011, a medical school announced 2021). No preferential benefit is shown.',
 'Bipartisan political giving and civic philanthropy; no preferential benefit shown',
 '1998-2025',
 [r('2004: $2.6 million to Progress for America; January 2012: $200,000 to Restore Our Future; 2016: $353,400 to the Hillary Victory Fund; 2015-2018 charter-school PACs. Northwest Arkansas Regional Airport 1998: $15 million initial funding and a $79.5 million bond underwritten by Llama Company; terminal named for her 1999; Crystal Bridges opened 2011 on family land; medical school announced March 2021. Figures not checked against FEC filings.','Wikipedia: Alice Walton',AW,'2026','Biographical summary (tertiary)',WIKI)],
 [r('The page describes no Walmart public-private projects tied to her and no investigation. Philanthropy, naming rights and donations to both parties do not show a preferential benefit. The 1983, 1989 and 1998 personal incidents on the page are unrelated to this question.','Reviewer scope note',AW,'2026','Explicit limit of evidence',WIKI)],
 'Not read: FEC records, airport authority agreements, Walmart LDA filings. Narrow review, not exoneration.')

assert not R
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
out=dict(supersedes=list(P),profiles=P,rubrics=R)
(ROOT/'data/review-batches/039.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
