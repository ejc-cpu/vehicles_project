# %%
import pandas as pd
import plotly_express as px
import streamlit as st

# %%
car_data = pd.read_csv(r'.\vehicles_us.csv')


st.header('Cuadro de mandos')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('construir grafico de dispersion')
if disp_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
