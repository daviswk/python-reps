# The daily plan system

One markdown file per calendar day lives in this folder, named `YYYY-MM-DD.md`.
Each file is a complete, numbered, step-by-step plan for that day — links included,
no summaries, no guessing.

## Reading your plan

```bash
today              # today's plan in the terminal (alias for: uv run python tools/plan.py)
today --next       # the next planned day (Sunday reading)
today --list 7     # the coming week, one line each
today --open       # open today's file in the editor instead
```

Aliases exist after the container rebuild; the long form always works.

## How new day files appear

Detailed files are generated in batches, one to two weeks ahead, so instructions
never rot (tools change — we learned that the hard way with uv 0.12). At the
Saturday review inside the final written week, paste one line to Claude:

> Generate plan files for Weeks N–M.

No other context needed — the repo, MASTERY_PLAN_V3.md, PRINCIPLES.md, and the scope
doc in the Claude project (`claude/plan-v3-scope.md`) carry it.
The current batch runs through **2026-08-30**; the Aug 29 file schedules the request.

## Day-file format (the contract — every batch must match)

Each day file is **self-contained**: Will should never need another file, or memory of
yesterday, to execute it. Required sections, in order:

1. `# <Day> — Week N, Day N: <title>` + **Today in one line** + **Time** breakdown
2. **Boot-up** — `cd /workspaces/python-reps && git pull` → `today`, phone away
3. One `##` section per block: a **Goal** line, then numbered atomic steps with EXACT
   commands, URLs, file paths, code cells, and commit messages — never "as usual",
   never "like yesterday". Repeat ritual commands verbatim every single day.
   Each block ends with **☑ done when:** one checkable line.
4. **Micro** — Anki (≤10 min cap) + LOG entry + final commit/push
5. **Bail-out plan** — what the day shrinks to when life happens (<90 min weekday, <3h weekend)
6. **Done when** checkboxes · **Log prompt** · **Sources**

The gauntlet line, everywhere it appears:
`uv run ruff format . && uv run ruff check . && uv run mypy . && uv run pytest`

## Editing

These are your files. Reorder a day, split a block, push something to tomorrow —
edit the markdown and commit. The plan bends; the daily habit doesn't.
