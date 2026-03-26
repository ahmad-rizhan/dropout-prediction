
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.joblib')

st.title("Prediksi Dropout Mahasiswa")

st.write("Masukkan data mahasiswa:")

age = st.number_input("Age at Enrollment", 15, 70, 20)
debtor = st.selectbox("Debtor", [0,1])
tuition = st.selectbox("Tuition Fees Up to Date", [0,1])
grade1 = st.number_input("Nilai Semester 1", 0.0, 20.0, 10.0)
grade2 = st.number_input("Nilai Semester 2", 0.0, 20.0, 10.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
    'Age at enrollment': [age],
    'Debtor': [debtor],
    'Tuition fees up to date': [tuition],
    'Curricular units 1st sem (grade)': [grade1],
    'Curricular units 2nd sem (grade)': [grade2]
})

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Mahasiswa berpotensi LULUS")
    else:
        st.error("Mahasiswa berpotensi DROPOUT")
