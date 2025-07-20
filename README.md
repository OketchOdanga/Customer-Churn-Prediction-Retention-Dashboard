# 🧠 Customer Churn Prediction & Retention Dashboard

This project is a complete machine learning pipeline designed to **predict bank customer churn** and generate actionable **retention strategies**. It also includes a rich, interactive **dashboard** for customer analytics and SHAP-based explainability.

---

## 🚀 Project Overview

Churn prediction helps businesses identify customers who are likely to leave, enabling proactive retention strategies. This project:

- Trains an XGBoost model to predict churn.
- Generates a churn probability score for each customer.
- Recommends personalized retention actions.
- Explains individual predictions using SHAP.
- Displays an interactive dashboard with filters, insights, and SHAP visualizations.

---

## 🏗️ Project Phases

| Phase | Description |
|-------|-------------|
| **Phase 1** | Data loading, cleaning, feature selection, and model training |
| **Phase 2** | Churn prediction, scoring customers, and saving results |
| **Phase 3** | Generating retention strategy per customer |
| **Phase 4** | SHAP analysis for global and individual prediction explanations |
| **Phase 5** | Streamlit dashboard for filtering, visualizing churn patterns, and inspecting individual customers |

---

## 📊 Dashboard Features

* **Filters**: Geography, Gender, Credit Score, Churn probability
* **KPI Metrics**: Churn Rate, Retention Suggestions
* **SHAP Insights**:

  * Global feature importance
  * Individual customer explanation using SHAP waterfall plot

---

## 🧠 Model Used

* **Model**: XGBoost Classifier
* **Evaluation**: Accuracy, ROC AUC, Confusion Matrix
* **Interpretability**: SHAP values

---

## 🎯 Retention Strategy Logic

Based on churn probability and balance:

| Condition                   | Action                 |
| --------------------------- | ---------------------- |
| Churn > 0.7 & Balance > 50K | Assign Personal Banker |
| Churn > 0.7                 | Offer Retention Bonus  |
| Churn > 0.5                 | Send Engagement Email  |
| Otherwise                   | No Action Needed       |

---

## ✅ Requirements

* Python 3.9+
* Libraries: `xgboost`, `shap`, `pandas`, `streamlit`, `scikit-learn`, `matplotlib`


