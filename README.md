Jalaan 
# Subscription Business Health Dashboard

Executive-level revenue analytics dashboard designed to evaluate subscription performance, Monthly Recurring Revenue (MRR), retention behavior, churn dynamics, and plan-tier risk across a subscription business.

This project simulates how Strategic Finance, Revenue Operations, Product, Growth, and Executive teams analyze subscription health to understand whether revenue growth is durable, where churn is creating financial risk, and which customer segments or plan tiers should be prioritized for retention, pricing, and lifecycle strategy.

---

## Executive Summary

Subscription businesses often report high-level revenue and churn metrics, but leadership teams need a deeper view into the quality of revenue growth.

This dashboard was built to move beyond surface-level reporting by connecting revenue performance, subscriber behavior, retention curves, churn impact, and plan-tier concentration into a single executive decision-support framework.

The analysis helps answer:

- Is revenue growth being supported by healthy retention?
- Which plan tiers are driving the most MRR?
- Where is churn creating the greatest financial impact?
- Are retention issues tied to pricing, product experience, or lifecycle engagement?
- Which customer segments should receive the most attention from finance, product, and growth teams?

---

## Business Problem

Subscription businesses often track top-line metrics such as revenue, subscriber count, and churn rate, but these measures alone do not explain why customers leave or how retention behavior impacts long-term revenue quality.

Common challenges include:

- Limited visibility into how retention changes across customer cohorts  
- Difficulty separating churn percentage from actual revenue impact  
- Lack of clarity on whether churn is driven by pricing, product, or lifecycle issues  
- Inability to connect subscriber behavior to revenue performance  
- Revenue growth that may be concentrated in a small number of higher-tier plans  
- Executive reporting that identifies performance trends but does not clearly show where action should be taken  

Without a structured view of subscriber health, leadership teams risk over-prioritizing acquisition while underinvesting in retention, onboarding, product engagement, and lifecycle strategy.

---

## Objective

Build an executive-ready dashboard that helps finance, product, and growth teams evaluate subscription business health and identify the highest-impact opportunities for improving revenue durability.

The dashboard is designed to answer:

- How is subscription revenue growing over time?  
- Which plan tiers contribute most to MRR and revenue concentration?  
- What are the true drivers of churn and retention?  
- Where does subscriber engagement decline across the lifecycle?  
- Which plan tiers carry the greatest churn and revenue risk?  
- Where should leadership focus to improve retention, LTV, and long-term revenue quality?  

---

## Approach

Developed a structured analytics framework combining revenue modeling, cohort analysis, churn diagnostics, and plan-level segmentation.

Key components:

- Built an executive KPI layer to track subscribers, MRR, churn, and retention  
- Developed cohort-based retention modeling using time-indexed lifecycle analysis  
- Segmented performance by subscription plan to isolate revenue and churn behavior  
- Modeled churn by both rate and volume to distinguish relative risk from financial impact  
- Designed dashboard views to separate revenue growth, retention quality, and churn exposure  
- Focused on executive usability, clear decision-making outputs, and strategic recommendations  

---

## Key Metrics

- Active Subscribers  
- Monthly Recurring Revenue (MRR)  
- MRR by Plan Tier  
- Churn Rate  
- Churn Volume by Plan  
- Retention Rate by Cohort  
- Plan-Level Revenue Concentration  
- Subscriber Mix by Plan Tier  
- Lifecycle Drop-Off Patterns  
- Revenue Risk by Plan Tier  

---

## Key Insights

- Retention decay follows a consistent pattern across plan tiers, indicating broader lifecycle issues rather than pricing-specific problems  
- Revenue growth is driven disproportionately by higher-tier plans, increasing concentration risk  
- Churn volume and churn rate tell different stories and must be evaluated together to understand true revenue impact  
- Early lifecycle drop-off presents the largest opportunity for improving long-term retention and customer lifetime value  
- Plan-tier segmentation helps leadership prioritize retention and product initiatives based on financial impact rather than broad averages  
- Monitoring revenue concentration is critical because strong MRR growth can still create risk if it depends heavily on a limited number of higher-value plan tiers  

---

## Recommendations

- Improve onboarding and early lifecycle engagement to reduce initial churn  
- Monitor revenue concentration across plan tiers to reduce dependency risk  
- Prioritize retention initiatives based on churn volume, not only churn percentage  
- Align pricing, product, and lifecycle strategies with observed retention patterns  
- Use cohort-based retention behavior to improve MRR forecasting and long-term revenue planning  
- Track plan-level subscriber behavior to identify whether churn is driven by customer lifecycle issues, product fit, or pricing sensitivity  

---

## Dashboard Overview

![Dashboard Overview](screenshots/01_dashboard_overview.png)

The dashboard provides a consolidated view of subscription performance, allowing stakeholders to quickly assess overall business health and identify areas of risk or opportunity.

This view is designed for executive review and provides a high-level snapshot of:

- Subscriber base health  
- Monthly Recurring Revenue performance  
- Churn exposure  
- Plan-tier performance  
- Retention trends  
- Areas requiring deeper analysis  

---

## KPI Summary

![KPI Summary](screenshots/02_kpi_summary.png)

Core metrics including subscribers, MRR, and churn rate provide a high-level snapshot of performance and serve as entry points for deeper analysis.

The KPI summary helps leadership quickly understand:

- Current subscriber base size  
- Revenue scale and MRR performance  
- Churn level and potential retention risk  
- Whether the business is growing through durable customer behavior or short-term acquisition volume  

---

## Revenue Trend Analysis

![Monthly MRR Trend](screenshots/03_monthly_mrr_trend.png)

