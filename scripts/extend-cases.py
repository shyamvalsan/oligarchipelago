"""Explicit researched additions, separate from automated source discovery."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
C={}
def r(text,source,url,date,kind='Reported evidence'):
 return dict(text=text,source=source,url=url,date=date,kind=kind)
def add(id,period,summary,mechanism,support,counter,limitations,confidence='Moderate'):
 C[id]=dict(status='mixed',reviewedAt='2026-10-08',reviewDepth='Initial source-led assessment; not independently reviewed',period=period,summary=summary,mechanism=mechanism,support=support,counter=counter,limitations=limitations,confidence=confidence)
add('aliko-dangote','Industrial-policy relationships documented through 2025',
 'The reviewed research connects political access and industrial-policy advocacy to protection of business interests. This supports an oligarchic relationship without implying every investment or protection is corrupt.',
 'Policy access ↔ protective industrial policy',
 [r('The World Bank describes Dangote chairing the private-sector side of an industrial-policy council advocating protections and incentives that can tilt competition.','World Bank, Nigeria private-sector diagnostic','https://documents1.worldbank.org/curated/en/099020112132213046/pdf/P176197054acf60380a7cf05e6db6e3df2d.pdf','2022','Institutional research'),r('Research on Nigerian cement describes links between politically connected entrepreneurs, political finance, import licensing and protection.','Journal of Development Studies','https://www.tandfonline.com/doi/full/10.1080/00220388.2025.2456904','2025','Academic analysis')],
 [r('The study also examines industrial-policy performance: protection can support domestic investment. Sector policy and development goals are not themselves a corrupt bargain.','Journal of Development Studies: alternative interpretation','https://www.tandfonline.com/doi/full/10.1080/00220388.2025.2456904','2025','Counterinterpretation')],
 'Policy influence is supported more strongly than a particular illegal transaction. The placement covers the documented relationship, not all 2026 refinery developments.')
add('carlos-slim-helu','Telmex privatization and subsequent historical regulation',
 'Historical research describes political backing and access surrounding a privatized telecom monopoly. The score concerns that historical mechanism, not a claim of unchanged present-day power.',
 'Political backing ↔ privatized monopoly protection',
 [r('The academic account describes Slim backing Salinas, acquiring control in Telmex privatization, and continuing to exercise political connections regarding monopoly practices under Zedillo.','Annales historiques de l’électricité','https://shs.cairn.info/revue-annales-historiques-de-l-electricite-2003-1-page-155?lang=en','2003','Academic historical analysis')],
 [r('Later competition reforms imposed obligations on the predominant telecom operator; historical privilege should not be projected unchanged into the present.','OECD competition peer review: Mexico','https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/07/oecd-peer-reviews-of-competition-law-and-policy-mexico-2020_aee76dc7/62051539-en.pdf','2020','Regulatory counterweight')],
 'Personal access plus a policy-protected asset is the historical rationale. This is not a current market-share estimate or a criminal finding.')
add('charles-koch','Long-running political organization and regulatory agenda',
 'The evidence concerns an organized effort to influence policy aligned with business interests, not simply a political donation or family inheritance.',
 'Business wealth → policy network → business-aligned regulation',
 [r('Academic research describes the Koch network coordinating donors, ideas and advocacy to reshape party agendas over time.','Cambridge: The Koch Network and Republican Party Extremism','https://www.cambridge.org/core/journals/perspectives-on-politics/article/abs/koch-network-and-republican-party-extremism/035F3D872B0CE930AF02D7706DF46EEE','2016','Academic analysis'),r('The chapter examines efforts by Charles and David Koch to limit climate mitigation in connection with fossil-fuel business interests.','Oxford: Billionaires in World Politics, Economy','https://academic.oup.com/book/39712/chapter-abstract/339731935','2020','Academic analysis')],
 [r('Policy advocacy also reflects stated free-market beliefs. Alignment with commercial interests does not show every campaign was a purchased favor or illegal.','TIME: Koch’s business and political philosophy','https://time.com/4072398/charles-koch-good-profit/','2015-10-13','Alternative explanation')],
 'An editorial political-economy interpretation, not a corruption allegation. It applies to Charles’s documented role, not automatically to Julia or other heirs.')
for id in ['gina-rinehart','andrew-forrest']:
 add(id,'Australian mining-tax campaign, 2010',
 'The documented episode links mining wealth, an organized tax campaign and a policy outcome affecting the industry. The personal causal contribution is less certain than the campaign’s existence.',
 'Mining wealth → tax campaign → industry tax treatment',
 [r('Coverage identifies Rinehart and Forrest as prominent opponents of the proposed mining super-profits tax.','ABC Lateline','https://www.abc.net.au/lateline/archive/articles/2010/06/09/s2923085.htm','2010-06-09'),r('The report discusses their campaign and how the reworked tax changed the position of different miners.','Forbes: Australia’s Resource Tax','https://www.forbes.com/2010/07/14/bhp-rio-fortescue-markets-equities-australia.html','2010-07-15')],
 [r('The revised policy affected firms differently; sector-wide democratic lobbying is an alternative to a personalized favor. The account does not prove either individual caused the outcome.','Forbes: scope of policy outcome','https://www.forbes.com/2010/07/14/bhp-rio-fortescue-markets-equities-australia.html','2010-07-15','Limitation')],
 'Historical campaign only. The estimate does not assert bribery, exclusive benefits, or control of the Australian government.')
add('peter-thiel','US political relationships and government-facing business, reported 2026',
 'Political access and government-dependent business overlap, but the reviewed reporting does not establish that contracts were awarded as a reward for support.',
 'Political network ↔ government-facing business; preferential link unresolved',
 [r('Reuters describes Thiel’s political ties and Palantir’s growth through government contracts.','Reuters','https://www.investing.com/news/stock-market-news/palantir-ceo-defends-surveillance-tech-as-us-government-contracts-boost-sales-4480012','2026-02-02')],
 [r('Palantir defended its technology and safeguards. The report establishes business and political connections, not a personal quid pro quo or an improper procurement finding.','Reuters: company response and limits','https://www.investing.com/news/stock-market-news/palantir-ceo-defends-surveillance-tech-as-us-government-contracts-boost-sales-4480012','2026-02-02','Counterevidence / limitation')],
 'Do not read contract value as proof of favoritism. A specific preferential-benefit mechanism requires more evidence.','Low to moderate')
add('jeff-yass','TikTok policy debate and investment exposure, 2024',
 'The reviewed episode creates a plausible link between political access and an investment affected by policy. The alleged influence on Trump’s position was explicitly denied.',
 'Political access → disputed policy protection for an investment',
 [r('Reuters reported a Trump meeting with Yass, whose firm held a ByteDance stake, while Trump argued against a TikTok ban.','Reuters','https://www.investing.com/news/world-news/tiktok-a-us-security-threat-says-trump-similar-to-facebook-cnbc-3332768','2024-03-11')],
 [r('Trump denied changing his position because of Yass. A meeting and parallel financial interests do not themselves establish the cause of a policy change.','AP: TikTok policy and denial','https://apnews.com/article/282d8df7b91dce270316509badd39978','2024-11','Subject response / counterevidence')],
 'This is an assessment of the documented 2024 episode, not the final 2026 ownership arrangement or a finding that policy was bought.','Low')
add('vincent-bollore','Alleged Togo port / campaign exchange; proceedings pending in 2026',
 'A specific alleged exchange connects political campaign services and a port concession. Its causal specificity matters, but the individual criminal allegations remained for trial.',
 'Alleged campaign assistance ↔ port concession',
 [r('The civil-party organization describes charges concerning the Lomé port concession and the referral of Bolloré and former executives for trial. It is a party to the case, not a neutral adjudicator.','Sherpa: case update','https://www.asso-sherpa.org/bollore-togo-referred-criminal-court','2026-03','Party allegation / procedural update')],
 [r('September reporting describes a trial scheduled for December 2026 and Bolloré’s challenge against judges. A rejected plea process is not a completed conviction.','Le Monde','https://www.lemonde.fr/en/france/article/2026/09/01/billionaire-bollore-files-complaint-against-judges-for-criminal-conspiracy-after-order-to-stand-trial-for-corruption_6757048_7.html','2026-09-01','Pending case / defense challenge')],
 'The individual’s liability is not established here. Corporate settlements and relatives’ conduct must not be substituted for personal findings.')
add('bernard-arnault','French political access and corporate policy interests, 2023–2026',
 'Reporting supports substantial access and influence, but commercial size, media ownership and lawful tax deductions do not alone establish a personalized exchange.',
 'Corporate resources ↔ political access; preferential exchange less established',
 [r('Le Monde describes extensive political access and the public cost of tax deductions associated with the Louis Vuitton Foundation.','Le Monde','https://www.lemonde.fr/en/politics/article/2023/08/07/how-bernard-arnault-the-world-s-richest-man-is-expanding-his-empire_6083553_5.html','2023-08-07')],
 [r('The same reporting notes the law was changed to reduce the relevant deduction rate. Lawful access to a general tax measure is not equivalent to a bespoke political favor.','Le Monde: policy limits','https://www.lemonde.fr/en/politics/article/2023/08/07/how-bernard-arnault-the-world-s-richest-man-is-expanding-his-empire_6083553_5.html','2023-08-07','Alternative explanation / constraint')],
 'Access is better documented than reciprocity. Tax benefits and elite meetings should not be treated as corruption findings.','Low to moderate')
(ROOT/'data/additional-cases.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
print(len(C),'additional researched cases')
