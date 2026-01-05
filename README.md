# 🥗 Halal Food Classification

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B)
![Type](https://img.shields.io/badge/Submission-UAS%20Data%20Science-red)

> **FINAL PROJECT**
> **Mata Kuliah:** Peminatan Data Science

---

## 📌 Project Overview (Gambaran Proyek)
Proyek ini dikembangkan untuk membangun sistem otomatisasi verifikasi status halal produk makanan kemasan berbasis **Machine Learning**. Model ini dilatih untuk membaca komposisi bahan (*ingredients list*) dalam format teks dan mengklasifikasikannya ke dalam dua kategori: **Halal** atau **Haram**.

### 🎯 Tujuan Utama
1.  Membangun model klasifikasi teks dengan akurasi tinggi (>90%) menggunakan algoritma **Linear SVM**.
2.  Mengimplementasikan teknik **TF-IDF** dan **N-Gram**.
3.  Menyediakan aplikasi web (**Streamlit**) untuk simulasi.

---

## 📊 Dataset
Dataset yang digunakan dalam proyek ini tidak disertakan dalam repositori karena ukurannya yang besar. Anda dapat mengunduh dataset asli melalui tautan berikut:
* **Sumber:** [Kaggle - List of food ingredients with halal label](https://www.kaggle.com/datasets/irfanakbarihabibi/list-of-food-ingredients-with-halal-label)
* **Nama File:** `2024-feb-final.csv`
* **Jumlah Data:** 528.092 baris
* **Distribusi:** Balanced (55.3% Halal : 44.7% Haram)

---

## 🛠️ Methodology (Metodologi)

### 1. Data Preprocessing
* **Case Folding:** Mengubah teks menjadi huruf kecil (*lowercase*).
* **Cleaning:** Menghapus tanda baca, angka, dan simbol menggunakan *Regular Expression (Regex)*.
* **Whitespace Removal:** Menghapus spasi berlebih.

### 2. Feature Engineering
* **TF-IDF Vectorization:** Mengubah teks menjadi representasi numerik.
* **N-Gram (1,2):** Mengambil kombinasi unigram dan bigram untuk menangkap konteks frasa.
* **Feature Selection:** Membatasi 3.000 fitur terpenting untuk efisiensi komputasi.

### 3. Modeling
Algoritma yang digunakan dan dibandingkan:
* Logistic Regression
* Multinomial Naive Bayes
* Random Forest
* **Linear Support Vector Machine (SVM) 🏆 (Best Model)**

---

## 📈 Results (Hasil Evaluasi)

Berdasarkan hasil pengujian pada data uji (20%), **Linear SVM** terpilih sebagai model terbaik:

| Metric | Score |
| :--- | :--- |
| **Accuracy** | **98.93%** |
| **Precision** | 99% |
| **Recall (Haram)** | 98% |
| **Training Time** | ~18 detik |

---

## 📂 File Structure (Struktur File)

File penting dalam repositori ini:

* `app.py`: Source code utama aplikasi web (Streamlit).
* `Training_Evaluasi_Klasifikasi_Haram_Halal.ipynb`: Notebook berisi proses training, EDA, dan evaluasi model.
* `halal_classification_linear_svm.pkl`: Model SVM yang sudah dilatih (disimpan).
* `tfidf_vectorizer.pkl`: Vectorizer TF-IDF yang sudah dilatih (disimpan).

---

## 🚀 How to Run (Cara Menjalankan)

Anda bisa menjalankan proyek ini dengan dua cara: menggunakan Website (Streamlit) atau Notebook.

### Opsi 1: Menjalankan Aplikasi Web (Streamlit)
Pastikan Anda sudah menginstall Python dan library yang dibutuhkan.

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/syifaauliyahk/Halal-Food-Classification.git]
    cd Halal-Food-Classification
    ```

2.  **Install library:**
    ```bash
    pip install streamlit scikit-learn pandas joblib scipy
    ```

3.  **Jalankan aplikasi:**
    ```bash
    streamlit run app.py
    ```
4.  Aplikasi akan otomatis terbuka di browser Anda (biasanya di `http://localhost:8501`).

### Opsi 2: Menggunakan Notebook (Google Colab)
1.  Buka file `Training_Evaluasi_Klasifikasi_Haram_Halal.ipynb` di Google Colab.
2.  Upload dataset ke environment Colab.
3.  Jalankan semua sel (*Run All*) untuk melatih model dari awal.

---

## 👤 Identitas Mahasiswa

**Syifa Auliyah Kusumawardani**
* **NIM:** 11230910000114
* **Program Studi:** Teknik Informatika
* **Fakultas:** Sains dan Teknologi, UIN Syarif Hidayatullah Jakarta
