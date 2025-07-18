import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Drop unused columns
    df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

    # Encode categorical features
    label_encoders = {}
    for col in ['Gender', 'Geography']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df

if __name__ == "__main__":
    df_clean = preprocess_data("data/raw/BankChurners.csv")
    df_clean.to_csv("data/processed/cleaned_bank_churn.csv", index=False)
    print("✅ Data cleaned and saved to processed folder.")
