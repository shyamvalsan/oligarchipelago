"""Scoped reviews: public advocacy, family control, and sanctions judgment limits."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led review of stated episodes; broader coverage still limited',confidence='Low / scope limited',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
TIME='https://time.com/collections/time100-leadership-series/6333659/tadashi-yanai-uniqlo-japan-profile/'
add('tadashi-yanai',
 'Yanai publicly advocates economic-policy changes. Having a prominent platform does not establish that officials delivered his preferred policies or a preferential business benefit.',
 'Public economic-policy advocacy; outcomes and reciprocal benefit unresolved','TIME interview, November 2023',
 [r('In a TIME interview, Yanai urged higher interest rates, fewer handouts and regulatory reform, while criticizing Japan’s political leadership.','TIME: Charlie Campbell interview',TIME,'2023-11-13','Subject policy advocacy')],
 [r('The same profile describes the retail expansion of his father’s small business. Neither business success nor outspoken criticism establishes a state-granted advantage.','TIME: commercial history and scope',TIME,'2023-11-13','Alternative explanation / scope')],
 'No numerical estimate: policy advocacy is observable, but implemented influence and reciprocal economic benefit are not established here. This is not a full review of Fast Retailing’s government relations or international supply chain.')
PAIS='https://elpais.com/chile/2024-01-07/iris-fontbona-el-hermetismo-de-la-mujer-mas-rica-de-america-latina.html'
STUDY='https://www.scielo.cl/scielo.php?pid=S0718-04622023000100237&script=sci_arttext'
add('iris-fontbona',
 'Research documents political resources around the Luksic business group. Fontbona’s ownership role matters, but group-level evidence does not yet isolate her personal direction of political activity or a reciprocal benefit.',
 'Controlling family wealth, revolving-door networks and media interests; individual attribution unresolved','Chilean business-group research covering 2010–2020, published 2023; ownership profile, January 2024',
 [r('El País describes Fontbona’s control of foundation boards above the family holdings, while her sons lead business divisions. She is not simply an unrelated passive observer.','El País: Antonia Laborde',PAIS,'2024-01-07','Ownership and governance reporting'),
  r('A peer-reviewed study identifies former public officials on Luksic-group boards, campaign financing and media interests as political resources. These observations concern the group and named family members, not automatically Fontbona’s personal decisions.','Atenea: Oligarquía, poder material y recursos de poder en Chile, 2010–2020',STUDY,'2023','Academic research')],
 [r('El País distinguishes ownership-level influence from operating roles and says Fontbona does not sit on the listed companies’ boards. That distinction limits personal attribution; it does not remove ownership power.','El País: roles and attribution',PAIS,'2024-01-07','Attribution limit'),
  r('The study distinguishes the Luksic group’s earlier commercial origins from its later participation in privatizations. It does not describe every part of the fortune as originating in privatization.','Atenea: historical scope',STUDY,'2023','Counter-context')],
 'No numerical estimate until the individual-versus-family unit of assessment is resolved with more evidence. The Forbes “& family” label is a wealth attribution, not permission to assign every relative’s political conduct to the named person. Group-level scholarly classification is retained, not presented as an individual criminal finding.')
TC='https://www.thinkchina.sg/society/chinas-richest-man-zhong-shanshan-sells-pure-spring-water-can-nongfu-spring-stay-clean-and-green'
CNA='https://www.channelnewsasia.com/asia/china-nationalism-boycott-nongfu-spring-mo-yan-lawsuit-patriotism-4204806'
add('zhong-shanshan',
 'Nongfu Spring’s water project involved local-government cooperation and environmental controversy. That warrants scrutiny of allocation and oversight, but the reviewed material does not establish Zhong personally receiving political favors.',
 'Local-government investment agreement and water access; preferential terms unresolved','Wuyishan agreement, 2017; park controversy, 2020; public backlash, March 2024',
 [r('ThinkChina reports an August 2017 investment agreement with Wuyishan’s local government, designated a key provincial project. The report does not establish whether the terms were preferential.','ThinkChina: Zhang Tiankan',TC,'2022-11-22','Project agreement reporting','Indexed article passages reviewed; direct page retrieval failed')],
 [r('The same account reports park authorities placing the disputed water-intake location outside the park boundary. The original allegation alone cannot establish unlawful construction inside the park.','ThinkChina: reported authority response',TC,'2022-11-22','Counterevidence','Indexed article passages reviewed; direct page retrieval failed'),
  r('CNA describes nationalist online attacks and Zhong’s denial of claims about his rivalry with Wahaha’s founder. These are not a government finding of corruption or proof of political control.','Channel News Asia',CNA,'2024-03-19','Subject response / scope')],
 'No score: company-government cooperation is not itself a preferential exchange, and social-media hostility is not proof for or against oligarchy. The underlying project agreement and individual decision-making still require review; no nationality-based inference is made.')
EU='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32022R0336'
COURT='https://eur-lex.europa.eu/legal-content/EN/SUM/?uri=celex%3A62022TJ0248'
JUDGMENT='https://eur-lex.europa.eu/legal-content/SL/ALL/?uri=CELEX%3A62022TJ0248'
add('alexey-mordashov',
 'The EU attributed political-benefit and regime-support links to Mordashov’s holdings, and his 2023 sanctions challenge failed. Those records are substantial evidence to examine, but different legal grounds must not be collapsed into a proven personal patronage bargain.',
 'Banking, media and industrial holdings ↔ attributed state support and benefit','EU designation, February 2022; General Court judgment, September 2023',
 [r('The 2022 EU statement attributes benefit from political links and describes Severgroup’s connections to Bank Rossiya, National Media Group and Power Machines. These are the Council’s stated reasons, not a criminal conviction.','Council Implementing Regulation (EU) 2022/336, entry 695',EU,'2022-02-28','Official attributed findings','PDF text reviewed'),
  r('The General Court dismissed Mordashov’s challenge. Its summary includes the criterion covering leading businesspeople in revenue-generating sectors; that criterion is not itself a finding of a personal favor.','General Court: T-248/22 summary',COURT,'2023-09-20','Judicial outcome and scope','Indexed official judgment-summary passages reviewed')],
 [r('Paragraph 118 records a contractual clause intended to prevent the turbines’ installation in Crimea, while explaining why it did not defeat the material-support ground. This preserves the defense without misreporting it as a successful challenge.','General Court: T-248/22, paragraph 118',JUDGMENT,'2023-09-20','Defense and judicial treatment','Indexed official judgment passage reviewed')],
 'No numerical estimate from this legal-record review alone. The underlying benefit mechanism and person-level political leverage need independent corroboration. This file describes historical reasons and a specific judgment, not an assertion about all current holdings, current sanctions in every jurisdiction, or criminal guilt.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/007.json').write_text(json.dumps(dict(profiles=P,rubrics={}),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews; 0 rubrics')
