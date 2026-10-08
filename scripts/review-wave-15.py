"""Economic importance and clemency, conditional incentives, and changed control."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
def r(text,source,url,date,kind='Reported evidence',access='Page text reviewed'):
 return dict(text=text,source=source,url=url,date=date,kind=kind,access=access)
def add(id,summary,mechanism,period,support,counter,limitations,decision=None):
 P[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Source-led historical episode review; not independently editorially reviewed',confidence='Moderate / episode limited' if decision else 'Low / attribution unresolved',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations)
 if decision:R[id]=decision
def rubric(levels,bounds,notes,refs):return dict(levels=levels,range=bounds,rationales=notes,sourceRefs=refs)
APPEAL='https://www.taipeitimes.com/News/worldbiz/archives/2007/09/07/2003377640'
RETRIAL='https://www.koreatimes.co.kr/southkorea/20080603/hyundai-motor-chief-gets-suspended-jail-term'
PARDON='https://www.korea.kr/news/policyNewsView.do?newsId=148656123'
FOLLOWUP='https://www.koreajoongangdaily.com/korea/pardons-granted-to-tycoons-and-pols/11448575'
add('mong-koo-chung',
 'The historical record explicitly links leniency toward Chung to Hyundai’s economic importance. His conviction, suspended sentence and subsequent presidential pardon must all remain visible. The influence assessment concerns protection of an economically powerful business leader, not an assertion of a purchased judgment.',
 'Corporate economic importance → judicial leniency and presidential clemency',
 'Hyundai embezzlement proceedings and clemency, 2007–2008',
 [r('AP reports the September 2007 appeals court suspending Chung’s prison sentence while explicitly invoking the economic risks of jailing Hyundai’s leader. Chung had asked to continue contributing through the company.','Associated Press, republished by Taipei Times',APPEAL,'2007-09-07','Reported judicial reasoning and personal appeal'),
  r('The Justice Ministry’s August 2008 announcement names Chung among 74 business figures included in the amnesty. It cites business-sector requests, investment, overseas expansion and job creation as reasons for including recently convicted conglomerate leaders.','South Korean Ministry of Justice: amnesty announcement',PARDON,'2008-08-12','Primary clemency decision and stated rationale','Korean article text retrieved and reviewed from the official HTML page'),
  r('The June 2008 retrial again imposed a three-year sentence suspended for five years, with physical community service. The Supreme Court’s intervention concerned the form of the earlier community-service order, not a reported acquittal.','The Korea Times / Park Si-soo: retrial outcome',RETRIAL,'2008-06-03','Reported intervening legal outcome')],
 [r('The retrial report says the judge found the funds mainly served company promotion and international-event bids rather than personal interests. Prosecutorial allegations about political donations are not treated here as separate adjudicated bribery findings.','The Korea Times: sentencing qualification',RETRIAL,'2008-06-03','Material distinction between findings and allegations'),
  r('The August report records the pardon’s effect on the remaining community-service obligation and the government’s economic-revival defense. The broader amnesty also included many people who were not conglomerate leaders.','Korea JoongAng Daily: pardon and government response',FOLLOWUP,'2008-08-12','Outcome, response and breadth of policy')],
 'Historical, episode-limited estimate. Clemency is not a cash subsidy, and the inference concerns private leadership protected through arguments about national economic dependence. No bribery of the judges or president is established by these receipts. The original court judgments were not directly reviewed; legal outcomes are supported by contemporaneous court reporting and the official pardon announcement. Nothing is transferred to his son’s assessment.',
 rubric([3,3,3],[45,90],['Reported judicial reasoning and the official amnesty rationale give substantial support to economic-importance leverage.','Sentence suspension and clemency provided concrete personal protection, not proof of a financial grant.','The stated expectation of renewed business investment and employment links favorable treatment to private economic power.'],[[0,1],[1,2],[0,1]]))
KEMP='https://gov.georgia.gov/press-releases/2022-10-25/gov-kemp-hyundai-motor-group-execs-break-ground-georgias-bryan-county'
INCENTIVES='https://www.gpb.org/news/2022/07/25/hyundai-gets-18b-in-aid-build-electric-cars-in-georgia'
UPDATE='https://www.wabe.org/higher-investment-means-hyundai-could-get-2-1-billion-in-aid-to-make-electric-cars-in-georgia/'
SON='https://www.taipeitimes.com/News/front/archives/2007/02/06/2003347862'
add('euisun-chung',
 'Euisun Chung publicly represented Hyundai’s Georgia factory partnership, which came with a large conditional incentive package. This is a documented company–government bargain, but it does not prove corruption or that he personally received the package’s value. His father’s criminal case is not his conviction.',
 'Private factory investment and employment commitments ↔ public incentives',
 'Georgia EV-factory agreement in 2022 and amended package in September 2023',
 [r('Georgia’s governor records Euisun Chung personally joining the October 2022 groundbreaking and speaking for Hyundai’s partnership with the state. This supplies individual executive attribution, not just a family connection.','Governor of Georgia: groundbreaking announcement',KEMP,'2022-10-25','Primary person-level role in public-private project'),
  r('AP reports the signed 2022 agreement offering an estimated $1.8 billion in tax breaks and other incentives in exchange for factory investment and jobs. The package includes several types of public support, not one cash payment.','Associated Press, republished by Georgia Public Broadcasting',INCENTIVES,'2022-07-25','Reported signed agreement and economic benefit'),
  r('AP’s September 2023 update reports a projected $2.1 billion package following increased investment and job commitments. The earlier $1.8 billion figure is therefore the original deal, not an unchanged lifetime total.','Associated Press, republished by WABE: amended incentives',UPDATE,'2023-09-13','Material update to the announced package','Indexed AP article passages reviewed; direct WABE article retrieval failed')],
 [r('The 2022 account describes partial repayment if investment or employment falls below 80% of commitments, along with payments in lieu of local taxes. Officials defend the deal through expected jobs and payroll.','Associated Press / GPB: conditions and government defense',INCENTIVES,'2022-07-25','Material contractual conditions and alternative explanation'),
  r('Reporting on Mong-Koo Chung’s 2007 case explicitly says the younger Eui-sun did not face trial in that proceeding. It cannot be imported as Euisun’s conviction.','Associated Press / Taipei Times: separate-person qualification',SON,'2007-02-06','Personal attribution boundary')],
 'Scoped to the Georgia incentive bargain, not all Hyundai activities or later US tariff negotiations. Public support benefits a company and project; it is not the executive’s personal income. The reviewed reports do not establish that Euisun personally dictated every term, that all projected incentives were disbursed, or that the bargain was illegitimate. Competitive investment recruitment and public employment benefits are substantial alternative explanations.',
 rubric([2,2,2],[20,75],['His documented executive role connects him to the partnership; personal control of public decisions is not demonstrated.','A specific large incentive agreement benefits the company, with investment, employment and repayment conditions.','An explicit investment-for-incentives relationship, not proof of exclusive political patronage or illicit exchange.'],[[0,1],[1,2],[0,1,2]]))
ALIPAY='https://www.sec.gov/Archives/edgar/data/1577552/000119312523190974/d517168dex991.pdf'
MEETING='https://www.voanews.com/a/china-s-xi-holds-rare-meeting-with-business-leaders-amid-slowing-economy-us-tensions/7977476.html'
CONTROL='https://www.marketscreener.com/business-leaders/JACK-MA-204/news/Ant-Group-says-Jack-Ma-relinquishes-control-of-company-42677058/'
add('jack-ma',
 'Ma’s government access and role in a regulated payments business are documented. But licensing, ownership changes and attendance at a leaders’ meeting do not by themselves establish a preferential political exchange. The record also changes materially over time, including relinquished Ant voting control.',
 'Regulated-business ownership and high-level access; preferential exchange unresolved',
 '2011 Alipay restructuring, Ant voting changes in January 2023 and Xi symposium in February 2025',
 [r('Alibaba’s SEC-hosted disclosure describes Alipay’s divestment and licensing in 2011, after which Ma held a substantial majority equity interest in its parent. This is the issuer’s account of regulatory compliance, not a regulator’s finding of a special favor.','Alibaba: major shareholders and related-party transactions',ALIPAY,'2023','Primary issuer disclosure of historical restructuring','Indexed disclosure passages reviewed; direct SEC PDF retrieval failed'),
  r('Reuters reports Ma attending Xi’s February 2025 private-business symposium, drawing on state-media coverage. The meeting included other business leaders and was framed around support for private enterprise.','Reuters, republished by VOA: business symposium',MEETING,'2025-02-17','Reported high-level access with source attribution')],
 [r('Reuters reports Ant’s January 2023 announcement that Ma no longer controlled the company after voting-rights changes. Earlier majority voting power must not be presented as unchanged current control.','Reuters: Yingzhi Yang and Brenda Goh, Ant governance change',CONTROL,'2023-01-07','Material control update')],
 'No numerical estimate: company size, a license and attendance at a group meeting do not establish private policy capture. A majority economic interest in the historical restructuring is distinct from later voting arrangements. The narrow indexed filing review is not a comprehensive assessment of subsidies, state investors or Ma’s political relationships, and loss of formal control does not prove absence of influence.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/015.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
