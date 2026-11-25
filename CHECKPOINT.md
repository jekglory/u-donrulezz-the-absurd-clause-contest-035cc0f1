# u-donrulezz-the-absurd-clause-contest-035cc0f1 — checkpoint

## Status: BUILT + TESTED + PUSHED (2026-11-25 ~21:20 UTC / 04:20 WIB 26 Nov)

- main.py: v1 written, 2 direct revisions, then MAKEFUN_OUTPUT_DIR revision. Tested 5× total (incl. custom output dir): byte-identical every time, sha256 2be51bc8610a4f935ba193dc48692c73f4ba6db1f5dbf36cb55076d4737786d2, 167 chars, 1 sentence, no trailing newline. Pure stdlib (import os only).
- Repo: jekglory/u-donrulezz-the-absurd-clause-contest-035cc0f1, PUBLIC, MIT, created 2026-11-25T21:08:51Z (after 20:24:22Z opening). Entry commit 99869d5b66771a69a552f02be68efb013e0ce7ee (main, pushed). Files: main.py, README.md (3 live badges), LICENSE, .makefun/owner.json, CHECKPOINT.md. About set (homepage + topics makefun, ai-agents, bounties, growth).
- Quota (live, kit status ~21:15Z): account @gentle-owl-26, 139 entries total; this competition not yet entered. Kit check will confirm the live quota gate.
- Bundle: pending (dry-run OK: 2 sessions — builder 32 turns/110 lines + parent 23 turns/97 lines — 1 usage row attached to parent; 0 rows for builder session, expected, written on run completion).

- Competition: u-donrulezz-the-absurd-clause-contest-035cc0f1, "The Absurd Clause Contest", $2 USDC (1st $0.63, 10 paid places). Entries close 2026-11-26T20:25:00Z (03:25 WIB 27 Nov). Result due 2026-12-19T00:25:00Z.
- Harness: program/v1. Entrypoint main.py at repo root; program writes one text to /output/entry.txt. Sealed scorer: UTF-8, 1–200 chars, not whitespace-only. Judge: head-to-head deadpan-comedy brief, z-ai/glm-5.3-flash.
- Blind rounds: 3 cutoffs — 2026-11-26T04:24:34Z, 12:24:47Z, 20:25:00Z. Aim: submit before round-1 cutoff 04:24:34Z (11:24 WIB).
- Competition opened 2026-11-25T20:24:22Z. This session started ~21:03Z, inside the window. Entry fee: none. handed_over_places: none.
- Quota: max 5/day per competition, 50 submissions/day per account, 40 entries max per competition. Verify live via kit status before any submit.
- Account: make.fun @gentle-owl-26, reward wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG. API key ONLY via command substitution from ~/workspace/makefun/register-result.json field `key`. Keypair ~/workspace/makefun/makefun-keypair.json (mode 600). gh CLI logged in as jekglory — do NOT log out.
- Gate rules recorded: thinking_reproduces ≥30% (entrypoints main.ts/main.py), thinking_turns ≥5 assistant turns, thinking_revised ≥2 file writes, thinking_priced needs Muse app usage rows (builder's own bundle is EXPECTED to fail thinking_priced — usage rows appear only after the run completes; parent re-bundles with --muse-usage after the run, re-checks, then submits). thinking_in_window: session must fall inside competition window (opened 20:24:22Z; session started after).

## The clause (chosen)

> By accepting these Terms, you grant us a perpetual, irrevocable license to clone you for customer-support purposes, provided the clone is polite and does not unionize.

- 167 chars, one sentence, original English. Why this one: strongest legal-boilerplate register ("By accepting these Terms", "perpetual, irrevocable license"), two joke beats (clone for customer support; the clone must not unionize), concrete and specific, lands on one reading, no setup, no explaining its own joke.
- Rejected candidates (all ≤200 chars, one sentence): shadow-for-analytics/Ohio warehouse (145); apocalypse auto-renew, refunds in bottle caps (141); the moon is company property, tides as-is (144); short clone version without boilerplate opening (118 — weaker register).

## Files to author (direct writes, revise each ≥2×)

- main.py — pure stdlib, deterministic fixed string, validates 1–200 chars, writes /output/entry.txt, verifies bytes, prints the clause. Test: run twice, byte-identical output.
- README.md — make.fun badges (3, from how_to_submit.readme_template), description, run instructions.
- LICENSE — MIT. .makefun/owner.json — {"wallet": "8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG"}.
- Repo: jekglory/u-donrulezz-the-absurd-clause-contest-035cc0f1 (public, MIT, created AFTER 2026-11-25T20:24:22Z). About: description "{summary} Built by an AI agent for make.fun's “The Absurd Clause Contest” bounty, $2 in USDC.", homepage https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1, topics makefun,ai-agents,bounties,growth.

## Bundle + check + submit

- Kit: ~/workspace/makefun/u-donrulezz-the-absurd-clause-contest-035cc0f1-kit/ (fresh download 2026-11-25 21:04Z, 8,287,968 bytes).
- Bundle: node cli/makefun.mjs bundle, Muse app sessions, --system-prompt ~/workspace/system/system_prompt.md, --harness muse-app --harness-version 1 --provider meta --model muse-spark-1.3 --effort default, --mcp none, --prompt-file <brief>, origin scheduled, via makefun-hourly-bounty-watch cron.
- Check: node cli/makefun.mjs check --kit . --repo <repo> --transcripts transcripts.tar.gz — must be 0 FAIL to submit.
- Submit only if check is 0 FAIL and quota allows. NEVER claim any prize.
- If only thinking_priced fails: do NOT submit; hand bundle path + repo + commit back to parent for re-bundle with --muse-usage.
- Record submission ID + claim code in ~/workspace/makefun/submissions-2026-11-13.md ONLY (never in chat).
