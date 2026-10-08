"""Historical steel privatizations, with contemporaneous defenses and later judgments."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,levels,bounds,notes,refs):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Moderate / historical scope',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 R[id]=dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
PM='https://hansard.parliament.uk/Commons/2002-02-13/debates/e55e4cc5-f23a-47c2-b515-dcbc201dc943/PrimeMinister'
DEBATE='https://publications.parliament.uk/pa/cm200102/cmhansrd/vo020305/debtext/20305-21.htm'
OPPOSITION='https://publications.parliament.uk/pa/cm200102/cmhansrd/vo020305/debtext/20305-06.htm'
add('lakshmi-mittal',
 'Blair acknowledged signing a supportive letter concerning Mittal’s company amid controversy over a Labour donation and the Sidex acquisition. The political-business overlap is documented; the government disputed both a donation-driven motive and the letter’s effect on the award.',
 'Party donation and diplomatic endorsement ↔ disputed influence on privatization','Sidex acquisition and Blair letter, 2001; parliamentary scrutiny, February–March 2002',
 [r('The March 2002 opposition motion recorded a £125,000 Labour donation and challenged the government’s support for the Sidex transaction. Its accusations were political arguments, not court findings.','UK Parliament: Sidex debate and prime-ministerial response',OPPOSITION,'2002-03-05','Parliamentary debate','Indexed Hansard passages reviewed'),
  r('The minister confirmed that both the letter and donation had been public for months, while rejecting a causal link. This independently establishes the overlap without adopting the opposition’s conclusion.','Hansard: Don Touhig’s response',DEBATE,'2002-03-05','Government acknowledgment and response')],
 [r('Blair said knowing of Mittal’s party support would not have changed his decision. He described the letter as justified by embassy advice and economic reform.','Hansard: Prime Minister',PM,'2002-02-13','Subject response'),
  r('Touhig cited Romania’s prime minister saying the evaluation and award decision preceded the letter. He also argued that privatization would reduce subsidies disadvantaging UK producers. These are attributed government explanations, not independent causal verification.','Hansard: government defense',DEBATE,'2002-03-05','Alternative explanation / disputed chronology')],
 'Historical estimate only, not a claim of present conduct or a purchased contract. Hansard records what speakers asserted; it does not adjudicate those assertions. The underlying Romanian procurement file was not independently audited, and an endorsement is not proof that it changed the winner.',
 [3,2,2],[20,80],['Prime-ministerial endorsement of the company is acknowledged.','A specific privatization interest coincided with political support; causal advantage is disputed.','The donation–endorsement–business sequence is concrete, but a reciprocal bargain is not established.'],[[0,1],[0,1],[0,1]])
AUCTION='https://www.rferl.org/a/1062364.html'
COURT='https://ks.echr.coe.int/documents/d/echr-ks/clin_june_2018_eng'
REUTERS='https://www.business-standard.com/article/reuters/ukrainian-court-revives-case-over-arcelormittal-steel-mill-113060600926_1.html'
EXIT='https://www.euronews.com/2022/07/12/us-urkaine-crisis-akhmetov'
add('rinat-akhmetov',
 'Akhmetov’s participation in the politically connected 2004 steel privatization provides a specific historical wealth–power case. The transaction was reversed, but later European human-rights findings against the reversal process prevent treating it as a simple, unqualified vindication of every accusation.',
 'Ruling-party connections ↔ contested state-asset acquisition','Kryvorizhstal sale, 2004–2005; ECHR ruling, 2018; media-exit statement, 2022',
 [r('Reuters identifies Akhmetov and Pinchuk as buyers in the $800 million 2004 sale, subsequently reversed before an open tender fetched approximately $4.8 billion. It identifies Akhmetov as a key Yanukovich backer.','Reuters: steel-mill litigation report',REUTERS,'2013-06-06','Historical transaction and political relationship','Indexed Reuters article passages reviewed'),
  r('The ECHR’s case-law note describes the acquiring consortium’s owners as linked to the ruling party and presidency. It records the original favorable court decisions, later reopening, return of the purchase money, and resale.','European Court of Human Rights: Information Note 219, pp. 8–10',COURT,'2018-06','Official judicial case summary','PDF text reviewed')],
 [r('The ECHR found a fair-hearing violation in the reopening and reversal proceedings, but no property-rights violation, and rejected the pecuniary-damage claim. The findings concern the consortium’s rights, not a criminal conviction of Akhmetov.','ECHR: case 10640/05 disposition',COURT,'2018-06-26','Material later legal outcome','PDF text reviewed'),
  r('In July 2022, Akhmetov announced his group’s exit from media and surrender of licenses in response to the anti-oligarch law, and rejected the oligarch label. The announcement concerns licenses, not transfer of the entire business to the state.','Reuters: Tom Balmforth, via Euronews',EXIT,'2022-07-12','Subject response / later constraint')],
 'The score concerns a historical acquisition, not ongoing possession of the steel mill, a criminal finding, or membership of a current legal register. A later auction’s price is not an exact measure of the earlier discount. The fair-hearing violation and his response are integral to the assessment; present wartime business conditions need separate review.',
 [3,3,2],[35,85],['Specific ruling-party connections, rather than nationality or wealth alone.','A named contested state-asset acquisition is documented, though later reversed and refunded.','Political connections and acquisition terms support a historical inference; procedural findings and the absence of an adjudicated personal bargain limit certainty.'],[[0,1],[0,1],[0,1]])
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/010.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
