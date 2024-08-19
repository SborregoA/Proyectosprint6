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
    fig = px.histogram(car_data, x="odometer",title= 'Distribución de kilometraje de carro')
    fig.update_layout(xaxis_title="Kilometraje", yaxis_title="Frecuencia")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir un diagrama de dispersión') # casilla de selección

if build_disp:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    fig2 = px.scatter(car_data, x="odometer", y='price', title= 'Diagrama de dispersión que relaciona el odometro y precio')
    fig2.update_layout(xaxis_title="Kilometraje", yaxis_title="Precio")
    
    st.plotly_chart(fig2, use_container_width=True)
    