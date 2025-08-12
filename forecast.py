import streamlit as st
import pandas as pd
import numpy as np

# Page setup
st.set_page_config(page_title="Energy Forecasting App", layout="centered")

# Title and description
st.title("🔋 Energy Forecasting App")
st.markdown("""
Upload your energy usage data as a CSV file.  
This app will display the data and generate a simple forecast using simulated values.
""")

# File uploader
uploaded_file = st.file_uploader("📁 Upload CSV File", type=["csv"])

# If a file is uploaded
if uploaded_file:
    # Read the CSV
    df = pd.read_csv(uploaded_file)

    # Show uploaded data
    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # Forecast logic: add random noise to numeric columns
    st.subheader("📈 Simulated Forecast")
    forecast_df = df.copy()
    numeric_cols = forecast_df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        forecast_df[col] = forecast_df[col] + np.random.normal(loc=0, scale=5, size=len(forecast_df))

    st.dataframe(forecast_df.head())

    st.success("✅ Forecast generated successfully!")

else:
    st.info("Please upload a CSV file to begin.")

