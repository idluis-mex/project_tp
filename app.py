import streamlit as st 
import pandas as pd
import plotly.graph_objects as go 


df= pd.read_csv('data/vehicles_us.csv')


st.header('Bienvenido a esta aplicacion de graficos', divider='orange' )

st.header('Con este boton crearas un grafico de histograma sobre la relacion del odometro y los precios de los autos')

#creamos el primer grafico
boton_de_histograma = st.button('Construir un histograma')

if boton_de_histograma:

	#Escribe un mensaje en la aplicacion
	st.write('Creando un histograma en la aplicacion')

	#crear el graifo histograma

	fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
	fig.update_layout(title_text='Distribución del Odómetro')

	st.plotly_chart(fig, use_container_width=True)

#Creamos un segundo grafico

st.header('Crea un grafico de dispersion de la relacion del precio y Odometro ')

boton_de_scatterplot= st.button('Crear un grafico de dispersion ')

if boton_de_scatterplot:

	#Escribe un mensaje en la aplicacion
	st.write('Estamos creando el graifco ')

	#crea el grafico
	fig = go.Figure(data=[go.Scatter(x=df['odometer'], y=df['price'], mode='markers')])
	fig.update_layout(title_text='Relación entre Odómetro y Precio')

	st.plotly_chart(fig, use_container_width=True)

st.header('Con el siguiente checkbox se crea un garfico de la caja para ver la distribucion de precios de acuerdo al tipo de auto')
#Creamos un tercer grafico 

boton_de_grfico_de_caja= st.checkbox('Este botn crea un grafico de caja')

if boton_de_grfico_de_caja:
	st.write('Estamos creando un grafico de caja para ti ')

	#creamos el grafico 
	fig = go.Figure(data=[go.Box(x=df['type'], y=df['price'])])
	fig.update_layout(title_text='Distribución de precios en relación al tipo de autos')

	st.plotly_chart(fig, use_container_width=True)




