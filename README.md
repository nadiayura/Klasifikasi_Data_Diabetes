### Perbandingan Klasifikasi Diabetes Menggunakan Algoritma Decision Tree Dengan Confusion Matrix 

### 1. Dataset  
Data yang digunakan dalam proyek ini adalah dataset diabetes yang diambil dari Kaggle. Dataset ini memiliki fitur seperti kadar glukosa, tekanan darah, dan lainnya. Ada juga fitur **Outcome** sebagai target untuk menentukan apakah seseorang menderita diabetes atau tidak. Fitur-fitur pada dataset diabetes adalah sebagai berikut:
- **Pregnancies**: Jumlah kehamilan
- **Glucose**: Kadar glukosa
- **BloodPressure**: Tekanan darah
- **SkinThickness**: Ketebalan kulit
- **Insulin**: Tingkat insulin
- **BMI**: Indeks Massa Tubuh (Body Mass Index)
- **DiabetesPedigreeFunction**: Fungsi riwayat diabetes
- **Age**: Usia
- **Outcome**: Hasil diagnosis diabetes (1 jika positif diabetes, 0 jika negatif)

### 2. Algoritma  
Algoritma **Decision Tree** digunakan untuk membangun model klasifikasi dalam bentuk pohon keputusan, di mana setiap cabang mewakili aturan yang diterapkan pada fitur dataset, dan setiap daun mewakili hasil prediksi.

### 3. Teknik Evaluasi  
- **Tanpa Menggunakan Teknik Prune**
  - Akurasi dihitung dengan membandingkan prediksi yang dihasilkan oleh model dengan nilai sebenarnya dari data uji. Berdasarkan pengujian, model Decision Tree ini memiliki tingkat akurasi sebesar **71.81%**.
  - **Confusion Matrix** digunakan untuk menggambarkan performa klasifikasi dengan menampilkan jumlah prediksi yang benar dan salah untuk setiap kelas.

- **Menggunakan Teknik Prune**
  - Akurasi dihitung dengan membandingkan prediksi yang dihasilkan oleh model dengan nilai sebenarnya dari data uji. Teknik pruning membatasi kedalaman pohon dan jumlah cabang, mengurangi overfitting. Meskipun ini dapat menyebabkan sedikit penurunan akurasi pada data uji dibandingkan dengan model tanpa pruning, model menjadi lebih sederhana dan lebih baik dalam generalisasi. Berdasarkan pengujian, model Decision Tree ini memiliki tingkat akurasi sebesar **73.83%**.
  - **Confusion Matrix** digunakan untuk mengevaluasi performa klasifikasi dengan cara yang sama seperti pada model tanpa pruning. Dengan pruning, matriks ini biasanya menunjukkan distribusi prediksi yang lebih seimbang karena model tidak terlalu fokus pada pola spesifik dari data latih.

### 4. Visualisasi Decision Tree  
- **Tanpa Menggunakan Teknik Prune**  
  ![image](https://github.com/user-attachments/assets/a4c38b52-7e76-45a7-a184-6a904d394b58)

- **Menggunakan Teknik Prune**  
  ![image](https://github.com/user-attachments/assets/cf56fc29-5ff4-4eb0-8ceb-253321a05be1)
