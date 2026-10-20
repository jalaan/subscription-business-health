-- Educational SQL preflight rules. This query is NOT an official MCAS validation set.
-- Output fields: rule_id, severity, record_id, detail.
SELECT 'P01_INVALID_TERM' AS rule_id, 'BLOCKER' AS severity, policy_id AS record_id,
       'expiry_date <= effective_date' AS detail
FROM policies WHERE expiry_date <= effective_date
UNION ALL
SELECT 'T01_DUPLICATE_ID', 'BLOCKER', premium_id, 'duplicate premium transaction identifier'
FROM premiums GROUP BY premium_id HAVING COUNT(*) > 1
UNION ALL
SELECT 'T02_ORPHAN_POLICY', 'BLOCKER', t.premium_id, 'premium references unknown policy'
FROM premiums t LEFT JOIN policies p ON p.policy_id = t.policy_id
WHERE p.policy_id IS NULL
UNION ALL
SELECT 'T03_NEGATIVE_PREMIUM', 'REVIEW', premium_id, 'negative premium requires classification or correction'
FROM premiums WHERE amount < 0
UNION ALL
SELECT 'C01_ORPHAN_POLICY', 'BLOCKER', c.claim_id, 'claim references unknown policy'
FROM claims c LEFT JOIN policies p ON p.policy_id = c.policy_id
WHERE p.policy_id IS NULL
UNION ALL
SELECT 'C02_LOSS_OUTSIDE_TERM', 'REVIEW', c.claim_id, 'loss date outside recorded policy term'
FROM claims c JOIN policies p ON p.policy_id = c.policy_id
WHERE c.loss_date < p.effective_date OR c.loss_date > p.expiry_date
UNION ALL
SELECT 'F01_LEDGER_VARIANCE', 'BLOCKER', 'WRITTEN_PREMIUM', 'source premium sum differs from ledger control total'
WHERE ABS((SELECT SUM(amount) FROM premiums) -
          (SELECT expected_total FROM ledger WHERE control_account='WRITTEN_PREMIUM')) > 0.01
ORDER BY rule_id, record_id;
