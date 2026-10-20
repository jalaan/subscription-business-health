"""Reproducible smoke and regression tests for reporting-control examples."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from pipeline import run  # noqa: E402

class ReportingControlsTests(unittest.TestCase):
    def test_injected_anomalies_are_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            summary = run(Path(temp))
            rules=summary["exception_count_by_rule"]
            for expected in ("P01_INVALID_TERM","T01_DUPLICATE_ID","T02_ORPHAN_POLICY",
                             "T03_NEGATIVE_PREMIUM","C02_LOSS_OUTSIDE_TERM","F01_LEDGER_VARIANCE"):
                self.assertGreaterEqual(rules.get(expected,0),1,expected)
            self.assertEqual(summary["submission_readiness"],"REVIEW_REQUIRED")
            self.assertEqual(summary["premium_reconciliation_difference"],-175.0)
            self.assertTrue((Path(temp)/"exceptions.csv").exists())
            self.assertEqual(json.loads((Path(temp)/"reporting_summary.json").read_text())["synthetic_only"],True)

    def test_reproducible_source_totals(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            a,b=run(Path(first)),run(Path(second))
            self.assertEqual(a["exception_count_by_rule"],b["exception_count_by_rule"])
            self.assertEqual(a["premium_transactions_sum"],b["premium_transactions_sum"])

if __name__=="__main__":
    unittest.main()
