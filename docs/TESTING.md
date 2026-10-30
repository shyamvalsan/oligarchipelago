# Testing — spectrum revision, 2026-10-08

## Automated

`node --test tests/*.test.mjs`: 42 tests passed after correcting the launch-cohort GDP expectation from 197 to 199. Syntax checks passed for `app.mjs`, `lib/model.mjs`, `lib/spectrum.mjs`, `lib/readiness.mjs`, `lib/universe.mjs` and `scripts/check-readiness.mjs`.

Coverage includes:
- 500 unique entries, snapshot dates, economic units and missing GDP.
- 500 discovery records, 108 case reviews and 61 estimates as distinct counts.
- The first 200 archive entries form the launch cohort: 94 reviews, 50 estimates, 106 discovery-only and 44 reviewed-but-unplaced entries; 199 GDP matches.
- Launch projection leaves the archive unchanged, filters country options, rejects missing profiles and clears links selecting people outside the cohort.
- Unknown assessments remain null, never zero; all scores recompute from the rubric, with valid range bounds and receipt references.
- Equal quadrant geometry on desktop/mobile, $50B logarithmic midpoint and $500B linear midpoint.
- All 50 local flags, MIT license and matching SHA-256 hashes.
- Sanctions-screen separation, Guryev ambiguity, retained material legal updates.
- Compound and assessment filters, boundary values, sorting, URL state, CSV/HTML escaping and missing-value formatting.

## Browser checks in Chromium

The browser observations below describe earlier 500-entry revisions. The current top-200 projection has automated coverage, but has not yet received a new browser regression. Do not treat historical marker counts as the current launch counts.

The earlier 20-estimate spectrum build was exercised at 1440×1000 and 390×844 in an isolated, temporary loopback preview:
- Default: 20 SVG markers plus 480 unplaced-entry buttons; coverage text states both counts.
- Four equal rectangles: desktop 432.5×270 SVG units, mobile 280×327.5.
- Local flags, continuous gradient and approved quadrant names render.
- Linear mode retains equal quadrants and changes the wealth divider to $500B.
- Economic lens: 492 markers. Taiwan filter: eight entries, zero mapped, all eight available separately.
- Positioned slice: 20 table rows; no categorical mixed/disputed UI labels.
- Search/empty state, shared-link selection, Adani's August 2026 dismissal, rubric and methodology dialog.
- Mobile chart uses its own aspect ratio; profile is full-width and the page has no horizontal overflow.
- No initial-view console errors or warnings.

Earlier builds exercised keyboard selection, overlap access, CSV download generation and a GitHub-style subpath. The current build retains relative runtime URLs; those earlier results are not a full new regression pass or actual GitHub deployment.

## Limits

Tests validate mechanics and preservation of specified updates, not the truth or fairness of editorial judgments. Independent review and most individual assessments remain unfinished. No Lighthouse score, full accessibility/contrast audit, screen-reader audit, cross-browser certification or public deployment is claimed. Dense overlaps remain; search and table provide alternative access.

## Research continuation

Three authored batches now merge into 40 reviewed files and 32 estimates. All 20 automated tests and app syntax checks passed after the additions. New receipts identify page-text versus indexed-excerpt access, and new rubrics cite dimension-specific receipts. The earlier browser counts above describe that tested revision, not current coverage. No publication has occurred.

Earlier 32-estimate browser smoke check: 32 markers, 468 unplaced entries, coverage text 40 reviewed files, Huang selected at 63/100, and expanded receipt access provenance displayed correctly. Equal-quadrant geometry was also rechecked during this continuation.

## Further source review (8 October 2026)

Two additional batches add 12 initial case files and five episode-limited estimates: 52 reviewed files, 37 estimates and 463 unplaced entries (448 discovery-only plus 15 insufficient reviews). Regression checks explicitly preserve failed policy attempts, dropped investigations and uncertain person-level attribution. Earlier browser observations above are not a claim that these latest data additions were browser-tested.

Earlier desktop smoke check after explicit reload: 37 flag markers, 463 unplaced buttons, 52 reviewed files in the coverage header, Daniel Gilbert selected at 56/100 with the new source-backed summary, and no horizontal viewport overflow. All 21 Node tests and three JavaScript syntax checks passed at that revision. No public deployment.

## Family attribution and release coverage check

Batches 006–007 add 12 scoped reviews and one estimate: 64 reviewed files, 38 numerical estimates, 436 discovery-only files and 26 reviewed-but-unplaced files. Regression tests preserve minority ownership, a dismissed proceeding, family-versus-person attribution, reported authority responses and the limits of sanctions judgments.

