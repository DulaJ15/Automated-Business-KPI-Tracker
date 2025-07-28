import pandas as pd
import numpy as np
from prophet import Prophet


def calculate_basic_kpis(df: pd.DataFrame):
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    df["Revenue Growth %"] = df["Revenue"].pct_change().fillna(0) * 100
    df["Avg Order Size"] = df["Revenue"] / df["Orders"]
    df["Retention %"] = (df["Returning Customers"] / df["New Customers"]).fillna(0) * 100

    return df


def detect_anomalies(df: pd.DataFrame, column: str):
    threshold = 2
    mean = df[column].mean()
    std = df[column].std()
    
    df["Anomaly"] = df[column].apply(lambda x: abs(x - mean) > threshold * std)
    return df


def forecast_kpi(df: pd.DataFrame, column: str, periods=4):
    forecast_df = df[["Date", column]].rename(columns={"Date": "ds", column: "y"})
    model = Prophet()
    model.fit(forecast_df)
    future = model.make_future_dataframe(periods=periods, freq="W")
    forecast = model.predict(future)
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
