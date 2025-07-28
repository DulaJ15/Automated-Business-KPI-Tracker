import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet.plot import plot_plotly
import plotly.graph_objs as go
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.kpi_calculations import calculate_basic_kpis, detect_anomalies, forecast_kpi

st.set_page_config(page_title="Automated KPI Tracker", layout="wide")

st.title("📊 Automated Business KPI Tracker")

uploaded_file = st.file_uploader("Upload your KPI Excel file", type=["xlsx", "xls"])

if uploaded_file:
    # Read Excel file
    df = pd.read_excel(uploaded_file)

    # Check required columns
    required_cols = {"Date", "Revenue", "Orders", "New Customers", "Returning Customers"}
    if not required_cols.issubset(df.columns):
        st.error(f"Uploaded file missing required columns: {required_cols}")
    else:
        # Calculate KPIs
        df_kpi = calculate_basic_kpis(df)

        # Detect anomalies on Revenue Growth %
        df_kpi = detect_anomalies(df_kpi, "Revenue Growth %")

        st.subheader("Raw Data with Calculated KPIs")
        st.dataframe(df_kpi)

        # Show anomalies
        st.subheader("🚨 Detected Anomalies in Revenue Growth")
        anomalies = df_kpi[df_kpi["Anomaly"] == True]
        if anomalies.empty:
            st.success("No significant anomalies detected in Revenue Growth %")
        else:
            st.table(anomalies[["Date", "Revenue Growth %"]])

        # KPI summary stats
        st.subheader("KPI Summary Statistics")
        st.write(df_kpi[["Revenue", "Orders", "Revenue Growth %", "Avg Order Size", "Retention %"]].describe())

        # Revenue forecast chart
        st.subheader("📈 Revenue Forecast (Next 4 Weeks)")
        forecast = forecast_kpi(df_kpi, "Revenue", periods=4)

        # Plot with Plotly for interactivity
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode="lines", name="Forecast"))
        fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_upper"], mode="lines", name="Upper Bound", line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_lower"], mode="lines", name="Lower Bound", line=dict(dash='dash')))
        st.plotly_chart(fig, use_container_width=True)

        st.info("⚙️ Upload new Excel files to update the analysis dynamically.")
else:
    st.info("Please upload an Excel file with KPI data to get started.")
