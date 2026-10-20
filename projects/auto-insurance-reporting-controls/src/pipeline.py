"""Synthetic auto insurance reporting preflight; educational, not an MCAS filing."""
from __future__ import annotations

import argparse
import csv
import json
import random
import sqlite3
from collections import Counter
from datetime import date, timedelta, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
QUERY_FILE = HERE / "sql" / "controls.sql"
START = date(2025, 1, 1)

def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

def synthesize(output: Path, seed: int = 42) -> dict[str, list[dict]]:
    """Create reproducible fictitious data plus deliberate exception cases."""
    rng = random.Random(seed)
    policies, premiums, claims = [], [], []
    for i in range(1, 121):
        pid = f"P{i:04d}"
        begin = START + timedelta(days=rng.randint(0, 180))
        end = begin + timedelta(days=365)
        region = ["TX", "IL", "CA"][i % 3]
        policies.append({"policy_id":pid,"state":region,"effective_date":begin.isoformat(),
                         "expiry_date":end.isoformat(),"status":"ACTIVE"})
        amount = 480 + (i % 8) * 115
        premiums.append({"premium_id":f"T{i:04d}","policy_id":pid,
                         "transaction_date":(begin + timedelta(days=3)).isoformat(),
                         "amount":amount})
        if i % 3 == 0:
            claims.append({"claim_id":f"C{i:04d}","policy_id":pid,
                           "loss_date":(begin + timedelta(days=20)).isoformat(),
                           "paid_amount":120 + (i % 7) * 50})
    # Explicit seeded defects: duplicate, orphan, negative amount, invalid policy dates, out-of-term claim.
    premiums.append(dict(premiums[0]))
    premiums.append({"premium_id":"T9998","policy_id":"P9999","transaction_date":"2025-07-01","amount":220})
    premiums.append({"premium_id":"T9999","policy_id":"P0002","transaction_date":"2025-06-01","amount":-100})
    policies[2]["expiry_date"] = "2024-12-01"
    claims.append({"claim_id":"C9999","policy_id":"P0004","loss_date":"2024-01-01","paid_amount":315})
    # Hypothetical accounting control total does not reconcile; separate from source transaction rows.
    ledger = [{"control_account":"WRITTEN_PREMIUM","expected_total":sum(int(x["amount"]) for x in premiums) + 175}]
    datasets = {"policies":policies,"premiums":premiums,"claims":claims,"ledger":ledger}
    for name, rows in datasets.items():
        write_csv(output / f"{name}.csv", rows, list(rows[0]))
    return datasets

SCHEMAS = {
"policies": """CREATE TABLE policies (policy_id TEXT, state TEXT, effective_date TEXT, expiry_date TEXT, status TEXT)""",
"premiums": """CREATE TABLE premiums (premium_id TEXT, policy_id TEXT, transaction_date TEXT, amount REAL)""",
"claims": """CREATE TABLE claims (claim_id TEXT, policy_id TEXT, loss_date TEXT, paid_amount REAL)""",
"ledger": """CREATE TABLE ledger (control_account TEXT, expected_total REAL)"""
}

def run(output: Path, seed: int = 42) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    data = synthesize(output, seed)
    with sqlite3.connect(":memory:") as db:
        for name, ddl in SCHEMAS.items():
            db.execute(ddl)
            keys = list(data[name][0])
            placeholders = ",".join("?" for _ in keys)
            db.executemany(f"INSERT INTO {name} VALUES ({placeholders})",
                           [[row[k] for k in keys] for row in data[name]])
        # Source SQL returns rule_id, severity, record_id, detail, and is reviewed before use.
        exceptions = [dict(zip(["rule_id","severity","record_id","detail"], row))
                      for row in db.execute(QUERY_FILE.read_text(encoding="utf-8"))]
        calculated = db.execute("SELECT ROUND(COALESCE(SUM(amount),0),2) FROM premiums").fetchone()[0]
        expected = db.execute("SELECT expected_total FROM ledger WHERE control_account='WRITTEN_PREMIUM'").fetchone()[0]
    write_csv(output / "exceptions.csv", exceptions, ["rule_id","severity","record_id","detail"])
    by_rule = dict(sorted(Counter(e["rule_id"] for e in exceptions).items()))
    result = {
        "project":"Auto Insurance Reporting Controls — independent simulation",
        "generated_at_utc":datetime.now(timezone.utc).isoformat(),
        "data_year":2025, "synthetic_only":True,
        "sources":{k:len(v) for k,v in data.items()},
        "premium_transactions_sum":round(calculated,2),
        "ledger_control_total":round(expected,2),
        "premium_reconciliation_difference":round(calculated-expected,2),
        "exception_count":len(exceptions), "exception_count_by_rule":by_rule,
        "blocking_exceptions":sum(e["severity"]=="BLOCKER" for e in exceptions),
        "submission_readiness":"REVIEW_REQUIRED" if exceptions else "PRELIMINARY_CHECKS_PASSED",
        "disclaimer":"Not an NAIC MCAS filing or official validation."
    }
    (output/"reporting_summary.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    return result

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE/"output")
    parser.add_argument("--seed",type=int,default=42)
    opts=parser.parse_args()
    summary=run(opts.output,opts.seed)
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
