import streamlit as st

#titulo de la app
st.title("Hola qué haces?")

#Solocotar nombre
nombre = st.text_input("¿Wanxito, me quieres?")

#mostrar saludo
if nombre:
    st.write("Muy bien, mucho mucho <3")
                      