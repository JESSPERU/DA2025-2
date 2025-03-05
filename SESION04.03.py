import streamlit as st

st.title("ESTRUCTURA DE CONTROL REPETITIVO")

limite=st.number_input("ingrese un numero limite para los bucles:", min_value=1, step=1)

st.subheader("Bucle FOR")

for i in range (1,limite+1):
    st.write(f"Iteracion{i} con for")