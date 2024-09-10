import pandas as pd
import streamlit as st
import plotly.express as px 

car_data = pd.read_csv('./vehicles_us.csv')

st.header('Venta de vehículos')

car_data[['paint_color', 'is_4wd', 'model_year']] = car_data[['paint_color', 'is_4wd', 'model_year']].fillna(0)

boton_histograma = st.button('Click aquí para dibujar el histograma')

if boton_histograma:

        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        fig = px.histogram(car_data, x="odometer")

        fig.show() # crear un histograma
        st.plotly_chart(fig)

boton_grafico_dispersion = st.button('Click aquí para dibujar el grafico de dispersion')

if boton_grafico_dispersion:
        
        st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

        fig = px.scatter(car_data, x="odometer", y="price")

        fig.show() # crear un gráfico de dispersión
        st.plotly_chart(fig)




        
        












