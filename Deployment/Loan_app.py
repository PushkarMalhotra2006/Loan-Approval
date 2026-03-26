import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Loan_LR.pkl")
scaler = joblib.load("Loan_scaler.pkl")
columns = joblib.load("Loan_columns.pkl")

st.title('Loan Approval Prediction')
st.write("This website will predict whether your loan will be approved or not")

st.header("📂 Batch Prediction")

uploaded_file = st.file_uploader("Upload CSV for batch prediction", type=["csv"])
if uploaded_file is not None:
    df_test = pd.read_csv(uploaded_file)

    df_test["Gender"] = df_test["Gender"].map({"Male":1, "Female":0})
    df_test["Married"] = df_test["Married"].map({"Yes":1, "No":0})
    df_test["Dependents"] = df_test["Dependents"].replace("3+", 3).astype(int)
    df_test["Education"] = df_test["Education"].map({"Not Graduate":1, "Graduate":0})
    df_test["Self_Employed"] = df_test["Self_Employed"].map({"Yes":1, "No":0})
    df_test["Credit_History"] = df_test["Credit_History"].fillna(0)
    df_test["Property_Area_Semiurban"] = (df_test["Property_Area"] == "Semiurban").astype(int)
    df_test["Property_Area_Urban"] = (df_test["Property_Area"] == "Urban").astype(int)

    df_test["Total_Income"] = df_test["ApplicantIncome"] + df_test["CoapplicantIncome"]

    for col in columns:
        if col not in df_test.columns:
            df_test[col] = 0

    df_test = df_test[columns]
    df_test = df_test.values

    df_scaled = scaler.transform(df_test)

    preds = model.predict(df_scaled)

    df_test["Prediction"] = preds.map({1: "Approved", 0: "Rejected"})

    st.write(df_test)
    
    st.write("Download Here 🔽")
    st.download_button(
        "Download Results",
        df_test.to_csv(index=False),
        file_name="loan_predictions.csv"
    )

st.divider()

st.header("🧾 Single Prediction")

gender = st.selectbox("Gender",["Male","Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
Applicantincome = st.number_input("Applicant Income",value=0)
co_income= st.number_input("CoApplicant Income",value=0)
loan_amount = st.number_input("Loan Amount (In Thousands)",value=0)
loan_term = st.number_input("Loan Amount Term",value=0)
credit_history = st.selectbox("Credit History", ["Good", "Bad"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Predict"):
    
    input_df = {
        "Gender": 1 if gender == "Male" else 0,
        "Married": 1 if married == "Yes" else 0,
        "Dependents": 3 if dependents == "3+" else int(dependents),
        "Education": 1 if education == "Not Graduate" else 0,
        "Self_Employed": 1 if self_employed == "Yes" else 0,
        "ApplicantIncome": Applicantincome,
        "CoapplicantIncome": co_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": 1 if credit_history == "Good" else 0,
        "Property_Area_" + property_area:1
    }

    df = pd.DataFrame([input_df])

    df["Total_Income"]= df["ApplicantIncome"] + df["CoapplicantIncome"]

    for col in columns:
        if col not in df.columns:
            df[col]=0

    df= df[columns]
    df = df.values

    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]

    if prediction==1:
        st.success("Your Loan will be APPROVED ✅")
    else:
        st.error("Your Loan will be REJECTED ❌")