The read-only `node scripts/check-readiness.mjs` reports no structural errors but fails the research gate, as expected. It reports 436 missing individual reviews and 462 missing numerical placements under the current model. Tests ensure discovery records cannot pass merely by adding scores, and that a legitimately authored zero is distinct from null. This gate checks coverage, not editorial truth, and does not authorize publication.

Earlier desktop check after an explicit cache-bypassing reload at 1440×1000: 38 markers, 462 unplaced buttons and 64 reviewed files in the coverage header. Devasini displays 50/100 and his scoped source-backed summary; Fontbona displays “Insufficient evidence to place” with the new ownership-attribution explanation. Neither selection produced horizontal overflow. The browser window-resize command was unsupported, so no new mobile verification is claimed for this batch. The earlier mobile observations remain historical. All 25 Node tests pass; no public deployment has occurred.

## Shipping review and current mobile smoke test

Batch 008 adds three files and two episode-limited estimates: 67 reviewed, 40 scored, 433 discovery-only and 27 reviewed-but-unplaced. New regression assertions cover the unsuccessful HHLA bid, Aponte’s witness status in the cited 2024 proceeding, the announced ownership transition, and the limits of a UK subsidiary control filing. All 26 Node tests pass.

The old timed preview process was confirmed exited and its port unbound before starting another temporary loopback preview. The browser’s viewport-emulation command worked where window resizing had not. On the current build at 390×844 with touch/mobile emulation: 40 markers, 460 unplaced entries, four equal 280×327.5 SVG-unit quadrants, and no horizontal page overflow. Gianluigi Aponte displays 56/100. Programmatic ArrowRight then Enter moved from his marker to Kuehne and focused the selected details panel; the tooltip closed. The Chromium accessibility snapshot exposes the chart’s marker buttons with names and estimates. These limited checks do not replace screen-reader testing, a touch-target/contrast audit, or cross-browser testing.


## Tax advocacy, historical steel transactions and public-private agreements

Batches 009–010 added six reviews and three positions, reaching 73 reviewed files and 43 estimates. All 28 tests passed at that revision. A cache-bypassing mobile reload at 390×844 showed 43 flag markers, 457 unplaced buttons and the correct coverage counts. Akhmetov's historical 63/100 assessment and the fair-hearing qualification were visible in the profile. The page had no horizontal overflow; all four quadrants remained 280×327.5 SVG units.

Batch 011 adds five reviews and three estimates: 78 reviewed, 46 scored, 422 discovery-only and 32 reviewed-but-unplaced. New assertions preserve Ratcliffe's funding safeguards, Ross's donation chronology, Ofer's unsuccessful attempt to prevent a specific reform, Strnad's framework-versus-order distinction, and the limits of inferring Kerimov's preferential treatment from office-holding. No release or public deployment is implied by these mechanical checks.


Batch 011 passed 29 tests. Its desktop browser check at 1440×1000 showed 46 markers, 454 unplaced entries, Ratcliffe at 50/100, equal 432.5×270 quadrants, no horizontal overflow and no console warnings/errors. The local “Surprise me” implementation was then corrected to include a legitimate score of zero, with a regression covering zero, null, empty and filtered pools (30 tests).

Batch 012 adds three reviews and two estimates: 81 reviewed, 48 scored, 419 discovery-only and 33 reviewed-but-unplaced. A new regression preserves Salim’s historical scope and shared scholarly research base, Vuong’s withdrawn-bid outcome, and the qualifications on claims of Razon’s presidential relationship. The published research gate must still fail; these tests are not editorial certification or publication approval.

After a cache-bypassing reload of batch 012, desktop showed 48 markers and 452 unplaced entries, with Anthoni Salim at 75/100. Mobile emulation at 390×844 then showed Pham Nhat Vuong at 25/100. Both retained equal quadrants (432.5×270 desktop, 280×327.5 mobile), with no horizontal page overflow. No console warnings/errors were listed. All 31 tests and four module syntax checks passed; the read-only readiness command reports no structural errors and the expected unfinished-research blockers.


## Political giving, sports funding and attribution limits

Batch 013 adds five individual reviews and two scoped estimates: 86 reviewed, 50 scored, 414 discovery-only and 36 reviewed-but-unplaced (450 unplaced in total). New checks preserve the distinction between Nike’s tax-method guarantee and a rate freeze, Charlotte’s retained ownership and qualified stadium retention clause, the September 2026 Reshet 13 control-transfer approval, corporate-versus-personal HCA findings, and company-versus-personal Fidelity advocacy. Source access is recorded; the Labor Department’s release was reviewed through its indexed full text after direct retrieval failed. These remain initial editorial assessments, not independent certification.

