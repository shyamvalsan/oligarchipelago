"""Historical privatization and corporate policy influence, with distinct attribution."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,levels,bounds,notes,refs):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Moderate / historical episode' if id=='mikhail-prokhorov' else 'Low / personal direction uncertain',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
WIDER='https://www.wider.unu.edu/sites/default/files/wp2010-63.pdf'
NBER='https://www.nber.org/papers/w15819.pdf'
NY='https://www.newyorker.com/magazine/2012/02/27/the-master-and-mikhail'
REUTERS='https://www.themoscowtimes.com/archive/candidate-prokhorov-says-putin-must-change'
add('mikhail-prokhorov',
 'Prokhorov’s role in the bank-led acquisition of Norilsk links his historical wealth formation to a politically structured privatization process. The reviewed scholarship supports that mechanism while disputing simplistic claims about asset values and economic damage. Potanin’s separate political role is not automatically Prokhorov’s.',
 'Bank participation in state financing → acquisition of privatized industrial equity',
 'Norilsk acquisition during 1990s privatization; scholarly reassessments in 2010 and personal responses in 2012',
 [r('Szelényi identifies Prokhorov as the bank’s board chairman and describes him working with Potanin to acquire Norilsk Nickel through it. The account also credits his subsequent management and restructuring.','Iván Szelényi / UNU-WIDER, Working Paper 2010/63',WIDER,'2010-05','Scholarly person-level acquisition account','PDF printed page 21 reviewed directly'),
  r('Treisman describes state share tranches pledged for budget loans, followed by sales after non-repayment, often to the creditors themselves. He finds that auction competition was restricted; Norilsk is among the transactions studied.','Daniel Treisman / NBER, Working Paper 15819',NBER,'2010-03','Scholarly account of the financing and allocation mechanism','PDF abstract and printed pages 2 and 8 reviewed directly'),
  r('The New Yorker’s interview-based profile identifies both partners as beneficiaries of the Norilsk transaction. Prokhorov describes a division of labor: he favored technical operations, while Potanin handled politics and lobbying.','Julia Ioffe / The New Yorker: The Master and Mikhail',NY,'2012-02','Individual participation and subject’s attribution boundary')],
 [r('Treisman challenges the scale of supposed underpricing and later economic damage, despite criticizing execution. His Norilsk discount estimates depend on contemporaneous market valuations; a later company valuation is not the price of the original stake.','Daniel Treisman / NBER: valuation and performance qualifications',NBER,'2010-03','Material competing economic interpretation','PDF abstract and printed pages 2 and 8 reviewed directly'),
  r('In a Reuters interview during his presidential campaign, Prokhorov denied being a Kremlin instrument and called for democratic reform. These are his stated positions, not independent proof of either political control or independence.','Reuters, republished by The Moscow Times',REUTERS,'2012-01-18','Direct subject response and later political context')],
 'Historical editorial assessment, not an allegation of a present-day crime or a comprehensive 2026 political profile. Bank-level participation and personal benefit are documented more clearly than his individual design of the rules. The later campaign is not evidence that the earlier acquisition was an election payment. The score does not treat all privatization, later growth, or Potanin’s conduct as Prokhorov’s misconduct.',
 [2,3,3],[40,85],
 ['His senior bank role places him inside the transaction; the reviewed interview assigns political lobbying more directly to his partner.','The literature links his acquisition to a restricted state-asset allocation process, while valuation and performance interpretations differ.','The loan-and-equity mechanism directly connects private finance, a government decision and personal industrial ownership; it is not proof of an individual criminal bargain.'],
 [[0,2],[0,1],[0,1]])
ROLE='https://www.euronews.com/2022/03/08/uk-ukraine-crisis-russia-nlmk'
JV='https://nlmk.com/en/media-center/press-releases/nlmk-group-and-belgian-sogepa-sign-agreement-on-joint-execution-of-nlmk-belgium-holdings-development/'
DISCLOSE='https://disclose.ngo/en/article/how-an-oligarch-with-links-to-the-russian-weapons-industry-is-shielded-from-eu-sanctions'
BELGA='https://www.brusselstimes.com/belgium/308584/sanctions-will-not-hurt-walloon-branches-of-russian-company-nlmk-for-now/'
QUOTA='https://eu.nlmk.com/en/media-center/news-groups/nlmk-belgium-holdings-slab-quota-decision-creates-a-platform-for-transformation/'
add('vladimir-lisin',
 'Lisin’s NLMK had a public co-investor and benefited from a phased steel-import restriction. The evidence supports a limited corporate economic-influence interpretation, not proof that Lisin personally bought an exemption or that his absence from a particular sanctions list was a favor.',
 'Public co-investment and employment interests → support for a steel-import transition',
 'NLMK’s 2019 co-investment agreement and European steel-import policy in 2022–2023',
 [r('Reuters identifies Lisin as NLMK’s chairman and main shareholder in March 2022. That connects him to the company but does not identify him as the author of every lobbying decision.','Reuters / Euronews: Lisin’s employee letter',ROLE,'2022-03-08','Individual company role'),
  r('NLMK’s 2019 announcement records 49% stakes for both NLMK and SOGEPA in Belgium Holdings, with each agreeing to invest €100 million over 2019–2021 and provide financing guarantees on equal terms.','NLMK Group: joint development agreement',JV,'2019-10-10','Primary public-private corporate arrangement'),
  r('Disclose reports NLMK warning European governments about job losses from sanctions, and its Walloon public investor later advocating protection of European operations. These are company-level interventions, not documented personal instructions from Lisin.','Disclose / Antoine Harari and Clément Fayol',DISCLOSE,'2022-12-13','Reported corporate advocacy and public-investor alignment'),
  r('Belga reports the Walloon economy minister explaining that a two-year transition would protect NLMK activity temporarily and that the government would discuss its situation with the Commission.','The Brussels Times with Belga',BELGA,'2022-10-18','Contemporaneous government explanation of policy benefit'),
  r('In December 2023, NLMK Belgium Holdings welcomed extension of the slab-import transition to September 2028, with progressively reduced volumes. This is the company’s dated account of policy relief, not a personal cash payment.','NLMK Belgium Holdings: slab quota statement',QUOTA,'2023-12-18','Primary company acknowledgment of economic benefit')],
 [r('The 2019 agreement requires matching private investment and guarantees. Public equity participation is not the same as an unconditional grant to Lisin.','NLMK Group: matching obligations',JV,'2019-10-10','Material financing distinction'),
  r('The minister defended local employment and industrial activity while supporting European sanctions. These public objectives can explain a transition without a corrupt bargain.','The Brussels Times with Belga: public-purpose rationale',BELGA,'2022-10-18','Material alternative explanation'),
  r('Disclose explicitly says it could not establish which states had proposed or opposed personal sanctions against Lisin, or whether that question was raised. A steel-product transition does not prove political protection from personal designation.','Disclose: limit on personal-sanctions inference',DISCLOSE,'2022-12-13','Explicit evidential boundary'),
  r('The company describes the extra time as enabling alternative supply and industrial transformation, with declining import allowances. Its claimed job and investment benefits are not an independent outcome audit.','NLMK Belgium Holdings: stated transition rationale',QUOTA,'2023-12-18','Company response and limits of claimed public benefit')],
 'A narrow corporate-policy assessment, not a sanctions-compliance opinion or complete review of his Russian business history. The evidence of Lisin’s personal direction remains limited; the feedback dimension is therefore weak. The 2023 statement is not verification of the rules applicable to any trade in 2026. No conclusion about disputed military end use or shipping conduct is drawn, and nationality, public ownership or a sanctions label alone does not determine the score.',
 [2,2,1],[10,65],
 ['The company and public co-investor advocated a policy affecting their operations; personal direction is less clear than corporate alignment.','A phased import restriction preserves company supply temporarily, with declining volumes and a stated transition purpose.','Public and private industrial interests align, but the record does not establish Lisin personally securing an exchange or a personal-sanctions waiver.'],
 [[0,1,2,3],[3,4],[1,2,3,4]])
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/020.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
