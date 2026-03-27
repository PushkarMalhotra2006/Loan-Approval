# Loan-Approval



\# 🏦 Loan Approval Prediction App



A machine learning web application that predicts whether a loan application will be approved or rejected based on applicant details.



\---



\## 🚀 Live Demo





\---



\## 📌 Problem Statement



Banks need to evaluate loan applications efficiently. This project predicts loan approval status using applicant information like income, credit history, and loan details.



\---



\## 📊 Dataset



The dataset contains loan application records with features such as:



\* Gender

\* Married

\* Dependents

\* Education

\* Self\_Employed

\* ApplicantIncome

\* CoapplicantIncome

\* LoanAmount \*(in thousands)\*

\* Loan\_Amount\_Term \*(in months)\*

\* Credit\_History

\* Property\_Area

\* Loan\_Status \*(Target)\*



Dataset file:



Dataset/loan-train.csv





\---



\## ⚙️ Preprocessing \& Feature Engineering



\* Handled missing values using mode/median imputation

\* Converted categorical variables to numerical

\* One-hot encoded Property\_Area

\* Created new feature: \*\*Total\_Income\*\*

\* Applied feature scaling using StandardScaler



\---



\## 🤖 Model



\* Logistic Regression



\### 📈 Performance



\* Accuracy: \~0.78

\* F1 Score: \~0.85



\---



\## 🧠 Key Insights



\* Strong dependency on \*\*Credit\_History\*\*

\* Dataset is relatively small (\~600 rows)

\* Model may reject unusual combinations due to data bias



\---



\## 🌐 Application Features



\* 🔹 Single Prediction (manual input)

\* 🔹 Batch Prediction via CSV upload

\* 🔹 Download predictions as CSV

\* 🔹 Built using Streamlit



\---



\## 🛠️ Tech Stack



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Streamlit

\* Joblib



\---



\## 📂 Project Structure



```id="ds2"

Loan-Approval/

│

├── Dataset/

│   └── loan-train.csv

│

├── Loan\_App.py        # Streamlit app

├── d.py               # Testing script

├── loan\_Approval.ipynb

│

├── Loan\_LR.pkl

├── Loan\_scaler.pkl

├── Loan\_columns.pkl

│

├── Requirements.txt

├── README.md

```



\---



\## ▶️ How to Run Locally



```bash id="ds3"

git clone https://github.com/your-username/Loan-Approval.git

cd Loan-Approval

pip install -r Requirements.txt

streamlit run Loan\_App.py

```



\---



\## ⚠️ Important Notes



\* LoanAmount is in thousands (e.g., 150 = ₹1,50,000)

\* Income values are monthly

\* Model performance depends on dataset quality



\---



\## 👨‍💻 Author



Pushkar



\---



⭐ If you found this useful, consider giving a star!



