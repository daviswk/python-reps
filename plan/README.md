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

No other context needed — the repo, MASTERY_PLAN_V2.md, and PRINCIPLES.md carry it.
The current batch runs through **2026-08-30**; the Aug 29 file schedules the request.

## Editing

These are your files. Reorder a day, split a block, push something to tomorrow —
edit the markdown and commit. The plan bends; the daily habit doesn't.
