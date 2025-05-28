import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Panel de Análisis de Anuncios de Vehículos')

# Botón para mostrar histograma
if st.button('Mostrar histograma de precios'):
    st.write('Distribución de precios de los vehículos')
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig)

# Botón para mostrar gráfico de dispersión
if st.button('Mostrar gráfico de kilometraje vs precio'):
    st.write('Relación entre kilometraje y precio')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)

