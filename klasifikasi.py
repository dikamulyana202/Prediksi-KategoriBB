import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('cl-obesitas.sav', 'rb'))

st.title('Prediksi berat badan')
Age = st.number_input('Umur Pasien')
Gender = st.number_input('Jenis Kelamin (1 = Pria; 0 = perempuan)')
Height = st.number_input('Tinggi Badan ')
Weight = st.number_input('Berat Badan')
BMI = st.number_input('Index Massa tubuh')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Age, Gender, Height, Weight, BMI]])

    if (prediksi[0] == 0):
        prediksi = 'kategori berdat badan orang tersebut ialah Normal'
    elif (prediksi == 1):
        prediksi = 'kategori berdat badan orang tersebut ialah Obesitas'
    elif (prediksi == 2):
        prediksi = 'kategori berdat badan orang tersebut ialah berat'
    else:
        prediksi = 'kategori berdat badan orang tersebut ialah kurus'

st.success(prediksi)
