import pandas as pd

def retention_recommendation(row):
    if row['Churn_Probability'] > 0.7 and row['Balance'] > 50000:
        return "Assign Personal Banker"
    elif row['Churn_Probability'] > 0.7:
        return "Offer Retention Bonus"
    elif row['Churn_Probability'] > 0.5:
        return "Send Engagement Email"
    else:
        return "No Action Needed"

def generate_retention_plan(input_path, output_path):
    df = pd.read_csv(input_path)
    df['Retention_Action'] = df.apply(retention_recommendation, axis=1)
    df.to_csv(output_path, index=False)
    print("✅ Retention plan saved:", output_path)

if __name__ == "__main__":
    generate_retention_plan(
        "data/processed/churn_scored_customers.csv",
        "data/processed/retention_plan.csv"
    )
