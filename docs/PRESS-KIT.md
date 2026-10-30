# The Oligarchipelago — press kit (draft, 2026-10-29)

**Status: research preview. Not live. Not independently reviewed.** Fill in the live URL and a contact address before sharing. Nothing here has been sent to anyone.

## One paragraph

After Elon Musk said on X on 7 October 2026 that unnamed "oligarchs" were blocking Starlink in India (and, the next day, asked "Is Ambani the real boss of India?"), this project asked a narrower question: if you apply one explicit, published test of wealth–political-power overlap to everyone on the same list, including Musk, what does the evidence show? The Oligarchipelago is an open, static, source-backed atlas of the Forbes 2026 top 200. Every entry has an individual review with cited sources and counter-evidence. Only 52 of 200 have enough evidence to be placed on the chart; the rest are explicitly shown as unplaced, not as clean or guilty.

## Key facts (checkable)

| Fact | Number | Where to check |
| --- | ---: | --- |
| People in the launch cohort (first 200 of Forbes' 2026 annual list, in list order) | 200 | `data/billionaires.json` |
| With an individual authored review | 200 | `docs/CLAIM-REGISTER.md` |
| Placed on the chart (all three rubric dimensions supported) | 52 | `data/assessments.json` |
| Reviewed but unplaced (evidence did not support all three) | 148 | same |
| Archive entries (500 on the Forbes list; not shown in the app) | 500, of which 219 reviewed, 63 placed | same |
| Source receipts across all reviews | 741 | `docs/CLAIM-REGISTER.md` |
| …of which flagged weak or secondary (Wikipedia, snippets, tool summaries, partial reads) | 202 (about 27%) | same |
| Runtime third-party requests, cookies, analytics | none | view source |

## The test

Operational definition: *private wealth and political power materially reinforce one another through preferential access, policy influence, state patronage, or an exchange securing private economic advantage.* Each person is scored on three dimensions (political leverage 25%, preferential economic benefit 25%, wealth–power feedback 50%), each 0–4, with a cited receipt, counter-evidence and a plausible range. If any dimension lacks evidence the person is **not scored**; unknown is never converted to zero or a midpoint. Wealth, nationality, inheritance, office, donations, contracts, company size or sanctions alone earn no points. Full rules: `docs/DATA.md`.

## What it does *not* say

- It does not say who is right about the Starlink licensing delay. India's Ministry of Communications says its framework is fair and non-discriminatory and that Starlink and two other licensed operators are at broadly the same regulatory stage; Reliance says Jio's own satellite services also await clearances. A neutral, dated chronology of the public record is in `docs/SATCOM-SPECTRUM-FACT-SHEET.md`.
- It is not a legal finding, and scores are not probabilities of guilt or measures of corruption.
- Mukesh Ambani and Sunil Mittal are **reviewed but not scored**: no single dated episode supported all three dimensions. That is not exoneration.
- Elon Musk is scored 63 (range 35–90, moderate confidence), scoped to his 2025 government role and a disputed Starlink benefit that senators have asked about and that is not established as a finding.

## Known weaknesses (please read before relying on anything)

1. **AI-assisted, one-pass research.** The reviews were drafted by AI agents under a shared search budget. They have not been independently edited or fact-checked by a human newsroom.
2. **Source quality is uneven.** More than a quarter of receipts are weak or secondary; the register labels each one. Many of the 148 unplaced reviews rest on a single press item or a Wikipedia summary, and some concern a relative or the company rather than the named person.
3. **Family entries.** Forbes lists some wealth as "X & family". Evidence about one member is not transferred to another; reviews say where this limits them.
4. **Primary documents.** The Indian reviews of Gautam Adani and Lakshmi Mittal read court, regulator and Hansard texts directly. Several others (for example the CAG reports, the 2014 coal-block judgment and Election Commission electoral-bond data) could not be opened and are listed as unverified.
5. **Historical vs current.** Each review states its period. A past episode does not establish present conduct.
6. **Source reuse.** Names, ranks and net-worth figures are facts taken from the public Forbes 2026 list, attributed to Forbes, with a retrieval date. No Forbes photos, biographies or other text are bundled, and the project is independent of Forbes. The maintainer's judgement (not legal advice) is that republishing facts with attribution is reasonable; Forbes' terms have not been formally cleared, and the data will be removed or reduced promptly if Forbes objects.

## For journalists: how to check it

- Every receipt, its access level and its URL: `docs/CLAIM-REGISTER.md` (regenerate with `python3 scripts/build-claim-register.py`).
- Rubric, scoring rule and material distinctions retained (for example the Adani legal status): `docs/DATA.md`.
- Tests, including the readiness gate that deliberately fails while evidence is incomplete: `docs/TESTING.md`.
- Everything is plain JSON and static HTML; there is no database and no build step.

## What we are asking

Scrutiny, not endorsement. If you find an error, a missing counter-argument or a misattributed source, please open an issue at https://github.com/shyamvalsan/oligarchipelago/issues (public) or write to **shyam.valsan@gmail.com**. Corrections will be logged in a versioned review history (not yet created).

## Likely questions

- **"Is [X] an oligarch?"** The project does not answer that with a yes/no. It reports what the sources support under a stated test, with a range and confidence.
- **"Why is [X] unscored?"** Because the reviewed evidence did not support all three dimensions. Open the profile to see what was and wasn't found.
- **"Why include Musk?"** Because the same test should apply to the accuser; his entry is on the same footing as everyone else's.
- **"Why India?"** The trigger was an India-specific dispute, and the Indian entries received the deepest primary-source review. That depth is uneven across people and should not be read as a ranking of Indian billionaires against others.
- **"Who funds this?"** Independent and self-funded by the maintainer, Shyam Valsan, as a personal project; no outside funding, sponsor or commissioning organisation. No advertising, analytics or paid services are used.

## Outreach

Contact research is in `docs/PRESS-CONTACTS.md` (only routes the outlets themselves publish, each fetched during research; ~19 verified, 20 unverified). Draft pitches there are marked DRAFT NOT SENT. Personalise each one, send individually, and disclose the AI-assisted nature and the limits above.
