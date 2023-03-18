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