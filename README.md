# The Oligarchipelago

**No billionaire is an island.** A static, source-backed atlas of money, economic scale, and wealth–political-power relationships. Built for GitHub Pages with no backend, dependency installation, API keys, analytics, cookies, or runtime third-party requests. Fonts are self-hosted with their OFL licenses.

## What is implemented

- A **top-200 launch cohort** from Forbes' **2026 annual** list, preserving family entries and tied ranks. The full **500-entry archive** is retained in the repository. The app selects the first 200 saved entries, not a handpicked subset of scored people.
- An SVG scatter plot with citizenship-flag markers, a continuous background gradient and four exactly equal quadrants: **Billionaires, Mega-Billionaires, Oligarchs, Mega-Oligarchs**.
- **Economic footprint:** USD net worth / national annual GDP. 199 of the 200 launch entries have GDP matches; Terry Gou remains explicitly unmapped because this World Bank snapshot lacks a matching Taiwan observation. The archive has 492 matches and 8 unmapped entries.
- **Oligarch spectrum (default):** the launch cohort has **94 authored case reviews and 50 numerical editorial estimates**. The chart positions those 50; the other 150 remain available in an expandable list, search, table and profiles. The archive contains 500 discovery records, 108 reviews and 61 estimates. Discovery is not a completed assessment.
- A published three-dimension editorial rubric, source receipts, counterevidence, confidence, historical scope, limitations and plausible editorial ranges. Scores are not objective measurements, probabilities or criminal findings.
- Full-list preliminary UK sanctions-name screening, separate from editorial assessments. A candidate match never automatically sets a verdict.
- Hover/focus tooltips, click/tap profiles, exact-overlap disambiguation, keyboard chart navigation, sortable/paginated table, empty states, and a responsive mobile layout.
- Search plus continent, country/territory, industry, wealth-origin, assessment, GDP, GDP-per-capita, and PPP-per-capita filters.
- Three marker styles (citizenship flags, continent, origin), a random-profile button, URL-encoded filters/selection, share/copy fallback, and filtered CSV export.
- Methodology, source notes, and data limitations in the app itself.

### An important boundary

**This is a working research preview, not a finished ranking.** Of the 200 launch entries, 106 are discovery-only and 44 have reviews that do not support an estimate: 150 remain unplaced. Across the preserved 500-entry archive, 392 are discovery-only and 47 are reviewed but unplaced. Unknowns are not given zero, random positions or a midpoint. Reducing the launch cohort does not resolve missing evidence.

The vertical axis uses 25% political leverage, 25% preferential economic benefit and 50% wealth–power feedback, each authored on a 0–4 scale and rescaled to 100. Individual rationales, source references, counterevidence and editorial ranges appear in profiles. The gradient runs from “Just another billionaire” to “Oligarch”; its endpoints and quadrant names are directional labels, not certificates of innocence or guilt. These AI-assisted judgments are not independently editorially reviewed. Historical cases do not establish current conduct.

Both dividers bisect the plot exactly. The default log wealth axis spans $2.5B–$1T with a $50B midpoint. Linear mode spans $0–$1T with a $500B midpoint. The spectrum midpoint is 50. Flags follow Forbes citizenship, not political allegiance.
Wealth, nationality, inheritance, public office, monopoly findings, media holdings, government contracts and sanctions **alone** are insufficient. The 500-name UK list check is only a narrow research screen; it is not comprehensive sanctions clearance or individual due diligence. Guryev’s father/son ambiguity is retained rather than resolved automatically.

The old equal-weight four-signal pilot is retired. Its archived `data/evidence.json` is not loaded by the app; only the assessment builder reads it to preserve source provenance for the six explicitly scoped reassessments.

## Run locally

From this directory, using Python already installed on your machine:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit `http://127.0.0.1:8000/`. A server is required for JavaScript modules and local JSON fetches; `file://` is not supported. No build step or `npm install` is needed. Use an available port if 8000 is occupied; do not stop another service to free it.

## Test

```sh
node --test tests/*.test.mjs
node --check app.mjs
```

The Node tests cover snapshot integrity, provenance fields, units, missing data, editorial assessments and screening separation, boundary values, filter combinations, sorting, shared URLs, and export escaping. See [testing notes](docs/TESTING.md) for browser checks and limitations.

`node scripts/check-readiness.mjs` is a read-only, offline coverage check. It currently exits **1**, as intended: research is incomplete. Passing the app tests does not mean the project is ready to publish. Even a future passing coverage check cannot certify the judgments, source-reuse rights, accessibility, or user approval.

## Host free on GitHub Pages

The development repository is `shyamvalsan/oligarchipelago`. A public source checkpoint is not a completed research release or a deployed website. GitHub Pages is not enabled by these files.

Before public launch, resolve the editorial and source-reuse items below. Then:

1. Use the public development repository, `shyamvalsan/oligarchipelago`.
2. In that repository, open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Choose the branch containing these files (usually `main`), select **`/ (root)`**, and save.
5. The expected URL is `https://shyamvalsan.github.io/oligarchipelago/` once an explicitly approved deployment completes; it is not currently advertised as live.

