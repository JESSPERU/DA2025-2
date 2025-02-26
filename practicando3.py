import streamlit as st

#funcion para clasificar el puntaje 
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "excelent"
    elif puntaje >= 70 :
        return "bueno"
    else:
        return "necesitas mejorar amigo"

#INTERFAZ EN STREAMLIT

st.title("Clasificacion de puntaje... chan!")

st.write("Ingresa un puntaje y el sistema lo calificara")

#entrada de usario

puntaje = st.number_input("Ingresa un puntaje (0-100):", min_value=0, max_value=100, step=1)

#boton para clasificar

if st.button("clasificar"):
    resultado = clasificar_puntaje(puntaje)
    st.success(f"el puntaje {puntaje} es clasificado como: {resultado}")
