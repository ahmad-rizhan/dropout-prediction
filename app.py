import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.joblib')

st.title("Prediksi Dropout Mahasiswa")

st.write("Masukkan data mahasiswa:")

# Input user
age = st.number_input("Age at Enrollment", 15, 70, 20)

debtor_label = st.selectbox(
    "Status Hutang",
    ["Tidak Punya Hutang", "Punya Hutang"]
)
debtor = 0 if debtor_label == "Tidak Punya Hutang" else 1

tuition_label = st.selectbox(
    "Status Pembayaran UKT",
    ["Belum Lunas", "Lunas"]
)
tuition = 0 if tuition_label == "Belum Lunas" else 1

grade1 = st.number_input("Nilai Semester 1", 0.0, 20.0, 10.0)
grade2 = st.number_input("Nilai Semester 2", 0.0, 20.0, 10.0)

# Tombol prediksi
if st.button("Predict"):
    input_data = pd.DataFrame(
        [[age, debtor, tuition, grade1, grade2]],
        columns=[
            'Age_at_enrollment',
            'Debtor',
            'Tuition_fees_up_to_date',
            'Curricular_units_1st_sem_grade',
            'Curricular_units_2nd_sem_grade'
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Mahasiswa berpotensi DROPOUT")
    else:
        st.success("Mahasiswa berpotensi LULUS")
