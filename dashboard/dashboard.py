import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bank Churn Dashboard", layout="wide")
st.title("📊 Customer Churn Prediction & Retention Strategy")

# Load data
df = pd.read_csv("data/processed/retention_plan.csv")

# KPIs
total_customers = df.shape[0]
churn_rate = df['Actual_Churn'].mean()
high_risk = df[df['Churn_Probability'] > 0.7].shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2%}")
col3.metric("High Risk Customers", high_risk)

# Filters
st.sidebar.header("🔍 Filters")
geo = st.sidebar.multiselect("Geography", options=df["Geography"].unique(), default=df["Geography"].unique())
age_range = st.sidebar.slider("Age Range", int(df.Age.min()), int(df.Age.max()), (25, 60))

filtered_df = df[(df['Geography'].isin(geo)) & (df['Age'].between(*age_range))]

# Show table
st.dataframe(filtered_df[['CustomerId', 'Churn_Probability', 'Balance', 'Age', 'Geography', 'Retention_Action']])

# Allow download
st.download_button("📥 Download Retention Plan", data=filtered_df.to_csv(index=False), file_name="retention_filtered.csv")
