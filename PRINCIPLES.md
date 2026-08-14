# Principles — junior dev in an agentic environment

Source: your own notes, Aug 2026. This file turns each principle into a scheduled, repeating practice so it shapes the program instead of sitting in a doc.

## 1. Ruthless code review as your superpower

**Practice: the weekly adversarial review rep** (Saturdays, 30 min, starting Week 2).
An AI writes a small piece of code on purpose (~30–60 lines: an input validator, a log parser, an auth helper). You review it line-by-line against the four-lens checklist below, write your findings in `REVIEWS.md`, and only then ask the AI to critique its own code — comparing what you caught against what it admits.

Four-lens checklist: **security** (injection, path traversal, secrets, trust boundaries) · **correctness & error handling** (edge cases, failure paths, silent excepts) · **performance** (accidental O(n²), needless work in loops) · **maintainability** (naming, structure, testability).

## 2. Learn through adversarial thinking

**Practice: the "how could this fail / be exploited?" section** in every self-PR description on project repos, starting with flashdown. Two honest sentences minimum before you're allowed to merge your own PR. In security contexts this is the job; here it becomes reflex.

## 3. Do the messy work deliberately

**Practice: debugging stays manual.** The debugger drills (visual + pdb) remain, and every project gets at least one scheduled "break it on purpose, then trace it" session. When something fails in the wild — CI red, hook weirdness, a tool changing under you — that *is* the curriculum, not an interruption; it gets a `LOG.md` entry written as problem → evidence → decision → lesson.

## 4. Master your domain first, coding second

**Practice: the domain thread runs through the projects.** `logwatch` (Phase 3) is explicitly a detection pipeline — parsing, correlation windows, threshold alerts — and the capstone menu keeps an evals/security option. Optional standing slot: 20 minutes of security reading (CVE write-ups, exploit-chain breakdowns) logged in `PATTERNS.md`, at most twice a week, never displacing a block.

## 5. Ask "why," not "how"

**Practice: every study block ends with one written "why" line** in `LOG.md` — why this data structure, why this API shape, why does the language do it this way. And the allowed AI mode during builds is exactly this: ask *why* about your finished code, never *write it for me*.

## 6. Develop a second brain for patterns

**Practice: `PATTERNS.md`.** Every elegant solution you meet (a CodingBat community trick, a stdlib idiom, a beautiful function in source reading) gets three lines: the pattern, where you saw it, when you'd reach for it. Every ugly one you catch in adversarial reps gets the same in `REVIEWS.md`. Reread both during Saturday review — this is the intuition that later makes you dangerous at *prompting and verifying* agents, not just writing code.

## The AI policy, stated once

| Mode | AI's role | Yours |
|---|---|---|
| Problems & study (Blocks A/B) | None. No autocomplete, no assistants. | Recall under mild pressure — the encoding. |
| Builds (Block C) | Reviewer and explainer of *finished* code; answers "why" questions. | Author of every line. |
| Adversarial rep (weekly) | Author, on purpose. | Ruthless reviewer with the four-lens checklist. |

The inversion you wrote is the target state: understand the problem domain better than the implementation, and verify better than you generate.
