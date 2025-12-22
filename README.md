# 🥗 Halal Food Classification 

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Type](https://img.shields.io/badge/Submission-UAS%20Data%20Science-red)

> **PROJECT SUBMISSION**
> **Mata Kuliah:** Peminatan Data Science


---

## 📌 Project Overview (Gambaran Proyek)
Proyek ini dikembangkan untuk membangun sistem otomatisasi verifikasi status halal produk makanan kemasan berbasis **Machine Learning**. Model ini dilatih untuk membaca komposisi bahan (*ingredients list*) dalam format teks dan mengklasifikasikannya ke dalam dua kategori: **Halal** atau **Haram**. 

### 🎯 Tujuan Utama
1.  Membangun model klasifikasi teks dengan akurasi tinggi (>90%) menggunakan algoritma **Linear SVM**.
2.  Mengimplementasikan teknik **TF-IDF** dan **N-Gram**.
3.  Menyediakan simulasi *deployment* berupa fungsi prediksi interaktif.

---

## 📊 Dataset
Data yang digunakan bersumber dari repositori publik Kaggle:
* **Nama Dataset:** List of food ingredients with halal label
* **Jumlah Data:** 528.092 baris
* **Fitur:** `text` (komposisi bahan) dan `label` (halal/haram)
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

Repositori ini terdiri dari 2 notebook utama:

1.  **`Training_Evaluasi_Klasifikasi_Haram_Halal.ipynb`**
    * Dokumentasi lengkap proses Data Science: EDA, Preprocessing, Training, hingga Evaluasi Grafik.
2.  **`Halal_Checker_Deployment.ipynb`**
    * Simulasi implementasi model.
    * Memuat fungsi interaktif *Halal Checker* untuk pengujian data baru.

---

## 🚀 How to Use (Cara Menggunakan)

1.  Buka file notebook `Halal_Checker_Deployment.ipynb` (disarankan menggunakan **Google Colab**).
2.  Jalankan semua sel kode untuk memuat model.
3.  Pada bagian input interaktif, masukkan daftar bahan produk (Bahasa Inggris).
4.  Sistem akan menampilkan status **HALAL/HARAM** beserta tingkat keyakinannya (*Confidence Score*).

**Contoh Input:**
wheat flour, water, salt, yeast, sugar

**Contoh Output:**
✅ STATUS: HALAL (Confidence: 69.23%)

---

## 👤 Identitas Mahasiswa 

Syifa Auliyah Kusumawardani (11230910000114)

