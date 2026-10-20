# Synthetic data dictionary and lineage

All identifiers and records are locally generated for this project; no real customer, policyholder, or insurer data is included.

| Source | Field | Meaning |
|---|---|---|
| policies | policy_id | Synthetic policy business key |
| policies | state | Illustrative jurisdiction attribute |
| policies | effective_date / expiry_date | ISO policy dates; not a legal coverage determination |
| policies | status | Simplified policy status |
| premiums | premium_id | Synthetic premium transaction key |
| premiums | policy_id | Policy foreign key |
| premiums | transaction_date | Transaction date |
| premiums | amount | Signed written-premium-like amount, not actuarial earned premium |
| claims | claim_id | Synthetic claim key |
| claims | policy_id | Policy foreign key |
| claims | loss_date | Illustrative date of loss |
| claims | paid_amount | Synthetic paid amount; excludes IBNR and claims reserves |
| ledger | control_account | Synthetic control account |
| ledger | expected_total | Independent simulated financial control total |

**Data lineage:** deterministic Python generator → raw CSV extracts → SQLite staging → SQL validation rules → exception inventory CSV + run summary JSON.

**Limitations:** No actuarial models, claim reserve adequacy, state-specific data calls or reporting thresholds, official MCAS field mapping, filings, signed approvals, regulated data handling, or insurer production integration.

For real regulatory reporting, Compliance and authorized reporting leads must map the current data-year and jurisdiction's requirements to approved sources and review all business rules and exceptions.