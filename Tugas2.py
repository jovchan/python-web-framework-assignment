import streamlit as st
import pandas as pd
import numpy as np

st.title("Tugas 2")

st.subheader("Line-chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.subheader("Widget")
df = pd.DataFrame({
    'first column': [2019, 2020, 2021]
    })

option = st.selectbox(
    'Which year you wanna see?',
     df['first column'])

st.sidebar.title("Layout")
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.subheader('Connection with googlesheet')
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

st.bar_chart(df)
