import joblib
import pandas as pd

print("Starting test...")

model = joblib.load("Loan_LR.pkl")
scaler = joblib.load("Loan_scaler.pkl")
columns = joblib.load("Loan_columns.pkl")

print("Files loaded")

input_dict = {
    "Gender": 1,
    "Married": 1,
    "Dependents": 0,
    "Education": 0,
    "Self_Employed": 0,
    "ApplicantIncome": 6000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 150,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area_Semiurban": 0,
    "Property_Area_Urban": 1
}

df = pd.DataFrame([input_dict])

df["Total_Income"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

for col in columns:
    if col not in df:
        df[col] = 0

df = df[columns]

df_scaled = scaler.transform(df)

prediction = model.predict(df_scaled)

print("Prediction:", prediction)

print("D.PY COEF:", model.coef_)