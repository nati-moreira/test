import streamlit as st

st.header('Jogando uma moeda')

number_of_trails = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executandoo o experimento de {number_of_trails} tentativas.')

st.write('Ainda não é um aplicativo funcional. Em construção')