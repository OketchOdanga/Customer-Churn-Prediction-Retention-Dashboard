import pandas as pd
import streamlit as st
import shap
import matplotlib.pyplot as plt
import seaborn as sns

# Load the final merged data
df = pd.read_csv("data/processed/retention_with_shap.csv")

# Identify SHAP value columns (skip original features)
feature_cols = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
shap_cols = [col for col in df.columns if col not in feature_cols + ['CustomerId', 'Surname', 'Churn_Probability', 'Retention_Action', 'Exited']]

# Configure Streamlit
st.set_page_config(page_title="Churn & Retention Dashboard", layout="wide")
st.title("📊 Customer Churn Prediction & Retention Strategy")

# Sidebar Filters
st.sidebar.header("🔎 Filter Customers")
geo = st.sidebar.multiselect("Geography", df["Geography"].unique(), default=df["Geography"].unique())
gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
age_range = st.sidebar.slider("Age Range", int(df["Age"].min()), int(df["Age"].max()), (30, 50))

filtered = df[
    (df["Geography"].isin(geo)) &
    (df["Gender"].isin(gender)) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

# KPIs
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(filtered))
col2.metric("Avg Churn Risk", f"{filtered['Churn_Probability'].mean():.2%}")
col3.metric("High Risk ( >70%)", (filtered['Churn_Probability'] > 0.7).sum())

# Table View
st.subheader("📋 Retention Plan Table")
st.dataframe(filtered[["CustomerId", "Geography", "Gender", "Age", "Balance", "Churn_Probability", "Retention_Action"]])

# Global SHAP Importance
st.subheader("📈 Global Feature Importance (SHAP)")
mean_shap = filtered[shap_cols].abs().mean().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=mean_shap.values, y=mean_shap.index, palette="viridis", ax=ax)
ax.set_title("Mean Absolute SHAP Values")
st.pyplot(fig)

# Individual SHAP Explanation
st.subheader("🧠 Individual Prediction Explanation")
selected_id = st.selectbox("Choose a Customer ID", filtered["CustomerId"].unique())
row = filtered[filtered["CustomerId"] == selected_id]
shap_values = row[shap_cols].values.flatten()

explainer = shap.Explanation(
    values=shap_values,
    base_values=0,  # Approximate, real model base value can be passed if needed
    data=row[feature_cols].values,
    feature_names=feature_cols
)

fig2 = shap.plots.waterfall(explainer, show=False)
st.pyplot(bbox_inches="tight")

# Download filtered data
st.download_button("📥 Download Filtered Results", filtered.to_csv(index=False), "filtered_retention.csv")
