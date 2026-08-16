# Python → ML → Safety — Plan v3

**Scope locked Aug 16, 2026 · Week 1 begins Mon Aug 17, 2026 · Week 36 ends Apr 25, 2027**
**Budget: 4h/day Mon–Fri + 6h/day Sat–Sun = 32h/week (~1,150 hrs). Scheduled load ≈ 30h; the ~2h gap is the anti-fragility buffer, on purpose.**
**Goal: Anthropic-fellowship-ready research engineering skills, via a Zero-to-Hero ladder where every phase's output is the next phase's prerequisite.**

This file is the skeleton. Daily instructions live in `plan/` and print via `today`. The scope contract (what's in, out, and parked) lives in the Claude project: `claude/plan-v3-scope.md`. V2 is retired.

---

## What changed from v2, and why

1. **Budget doubled.** v2 assumed 2–2.5h/day. v3 schedules 4h weekdays / 6h weekends, with block structure to match.
2. **Math, stats, and ML are in from Day 1.** v2 deferred all of it to week 25. v3 front-loads a 6-week math/stats/pandas runway so the fall course's prereqs (calc, linear algebra, prob/stats, regression, Python data handling) are green before the quarter starts.
3. **The fall course is now the ML core.** Weeks ~7–16 sync to the 10-week syllabus (ML workflow → data management → evaluation → unsupervised → supervised → RL → end-to-end evaluation). Homework is submitted via GitHub anyway — every assignment doubles as portfolio.
4. **CodingBat is out** (fence). Exercism carries concepts now; NeetCode carries patterns from the course era onward.
5. **Karpathy Zero-to-Hero is the deep-learning arc** (weeks ~17–27), not a someday. ARENA is parked with a trigger: it activates the week Karpathy finishes.
6. **Fellowship application prep is parked with a trigger:** a 15-minute window check on the first Saturday of each month; the track activates when a window opens.
7. **The systems stay.** `today` engine, Sunday re-solve queue, Saturday review, three-mode AI policy, MISTAKES/PATTERNS/REVIEWS, gauntlet-green commits. Anki joins them, capped at 10 min/day.

## The daily engine (unchanged)

- `today` → today's numbered plan · `today --next` · `today --list 7` · `today --open`
- Day files generated just-in-time, 2 weeks per batch, at the Saturday review inside the final written week: tell Claude *"Generate plan files for Weeks N–M."* The repo, this skeleton, and the scope doc carry all context.

## Block shapes

**Weekdays (4h):**

| Block | Time | Content by phase |
|---|---|---|
| A — Problems | 60m | Exercism (P1) → NeetCode (P2–3) → maintenance (P4) |
| B — Math | 60m | Math Academy daily XP (P1–2) → tapers to 30m (P3–4) |
| C — Applied | 60m | Stats/pandas notebooks (P1) → course + homework (P2) → Karpathy (P3) → capstone/ARENA (P4) |
| D — Build/Study | 45m | Learn Git (W1–2) → builds ladder → infra (W20+) |
| Micro | 15m | Anki ≤10m + one LOG line |

On class days in P2, the class itself replaces Blocks C+D.

**Saturday (6h):** Long build/apply block (2h) · adversarial review rep (45m) · problems (1h) · Math Academy (1h) · Saturday review ritual (45m) · monthly fellowship-window check (15m, first Sat).
**Sunday (~4.5h scheduled):** Re-solve queue (1h) · weekly safety paper + note (1h) · Math Academy (1h) · polish/get-ahead (45m) · next-week preview (30m) · Anki (10m). Remaining ~1.5h is **banked recovery** — spend it only on catch-up, else it's free time.

## Phase map

| Phase | Weeks | Dates | Active tracks (≤4 hour-consuming) | Ships / gates |
|---|---|---|---|---|
| 1 — Runway | 1–6 | Aug 17–Sep 27 | Exercism · Math Academy · stats/pandas notebooks · git→flashdown | Git done (W2) · runway notebooks 01–06 · **prereq gauntlet green (W6)** |
| 2 — Course core | 7–16 | Sep 28–Dec 6* | Course+companion · NeetCode (from W8) · MA maintenance · repolens (weekends) | flashdown v1.0 (W7) · Exercism syllabus done (~W10) · midterm (~W11) · repolens v1.0 (W15) · final + course portfolio (W16) |
| 3 — Deep learning | 17–27 | Dec 7–Feb 21 | Karpathy Z2H · NeetCode finish · logwatch (weekends) · Docker (W20+, weekends) | Karpathy units 1–9 · logwatch v1.0 (W24) · **NeetCode 150 + Karpathy complete (~W27)** |
| 4 — Frontier | 28–36 | Feb 22–Apr 25 | ARENA (trigger fired) · capstone · K8s/AWS (light, weekends) · app prep (when window opens) | capstone scoped (W28) · ships with README-grade writeup (W35) · polished profile + retrospective (W36) |

*Buffer weeks (sacred, half-load): **W15** (Thanksgiving), **W19** (holidays), **W30** (breather).*

**\*Assumption to confirm:** fall quarter starts ~Sep 28 (W7). When the real syllabus lands, say so at any Saturday review — course-era weeks reflow; the W6 runway gate does not move. If the course starts later, W7 becomes consolidation (flashdown v1.0 + stats depth), not idle.

## Milestone ribbon (the visible-wins line)

W2 git ✓ → W6 gauntlet ✓ → W7 flashdown v1.0 → W10 Exercism done → W11 midterm → W15 repolens v1.0 → W16 course final + portfolio → W24 logwatch v1.0 → W27 NeetCode 150 + Karpathy done → W35 capstone ships → W36 retro + what's next.

## Phase details

### Phase 1 — Runway (W1–6): earn the course
- **Exercism** (Block A): one concept exercise/day down the syllabus tree + practice exercises; solve on site → skim community solutions → re-type from memory into `exercism/` with type hints + asserts → commit.
- **Math Academy** (Block B): Day 1 diagnostic places you; then daily ~60 XP. It adapts — that's the point. (Paid, ~$49/mo: it is the math spine, budget for it.)
- **Stats/pandas notebooks** (Block C), one per week, each building on the last: 01 NumPy + randomness → 02 pandas + descriptive stats + CLT → 03 probability rules/Bayes in simulation → 04 distributions + hypothesis tests → 05 linear regression (statsmodels) → 06 logistic regression + gauntlet prep. Home: `notebooks/`, authored in Colab, saved to GitHub.
- **Block D:** finish Learn Git ch 4–11 (W1–2), then **flashdown**: a CLI that parses MISTAKES.md into Anki-importable decks — the build dogfoods the review system.
- **W6 gate — prereq gauntlet (pass ≥4/5):** multiply a 2×3·3×2 by hand · take ∂/∂x of x²y + eˣ · explain a confidence interval to a non-stats friend in one sentence · fresh CSV → load/groupby/plot in under 20 min · fit + interpret linear and logistic regressions on an unseen dataset.

### Phase 2 — Course core (W7–16): the course is the curriculum
- Course homework **outranks everything in its week.** Sat long block = homework block.
- **Companion reps** (Block C alongside lectures): reimplement each week's method minimally — PCA and k-means from scratch in NumPy (course wks 4–5), one decision tree by hand + sklearn forests (wks 6–7), a tiny NumPy neural net (pre-Karpathy warmup), a bandit/gridworld for RL week.
- **NeetCode** starts W8, ~5/wk (Block A), patterns in roadmap order. Exercism syllabus wraps ~W10; after that Exercism is weekend variety only.
- **repolens** (weekends): analyzer for your own repos — commit cadence, test coverage trend, TODO debt. v1.0 by W15.

### Phase 3 — Deep learning (W17–27): Karpathy, properly
- One Z2H unit ≈ 1–1.5 weeks at 4h/day: micrograd → makemore 1–5 → build GPT → tokenizer → reproduce GPT-2. Method: watch in chunks, rebuild from memory, do the exercises, commit each unit's repo dir.
- **NeetCode** rises to ~8/wk; finish 150 by ~W27.
- **logwatch** (weekends): log-anomaly detection pipeline — parse auth logs, engineer features, train the detector with course-learned evaluation discipline. Safety-flavored by design. v1.0 W24.
- **Docker** (W20+, weekend Block D only): boot.dev course; containerize logwatch as the exercise.

### Phase 4 — Frontier (W28–36): prove it
- **Trigger check, W27–28:** Karpathy done → **ARENA activates** (transformers → interp chapters; skip what Z2H already covered).
- **Capstone** scoped at W28 from a shortlist you'll have earned: small interp experiment on your own nanoGPT · an eval harness for a failure mode from the paper shelf · extend logwatch into a monitoring/eval tool. Ship W35 with README-grade writeup (in-repo — public blogging stays out of scope).
- **K8s/AWS** (weekends, light): boot.dev courses; deploy something real once, then stop.
- **App prep** activates whenever the monthly window check fires — research statement drafts pull from LOG.md, papers/notes.md, and shipped repos.

## Rules v3 (the ten that survived)

1. **Three-mode AI policy.** Problems/study: no AI, no autocomplete (repo settings enforce). Builds: AI reviews finished code, never writes. Weekly adversarial rep: AI writes on purpose; you tear it down with the four-lens checklist → REVIEWS.md.
2. Struggle ~15 min before hints. Discomfort is the mechanism; it's a ladder, not hazing.
3. Any solution you didn't produce cleanly: close it, re-type from memory.
4. MISTAKES.md gets every stumble · PATTERNS.md every elegant find · REVIEWS.md every adversarial teardown.
5. Sunday re-solve queue, from memory. Anki ≤10 min/day — two spaced systems, one hard cap.
6. Commit every session; conventional commits; gauntlet (ruff · mypy strict · pytest) stays green.
7. One build at a time. Shiny ideas → SOMEDAY.md.
8. Every study block ends with one written "why is it built this way" line in LOG.md.
9. Ship on the listed week, imperfect and tagged. Buffer weeks are sacred — half-load, no guilt.
10. Never fake the streak. (Stuck on a loop? Paste it into pythontutor.com and watch it run — that's not cheating, that's instrumentation.)

## Weekly safety paper — starter shelf (easy → hard, swap freely at Sunday pick)

1. Anthropic, *Core Views on AI Safety* (W1)
2. Amodei et al., *Concrete Problems in AI Safety* (W2)
3. Bai et al., *Constitutional AI* (W3–4)
4. Ouyang et al., *InstructGPT* (W5–6)
5. Vaswani et al., *Attention Is All You Need* (save for W17+, pairs with GPT-from-scratch)
6. Elhage et al., *A Mathematical Framework for Transformer Circuits* (W25+)
7. Elhage et al., *Toy Models of Superposition* (W28+)
8. One recent Anthropic alignment paper of your choice (W30+)

Notes live in `papers/notes.md`, five lines each: claim · why it matters · one question · one connection · next paper.

## Sources shelf → where each one lives

boot.dev Learn Git (P1, W1–2) · Learn Git 2 (SOMEDAY) · Docker (P3, W20+) · Kubernetes + AWS (P4) · Exercism (P1–2, Block A) · NeetCode roadmap (P2–3, Block A) · Math Academy (P1–4, Block B) · Colab (P1–2 notebook home) · Karpathy Zero-to-Hero (P3) · ARENA (P4, on trigger) · pythontutor (debugging aid, any phase) · Codewars / PracticePython / 30-Days-of-Python (nice-to-have variety shelf — never scheduled) · GitHub (everything ships there).