Batch 013 passed all 32 Node tests and four module syntax checks. The read-only readiness gate reports no structural errors, but correctly fails on 414 missing individual reviews and 450 missing numerical placements. In a new temporary loopback preview (the earlier timer had expired), desktop at 1440×1000 showed 50 flag markers, 450 unplaced entries, 86 reviews in the header and Tepper at 50/100. Mobile at 390×844 showed Blavatnik unplaced with his September 2026 update. Equal quadrants remained 432.5×270 and 280×327.5 respectively, with no horizontal overflow or listed console warnings/errors. These are smoke checks, not final acceptance or public deployment.

## Individual donations, media succession and historical advisory roles

Batch 014 adds four reviews and two scoped estimates: 90 reviewed, 52 scored, 410 discovery-only and 38 reviewed-but-unplaced. Individually named parliamentary donation disclosures support separate Quandt and Klatten cases; each preserves the party's denial, the family's alternative chronology and the subsequent EU emissions target. Mateschitz's ownership is not conflated with his father's authority. Ding's earlier advisory role is qualified by the 2023 delegate-list update and licensing constraints. No personal or corporate sanctions are inferred from these records.

All 33 Node tests and four module syntax checks passed. The read-only readiness gate remains failed for unfinished research, with no structural errors. A cache-bypassing mobile reload at 390×844 showed 52 flag markers, 448 unplaced entries, 90 reviewed files and Klatten at 38/100. Four quadrants remained 280×327.5 SVG units, without horizontal overflow or listed console warnings/errors. No new full desktop regression, independent editorial review or public deployment is claimed for this batch.

## Economic importance, clemency and conditional factory incentives

Batch 015 adds separate reviews for Mong-Koo Chung, Euisun Chung and Jack Ma: 93 reviewed, 54 scored, 407 discovery-only and 39 reviewed-but-unplaced. New assertions preserve the senior Chung's retrial and pardon, the distinction between allegations and adjudicated bribery, the younger Chung's separate identity and conditional incentive package, and Ma's changed voting control. The Korean official pardon announcement was read from its HTML text; indexed-only access is explicitly retained for the SEC disclosure and the AP incentive-update passages.

All 34 Node tests and four module syntax checks passed. The readiness gate has no structural errors but correctly fails unfinished research (407 missing individual reviews and 446 missing numerical positions). No new browser regression or public deployment is claimed for this data-only batch; previous browser observations above describe the tested revisions.

## Access and attribution batch — 2026-10-08

Batch 016 adds James Dyson, Anthony Bamford and Kerry Stokes: 96 reviewed files, 56 numerical estimates, 404 discovery-only records and 40 reviewed-but-unplaced entries. The new regression protects general versus bespoke tax relief, the BBC correction reproduced by Dyson, a joint rather than sole donor attribution, ended parliamentary membership, and Stokes's direct denial of policy discussion. These narrow historical reviews are not comprehensive present-day assessments.

All 35 Node tests and four module syntax checks passed. The readiness gate reports no structural errors and correctly retains the unfinished-research blockers (404 missing case reviews and 444 missing placements). A cache-bypassing mobile reload at 390×844 showed 56 markers, 444 unplaced entries, 96 reviews and Dyson at 38/100. All four quadrants remained 280×327.5 SVG units, with no horizontal overflow or listed console warnings/errors. This is a smoke check, not independent editorial review, final acceptance or publication.

## Stadium financing and company attribution batch — 2026-10-08

Batch 017 adds Jerry Jones, Terrence Pegula, Stanley Kroenke and Anthony Pratt: 100 reviewed files, 58 estimates, 400 discovery-only and 42 reviewed-but-unplaced. The tests retain team versus individual campaign spending, construction versus lifecycle public costs, non-relocation enforcement and overrun obligations, the September 2026 SoFi ruling and its limited procedural scope, and corporate donations that postdate the reviewed recovery grant. The relevant Bills contract sections were read directly; indexed-only and third-party reproduction limitations remain explicit elsewhere.

All 36 Node tests and four module syntax checks passed. Readiness still fails on 400 unfinished reviews and 442 missing positions, with no structural errors. A cache-bypassing mobile reload at 390×844 showed 58 markers, 442 unplaced entries, 100 reviewed files and Kroenke unplaced with the September 2026 update. The four quadrants remained 280×327.5 SVG units, with no horizontal overflow or listed console warnings/errors. No full browser audit, independent editorial review or deployment is claimed.

## Regulatory representation and personal attribution batch — 2026-10-08

Batch 018 adds van der Velde, Hoegner, Colin Huang and Eduardo Saverin: 104 reviewed files, still 58 estimates, 396 discovery-only and 46 reviewed-but-unplaced. None of these narrow reviews establishes all three personal-level dimensions. The regression preserves company versus personal enforcement, legal advocacy versus adjudication, Hoegner's retirement, Huang's historical tax eligibility and voting changes, and proposed legislation versus a finding against Saverin. The official New York settlement and relevant Pinduoduo disclosures were read directly; Saverin's response was reviewed in Reuters' Portuguese republication.