MRR is tracked over time and segmented by plan tier, enabling comparison of growth trajectories and identification of revenue concentration across plans.

This analysis helps identify:

- Which plan tiers are driving revenue growth  
- Whether revenue is diversified or concentrated  
- Where revenue dependency risk may exist  
- Whether changes in subscriber mix are improving or weakening revenue quality  

---

## Retention and Lifecycle Analysis

![Retention Curve](screenshots/04_retention_curve.png)

Cohort-based retention curves show how subscriber engagement declines over time.

The consistency of retention decay across plans suggests that churn is driven more by lifecycle and engagement factors than pricing differences.

This view helps leadership evaluate:

- Early lifecycle drop-off  
- Long-term retention quality  
- Whether churn is systemic or plan-specific  
- Where onboarding, engagement, or product experience improvements may have the greatest impact  

---

## Churn Diagnostics

![Churn by Plan Tier](screenshots/05_churn_by_plan.png)

Churn is analyzed by plan tier to distinguish between relative churn rates and total business impact.

This helps prioritize retention efforts based on where the largest revenue losses occur.

A plan with a lower churn rate can still create meaningful revenue risk if it represents a large share of total MRR or churn volume. This view helps leadership avoid relying only on percentage-based churn analysis.

---

## Modeling and Technical Approach

![Retention Modeling](screenshots/06_retention_curve_by_plan_tier_worksheet.png)

Key analytical techniques include:

- Cohort-based retention modeling using a Month Index  
- Time-aware subscription activity logic based on start and end dates  
- Active subscriber flagging by reporting period  
- MRR aggregation by month and plan tier  
- KPI aggregation for executive reporting  
- Plan-level segmentation to separate churn risk from revenue impact  
- Distinction between behavioral trends and financial outcomes  
- Churn analysis using both rate-based and volume-based perspectives  

---

## Data Model Logic

The dashboard is structured around subscription lifecycle behavior and recurring revenue performance.

Core modeling concepts include:

| Modeling Area | Purpose |
|---|---|
| MRR Calculation | Measures recurring revenue performance over time |
| Active Subscriber Logic | Identifies whether a subscriber is active during each reporting period |
| Cohort Month Index | Tracks customer retention over time from signup |
| Plan-Tier Segmentation | Compares monetization and churn behavior across plans |
| Churn Volume Analysis | Measures total subscriber loss by plan tier |
| Churn Rate Analysis | Evaluates relative churn risk |
| Retention Curve Modeling | Shows lifecycle decay and long-term subscriber behavior |

---

## How This Dashboard Is Used

This dashboard supports decision-making across product, finance, growth, marketing, and executive teams.

Typical use cases include:

- Monitoring subscription health in executive reviews  
- Identifying churn drivers and retention opportunities  
- Evaluating pricing and plan performance  
- Supporting lifecycle and engagement strategy decisions  
- Improving MRR forecasting through cohort analysis  
- Prioritizing onboarding and retention initiatives  
- Understanding whether growth is being driven by durable customer behavior  
- Translating subscriber behavior into financial recommendations  

---

## Business Impact (Simulated)

If applied in a production environment, this system would help subscription businesses:

- Improve retention strategy by identifying key lifecycle drop-off points  
- Enable more accurate revenue forecasting through cohort analysis  
- Support data-driven decisions for pricing, product, and growth initiatives  
- Identify revenue concentration risk across plan tiers  
- Prioritize retention efforts based on financial impact  
- Improve executive visibility into MRR, churn, and customer lifecycle health  
- Align finance, product, and growth teams around consistent KPI definitions  
- Reduce reliance on surface-level metrics by connecting churn, retention, and revenue impact  

---

## Strategic Finance Relevance

This project mirrors the type of analysis used by Strategic Finance and Revenue Finance teams to evaluate top-line performance and revenue quality.

It demonstrates the ability to:

- Build revenue performance reporting  
- Analyze MRR trends and subscription growth  
- Evaluate churn and retention behavior  
- Develop KPI frameworks for executive decision-making  
- Translate customer behavior into financial insights  
- Support pricing, product, and growth strategy  
- Identify lifecycle risk and revenue concentration  
- Build dashboards that connect analytics to business action  

---

## Tech Stack

- Tableau  
- SQL  
- Data modeling  
- Cohort analysis  
- MRR calculations  
- Retention modeling  
- Plan-tier segmentation  
- KPI framework design  

---

## Skills Demonstrated

- Revenue Analytics  
- Subscription Business Analysis  
- Monthly Recurring Revenue Analysis  
- Cohort-Based Retention Modeling  
- Churn Diagnostics  
- Customer Lifecycle Analytics  
- KPI Framework Development  
- Financial Performance Reporting  
- Executive Dashboard Design  
- Strategic Finance Analysis  
- Pricing and Plan-Tier Evaluation  
- SQL-Based Data Modeling  
- Tableau Dashboard Development  
- Executive Recommendation Development  

---

## Why This Matters

Subscription businesses succeed when they understand not only how much revenue they are generating, but whether that revenue is durable.

This project demonstrates how financial, customer, and lifecycle data can be combined into a structured executive reporting framework that helps leadership identify revenue risks, prioritize retention opportunities, and make better decisions around product, pricing, and growth strategy.

It is designed to mirror real-world analytics workflows used by subscription-based platforms, fintech companies, streaming businesses, and other recurring-revenue organizations.

---

## About

Tableau dashboard analyzing subscription revenue, Monthly Recurring Revenue, retention, churn behavior, lifecycle performance, and plan-tier risk using cohort-based analytics and revenue performance modeling.
```
Jalaan Fields
