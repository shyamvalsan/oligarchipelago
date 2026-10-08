"""Historical patronage, a withdrawn rail bid, and uncertain political mediation."""
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
STUDY='https://www.researchgate.net/publication/228217616_Using_Organization_Structure_to_Buffer_Political_Ties_in_Emerging_Markets_A_Case_Study'
BOOK='https://web2-bschool.nus.edu.sg/wp-content/uploads/media_rp/publications/Q35HU1431488287.pdf'
add('anthoni-salim-1',
 'Research places Anthoni, not only his father, inside the Salim Group’s historical state–business network. It also describes his efforts to reduce dependence on the Suharto relationship. This is a historical assessment, not an assertion of continuing presidential patronage.',
 'Politically connected ventures and industrial-policy service ↔ protection and support','Suharto-era business relationships and post-1998 restructuring; studies published 2007 and 2012',
 [r('Dieleman and Boddewyn identify Anthony Salim in management roles in ventures with Suharto-family participants. Their case study also cites his explanation that a steel investment served a government industrialization task.','Dieleman & Boddewyn: Organization Studies case study, Tables 2–3',STUDY,'2012','Scholarly person-level attribution','Author manuscript text reviewed'),
  r('Dieleman’s corporate history describes continuing protected licenses and state support during Anthoni’s modernization efforts, rather than treating every benefit as confined to his father’s founding period.','Marleen Dieleman: The Rhythm of Strategy, pp. 124–125',BOOK,'2007','Scholarly historical analysis','PDF text reviewed')],
 [r('The same history describes diversification and professional management intended to reduce reliance on political relationships. New politically connected ventures were a minority of the group’s new partnerships.','Dieleman: modernization and dependence limits',BOOK,'2007','Material counterevidence','PDF text reviewed'),
  r('The manuscript warns that its company-database entries do not necessarily describe still-operating firms or unchanged ownership. Historical board links cannot be presented as current ones.','Dieleman & Boddewyn: Table 2 qualification',STUDY,'2012','Temporal and attribution limit','Author manuscript text reviewed')],
 'The two works share an author and research base, not two wholly independent investigations. Anthoni is also rendered Anthony in the sources. No personal criminal finding is asserted. Group benefits are linked to his documented management role, not inherited guilt; the extent of his individual direction is less certain than the historical network.',
 rubric([3,3,3],[45,90],['Scholarly documentation of his own roles within connected ventures.','Research identifies protective and support arrangements during the period examined.','His reported industrial-policy role links private investment and state objectives; modernization and later restructuring limit extrapolation.'],[[0],[1],[0,1]]))
BID='https://www.marketscreener.com/quote/stock/VINGROUP-6603353/news/Vietnam-to-consider-Vinspeed-proposal-to-build-high-speed-railway-49966016/'
WITHDRAW='https://hk.marketscreener.com/news/vietnam-s-vingroup-to-withdraw-bid-for-67-bln-north-south-high-speed-railway-ce7e59dadf8af620'
VNA='https://en.vietnamplus.vn/vingroup-withdraws-bid-for-northsouth-high-speed-railway-project-post334917.vnp'
add('pham-nhat-vuong',
 'Vuong’s newly established railway company sought unusually favorable public financing and received high-level consideration. But the proposal was withdrawn; a request for a subsidy must not be reported as an awarded or paid benefit.',
 'Owner-founded infrastructure bid → requested public financing, not a completed award','North–South high-speed railway proposal, May–December 2025',
 [r('Reuters links Vuong personally to the newly established VinSpeed and reports a government document welcoming consideration of its bid. The proposal sought state financing for 80% of costs, at zero interest over 35 years.','Reuters: Khanh Vu and Francesco Guarascio',BID,'2025-05-15','Named proposal and official consideration'),
  r('Reuters reports Vingroup’s December withdrawal and concerns raised by the central bank and finance ministry about leverage, guarantees and the subsidy implications of the requested terms.','Reuters: Phuong Nguyen, withdrawal report',WITHDRAW,'2025-12-25','Documented outcome and official reservations')],
 [r('Vietnam News Agency reports the company’s explanation: it wanted to concentrate resources on other assigned projects. This is its stated rationale, not independent proof of why it withdrew.','Vietnam News Agency: withdrawal statement',VNA,'2025-12-25','Subject response as reported by state news agency'),
  r('The December report documents a withdrawn bid, not a loan disbursement. Ministry objections show that initial political welcome did not remove scrutiny of the requested terms.','Reuters: outcome qualification',WITHDRAW,'2025-12-25','Material counterevidence')],
 'Narrow estimate of this proposal only. A zero benefit level means the requested North–South financing was not obtained through this withdrawn bid; it says nothing about other Vingroup land, infrastructure or subsidy arrangements. Formal consideration is not proof Vuong dictated policy, and project cost is not personal income.',
 rubric([2,0,1],[5,60],['A personally linked proposal received documented high-level consideration.','The bid was withdrawn; proposed zero-interest financing is not an awarded benefit.','A concrete attempt to link private investment with favorable public terms, without a completed reinforcing exchange.'],[[0],[1],[0,1]]))
RAZON='https://ph.investing.com/news/stock-market-news/update-2embattled-manila-water-shares-jump-after-tycoon-razon-buys-stake-127012'
MWSS='https://ro.mwss.gov.ph/wp-content/uploads/2022/12/22-002.Rev2_.29Dec22.Preliminary-Rate-Rebasing-Report.pdf'
add('enrique-razon-jr',
 'Razon’s Manila Water purchase occurred during intense presidential pressure on the existing owners. Reporting describes hopes that he could mediate, but explicitly stops short of establishing clear presidential ties. This review cannot turn that market expectation into a proven political favor.',
 'Acquisition during a concession dispute; claimed mediation remains unverified','Manila Water acquisition, February 2020; revised agreement, March 2021',
 [r('Reuters reports his infrastructure firm buying a 25% Manila Water stake while Duterte threatened the concessions. It quotes an investor’s conditional view that a good government relationship could help; that is market interpretation.','Reuters: Neil Jerome Morales',RAZON,'2020-02-03','Transaction and attributed interpretation'),
  r('The regulator-hosted preliminary rate-rebasing report records Manila Water’s revised agreement on 31 March 2021 and identifies Razon’s group as taking over ownership and management.','MWSS Regulatory Office: preliminary rate-rebasing report',MWSS,'2022-12-29','Regulatory consultant account','Indexed PDF passages reviewed; direct retrieval unavailable')],
 [r('Reuters explicitly says Razon had no clear ties to Duterte in its account. It reports a premium to the preceding share price and his explanation emphasizing operating expertise and corporate synergies.','Reuters: qualifications and subject response',RAZON,'2020-02-03','Counterevidence and alternative explanation')],
 'No numerical estimate: the reviewed record establishes investment and subsequent concession arrangements, not personal intervention, preferential terms or a reciprocal bargain. An investor’s conditional speculation is not a finding. The consultant report was accessible only through indexed passages; the contract terms and later outcomes need direct review.')
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
(ROOT/'data/review-batches/012.json').write_text(json.dumps(dict(profiles=P,rubrics=R),ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
