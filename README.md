
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institute

## Business Understanding
Jaya Jaya Institute merupakan institusi pendidikan yang menghadapi permasalahan dalam pengelolaan mahasiswa, khususnya tingginya tingkat mahasiswa yang tidak menyelesaikan studi (dropout).
Hal ini berdampak pada kualitas pendidikan, reputasi institusi, serta efisiensi operasional. Oleh karena itu, diperlukan analisis berbasis data untuk mengidentifikasi faktor-faktor yang mempengaruhi dropout mahasiswa.

### Permasalahan Bisnis
- Tingginya tingkat dropout mahasiswa
- Kurangnya insight terkait faktor penyebab mahasiswa tidak lulus
- Belum adanya sistem monitoring berbasis data

### Cakupan Proyek
- Analisis data mahasiswa
- Data preprocessing (cleaning, encoding, transformasi)
- Pembuatan model machine learning
- Pembuatan dashboard visualisasi

## Persiapan

### 1. Sumber Data
Dataset dapat diunduh melalui link berikut :
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

### 2. Membuat Virtual Environment (venv)
Jalankan perintah berikut di terminal:

python -m venv venv

### 3. Mengaktifkan Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4. Menginstal Dependencies
Gunakan file requirements.txt agar instalasi lebih konsisten:

pip install -r requirements.txt

### 5. Menjalankan Program
Jalankan file berikut untuk melakukan prediksi:

python app.py

---

## Deployment
Aplikasi prediksi dropout mahasiswa telah di-deploy menggunakan Streamlit Cloud dan dapat diakses melalui:
🔗 https://dropout-prediction-rizhan.streamlit.app

---

## Business Dashboard
Dashboard dibuat menggunakan Looker Studio untuk memvisualisasikan faktor-faktor yang mempengaruhi dropout mahasiswa.

Dashboard menampilkan:
- Distribusi status mahasiswa (Dropout vs Graduate)
- Perbandingan nilai semester 1 dan 2
- Jumlah mata kuliah lulus
- Pengaruh status hutang (Debtor)
- Pengaruh pembayaran UKT
- Perbandingan umur mahasiswa

Dashboard ini membantu institusi dalam:
- Mengidentifikasi faktor utama penyebab dropout
- Melihat pola dropout berdasarkan berbagai aspek
- Mendukung pengambilan keputusan berbasis data

Link Dashboard:
https://lookerstudio.google.com/reporting/e8cfa546-1cb8-44c7-adca-387ee672d9e1

---

## Conclusion

Model machine learning telah berhasil dibangun untuk memprediksi kemungkinan mahasiswa mengalami dropout.

### Performa Model
Model Random Forest dibangun menggunakan fitur yang telah dipilih berdasarkan relevansi, yaitu mencakup aspek akademik, finansial, dan demografis mahasiswa.

Model dilatih menggunakan data yang telah difilter (hanya status Dropout dan Graduate) dan menunjukkan performa yang baik dalam mengklasifikasikan kedua kategori tersebut.

Penggunaan fitur yang lebih representatif dibandingkan sebelumnya memungkinkan model menangkap pola yang lebih kompleks dan meningkatkan kualitas prediksi.

### Fitur yang Digunakan
Fitur yang digunakan dalam model ini meliputi:
- Age at Enrollment  
- Debtor  
- Tuition Fees Up To Date  
- Scholarship Holder  
- Gender  
- Admission Grade  
- Nilai dan jumlah mata kuliah lulus pada semester 1 dan 2  

Pemilihan fitur ini dilakukan untuk menjaga keseimbangan antara performa model dan kemudahan implementasi pada aplikasi Streamlit.

### Insight Utama
- Mahasiswa dengan nilai akademik rendah memiliki risiko dropout lebih tinggi
- Jumlah mata kuliah yang sedikit lulus berhubungan dengan kemungkinan dropout
- Mahasiswa dengan status hutang (debtor) lebih rentan mengalami dropout
- Pembayaran UKT yang tidak lancar meningkatkan risiko dropout
- Faktor umur juga menunjukkan pengaruh terhadap status mahasiswa

### Rekomendasi
- Memberikan bimbingan akademik bagi mahasiswa dengan nilai rendah
- Monitoring jumlah mata kuliah lulus sejak semester awal
- Memberikan bantuan finansial atau skema pembayaran fleksibel
- Menerapkan sistem early warning berbasis data
- Melakukan evaluasi berkala terhadap performa mahasiswa
- Fokus intervensi pada semester awal

