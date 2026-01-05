import streamlit as st
import joblib
import pickle
import re
import numpy as np
from scipy.special import expit, softmax

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Halal Checker",
    page_icon="🍲",
    layout="centered"
)

# --- LOAD MODEL (CACHED) ---
@st.cache_resource
def load_resources():
    try:
        model = joblib.load('halal_classification_linear_svm.pkl')
        with open('tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        st.error("❌ File model tidak ditemukan! Pastikan file .pkl ada di folder yang sama.")
        return None, None

model, vectorizer = load_resources()

# --- PREDICTION LOGIC ---
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    return ' '.join(text.split())

def predict_halal(text):
    if not text or not model:
        return None

    cleaned_text = preprocess_text(text)
    
    # Vectorize
    vector = vectorizer.transform([cleaned_text])
    
    # Predict
    pred_label = model.predict(vector)[0]
    
    # Calculate Confidence
    decision_scores = model.decision_function(vector)
    
    # Handle probabilitas
    if decision_scores.ndim == 1:
        prob_pos = expit(decision_scores[0])
        probabilities = [1 - prob_pos, prob_pos] 
    else:
        probabilities = softmax(decision_scores[0])
    
    classes = model.classes_
    prob_dict = {classes[i]: probabilities[i] for i in range(len(classes))}
    
    status = "HALAL" if pred_label == "halal" else "HARAM"
    confidence = prob_dict[pred_label]
    
    return {
        'status': status,
        'confidence': confidence
    }


st.title("🍲 Cek Halal/Haram")
st.write("Masukkan komposisi bahan makanan di bawah ini:")

# Input Section
input_text = st.text_area("", placeholder="Contoh: Wheat flour, water, salt, pork gelatin...", height=100)

if st.button("CEK SEKARANG", type="primary", use_container_width=True):
    if input_text.strip():
        with st.spinner('Menganalisis...'):
            result = predict_halal(input_text)
            
            if result:
                st.divider()
                st.subheader("Hasil Analisis:")
                
                # Tampilan Sederhana & Jelas
                if result['status'] == 'HALAL':
                    st.success(f"✅ **{result['status']}**")
                else:
                    st.error(f"❌ **{result['status']}**")
                
                # Confidence Score
                st.info(f"Tingkat Keyakinan AI: **{result['confidence']:.2%}**")
            
    else:
        st.warning("⚠️ Masukkan teks bahan dulu.")

# Footer
st.divider()
st.caption("Model: Linear SVM | Akurasi: 98.93%")
