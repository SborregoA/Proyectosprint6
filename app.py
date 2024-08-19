import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Venta de coches')

print(car_data.head(15))

build_histogram = st.checkbox('Construir histograma') # casilla de selección

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir un diagrama de dispersión') # casilla de selección

if build_disp:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig2 = px.scatter(car_data, y="odometer")
    
    st.plotly_chart(fig2, use_container_width=True)
    