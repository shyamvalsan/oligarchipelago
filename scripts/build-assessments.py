"""Rebuild the explicitly authored editorial ledger. No automated verdicts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
profiles={}
def receipt(text,title,url,date,kind): return dict(text=text,source=title,url=url,date=date,kind=kind)
def case(id,status,confidence,period,summary,mechanism,support,counter,limit):
 profiles[id]=dict(status=status,confidence=confidence,reviewedAt='2026-10-08',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limit,reviewDepth='Initial source-led assessment; not independently reviewed')
r=receipt
case('alisher-usmanov','likely','Moderate','Historical relationships; official records checked in 2026',
 'Likely under our definition: official accounts describe political relationships that both sustain power and benefit his business interests.',
 'Political patronage ↔ business benefit',
 [r('US Treasury attributes enrichment to Kremlin ties and alleges financial links to Putin and benefits provided to Medvedev. These are government assertions, not criminal findings.','US Treasury','https://home.treasury.gov/news/press-releases/jy0628','2022-03-03','Official attribution'),r('The UK statement identifies financial or material benefit from Putin, beyond simply operating in a strategic sector.','UK designation RUS0266','https://search-uk-sanctions-list.service.gov.uk/designations/RUS0266/Individual','2026-10-08 snapshot','Official attribution')],
 [r('German prosecutors agreed to end a sanctions probe after a €10m payment, without an admission of guilt. A separate money-laundering investigation had been dropped in 2024. Neither should be presented as a conviction.','AP','https://apnews.com/article/fb34fa24678eb31d4e93f6e6c56443d7','2025-12-30','Case update / counterevidence')],
 'The inference relies on sanctioning authorities’ accounts. Their designation standards differ from proof of corruption, and this is not a criminal verdict.')
case('mikhail-gutseriev','likely','Moderate','Belarus relationships documented in 2021–2025',
 'Likely: the cited records describe business-backed support for an entrenched ruler and economic benefits from that government.',
 'Regime support ↔ access to strategic business',
 [r('The UK describes a longstanding Lukashenko associate providing support through his business interests.','UK FCDO','https://www.gov.uk/government/news/belarus-uk-imposes-significant-new-package-of-economic-sanctions-on-belarus-on-anniversary-of-fraudulent-election','2021-08-09','Official attribution'),r('The reasons include economic benefit or support, business control in energy and extractives, and association with Lukashenko.','UK designation BEL0110','https://search-uk-sanctions-list.service.gov.uk/designations/BEL0110/Individual','2025-04-09; snapshot 2026-10-08','Official attribution')],
 [r('The designation is an administrative measure with alternative grounds, not a court finding of a specific corrupt bargain. Strategic-sector investment alone would not meet our test.','UK statement: scope of evidence','https://search-uk-sanctions-list.service.gov.uk/designations/BEL0110/Individual','2026-10-08 snapshot','Limitation of source')],
 'Independent transaction-level corroboration and a detailed response from the subject remain research gaps. Moderate, not high, confidence.')
case('jay-y-lee','likely','High for historical mechanism','2015 merger / prior bribery case; subsequent pardon and acquittal',
 'Likely on the historical record: a separate bribery conviction establishes an attempted exchange of money for state support of family business control.',
 'Bribes → government support → corporate control',
 [r('Lee was convicted of bribing President Park and her confidante for government support of the merger that strengthened his control of Samsung.','AP: separate bribery case','https://apnews.com/article/ec012d7d7d171971810e27bd76528d86','2025-07-17','Reporting on court finding')],
 [r('He was pardoned in 2022. In July 2025, the Supreme Court finally upheld his acquittal in the separate merger financial-crimes case. This assessment does not allege ongoing bribery.','AP: pardon and final acquittal','https://apnews.com/article/ec012d7d7d171971810e27bd76528d86','2025-07-17','Material counterevidence')],
 'Historical mechanism, not a claim that every act of the merger was criminal or that the conduct continues in 2026. Other Samsung family members do not inherit this assessment.')
case('prajogo-pangestu','likely','Moderate','Soeharto-era wealth formation; not a 2026 conduct finding',
 'Likely on the historical record: World Bank research places him among the beneficiaries of politically allocated timber concessions and privileged finance.',
 'Political loyalty ↔ concessions and subsidized finance',
 [r('The report’s state-capture case study names Prayogo Pangestu among Soeharto associates dominating timber concessions, describing discretionary rights and directed concessional state-bank loans.','World Bank, Combating Corruption in Indonesia, printed p.69 / PDF p.106','https://documents1.worldbank.org/curated/en/548131468774967556/pdf/272460IND.pdf','2003-11-12','Institutional research')],
 [r('This account concerns the New Order forestry system. It does not establish current political control or wrongdoing in today’s energy businesses.','World Bank: historical scope','https://documents1.worldbank.org/curated/en/548131468774967556/pdf/272460IND.pdf','2003-11-12','Limitation of source')],
 'The historical political allocation is stronger evidence than nationality or company size; a present-day feedback relationship still needs research.')
case('vladimir-potanin','likely','Moderate','1995–1997 wealth formation',
 'Likely on the historical record: he helped shape the privatization mechanism from which his business obtained a major state asset.',
 'Policy access → privatization → concentrated ownership',
 [r('Treisman traces the loans-for-shares proposal to Potanin, his acquisition of a Norilsk Nickel stake, and his later deputy-premier role. The paper documents auction restrictions and apparent cronyism.','Daniel Treisman, NBER working paper 15819, pp.10–12,23','https://www.nber.org/system/files/working_papers/w15819/w15819.pdf','2010-03','Academic analysis')],
 [r('The same paper challenges exaggerated underpricing claims and finds subsequent operating improvements; it also describes limits on oligarchs’ political power. This is not evidence that Potanin controlled the government.','Treisman: competing interpretation','https://www.nber.org/system/files/working_papers/w15819/w15819.pdf','2010-03','Counterinterpretation')],
 'A historical editorial inference, not a finding about every subsequent asset or a verified description of his 2026 influence.')
case('roman-abramovich','likely','Moderate','Historical preferential-treatment allegations; legal update 2026',
 'Likely under our definition, based on the UK’s specific account of political access yielding business concessions—not merely his sanctions status.',
 'Political access ↔ preferential business treatment',
 [r('The 2022 UK statement alleged tax concessions, favorable state share transactions and pre-World-Cup contracts linked to preferential treatment by Putin.','UK notice archived by Bermuda Monetary Authority, RUS0270','https://cdn.bma.bm/documents/2022-03-31-11-45-33-Financial-Sanctions-Update.-Russia-Regime.-31-March-2022.pdf','2022-03-31','Official allegations')],
 [r('The General Court rejected his latest sanctions challenge in September 2026, applying business/sector criteria. That decision is not a criminal conviction or independent proof of each alleged favor; a legal appeal remained possible.','EU General Court, T-358/25','https://curia.europa.eu/site/upload/docs/application/pdf/2026-09/cp260124en.pdf','2026-09-09','Court decision / limits')],
 'The specific patronage narrative is an authority’s attribution, disputed through legal challenges. Current screening reasons are not identical to the historical 2022 statement.')
case('mikhail-fridman','mixed','Moderate','2022–2024 disputed designations; UK snapshot 2026',
 'Mixed / disputed: proximity and sector exposure are documented, but a court found the evidence insufficient for important earlier support-or-benefit allegations.',
 'Political proximity; reciprocal benefit contested',
 [r('The UK designation cites Alfa-related financial-sector business. This establishes the authority’s designation rationale, not personal control of public policy.','UK designation RUS0664','https://search-uk-sanctions-list.service.gov.uk/designations/RUS0664/Individual','2026-10-08 snapshot','Official attribution')],
 [r('The General Court annulled listings covering February 2022–March 2023: proximity alone did not sufficiently establish support for, or benefit from, Russian decision-makers. This did not annul every later sanction.','EU General Court','https://curia.europa.eu/site/upload/docs/application/pdf/2024-04/cp240061en.pdf','2024-04-10','Material counterevidence')],
 'Neither “sanctioned therefore oligarch” nor “all sanctions cleared” is a defensible reading. Further individual evidence is needed.')
case('elon-musk','mixed','Moderate','2025 government role and disputed Starlink benefit',
 'Mixed / disputed: unusual public power and private business interests overlap, with a specific allegation of trade leverage benefiting Starlink. That alleged exchange is not established here as a finding.',
 'Public office / trade leverage → alleged private benefit',
 [r('Democratic senators requested an investigation into reports of US trade diplomacy helping Starlink gain foreign approvals. This is a partisan oversight allegation, not an investigation’s conclusion.','US Senate: Warren and colleagues','https://www.warren.senate.gov/newsroom/press-releases/warren-warner-shaheen-lawmakers-push-for-corruption-investigation-into-trump-administration-favors-for-elon-musks-starlink/','2025-05-14','Allegation / investigation request')],
 [r('AP reported his departure from the temporary government role in May 2025. A historical appointment is not current office or proof of a corrupt exchange.','AP','https://apnews.com/article/aa2bc70b0ebdb219b5dd3e9f8fae03af','2025-05-28','Changed circumstances'),r('The lunar-lander procurement documents a major contract, not favoritism. Ordinary government purchasing does not independently meet our definition.','NASA','https://www.nasa.gov/news-release/as-artemis-moves-forward-nasa-picks-spacex-to-land-next-americans-on-moon/','2021-04-16','Alternative explanation')],
 'No adjudicated finding of the alleged Starlink exchange is established by the reviewed sources. These records do not comprehensively assess all political activity.')
case('gautam-adani-1','mixed','Moderate','Alleged 2021 conduct; case updates through September 2026',
 'Mixed / disputed: the alleged power-contract bargain fits our mechanism if true, but allegations are not findings, the civil resolution admitted no liability, and the criminal case was dismissed.',
 'Alleged payments → favorable power-purchase commitments',
 [r('The SEC alleged promises of bribes for above-market energy-purchase commitments. In May 2026 it proposed consent judgments without admitting or denying the allegations.','SEC litigation release 26554','https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26554','2026-05-14','Allegation / civil settlement')],
 [r('A judge dismissed the criminal charges on August 10 at prosecutors’ request. Do not display the 2024 indictment as an ongoing prosecution or conviction.','Reuters','https://www.investing.com/news/world-news/us-judge-dismisses-criminal-case-against-indian-billionaire-adani-4850065','2026-08-10','Material case update'),r('The SEC’s later notice records August 10, 2026 as the civil qualifying judgment date; the May settlement terms did not admit or deny the allegations.','SEC covered-action notice 2026-071','https://www.sec.gov/enforcement-litigation/whistleblower-program/notice-covered-actions/award-claim-2026-071','2026-09-30','Civil judgment update')],
 'The group denied the allegations. Neither dismissal nor a no-admission civil settlement determines the full political-economy question.')
case('rupert-murdoch','mixed','Moderate','UK press / political relationships assessed in 2017',
 'Mixed / disputed: political agenda-setting power is documented, but a specific exchange securing business favors is not established by the reviewed regulator’s account.',
 'Media power → political access; return benefit unresolved',
 [r('Ofcom discusses the Murdoch family’s access to senior politicians and influence over the political agenda.','Ofcom public-interest report, §§8.30–8.37','https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/623244/Public_Interest_Test_report_-_non_confidential_-_For_publication.pdf','2017-06','Regulatory analysis')],
 [r('Ofcom cautions that frequent meetings do not themselves prove influence over decisions, and that the degree of influence is difficult to evidence.','Ofcom: evidential limits','https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/623244/Public_Interest_Test_report_-_non_confidential_-_For_publication.pdf','2017-06','Counterevidence / limitation')],
 'This historical UK review is not a current global account of the family’s media control. Media ownership alone is insufficient.')
case('jeff-bezos','mixed','Low','2024 endorsement controversy',
 'Mixed / disputed: overlapping media ownership and government-facing business create a plausible conflict, but the claimed exchange is not established.',
 'Media decisions ↔ government-facing business: disputed link',
 [r('AP reported the Washington Post’s non-endorsement decision alongside a meeting between Blue Origin executives and Trump. Timing raises a question, not proof of a bargain.','AP','https://apnews.com/article/51de8348502aa17f432504c4764c63f5','2024-10-25','Reporting / circumstantial evidence')],
 [r('Bezos denied that the non-endorsement involved a quid pro quo and said he had not known of the Blue Origin meeting beforehand.','AP: Bezos’s response','https://apnews.com/article/07d752d987dbb64b68da63d9ac37b7e8','2024-10-28','Subject response')],
 'Low confidence: temporal coincidence, media ownership and public contracts cannot establish oligarchy on their own.')
# A deliberately narrow reconsideration of the six other original pilot dossiers.
# These are NOT comprehensive negative background checks.
old=json.loads((ROOT/'data/evidence.json').read_text())
for id in ['michael-bloomberg','larry-page','sergey-brin','mark-zuckerberg','larry-ellison','mukesh-ambani']:
 signals=list(old['profiles'][id]['signals'].values())
 support=[r(s['text'],s['source'],s['url'],s['date'],'Scoped source review') for s in signals]
 case(id,'no-strong','Low / narrow review','Only the listed original-pilot records',
  'No strong evidence in these reviewed sources—not a clean bill of health. The original pilot documented connections, not a demonstrated wealth–political-power exchange.',
  'Reciprocal political-economic mechanism not established in this file',support,
  [r('This record establishes a role, corporate connection or company-level fact. It does not by itself establish political favoritism benefiting this individual. Other evidence could change the assessment.',signals[0]['source'],signals[0]['url'],signals[0]['date'],'Limitation, not exoneration')],
  'Not a comprehensive investigation. Donations, lobbying, preferential regulation, informal influence and newer developments require further research. Low confidence applies to the negative assessment.')
profiles.update(json.loads((ROOT/'data/additional-cases.json').read_text()))
reviewed_ids=set()
for path in sorted((ROOT/'data/review-batches').glob('*.json')):
 additions=json.loads(path.read_text())['profiles']
 assert not reviewed_ids.intersection(additions), f'Duplicate authored review: {path}'
 reviewed_ids.update(additions)
 profiles.update(additions)
ledger=dict(version='0.2-editorial-assessments',reviewedAt='2026-10-08',definition='A billionaire whose wealth and political power materially reinforce one another through preferential access, policy influence, state patronage, or a documented exchange securing private economic advantage.',method='Case-based editorial assessment, not a numerical corruption score. Historical and disputed evidence is labeled. Wealth, nationality, inheritance, office, monopoly, donations, contracts or sanctions alone do not determine a verdict.',limitations='Initial research, AI-assisted and not independently editorially reviewed. Coverage is uneven and mostly unassessed. Historical evidence does not establish ongoing 2026 conduct. Narrow source checks must not be treated as exoneration.',profiles=profiles)
known={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(profiles)<=known
(ROOT/'data/cases.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(len(profiles),'case files')
