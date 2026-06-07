# AI Use Case Analysis - E-Commerce 🛒

## Project Overview
Analysis of a real-world e-commerce dataset to uncover business insights 
and segment customers using Machine Learning.

## Dataset
- **Source:** UCI Machine Learning Repository
- **Records:** 500,000+ transactions
- **Period:** 2010-2011

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Git & GitHub

## Analysis Performed
### 1. Business Analysis
- Top countries by number of orders
- Most popular products
- Total and per-country revenue

### 2. Time Analysis
- Monthly revenue trends
- Peak sales periods

### 3. Customer Segmentation (ML)
- RFM Analysis (Recency, Frequency, Monetary)
- KMeans Clustering — 4 customer segments:
  - 🏆 Champions
  - 💚 Loyal Customers
  - ⚠️ At Risk
  - ❌ Lost Customers

## Key Insights
- UK generates the highest revenue
- November-December are peak sales months
- Top 10 customers contribute significant revenue

## How to Run
```bash
git clone https://github.com/SumanRajput06/AI-Use-Case-Analysis-Ecommerce.git
cd AI-Use-Case-Analysis-Ecommerce
pip install pandas matplotlib scikit-learn
python main.py
```

## Output Files
- `revenue_by_country.png` — Revenue by country chart
- `monthly_revenue.png` — Monthly revenue trend
- `customer_segments.png` — Customer segmentation chart
- `rfm_analysis.csv` — RFM scores per customer
- `customer_segments.csv` — Customer segment labels

## Author
**Suman Rajput**