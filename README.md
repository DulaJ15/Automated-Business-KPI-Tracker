# 📊 Automated Business KPI Tracker

A smart KPI monitoring system that ingests Excel sheets, calculates key performance metrics, detects anomalies, and optionally sends alerts when thresholds are crossed.

## 🚀 Features
- Upload weekly/monthly Excel reports
- Auto-calculate KPIs: Revenue, Growth, Retention, Churn, Avg. Order Size, etc.
- Detect anomalies using statistical thresholds (Z-score, Prophet)
- Visual dashboard (Streamlit)
- Optional email/Slack alert system for KPI drops

## 📁 Project Structure
- `/data`: Example Excel files
- `/app`: Streamlit app for interaction
- `/utils`: Business logic & anomaly detection
- `/notebooks`: Exploratory analysis and prototyping

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Streamlit
- Prophet or Scikit-learn
- SMTP / Slack API for alerts

## ✅ Demo
[Include Colab / Streamlit link]

## 📥 Input Format
Upload Excel file like:
| Date       | Revenue | Orders | New Customers | Returning Customers |
|------------|---------|--------|----------------|----------------------|
| 2025-07-01 | 500000  | 250    | 45             | 205                  |

## 📤 Output
- Dashboard showing KPIs and trends
- Alerts when revenue drops 2+ std deviations
