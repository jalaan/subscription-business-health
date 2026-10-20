-- Illustrative analytical query: joins, CTEs, aggregations, and window functions.
-- Not statutory earned premium or a regulator-prescribed metric.
WITH premium_by_policy AS (
  SELECT policy_id, SUM(amount) AS written_premium_proxy,
         COUNT(*) AS premium_record_count
  FROM premiums GROUP BY policy_id
), claims_by_policy AS (
  SELECT policy_id, COUNT(*) AS reported_claims, SUM(paid_amount) AS paid_loss_proxy
  FROM claims GROUP BY policy_id
), policy_view AS (
  SELECT p.state, p.policy_id,
         COALESCE(pr.written_premium_proxy,0) AS premium,
         COALESCE(cl.reported_claims,0) AS claim_count,
         COALESCE(cl.paid_loss_proxy,0) AS paid_loss
  FROM policies p
  LEFT JOIN premium_by_policy pr ON p.policy_id = pr.policy_id
  LEFT JOIN claims_by_policy cl ON p.policy_id = cl.policy_id
)
SELECT state, policy_id, premium, claim_count, paid_loss,
       SUM(premium) OVER(PARTITION BY state) AS state_premium_proxy,
       SUM(paid_loss) OVER(PARTITION BY state) AS state_paid_loss_proxy,
       ROUND(100.0*paid_loss/NULLIF(premium,0),2) AS illustrative_paid_loss_to_premium_pct,
       DENSE_RANK() OVER(PARTITION BY state ORDER BY paid_loss DESC) AS loss_amount_rank
FROM policy_view
ORDER BY state, loss_amount_rank, policy_id;
