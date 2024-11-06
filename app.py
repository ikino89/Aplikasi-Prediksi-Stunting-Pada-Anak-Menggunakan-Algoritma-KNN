import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import KNeighborsClassifier
from sklearn.model_selection import train_test_split

st.title("Aplikasi Prediksi Stunting Anak")

st.sidebar.header("Masukkan Data Anak")
def user_input_features():
    Umur_bulan = st.sidebar.slider("Umur (bulan)", 0, 60)
    Jenis_Kelamin = st.sidebar.selectbox("Jenis Kelamin", (1, 2))
    Tinggi_Badan_cm = st.sidebar.slider("Tinggi Badan (cm)", 0, 100)
    Status_Gizi = st.sidebar.selectbox("Status Gizi", (0, 1, 2, 3))
    return pd.DataFrame({'Umur_bulan': [Umur_bulan],
                         'Jenis_Kelamin': [Jenis_Kelamin],
                         'Tinggi_Badan_cm': [Tinggi_Badan_cm],
                         'Status_Gizi': [Status_Gizi]})

try:
    # Load the model
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model tidak ditemukan. Pastikan file model.pkl ada di direktori yang benar.")
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")
