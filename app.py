import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Import sklearn setelah package lain
try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
except ImportError:
    st.error("Error: Tidak dapat mengimport sklearn. Pastikan scikit-learn terinstal dengan benar.")
    st.stop()

# Lanjutkan dengan kode Anda
try:
    model_klasifikasi = pickle.load(open('model_klasifikasi.pkl', 'rb'))
except FileNotFoundError:
    st.error("File model_klasifikasi.pkl tidak ditemukan")
    st.stop()

st.title("Aplikasi Prediksi Stunting Anak")

st.sidebar.header("Masukkan Data Anak")
def user_input_features():
    Umur_bulan = st.sidebar.slider("Umur (bulan)", 0, 60)
    Jenis_Kelamin = st.sidebar.selectbox("Jenis Kelamin", (1,2))
    Tinggi_Badan_cm = st.sidebar.slider("Tinggi Badan (cm)", 0, 100)
    Status_Gizi = st.sidebar.selectbox("Status Gizi", (0,1,2,3))
    
    data = {
        'Umur_bulan': Umur_bulan,
        'Jenis_Kelamin': Jenis_Kelamin,
        'Tinggi_Badan_cm': Tinggi_Badan_cm,
        'Status_Gizi': Status_Gizi
    }
    return pd.DataFrame(data, index=[0])
