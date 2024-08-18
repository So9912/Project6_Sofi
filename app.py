import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv ('vehicles_us.csv')

print(car_data)
st.header("Autos en EEUU")

hist_button = st.button('Construir Histograma')
scatter_plot_button = st.button('Construir grafico de dispersion')

if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos.')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width = True)
    
if scatter_plot_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos.')
    fig = px.scatter(car_data, x="odometer", y="price", title='Gráfico de dispersión entre odómetro y precio')
    st.plotly_chart(fig, use_container_width=True)
