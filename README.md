# 📊 Automated Business KPI Tracker

A smart KPI monitoring system that ingests Excel sheets, calculates key performance metrics, detects anomalies, and optionally sends alerts when thresholds are crossed — designed for easy customization and scalable reporting.

## 🚀 Features
- Upload weekly/monthly Excel reports via an intuitive Streamlit dashboard
- Auto-calculate KPIs including Revenue, Growth %, Customer Retention, Churn Rate, Average Order Size, and more
- Detect anomalies with statistical methods like Z-score and Prophet forecasting
- Interactive visualizations for KPI trends and anomaly highlights
- Optional integrations for automated alerts via Email or Slack when critical KPIs deviate beyond thresholds
- Modular and extendable codebase for easy addition of new KPIs or alert channels

## 📁 Project Structure
- `/data`: Example Excel files
- `/app`: Streamlit app for interaction
- `/utils`: Business logic & anomaly detection
- `/notebooks`: Exploratory analysis and prototyping
- `/requirements.txt`: Python dependencies
- `/README.md`: Project overview and setup instructions

## 🛠️ Tech Stack
- Python 3.8+  
- Pandas, NumPy for data processing  
- Streamlit for interactive dashboard and app UI  
- Prophet for time series anomaly detection and forecasting  
- Matplotlib, Seaborn for charts and visualizations  
- SMTP and Slack APIs for alert notifications

## 📥 Input Format
Upload Excel file like:
| Date       | Revenue | Orders | New Customers | Returning Customers |
|------------|---------|--------|----------------|----------------------|
| 2025-07-01 | 500000  | 250    | 45             | 205                  |

## 📤 Output
- Real-time dashboard showing calculated KPIs and their historical trends  
- Anomaly detection visual cues and flagged data points  
- Optional email or Slack alerts when revenue or other KPIs drop below defined thresholds (e.g., 2+ standard deviations)  
- Downloadable reports and charts (future feature roadmap)

## ⚙️ Getting Started

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/automated-kpi-tracker.git
   cd automated-kpi-tracker

2. **Install dependencies:**

   ```bash
    python -m venv venv
    source venv/bin/activate       # macOS/Linux
    venv\\Scripts\\activate        # Windows
    pip install -r requirements.txt

3. **Run the Streamlit app:**

   ```bash
    streamlit run app/kpi_tracker_app.py
   
4. Upload your Excel data and explore KPIs with the interactive dashboard.

## 🔮 Future Enhancements
- Add support for automated scheduling and email/Slack alerts
- Incorporate more sophisticated anomaly detection models (e.g., LSTM)
- Enable export of PDF reports with charts and executive summaries
- Build a multi-user web app with authentication and access controls
