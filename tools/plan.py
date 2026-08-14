"""Print the day's study plan from the plan/ directory.

Usage (from the repo root):
    uv run python tools/plan.py              # today's plan
    uv run python tools/plan.py --next       # next planned day on or after today
    uv run python tools/plan.py --list 7     # the coming week at a glance
    uv run python tools/plan.py -d 2026-08-17
    uv run python tools/plan.py --open       # open in the editor instead

After the container rebuild, `today` and `plan` are shell aliases for this.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLAN_DIR = REPO_ROOT / "plan"
HORIZON_DAYS = 120


def plan_path(plan_dir: Path, day: date) -> Path:
    """Return the expected plan file path for a given day."""
    return plan_dir / f"{day.isoformat()}.md"


def next_plan(plan_dir: Path, start: date, horizon: int = HORIZON_DAYS) -> Path | None:
    """Return the first existing plan file on or after start, or None."""
    for offset in range(horizon):
        candidate = plan_path(plan_dir, start + timedelta(days=offset))
        if candidate.exists():
            return candidate
    return None


def upcoming(plan_dir: Path, start: date, count: int) -> list[Path]:
    """Return up to count existing plan files on or after start."""
    found: list[Path] = []
    for offset in range(HORIZON_DAYS):
        candidate = plan_path(plan_dir, start + timedelta(days=offset))
        if candidate.exists():
            found.append(candidate)
            if len(found) >= count:
                break
    return found


def first_line(path: Path) -> str:
    """Return the first non-empty line of a file, stripped of markdown #."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            return line.lstrip("# ").strip()
    return path.stem


def show(path: Path, open_in_editor: bool) -> int:
    """Print a plan file to stdout, or open it in the editor."""
    if open_in_editor and shutil.which("code"):
        subprocess.run(["code", "-r", str(path)], check=False)
        return 0
    banner = "=" * 72
    try:
        print(banner)
        print(f"  {path.stem}  ·  {path.relative_to(REPO_ROOT)}")
        print(banner)
        print(path.read_text(encoding="utf-8"))
    except BrokenPipeError:
        sys.stderr.close()
    return 0


def main(argv: list[str] | None = None) -> int:
    """Entry point."""
    parser = argparse.ArgumentParser(description="Show the day's study plan.")
    parser.add_argument("-d", "--date", help="ISO date, e.g. 2026-08-17")
    parser.add_argument("--next", action="store_true", help="next planned day")
    parser.add_argument("--list", type=int, metavar="N", help="list the next N planned days")
    parser.add_argument("--open", action="store_true", help="open in editor instead of printing")
    args = parser.parse_args(argv)

    if not PLAN_DIR.is_dir():
        print(f"No plan/ directory found at {PLAN_DIR}", file=sys.stderr)
        return 1

    start = date.fromisoformat(args.date) if args.date else date.today()

    if args.list:
        for path in upcoming(PLAN_DIR, start, args.list):
            print(f"{path.stem}  ·  {first_line(path)}")
        return 0

    target: Path | None
    if args.next:
        target = next_plan(PLAN_DIR, start + timedelta(days=1))
    else:
        candidate = plan_path(PLAN_DIR, start)
        target = candidate if candidate.exists() else None

    if target is None:
        upcoming_file = next_plan(PLAN_DIR, start)
        print(f"No plan file for {start.isoformat()}.")
        if upcoming_file is not None:
            print(f"Next planned day: {upcoming_file.stem} (try --next).")
        else:
            print("No upcoming files — time to generate the next batch (see plan/README.md).")
        return 0

    return show(target, args.open)


if __name__ == "__main__":
    raise SystemExit(main())
