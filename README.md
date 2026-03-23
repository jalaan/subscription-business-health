# Subscription Business Health Dashboard

Executive-level analytics dashboard designed to evaluate subscription performance, revenue growth, retention behavior, and churn dynamics across plan tiers.

This project reflects how subscription-based businesses analyze monetization, lifecycle performance, and customer retention to inform product, pricing, and growth strategies.

---

## Business Problem

Subscription businesses often track high-level metrics like revenue and churn, but lack a clear understanding of *why* customers leave and how retention behavior impacts long-term revenue.

Common challenges include:

- Limited visibility into how retention changes over time  
- Difficulty separating churn rate from actual revenue impact  
- Lack of clarity on whether churn is driven by pricing, product, or lifecycle issues  
- Inability to connect subscriber behavior to revenue performance  

---

## Objective

Build an executive-ready dashboard that helps answer:

- How is subscription revenue growing over time?  
- What are the true drivers of churn and retention?  
- Which plan tiers contribute most to revenue and churn risk?  
- Where should the business focus to improve retention and lifetime value?  

---

## Approach

Developed a structured analytics framework combining revenue modeling, cohort analysis, and plan-level segmentation.

Key components:

- Built KPI layer to track subscribers, MRR, and churn  
- Developed cohort-based retention modeling using time-indexed analysis  
- Segmented performance by subscription plan to isolate behavioral patterns  
- Designed visualizations to separate churn rate from churn impact  
- Focused on executive usability and clear decision-making outputs  

---

## Key Metrics

- Active Subscribers  
- Monthly Recurring Revenue (MRR)  
- Churn Rate  
- Retention Rate by Cohort  
- Churn Volume by Plan  

---

## Key Insights

- Retention decay follows a consistent pattern across plan tiers, indicating systemic lifecycle issues rather than pricing-specific problems  
- Revenue growth is driven disproportionately by higher-tier plans, increasing concentration risk  
- Churn volume and churn rate tell different stories, and both must be evaluated together  
- Early lifecycle drop-off presents the largest opportunity for improving long-term retention  

---

## Recommendations

- Improve onboarding and early user experience to reduce initial churn  
- Monitor revenue concentration across plans to mitigate dependency risk  
- Prioritize retention initiatives based on churn volume, not just percentage  
- Align product and lifecycle strategies with observed retention patterns  

---

## Dashboard Overview

![Dashboard Overview](screenshots/01_dashboard_overview.png)

The dashboard provides a consolidated view of subscription performance, allowing stakeholders to quickly assess overall business health and identify areas of risk or opportunity.

---

## KPI Summary

![KPI Summary](screenshots/02_kpi_summary.png)

Core metrics including subscribers, MRR, and churn rate provide a high-level snapshot of performance and serve as entry points for deeper analysis.

---

## Revenue Trend Analysis

![Monthly MRR Trend](screenshots/03_monthly_mrr_trend.png)

MRR is tracked over time and segmented by plan tier, enabling comparison of growth trajectories and identification of revenue concentration across plans.

---

## Retention and Lifecycle Analysis

![Retention Curve](screenshots/04_retention_curve.png)

Cohort-based retention curves show how subscriber engagement declines over time.

The consistency of retention decay across plans suggests that churn is driven more by lifecycle and engagement factors than pricing differences.

---

## Churn Diagnostics

![Churn by Plan Tier](screenshots/05_churn_by_plan.png)

Churn is analyzed by plan tier to distinguish between relative churn rates and total business impact.

This helps prioritize retention efforts based on where the largest revenue losses occur.

---

## Modeling and Technical Approach

![Retention Modeling](screenshots/06_retention_curve_by_plan_tier_worksheet.png)

Key analytical techniques include:

- Cohort-based retention modeling using a Month Index  
- Time-aware subscription activity logic based on start and end dates  
- KPI aggregation for executive reporting  
- Plan-level segmentation to separate churn risk from impact  
- Distinction between behavioral trends and revenue outcomes  

---

## How This Dashboard Is Used

This dashboard supports decision-making across product, finance, and growth teams.

Typical use cases include:

- Monitoring subscription health in executive reviews  
- Identifying churn drivers and retention opportunities  
- Evaluating pricing and plan performance  
- Supporting lifecycle and engagement strategy decisions  

---

## Business Impact (Simulated)

If applied in a production environment, this system would:

- Improve retention strategy by identifying key lifecycle drop-off points  
- Enable more accurate revenue forecasting through cohort analysis  
- Support data-driven decisions for pricing, product, and growth initiatives  

---

## Tech Stack

- Tableau  
- SQL  
- Data modeling (cohort analysis, MRR calculations)  

---

## Why This Matters

This project reflects how modern subscription and streaming businesses evaluate:

- Revenue growth and monetization  
- Customer retention and churn behavior  
- Lifecycle performance across user cohorts  

It is designed to mirror real-world analytics workflows used by subscription-based platforms and media companies.
