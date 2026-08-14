"""Tests for the daily plan tool."""

from __future__ import annotations

import importlib.util
from datetime import date
from pathlib import Path
from types import ModuleType


def load_plan_module() -> ModuleType:
    """Load tools/plan.py as a module without package installation."""
    root = Path(__file__).resolve().parent.parent
    spec = importlib.util.spec_from_file_location("plan_tool", root / "tools" / "plan.py")
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_plan_path_names_files_by_iso_date(tmp_path: Path) -> None:
    module = load_plan_module()
    result = module.plan_path(tmp_path, date(2026, 8, 17))
    assert result.name == "2026-08-17.md"


def test_next_plan_finds_first_existing_file(tmp_path: Path) -> None:
    module = load_plan_module()
    (tmp_path / "2026-08-19.md").write_text("# later", encoding="utf-8")
    found = module.next_plan(tmp_path, date(2026, 8, 17))
    assert found is not None
    assert found.name == "2026-08-19.md"


def test_next_plan_returns_none_when_empty(tmp_path: Path) -> None:
    module = load_plan_module()
    assert module.next_plan(tmp_path, date(2026, 8, 17), horizon=10) is None
