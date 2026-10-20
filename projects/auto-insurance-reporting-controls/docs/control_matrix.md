# Reporting control matrix — illustrative

| Rule | Control objective | Evidence | Action / accountable reviewer |
|---|---|---|---|
| P01 | Policy term dates valid | Exception inventory + policy source | Policy Operations correct source or explain |
| T01 | Unique premium transaction IDs | Duplicate transaction exceptions | Billing/Data Engineering reconcile duplicates |
| T02 | Premium references an existing policy | SQL unmatched join rows | Policy/Billing owners investigate missing keys |
| T03 | Negative premium classified before aggregation | Negative premium review exceptions | Finance decide refund/adjustment vs error |
| C01 | Claim references an existing policy | SQL unmatched claim keys | Claims Operations confirm mapping |
| C02 | Loss date is consistent with policy term | Date-range exception output | Claims/Legal review coverage context |
| F01 | Source premium total reconciles to simulated ledger | Summary amount variance | Accounting reconcile and approve |

## Illustrative reporting inventory / runbook

| Stage | Owner in a real team | Required artifact |
|---|---|---|
| Define jurisdiction, reporting period, and official submission instructions | Regulatory Compliance | Approved requirements document |
| Identify source-system owners and definitions | Data & Analytics / Claims / Policy Operations | Source-to-target mapping and data dictionary |
| Extract data with approved as-of date | Data Engineering | Source files, record counts, extract timestamp |
| Validate key uniqueness, referential integrity and reasonableness | Reporting Analyst | Exceptions inventory, rule results |
| Reconcile financial aggregates to Accounting | Accounting / Reporting Analyst | Control totals and signed variance explanation |
| Remediate material exceptions | Source-system owners | Case log, assigned owner, fix evidence |
| Independent review and approval | Reporting lead / Compliance / Accounting | Review signoff and control evidence |
| Submit through official state/NAIC process | Authorized designated filer | Receipt and retention record |

**Current prototype implements only synthetic extraction, controls, and exception exports.** It does not implement organizational approvals, regulated record retention, submission, or filing attestation. Do not claim otherwise.

## Sample exception lifecycle
`OPEN → ASSIGNED → UNDER_INVESTIGATION → CORRECTED_OR_EXPLAINED → RECHECKED → REVIEWED`.

A `REVIEW_REQUIRED` output is expected: intentionally bad source data proves that controls can identify problems rather than certifying invalid data.
