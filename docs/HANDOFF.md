# Oligarchipelago development handoff

This checkpoint lets development continue from another computer. It contains the static app, saved data, authored research, reproducible builders and tests. It is not a finished ranking or a deployed GitHub Pages site.

## Continue on a laptop

With Git, Python 3 and a recent Node.js version already available:

```sh
git clone https://github.com/shyamvalsan/oligarchipelago.git
cd oligarchipelago
node --test tests/*.test.mjs
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. There is no build step, package installation, API key or environment file. Choose another available port if needed. To push changes back, authenticate Git with an account authorized to write to the repository.

## Checkpoint status

The user permitted a smaller round launch cohort. The app now uses the first 200 entries in the saved Forbes annual 2026 order; all 500 entries remain in the data archive. Do not select only easy-to-score people.

| Measure | Launch cohort | Archive |
| --- | ---: | ---: |
| Entries | 200 | 500 |
| Initial source-led reviews | 94 | 108 |
| Numerical editorial estimates | 50 | 61 |
| Discovery-only | 106 | 392 |
| Reviewed but unplaced | 44 | 47 |
| GDP matches | 199 | 492 |

All 42 automated tests and six module syntax checks passed. `node scripts/check-readiness.mjs` intentionally exits 1 while research is incomplete; its structural-error list is empty. Earlier browser checks used the 500-entry UI. Recheck the current 200-entry UI before release.

## Next work

1. Verify the current UI on desktop and mobile: 50 spectrum positions, 150 unplaced entries, 199 economic positions, one unmatched Taiwan entry, equal quadrants, filters, hover, overlap selection and profiles.
2. Confirm the editorial model and complete the remaining individual research. The current rubric weights political leverage at 25%, preferential economic benefit at 25%, and wealth–power feedback at 50%. Unknown evidence must stay null, not become zero or a fabricated position.
3. Validate claims, dates, person-versus-company attribution, responses and current legal developments. Existing AI-assisted reviews and plausible ranges are not independent editorial certification.
4. Complete independent editorial review, source-reuse review, corrections/contact arrangements, accessibility and cross-browser checks.
5. Obtain explicit approval before enabling GitHub Pages. The intended future URL is `https://shyamvalsan.github.io/oligarchipelago/`; source publication does not mean the website is live.
6. Recheck the press contacts and prepare personalized outreach only after launch. No email has been sent.

## Research files

Read [DATA.md](DATA.md) for the scoring model and [TESTING.md](TESTING.md) for verification scope. The authored additions live in `scripts/review-wave-1.py` through `scripts/review-wave-20.py`, producing matching files in `data/review-batches/`. Re-run an edited wave script before rebuilding the aggregate ledgers. Builders reproduce decisions; they do not perform source verification.

```sh
python3 scripts/extend-cases.py
python3 scripts/build-assessments.py
python3 scripts/build-spectrum.py
node --test tests/*.test.mjs
node scripts/check-readiness.mjs
```

These builders overwrite generated local ledgers. Review diffs and update both archive and launch coverage assertions when adding cases. Do not run the network refresh scripts merely to start the app. The public-source snapshot and the authored assessments are separate.

Two additional research leads were investigated but are not yet authored into the ledger:

- **Diane Hendricks:** distinguish the filmed 2011 Walker conversation, personal donations and the 2015 right-to-work law. Policy alignment and access alone do not establish a private economic reward or a purchased decision. Start with [WPR's chronology](https://www.wpr.org/politics/years-walker-said-he-wasnt-interested-right-work).
- **Lei Jun:** distinguish a 2021 smartphone-factory approval from electric-vehicle projects and later legislative proposals. Expedited corporate approvals do not by themselves prove personal patronage. Start with the [Beijing planning authority's dated account](https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/gzdt/cp/202106/t20210630_2426351.html) and [Xiaomi's 2021 interim report](https://www.hkexnews.hk/listedco/listconews/sehk/2021/0928/2021092800380.pdf).

## Press outreach after launch

The proposed angle is one consistent test of wealth and political power, including Musk and Indian billionaires, rather than a predetermined accusation. Public professional contact pages identified for later rechecking:

- [Paranjoy Guha Thakurta](https://paranjoy.in/): political economy and corporate power.
- [Indulekha Aravind](https://indulekhaaravind.com/): business and long-form features.
- [Vijay Jadhav](https://vijayjadhav.in/): data journalism and interactive visualization.
- [The Reporters' Collective](https://www.reporters-collective.in/contact): investigative public-interest reporting.

Draft subject: **Who gets called an oligarch? An interactive look at 200 billionaires**

> Hi [Name],
>
> A public exchange about who gets called an oligarch prompted a question: what would happen if we applied the same transparent test to billionaires everywhere, including Elon Musk?
>
> I've built The Oligarchipelago, an interactive look at the Forbes 2026 top 200. Readers can explore wealth and political influence, filter by country and wealth origin, and inspect the evidence, counterarguments and uncertainty behind each assessment.
>
> [After launch, insert the verified live URL and an accurate statement of completed coverage.]
>
> This is an AI-assisted editorial project, not a legal finding or an objective measurement. The methodology and data are open to scrutiny. I thought it might fit your work on [specific relevant beat/story]. Would you be interested in a critical walkthrough or feature? I can share the data, screenshots and methodology.
>
> Best,
> Shyam

This draft is not ready to send until coverage, the live link and claims have been verified. Personalize each pitch; do not send a bulk email or imply independent editorial review has already happened.