All 37 Node tests and four module syntax checks passed. The read-only readiness gate has no structural errors but correctly fails on 396 missing reviews and 442 unplaced entries. No new browser regression is claimed for this data-only batch; the preceding observations identify the revisions actually tested. Nothing has been deployed.

## State credit and updated sanctions reasons — 2026-10-08

Batch 019 adds Vekselberg and Kantor: 106 reviewed files, 59 estimates, 394 discovery-only and 47 reviewed-but-unplaced. The regression preserves repayable state-arranged credit versus a treasury grant, the absence of disclosed loan pricing, an ended appointment, and the weak rather than established causal connection. Kantor remains unplaced. The UK notice was visually checked to distinguish deleted wording from retained reasons; the separate EU Council delisting and the subject's appeal arguments retain their jurisdiction and procedural limits.

All 38 Node tests and four module syntax checks passed. Readiness reports no structural errors and the expected blockers: 394 missing reviews and 441 missing positions. After the previous temporary preview expired, a new timed loopback preview at a free port showed 59 markers, 441 unplaced entries and 106 reviews at 390×844. Vekselberg displays 44/100; Kantor displays insufficient evidence with the updated notice explanation. The four quadrants remain 280×327.5 SVG units, with no horizontal overflow or listed console warnings/errors. This limited smoke check is not independent editorial review, final acceptance or public deployment.

## Privatization and European industrial policy — 2026-10-08

Batch 020 adds Prokhorov and Lisin: 108 reviewed files, 61 estimates, 392 discovery-only and 47 reviewed-but-unplaced. Prokhorov's historical acquisition is separated from his partner's personal political role and from the later presidential campaign. The scholarly valuation and performance counterarguments remain visible. Lisin's case concerns corporate advocacy, public co-investment and a dated steel-import transition, not proof that he obtained protection from personal sanctions. Matching investment, public employment objectives and uncertain personal direction qualify that estimate.

All 39 Node tests and four module syntax checks passed. Readiness has no structural errors but correctly fails on 392 missing individual reviews and 439 missing positions. The relevant UNU-WIDER and NBER PDF passages were read directly; NLMK's co-investment and quota announcements were also checked. No new browser regression, independent editorial review or public deployment is claimed for this data-only batch.

## Top 200 development checkpoint

All 42 Node tests and six syntax checks passed. No source data or editorial estimates changed in the GDP test correction. The readiness command correctly exits 1 with no structural errors: 106 launch entries still need individual reviews and 150 lack numerical positions. It separately reports the 500-entry archive. Repository publication is for continued development, not a completed research release; GitHub Pages remains a separate deployment step.

## Waves 21–38 (2026-10-29)

Fifteen parallel research waves reviewed the 150 previously unplaced launch entries. All 200 launch entries now have an individual review. Two entries gained estimates (Harold Hamm, Charles Ergen), for 52 launch estimates and 63 in the archive. Two further rubrics (Mukesh Ambani, John Menard Jr.) were deliberately withheld because they rested on partly read or secondhand evidence. Each wave script drops entries already authored in waves 1–20 (41 duplicates), so earlier reviews are retained.

All 42 Node tests and the module syntax checks pass. Counts in the tests were updated; the 2026-10-29 review date is accepted alongside 2026-10-08. A request check of all 202 new receipt URLs found 193 reachable, eight returning 403 (bot blocking or paywalls) and one unreachable (law.com); none was a 404. Reachability does not verify that a page supports the claim. `node scripts/check-readiness.mjs` exits 1 with no structural errors; its single blocker is that 148 entries lack a numerical placement, which must not be fixed by inventing scores.

Waves 36–38 are deeper, primary-source reviews of the Indian billionaires (telecom, conglomerates, pharma/IT/retail), written to replace thinner earlier entries; builders now accept a `supersedes` list in a batch for that purpose. They added five archive reviews (Sunil Mittal, Uday Kotak, Azim Premji, Ravi Jaipuria, Kushal Pal Singh) and re-verified Adani (score 50, with the legal status corrected) and Lakshmi Mittal (56). A proposed Kumar Birla score (31) was withheld because the Supreme Court and CBI documents were not opened. Totals: 219 reviews, 63 estimates in the archive; 200 reviews and 52 estimates in the launch cohort. All 42 tests pass. `docs/SATCOM-SPECTRUM-FACT-SHEET.md`, `docs/CLAIM-REGISTER.md` (generated by `scripts/build-claim-register.py`) and `docs/PRESS-CONTACTS.md` support journalists.
