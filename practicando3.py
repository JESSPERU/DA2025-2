import streamlit as st

#funcion para clasificar el puntaje 
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "excelent"
    elif puntaje >= 70 :
        return "bueno"
    else:
        return "necesitas mejorar amigo"

#menu lateral
st.sidebar.title("menu de bavegacion")
opcion = st.sidebar.selectbox("lecciona una opcion",  ["inicio","Clasificacion de puntaje... chan!"])

#seccion inciio
if opcion == "inicio":
    st.title("bienvenido a la app")
    st.write("mueva el deslizador para ver como se clasifica el puntaje en tiempo real")

#seccion clasifciacon del puntaje

elif opcion ==  "Clasificacion de puntaje... chan!":
    st.title("Clasificacion de puntaje... chan!")
    st.write("Ingresa un puntaje y el sistema lo calificara")

    #iltro despazable
    puntaje_slider = st.slider("Selecciona un puntaje: ",0,100,50)

    #mostrar la claifi en tiempo real
    st.info(f"el puntaje {puntaje_slider} es clasificado como : **{clasificar_puntaje(puntaje_slider)}** ")

    #entrada de usario

    puntaje = st.number_input("Ingresa un puntaje (0-100):", min_value=0, max_value=100, step=1)

#boton para clasificar

    if st.button("clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"el puntaje {puntaje} es clasificado como: {resultado}")
