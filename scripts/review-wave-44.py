"""Wave 44: Blavatnik, Jack Ma, Bechtolsheim, Pinault. Profile-only reviews; supersede thin earlier entries where authored in batches."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,status,summary,mechanism,period,support,counter,limitations,confidence='Low / narrow review'):
 P[id]=dict(status=status,reviewedAt='2026-10-30',reviewDepth='Narrow source-led review under a limited search budget; not independently editorially reviewed; no rubric assigned (dimensions lacking evidence are stated in limitations)',confidence=confidence,period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
FS='Page text reviewed via fetch tool summary'

# Blavatnik
PF='https://www.politifact.com/factchecks/2019/feb/14/facebook-posts/fact-checking-claim-mitch-mcconnells-biggest-donor'
GL='https://en.globes.co.il/en/article-What-does-Len-Blavatnik-want-at-News-13-1001483304'
CT='https://www.calcalistech.com/ctechnews/article/5bojt3sn4'
add('len-blavatnik','mixed',
 'Two strands are documented. First, US political giving: PolitiFact reports that Blavatnik-linked companies (Access Industries, AI-Altep Holdings) gave about $6.3 million, mostly to Republican committees, in the 2015-16 cycle, including $2.5 million to the Senate Leadership Fund, and a further $1 million in 2017. Second, Israeli media: Globes reported in July 2024 on his support for a News 13 CEO appointment, and in September 2026 regulators approved transfer of Reshet 13 control to another vehicle. Neither strand shows a specific preferential benefit received from officials, so no estimate is made.',
 'Political donations in the US and media ownership in Israel; a link to a specific official benefit is not shown in the sources read',
 'US donations 2015-2017; Israeli News 13 episode July 2024; control transfer approval September 2026',
 [r('PolitiFact reports that Blavatnik companies gave McConnell-aligned Senate Leadership Fund $2.5 million in 2015-16 and $1 million in 2017 (total $3.5 million), within over $6.3 million to mostly GOP groups in the 2015-16 cycle. Report is a 2019 fact-check; the underlying FEC records were not opened.','PolitiFact: fact-checking claim on McConnell\'s biggest donor',PF,'2019-02-14','Secondary report of campaign-finance totals',FS+' (first 100,000 of ~129,000 characters read)'),
  r('Globes reports controlling shareholder Blavatnik supported Yulia Shamalov Berkovich\'s appointment as News 13 CEO; interviews canvass political and commercial explanations.','Globes',GL,'2024-07-03','Reported ownership and appointment controversy'),
  r('Ctech reports the Second Authority council approving transfer of Reshet 13 control to the Merit Fund with funding-disclosure and independence conditions.','Ctech',CT,'2026-09-16','Reported regulatory outcome')],
 [r('PolitiFact rated false the claim that he was McConnell\'s biggest donor, noting Sheldon and Miriam Adelson gave $25 million each to the fund in 2017-18, and states no motive or policy benefit tied to Blavatnik\'s gifts.','PolitiFact',PF,'2019-02-14','Explicit limit and rebuttal of an overstated claim',FS),
  r('Globes records former executives denying content interference and associates disputing recent Netanyahu contact; the September 2026 approval concerns a change of control, not proof of full exit.','Globes; Ctech',GL,'2024-07-03','Subject-associated responses; ownership qualification')],
 'Narrow review, not exoneration. Rubric withheld: leverage is only partly shown (donor access, ownership of a news channel), no specific preferential benefit is documented, and the exchange dimension has no receipts. FEC and OpenSecrets records, UK/US Warner Music and Access Industries regulatory matters, and 2019-2026 giving were not opened. Donations are legal and bipartisan reporting (including to Democrats) was not independently verified here.')

# Jack Ma
CNN='https://ktvz.com/money/cnn-business-consumer/2023/07/07/china-fines-jack-mas-ant-group-nearly-1-billion/'
NBC='https://www.nbcnews.com/business/business-news/world-s-biggest-ipo-just-got-suspended-executives-face-questions-n1245940'
add('jack-ma','mixed',
 'The reviewed record is mainly one of state power exercised over Ma\'s companies, not of benefits flowing to him. In November 2020 regulators summoned Ma and two Ant executives and the Shanghai exchange suspended Ant\'s planned listing citing a changed fintech regulatory environment; Alibaba was fined 18.2 billion yuan in April 2021 for monopolistic conduct; Ant was fined about 7.1 billion yuan in July 2023; and Ma ceded control of Ant in January 2023. Earlier access (a February 2025 symposium with Xi) is documented in the prior entry. No preferential benefit linked to public power was found in these sources.',
 'Regulatory leverage over the founder runs against him; no benefit or exchange shown',
 'November 2020 to July 2023; symposium February 2025',
 [r('NBC reports that Ma, Ant executive chairman Eric Jing and CEO Simon Hu were summoned and interviewed by regulators (CSRC statement); the Shanghai Stock Exchange cited changes in the fintech regulatory environment and suspended the STAR listing; Hong Kong listing was then suspended.','NBC News',NBC,'2020-11-03','Reported regulatory action against a founder\'s company'),
  r('CNN reports Ant was fined about 7.1 billion yuan ($994 million) on 7 July 2023 for consumer-protection and governance breaches, that Alibaba was fined a record 18.2 billion yuan in April 2021, and that Ma ceded control of Ant in January 2023.','CNN via KTVZ',CNN,'2023-07-07','Reported enforcement outcomes')],
 [r('The NBC page does not mention Ma\'s October 2020 speech, so the cause of the suspension is not established by it; the official stated reason was the regulatory environment.','NBC News',NBC,'2020-11-03','Explicit limit of evidence',FS),
  r('The CNN article contains no direct comment from Ma and states Ant would comply with the penalty; it records no favourable treatment.','CNN via KTVZ',CNN,'2023-07-07','Counter-evidence: sanctions rather than benefits',FS)],
 'Narrow review, not exoneration. Rubric withheld: leverage and benefit are not both supported (the evidence shows regulators acting against his businesses), and the exchange dimension has no receipts. Earlier-period state support for Alibaba, Ma\'s party ties, and state-investor holdings were not examined. Accounts linking the 2020 speech to the suspension were seen only in search snippets and are not relied on.')

# Bechtolsheim
SECL='https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25955'
SECP='https://www.sec.gov/news/press-release/2024-40'
add('andreas-von-bechtolsheim','no-strong',
 'No evidence of political leverage, a preferential benefit linked to public power, or a wealth-power exchange was found. The one primary-source matter is a securities case: on 26 March 2024 the SEC alleged that Bechtolsheim, then Arista chair, learned of Cisco\'s planned Acacia acquisition on 8 July 2019 and traded Acacia options through accounts of a close relative and an associate, producing $415,726 in profits. He settled without admitting or denying, agreeing to a five-year officer/director bar and a $923,740 penalty. This is an enforcement action against him, not a political mechanism.',
 'No wealth-power mechanism established; securities enforcement matter only',
 'July 2019 conduct; SEC action March 2024',
 [r('SEC litigation release 25955 describes the complaint (N.D. Cal., 5:24-cv-01845), the alleged tips and trades, and the consent judgment terms subject to court approval. The relatives\' accounts hold the trades; the allegation is against Bechtolsheim, and settlement involved no admission.','SEC Litigation Release 25955',SECL,'2024-03-26','Primary regulator document (role-only for this review: no political content)',FS),
  r('SEC press release 2024-40 repeats the allegations with an enforcement official\'s statement and the settlement terms.','SEC Press Release 2024-40',SECP,'2024-03-26','Primary regulator document',FS)],
 [r('Neither SEC document mentions lobbying, political donations, government contracts or officials; the matter concerns trading on non-public information about a private-sector deal.','SEC releases',SECL,'2024-03-26','Scope limit: nothing political in the primary documents',FS)],
 'Narrow review, not exoneration: only SEC materials were read. Donations, lobbying disclosures, Arista government sales, export-control matters and Bechtolsheim\'s other investments were not searched. Entry covers Andreas von Bechtolsheim; the conduct evidenced is his own alleged trading, and no conduct of family members is attributed. Court approval of the judgment was not independently confirmed.')

# Pinault
KF='https://fashionunited.com/news/business/kering-settles-italian-tax-probe-owes-1-25bn-euros/2019051027720'
SA='https://www.staradvertiser.com/?p=821783'
add('francois-pinault','no-strong',
 'No evidence of a political-power mechanism was found. Two documented items: a April 2019 pledge of EUR 100 million to Notre-Dame by the Pinault family through Artemis, and a May 2019 Kering settlement of EUR 1.25 billion with the Italian tax authority (EUR 897 million in additional tax plus penalties and interest) over Gucci in 2011-2017. The tax settlement is a state enforcement outcome against a company chaired by François-Henri Pinault, not a benefit; Kering did not admit wrongdoing.',
 'No mechanism established; charitable pledge and a corporate tax settlement only',
 'April 2019 pledge; Italian tax settlement May 2019 (covering 2011-2017)',
 [r('Kering agreed to pay EUR 897 million in additional tax, EUR 1.25 billion in total, to the Italian Revenue Agency over its Swiss subsidiary LGI and Gucci for 2011-2017; Kering said it was reached in a collaborative spirit and did not admit wrongdoing; Gucci executives were under criminal investigation as legal representatives. Concerns the group chaired by François-Henri Pinault, not François Pinault personally.','FashionUnited (Reuters-based)',KF,'2019-05-10','Context only: corporate enforcement matter',FS),
  r('The Pinault family through Artemis pledged EUR 100 million to rebuild Notre-Dame; statement issued by Francois-Henri Pinault and François Pinault.','Star Advertiser (wire)',SA,'2019-04-15','Context only: charitable pledge')],
 [r('The Notre-Dame article mentions no tax deduction or government favour; the reviewed evidence links neither the gift nor the tax settlement to any official benefit.','Star Advertiser',SA,'2019-04-15','Explicit limit of evidence'),
  r('The Italian settlement shows a government extracting payment from the Kering group; it is counter-evidence to a favourable-treatment narrative within Italy, though French-government dealings were not examined.','FashionUnited',KF,'2019-05-10','Counter-evidence and scope limit',FS)],
 'Narrow review, not exoneration. Family entry: François Pinault and François-Henri Pinault are distinct people and evidence about one is not transferred to the other; most evidence here concerns Kering, chaired by the son. French lobbying disclosures (HATVP), Artemis holdings, media and art-museum ties, and 1990s financing history were not examined. The Italian criminal investigation outcome was not read.')

_ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=_ids
sup=[k for k in P for f in (ROOT/'data/review-batches').glob('0[0-9][0-9].json') if f.name!='044.json' and k in json.loads(f.read_text()).get('profiles',{})]
(ROOT/'data/review-batches/044.json').write_text(json.dumps(dict(supersedes=sorted(set(sup)),profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics; supersedes',sorted(set(sup)))
