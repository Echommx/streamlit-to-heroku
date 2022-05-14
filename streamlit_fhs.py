import streamlit as st
import joblib
import pandas as pd
st.write("# Mortality Prediction in Elderly Patients with AKD")

col1, col2, col3 = st.columns(3)

# getting user inputgender = col1.selectbox("Enter your gender",["Male", "Female"])

Age = col1.number_input("Age")
BMI = col2.number_input("BMI")
Gender = col3.selectbox("Gender(0:Male;1:Female)", ["0", "1"])
Ethnicity = col1.selectbox("Ethnicity(0:White;1:Black;2:Asian;3:Other)", ["0", "1", "2", "3"])
Aki_stage = col2.selectbox("Aki_stage(1:I;2:II;3:III)", ["1", "2", "3"])
Sepsis = col3.selectbox("Sepsis(0:False;1:True)", ["0", "1"])
Hypertension = col1.selectbox("Hypertension(0:False;1:True)", ["0", "1"])
Diabetes_mellitus = col2.selectbox("Diabetes_mellitus(0:False;1:True)", ["0", "1"])
Cerebrovascular_disease = col3.selectbox("Cerebrovascular_disease(0:False;1:True)", ["0", "1"])
CHF = col1.selectbox("CHF(0:False;1:True)", ["0", "1"])
CKD = col2.selectbox("CKD(0:False;1:True)", ["0", "1"])
MV = col3.selectbox("MV(0:False;1:True)", ["0", "1"])
RRT = col1.selectbox("RRT(0:False;1:True)", ["0", "1"])
Renal_toxic_drugs = col2.selectbox("Renal_toxic_drugs(0:False;1:True)", ["0", "1"])
Vasopressor_use = col3.selectbox("Vasopressor_use(0:False;1:True)", ["0", "1"])

GCS_score = col1.number_input("GCS score")
Delta_GCS_score = col2.number_input("Delta_GCS score")
SOFA_score = col3.number_input("SOFA score")

Delta_SOFA_score = col1.number_input("Delta SOFA score")
Heart_rate = col2.number_input("Heart rate")
Delta_heart_rate = col3.number_input("Delta heart rate")

SBP = col1.number_input("SBP")
Delta_SBP = col2.number_input("Delta SBP")
DBP = col3.number_input("DBP")


Delta_DBP = col1.number_input("Delta DBP")
MAP = col2.number_input("MAP")
Delta_MAP = col3.number_input("Delta MAP")

Temperature = col1.number_input("Temperature")
Delta_Temperature = col2.number_input("Delta Temperature")
Respiratory_rate = col3.number_input("Respiratory rate")

Delta_Respiratory_rate = col1.number_input("Delta Respiratory rate")
SpO2 = col2.number_input("SpO2")
Delta_SpO2 = col3.number_input("Delta SpO2")



df_pred = pd.DataFrame([[Age, BMI, Gender, Ethnicity, Aki_stage, Sepsis,
                         Hypertension, Renal_toxic_drugs, MV, Diabetes_mellitus,
                         Cerebrovascular_disease, CHF, CKD, RRT, GCS_score,
                         SOFA_score, Delta_GCS_score, Delta_SOFA_score, Vasopressor_use,
                         Heart_rate, SBP, DBP, MAP, Temperature, SpO2,
                         Respiratory_rate, Delta_Respiratory_rate, Delta_SBP, Delta_DBP,
                         Delta_MAP, Delta_heart_rate, Delta_Temperature, Delta_SpO2]],

columns = ['Age', 'BMI', 'Gender', 'Ethnicity', 'Aki_stage', 'Sepsis', 'Hypertension',
           'Renal_toxic_drugs', 'MV', 'Diabetes_mellitus', 'Cerebrovascular_disease', 'CHF',
           'CKD', 'RRT', 'GCS_score', 'SOFA_score', 'Delta_GCS_score', 'Delta_SOFA_score', 'Vasopressor_use',
           'Heart_rate', 'SBP', 'DBP', 'MAP', 'Temperature', 'SpO2', 'Respiratory_rate', 'Delta_Respiratory_rate',
           'Delta_SBP', 'Delta_DBP', 'Delta_MAP', 'Delta_heart_rate', 'Delta_Temperature', 'Delta_SpO2'])

model = joblib.load ('svmbest_clf_model.pkl')
prediction = model.predict(df_pred)
if st.button('Predict'):

    if(prediction[0]==0):
        st.write('<p class="big-font">Survival.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">Death.</p>',unsafe_allow_html=True)

