import streamlit as st
import pandas as pd
import numpy as np

st.title("Tugas 1")

st.subheader('Data Penduduk dalam ribuan tahun 2019-2021')
df = pd.DataFrame(
    [
        {"Kota": "Jakarta Utara", "2019" : 1812, "2020": 1778, "2021": 1784},
        {"Kota": "Jakarta Pusat", "2019" : 928, "2020": 1056, "2021": 1066},
        {"Kota": "Jakarta Barat", "2019" : 2589, "2020": 2434, "2021": 2440},
        {"Kota": "Jakarta Timur", "2019": 2937, "2020": 3037, "2021": 3056},
        {"Kota": "Jakarta Selatan", "2019" : 2264, "2020": 2226, "2021": 2233},
    ]
)
st.dataframe(df, use_container_width=True)

years = st.slider('What year you wanna see?', 2019, 2021, 2019)

converted_year = str(years)

st.subheader('Jumlah Penduduk dalam ribu')
st.bar_chart(
    df,
    x = "Kota",
    y = converted_year)