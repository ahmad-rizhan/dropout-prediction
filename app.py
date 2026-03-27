
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.joblib')

st.title("Prediksi Dropout Mahasiswa")
st.write("Masukkan data mahasiswa:")

# INPUT USER
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

scholarship_label = st.selectbox(
    "Penerima Beasiswa",
    ["Tidak", "Ya"]
)
scholarship = 1 if scholarship_label == "Ya" else 0

gender_label = st.selectbox(
    "Jenis Kelamin",
    ["Perempuan", "Laki-laki"]
)
gender = 1 if gender_label == "Laki-laki" else 0

admission_grade = st.number_input("Nilai Masuk", 0.0, 20.0, 10.0)

grade1 = st.number_input("Nilai Semester 1", 0.0, 20.0, 10.0)
approved1 = st.number_input("Jumlah Matkul Lulus Semester 1", 0, 20, 5)

grade2 = st.number_input("Nilai Semester 2", 0.0, 20.0, 10.0)
approved2 = st.number_input("Jumlah Matkul Lulus Semester 2", 0, 20, 5)

# PREDICT
if st.button("Predict"):
    input_data = pd.DataFrame(
        [[
            age,
            debtor,
            tuition,
            scholarship,
            gender,
            admission_grade,
            grade1,
            approved1,
            grade2,
            approved2
        ]],
        columns=[
            'Age_at_enrollment',
            'Debtor',
            'Tuition_fees_up_to_date',
            'Scholarship_holder',
            'Gender',
            'Admission_grade',
            'Curricular_units_1st_sem_grade',
            'Curricular_units_1st_sem_approved',
            'Curricular_units_2nd_sem_grade',
            'Curricular_units_2nd_sem_approved'
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Mahasiswa berpotensi LULUS")
    else:
        st.error("Mahasiswa berpotensi DROPOUT")
