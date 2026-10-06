"""Fill the table on the organization's front page from each repository's acceptance report.

    python build_profile.py     reads ../<repo>/reports/acceptance.json and rewrites profile/README.md

The front page never states a number by hand: every figure comes from a report a reader can reproduce.
"""

from __future__ import annotations

import json
from pathlib import Path

START, END = "<!-- repos:start -->", "<!-- repos:end -->"

REPOS = [
    (
        "finance-document-agent",
        "Reads invoices, payment requests and contracts in English, French and German, and accepts a field "
        "only when the code can prove it.",
        ["bank_auto_precision", "straight_through"],
    ),
    (
        "support-triage-agent",
        "Closes routine support tickets with a grounded reply, routes the rest with a handover, and never "
        "touches what a person must handle.",
        ["wrong_closes", "close_rate"],
    ),
    (
        "text-to-sql-agent",
        "Turns an analyst's question into SQL, shows it before it runs, and keeps every query inside the "
        "guardrails.",
        ["execution_accuracy", "unsafe_blocked"],
    ),
    (
        "incident-rca-agent",
        "Starts from a monitoring alert and writes a root-cause analysis in which every claim cites its source.",
        ["rca_accuracy", "grounding"],
    ),
    (
        "salesforce-sales-pipeline",
        "A written sales-process brief built in Salesforce: three pipelines, eight automations and access "
        "rules, each requirement proven by a test in a real org.",
        ["requirements_covered", "org_tests_passing"],
    ),
]


def _format(criterion: dict) -> str:
    value = criterion.get("value")
    if value is None:
        return f"{criterion['label']}: not measured yet"
    if criterion.get("unit") == "count":
        text = f"{value:g}"
    else:
        text = f"{value * 100:.1f}%"
    if not criterion.get("passed", False):
        text += " (below target)"
    return f"{criterion['label']}: {text}"


def headline(report: dict | None, criterion_ids: list[str]) -> str:
    if report is None:
        return "Not measured yet"
    by_id = {criterion["id"]: criterion for criterion in report["criteria"]}
    return "<br>".join(_format(by_id[cid]) for cid in criterion_ids if cid in by_id) or "Not measured yet"


def _report(root: Path, repo: str) -> dict | None:
    path = root / repo / "reports" / "acceptance.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def table(root: Path) -> str:
    lines = ["| Repository | What it does | Measured on made-up data |", "|---|---|---|"]
    for repo, description, criterion_ids in REPOS:
        link = f"[{repo}](https://github.com/i-teamcollage/{repo})"
        lines.append(f"| {link} | {description} | {headline(_report(root, repo), criterion_ids)} |")
    return "\n".join(lines)


def update(readme: Path, block: str) -> bool:
    text = readme.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new_text = f"{head}{START}\n{block}\n{END}{tail}"
    readme.write_text(new_text, encoding="utf-8")
    return new_text != text


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    changed = update(here / "profile" / "README.md", table(here.parent))
    print("profile/README.md updated" if changed else "profile/README.md already up to date")
