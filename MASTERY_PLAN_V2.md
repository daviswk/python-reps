# Python Mastery — Plan v2

**Restarted Friday, Aug 14, 2026 · Week 1 begins Monday, Aug 17 · Week 36 ends April 25, 2027**

This file is the *skeleton*: phases, rules, and rhythm. The *muscle* — your detailed, step-by-step daily instructions — lives in `plan/` and is served by the `today` command. You should almost never need to open this file on a normal day.

---

## What changed from v1, and why

1. **Daily plans are now code in the repo.** One markdown file per calendar day in `plan/`, printed by `uv run python tools/plan.py` (aliased to `today` and `plan` after the container rebuild). No summaries, no asking anyone what to do — open the terminal, type `today`, follow the numbers.
2. **Timed closed-book gauntlets are retired.** Measurement now comes from completion with instant feedback: CodingBat modules finished, boot.dev chapters passed, gauntlet-green commits, courses certificated. Pressure-testing can return in Phase 3 — only if and when you want it.
3. **CodingBat replaces the early drill/assessment layer.** All eight modules — Warmup-1, Warmup-2, String-1, String-2, List-1, List-2, Logic-1, Logic-2 (~85–90 short problems) — solved on the site for instant feedback, then **re-typed from memory into this repo with type hints and asserts**. Solve = feedback; re-type = encoding; repo = portfolio. That's the active-encoding loop you asked for.
4. **Git is now a curriculum, not a drill.** boot.dev's *Learn Git* (11 chapters: Setup, Repositories, Internals, Config, Branching, Merge, Rebase, Reset, Remote, GitHub, Gitignore) runs natively in the codespace via the bootdev CLI, scheduled across Weeks 0–2. *Learn Git 2* (Fork, Reflog, Merge Conflicts, Rebase Conflicts, Squash, Stash, Revert, Cherry Pick, Bisect, Worktrees, Tags) is the optional Saturday track from Week 4.
5. **Exercism and NeetCode stay.** Exercism resumes in Week 3 (deliberately paused for two weeks so CodingBat can build the base without overload). NeetCode 150 remains the Phase 2–3 problem engine, unchanged.
6. **The junior-dev-in-an-agentic-world principles are woven in** — see `PRINCIPLES.md` for the full mapping. Headlines: a weekly *adversarial review rep* (an AI writes code; you tear it apart line-by-line with a four-lens checklist), self-PRs gain a "how could this fail / be exploited" section, and a `PATTERNS.md` second-brain joins `MISTAKES.md`.
7. **Gentler on-ramp.** Fluent Python now starts end of Week 2 instead of Day 8, mini-builds precede flashdown, and no day asks for more than ~2–2.5 focused hours.

## The daily engine

- `today` → prints today's plan file, numbered steps, links included.
- `today --next` → the next planned day (for Sunday reading).
- `today --list 7` → the coming week at a glance.
- `today --open` → opens the file in the editor instead.

**Generation cadence (important):** detailed day files exist through **Aug 30** right now. At each Saturday review, when you're inside the final week of written plans, paste one line to Claude — *"Generate plan files for Weeks N–M"* — attach nothing; the repo and this skeleton carry the context. Why just-in-time instead of all 36 weeks up front: detailed instructions written months ahead rot (the uv 0.12 incident was exactly this), and the plan should bend to what the previous weeks revealed. The skeleton below is the contract; the day files are its fresh implementation.

## Blocks and the rules, v2

Weekday shape (~2–2.5h): **A — Problems** (30–40m: CodingBat now, Exercism from W3, NeetCode from W8) · **B — Study** (40–50m: Mon/Wed/Fri = git course, then Fluent Python; Tue/Thu = Effective Python items) · **C — Build** (45–60m: mini-builds, then flashdown → repolens → logwatch → capstone). Saturday ~3h long block + rituals. Sunday ~45–60m: re-type-from-memory queue + read next week.

The rules that survived, sharpened:

1. **AI policy, three modes.** Problems and study: no AI, no autocomplete (the practice repo's settings enforce it). Builds: AI may *review* your finished code and answer "why" questions — it never writes. Weekly adversarial rep: AI *writes on purpose*, and you verify ruthlessly. Reviewing machine output line-by-line is a first-class skill now, so we train it deliberately.
2. Sit with a stuck problem ~15 minutes before hints; discomfort is the mechanism, but this is a ladder, not a hazing.
3. After any solution you didn't produce cleanly: close it, re-type from scratch. Reading ≠ learning.
4. `MISTAKES.md` gets every stumble; `PATTERNS.md` gets every elegant thing you meet (yours or found); `REVIEWS.md` gets adversarial-rep findings.
5. Sunday's queue: re-type 5 recent solutions from memory. Encoding through recall, without a stopwatch.
6. Commit every session; conventional commits; the gauntlet (ruff, mypy strict, pytest) stays green.
7. One project deep at a time; shiny ideas go to `SOMEDAY.md`.
8. Ask *why*, not just *how* — every study block ends with one written "why is it built this way" line in `LOG.md`.
9. Ship on schedule, imperfect and public.
10. Never fake the streak; the graph reflects reality or it reflects nothing.

## Phase map v2

| Phase | Weeks | Dates | Problem engine | Study | Ships |
|---|---|---|---|---|---|
| 0 — Restart | — | Aug 14–16 | CodingBat Warmup-1 | Learn Git ch 1–3, bootdev CLI live | v2 system installed |
| 1 — Foundations | 1–7 | Aug 17–Oct 4 | CodingBat all 8 modules → Exercism (W3+) | Learn Git done (W2), EP items 1–39, FP ch 1–6 | `flashdown` v1.0 (W6–7) |
| 2 — Patterns | 8–16 | Oct 5–Dec 6 | NeetCode ~75 by pattern | FP ch 7–14, EP continues, Learn Git 2 (opt.) | `repolens` v1.0 |
| 3 — Engineering | 17–24 | Dec 7–Jan 31 | NeetCode finish | FP ch 15–21 + concurrency, EP done, source reading | `logwatch` v1.0 (security-flavored detection pipeline) |
| 4 — Research eng. | 25–36 | Feb 1–Apr 25 | Maintenance + agent-collab reps | Karpathy zero-to-hero, ARENA, capstone | Capstone + writeup + polished profile |

Boundaries are contracts; day files implement them freshly each batch. Buffer/consolidation weeks: 16 (Thanksgiving), 20 (holidays), 30.

## Measurement without stopwatches

Progress is visible, not timed: CodingBat modules completed (8 total), Learn Git chapters passed (11 + optional 11), Exercism exercises archived, NeetCode problems solved and re-typed, projects tagged v1.0, gauntlet-green weeks, and — the one that compounds — the Sunday re-type queue done from memory. If you ever *want* friendly pressure tests later, they'll be opt-in and we'll design them together.

## Sources shelf

boot.dev Learn Git — https://www.boot.dev/courses/learn-git · Learn Git 2 — https://www.boot.dev/courses/learn-git-2 · bootdev CLI — https://github.com/bootdotdev/bootdev · CodingBat Python — https://codingbat.com/python · Exercism — https://exercism.org/tracks/python · NeetCode roadmap — https://neetcode.io/roadmap · *Effective Python* 3e (items by number) · *Fluent Python* 2e (chapters) · Karpathy Zero to Hero — https://karpathy.ai/zero-to-hero.html · ARENA — https://www.arena.education · Python docs — https://docs.python.org/3/
