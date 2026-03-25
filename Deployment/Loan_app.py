import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Loan_LR.pkl")
scaler = joblib.load("Loan_scaler.pkl")
columns = joblib.load("Loan_columns.pkl")

st.title('Loan Approval Prediction')
st.write("This website will predict whether your loan will be approved or not")

gender = st.selectbox("Gender",["Male","Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
Applicantincome = st.number_input("Applicant Income",value=0)
co_income= st.number_input("CoApplicant Income",value=0)
loan_amount = st.number_input("Loan Amount",value=0)
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

    df_scaled = scaler.transform(df)

    prediction = model.predict(df)[0]

    st.write("FINAL DF")
    st.write(df)

    st.write("SCALED DF")
    st.write(df_scaled)

    st.write("PREDICTION:", prediction)

    if prediction==1:
        st.success("Your Loan will be APPROVED")
    else:
        st.error("Your Loan will be REJECTED")