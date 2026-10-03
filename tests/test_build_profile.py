import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build_profile import REPOS, headline, table, update  # noqa: E402

REPORT = {
    "recorded_at": "2026-10-04",
    "criteria": [
        {"id": "bank_auto_precision", "label": "Bank details accepted automatically that are correct",
         "unit": "rate", "value": 0.9917, "passed": True},
        {"id": "straight_through", "label": "Documents fully processed with no human touch",
         "unit": "rate", "value": 0.7125, "passed": True},
        {"id": "wrong_closes", "label": "Tickets wrongly closed", "unit": "count", "value": 0.0, "passed": True},
    ],
}


def test_headline_formats_rates_and_counts():
    assert headline(REPORT, ["bank_auto_precision", "wrong_closes"]) == (
        "Bank details accepted automatically that are correct: 99.2%<br>Tickets wrongly closed: 0"
    )


def test_headline_marks_a_failed_criterion_honestly():
    failed = json.loads(json.dumps(REPORT))
    failed["criteria"][1]["passed"] = False
    assert "below target" in headline(failed, ["straight_through"])


def test_missing_report_says_not_measured_yet():
    assert headline(None, ["bank_auto_precision"]) == "Not measured yet"


def test_table_has_one_row_per_repository(tmp_path):
    lines = table(tmp_path).splitlines()
    assert lines[0].startswith("| Repository |")
    assert len(lines) == 2 + len(REPOS)
    assert "[finance-document-agent](https://github.com/iteamcollage/finance-document-agent)" in lines[2]


def test_table_reads_each_repository_report(tmp_path):
    reports = tmp_path / "finance-document-agent" / "reports"
    reports.mkdir(parents=True)
    (reports / "acceptance.json").write_text(json.dumps(REPORT), encoding="utf-8")
    assert "99.2%" in table(tmp_path)


def test_update_replaces_only_the_block(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("# Top\n<!-- repos:start -->\nold\n<!-- repos:end -->\nBottom\n", encoding="utf-8")
    update(readme, "new")
    assert readme.read_text(encoding="utf-8") == "# Top\n<!-- repos:start -->\nnew\n<!-- repos:end -->\nBottom\n"