The entry point is `index.html`; `.nojekyll` keeps the plain static layout. All app assets use relative paths so a repository subdirectory works. No workflow, custom domain, secret, or paid service is required. Free Pages hosting for public repositories is subject to [GitHub's usage limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

Do not upload `.preview/` if creating a repository by hand; it is excluded by `.gitignore` and may contain local test artifacts.

## Data and maintenance

| File | Purpose |
| --- | --- |
| `data/billionaires.json` | 2026 annual wealth fields + 2024 World Bank economic observations |
| `data/assessments.json` | 500 research records, including 61 estimates, source receipts and limitations |
| `data/cases.json`, `data/additional-cases.json` | Authored case ledgers |
| `data/research-batches/`, `data/research-discovery.json` | Saved discovery queries and unverified candidate links |
| `data/screening.json` | All 500 preliminary name checks and source provenance |
| `data/evidence.json` | Retired pilot archive; not runtime data |
| `scripts/extend-cases.py`, `scripts/build-assessments.py` | Reproduce explicitly authored case ledgers |
| `scripts/build-spectrum.py` | Apply authored rubric decisions and merge discovery audit |
| `scripts/check-readiness.mjs`, `lib/readiness.mjs` | Read-only research-coverage gate; never publishes or grants approval |
| `lib/spectrum.mjs` | Published scoring formula and equal-quadrant geometry |
| `lib/universe.mjs` | Selects the first 200 entries for the app without changing the 500-entry archive |
| `assets/flags/`, `scripts/fetch-flags.py` | Pinned local flag artwork, hashes and MIT license |
| `scripts/screen-uk-list.py` | Narrow UK list candidate matcher; no automatic verdicts |
| `lib/model.mjs` | Pure filtering, metrics, URL state, formatting, and export logic |
| `app.mjs` | UI, SVG rendering, accessibility behavior, and methodology dialogs |
| `styles.css` | Responsive editorial visual system |
| `scripts/refresh-data.py` | Explicit source refresh, standard-library Python only |
| `tests/model.test.mjs` | Dependency-free test suite |

The website never calls Forbes or World Bank at runtime. To deliberately refresh the local snapshot:

```sh
python3 scripts/refresh-data.py
node --test tests/*.test.mjs
```

This command **overwrites `data/billionaires.json`**, not the evidence ledger. It reads public endpoints, validates the data, and writes only after all requests succeed. It stops on unmapped countries or an unexpected list length. Review every resulting diff; remote annual-list records and economic series can be revised after publication. The command is not scheduled and is never run by the website.

The script pins the annual list to 2026 and the economic series to 2024. Update those deliberately, together with UI labels, tests, and documentation—not by silently fetching live wealth.

## Public-launch checklist

- [ ] Review Forbes' terms and permissions for publishing this 500-entry derived snapshot. A public endpoint is not a reuse license. No Forbes photos or biography text are bundled.
- [ ] Complete individual research for the launch cohort's 106 discovery-only entries and broaden its 44 insufficient reviews. Require specific mechanisms, counterevidence and dated citations. The full archive still has 392 discovery-only and 47 insufficient reviews.
- [ ] Independently review and agree on the operational definition, rubric weights, anchors, uncertainty ranges, historical window, company-to-person attribution, and treatment of unknowns.
- [ ] Establish a public corrections process and versioned evidence-review history.
- [ ] Conduct a full accessibility audit and cross-browser check; current checks are not accessibility certification.
- [ ] Enable GitHub Pages only after explicit approval of the public-facing content and deployment plan. Approval to push a development checkpoint is not editorial sign-off.

World Bank data are attributed under CC BY 4.0. Font license notices are under `assets/fonts/`; flag artwork carries its MIT notice and pinned-source hashes under `assets/flags/`. This project does not grant any third-party data or branding rights. It is independent of Forbes and the World Bank.

## Continuing research and publication

The current research additions are authored in `scripts/review-wave-1.py` through `scripts/review-wave-20.py`, producing `data/review-batches/001.json` through `020.json`. Both builders merge these batches. Each new rubric points to specific supporting receipts; receipts state when only an indexed excerpt was accessible. Re-run the corresponding wave script before the case and spectrum builders when editing those authored records.

The user approved a public development checkpoint in `shyamvalsan/oligarchipelago` to continue work from another computer. Website deployment and editorial sign-off remain separate. See [the handoff](docs/HANDOFF.md) for laptop setup, current counts and next steps.

## Updating case files

Edit authored cases in `scripts/build-assessments.py` and `scripts/extend-cases.py`, and rubric decisions in `scripts/build-spectrum.py`. Deliberately rebuild in this order:

```sh
python3 scripts/extend-cases.py
python3 scripts/build-assessments.py
python3 scripts/build-spectrum.py
node --test tests/*.test.mjs
```

These commands overwrite the corresponding local JSON ledgers; they do not fetch or independently validate sources. Review claims, identity, source passages, responses and current legal developments before changing an estimate. Update coverage assertions when adding a case. See [data methodology](docs/DATA.md) for field semantics and limitations.

`scripts/screen-uk-list.py` downloads the official UK list (roughly 50 MB) into memory and overwrites `data/screening.json`; it is never run in the browser. The output preserves the source hash and candidate reasons, not unnecessary personal identifiers. A list refresh must not be used to infer new editorial assessments.
