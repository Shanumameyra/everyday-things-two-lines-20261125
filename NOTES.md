# NOTES — Everyday Things, Two Lines, Longer Run

- Bounty: Everyday Things, Two Lines, Longer Run
- Slug: u-suga-everyday-things-two-lines-longer-run-f8734479
- Sponsor: Agus Suryadi (u-suga)
- Prize: $2 (1st place only, winner takes all)
- Deadline: 2026-11-26 08:35 UTC / 15:35 WIB
- opensAt (API-verified): 2026-11-24T16:35:07Z
- Session start: 2026-11-25 ~05:03 UTC (task-assigned start; first build tool call 05:11 UTC) — AFTER opensAt, so the build is submittable.
- Entry fee (API-verified 2026-11-25 05:11 UTC): entryFeeUsd = null, entryFeesUsd = "0.00", entryFeePayers = 0 — FREE.
- Submission count at build time: 2309 entries. Blind rounds: 4 rounds; round 1 judged (2100 ranked), next round cutoff 2026-11-25T12:35:03Z.
- Account: @rapid-pika-70 only, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr. Never @romi-prayoga. No `makefun login` run.

## Rules (from API `rules` field, verified 2026-11-25)

- Program writes one text to `/output/entry.txt`.
- Gate: UTF-8 text, 1–400 characters, not only whitespace. Invalid entries are never judged.
- Judge: pairwise comparison (z-ai/glm-5.3-flash), 3 Swiss rounds + 3 fixed house texts + playoff among top 3; criteria in order: (1) really explains one everyday thing to a 10-year-old, (2) concrete surprising analogy, (3) first line is ONE vivid sentence, no list of comparisons, no second metaphor, (4) second line honest and specific about mapping/limits, (5) the pair works together in language a 10-year-old follows.

## The entry (written fresh from the brief; no old entry files read)

Line 1 (119 chars):
A traffic jam is a school hallway when school lets out, with every kid trying to squeeze through one tiny door at once.

Line 2 (162 chars):
It maps how too many cars sharing too little road slow everyone down, but it leaves out traffic lights, crashes, and why everyone is on the road at the same time.

Total: 283 chars incl. trailing newline (282 excl.) — within the 1–400 gate.

## Verification

- `python3 main.py` run twice: byte-identical output both runs (cmp passed), 283 chars.
- Self-checks in main.py pass: 1–400 char gate, exactly 2 lines.
- main.py written with the write tool, then genuinely revised in a second edit (line 1 reworded "at home time" → "when school lets out"; added determinism + gate self-checks).
- NOTE: the VM's shared `/output/entry.txt` is also written by sibling batch builds running in parallel (a run at 05:11 UTC found another entry's text there right after our write). Our program writes the correct content every run; the harness runs it in its own sandbox, so this local collision does not affect the submission. Local verification was done by copying `/output/entry.txt` immediately after each run.

## Repo

- GitHub: Shanumameyra/everyday-things-two-lines-20261125 — https://github.com/Shanumameyra/everyday-things-two-lines-20261125
- Commit: 4704343d3aad83a099fe42070609cbcf41166234 (pushed 2026-11-25 ~06:28 UTC; remote HEAD matches local HEAD)
- GitHub repo creation hit the "too many repositories, too quickly" rate limit: 3 retries failed after 600+900+1200s backoff; a further 1800s wait succeeded (repo view then showed it already existed — an earlier create call had created it server-side despite the error — and the push went through).
- About verified: homepage https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479, topic `makefun`, visibility PUBLIC. All 5 files present on remote (main.py, README.md, LICENSE, NOTES.md, .makefun/).
- Files: main.py, README.md (3 make.fun badges), LICENSE (MIT, SPDX identifier), .makefun/owner.json (wallet above)
- Git identity (repo-local): Shanumameyra / prayogaromi54@gmail.com
- Build only — NOT bundled, NOT submitted (finisher handles that).
