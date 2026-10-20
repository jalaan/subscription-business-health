# Auto Insurance Reporting Controls | Independent Simulation

**Portfolio project | Python · SQL (SQLite) · Data quality · Reporting reconciliation · Governance**

A reproducible **synthetic** private-passenger-auto reporting control pipeline designed to demonstrate how an insurance analytics team might validate policy, premium, and claim records before producing controlled management and regulatory-support reporting.

> **Not an official NAIC MCAS template, filing, attestation, regulatory submission, or representation of insurer production systems.** The checks and labels are illustrative, not a definitive interpretation of state regulations.

## Business case
Insurance analytics teams must translate requirements into business rules; reconcile policy, claim, premium, and general-ledger-like source data; identify exceptions; document data lineage; and provide a clear review trail before reporting deadlines. This project implements those controls on generated test data.

## What is included
- A **deterministic data generator** for synthetic policies, premium transactions, claims, and ledger control totals, with deliberate defects.
- SQL controls for missing policy references, duplicate transactions, invalid policy terms, negative amounts, coverage timing, and ledger/premium reconciliation.
- A Python pipeline that stages records in SQLite, runs controls, exports an exception inventory, and writes a machine-readable run summary.
- A reporting control matrix with owner, check, exception handling, review status, and evidence requirements.
- A lightweight automated test and a data dictionary.

## Quick start

Requires **Python 3.10+**, no third-party packages.

```bash
python projects/auto-insurance-reporting-controls/src/pipeline.py --output projects/auto-insurance-reporting-controls/output
python -m unittest discover -s projects/auto-insurance-reporting-controls/tests -v
```

Run from the **repository root**. Output files are generated locally and ignored by Git:
- `output/policies.csv`, `premiums.csv`, `claims.csv`, `ledger.csv` — synthetic raw input evidence;
- `output/exceptions.csv` — exception-level inventory with severity and rule IDs;
- `output/reporting_summary.json` — run date, source counts, financial reconciliation, defects by category, and `REVIEW_REQUIRED` status.

**Decision gate:** Do not certify data as submission-ready when blocking exceptions remain. Investigate and document fixes; re-run controls before review.

## Scope and boundaries

This is a deliberately simplified **reporting preflight and control demonstration**. It does **not** produce a state-specific filing, model earned premium actuarially, determine statutory reserve adequacy, compute official MCAS question responses, or provide regulatory/legal guidance. The ledger is a simulated independent control source rather than a GAAP insurance accounting system.

### Public regulatory reference (for context only)
The NAIC's MCAS resources include private-passenger-auto data collection worksheets, definitions, user guides, and validation/warning documentation. Requirements vary with data year and jurisdiction: https://content.naic.org/mcas-2026.htm

For production use, obtain the applicable state/data-year instructions, map each official field to approved source systems, document signoff/attestation, and have Compliance/Actuarial/Accounting review the logic. **This educational project does not claim that mapping is complete.**

## Portfolio relevance
Demonstrates: SQL joins/aggregations, record-level exception management, multi-system data reconciliation, reporting inventory, traceable business rules, reproducible controls, and review-ready evidence. See [control matrix](docs/control_matrix.md) and [data dictionary](docs/data_dictionary.md).

**Author:** Jalaan Fields — independent portfolio simulation; not work performed for GM Financial or any insurer.
