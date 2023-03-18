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

years = st.sidebar.slider('What year you wanna see?', 2019, 2021, 2019)

converted_year = str(years)

st.subheader('Jumlah Penduduk dalam ribu')
st.bar_chart(
    df,
    x = "Kota",
    y = converted_year)

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

st.sidebar.title("(still on Tugas 2) Layout")
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


st.title('Tugas 3')

st.write('\n')
st.write('\n')

st.subheader('write and magic')
st.write('this is the test of write')

st.write('\n')
st.write('\n')

st.subheader('Text Elements')
st.markdown('(markdown) My name is **Jovian Chandra Santoso**.')
st.caption('(caption) This is example of caption')
code = '''(codeblock) st.write('my name is Jovian')
    # that's the example of codeblock'''
st.code(code, language='python')

st.write('\n')
st.write('\n')

st.subheader('Data Display Elements')
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


st.write('\n')
st.write('\n')

st.subheader('Chart Element')

st.caption('Jumlah Penduduk dalam ribu')
st.bar_chart(
    df,
    x = "Kota",
    y = converted_year)

st.write('\n')
st.write('\n')

st.subheader('Input Widgets')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.write('\n')
st.write('\n')

st.subheader('Media Element')
st.caption('this is my youtube video, thanks for watching!!')
st.video('https://www.youtube.com/watch?v=y3VNsLCFVG8')

st.write('\n')
st.write('\n')

st.subheader('Layout and Container')
st.write('as u can see there is slider on sidebar thats called sidebar layout')

st.write('\n')
st.write('\n')

st.subheader('Status Element')
st.balloons()
st.success('Helloooooooo!! glad that u here <3', icon="✅")

st.write('\n')
st.write('\n')

st.subheader('Control Flow')
name = st.text_input('Name')
if not name:
  st.warning('try fill the blank and press enter, several datas will appear!!')
  st.stop()
st.success('Yeahhhhhh u see that balooon??!!')

st.write('\n')
st.write('\n')

st.subheader('Utilities')
with st.echo():
    st.write('This code will be printed')
    
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.experimental_show(dataframe)