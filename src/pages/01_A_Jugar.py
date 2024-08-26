from pathlib import Path

import streamlit as st

from PIL import Image

im = Image.open("favicon.ico")
#st.set_page_config(
#    "EsKape Room",
#    im,
#    initial_sidebar_state="expanded",
#    layout="wide",
#)

def explanation():
    st.header("Página principal")

    st.subheader("Objetivo")

    st.write("""
             El objetivo es de la tarea es habilitar la sección `A jugar` para que tengamos un panel como el siguiente:
    """)

    st.image("src/img/canvas.png")

    st.write("""en el cuál podamos ejecutar una operación matemática sencilla.

    Tenemos entonces tres tipos de input en nuestro canvas:""")

    st.image("src/img/canvas2.png")

    st.write("""1. Exponentes: 3 posibles referentes a los cuadrados morados. Deben ser números del 0 al 9.
    2. Operadores: 2 posibles referentes a los cuadrados azules. Explicados en la siguiente sección.
    3. Números: 3 posibles referentes a los cuadrados rojos. Deben ser números del 0 al 9.""")

    st.subheader("Operadores")

    st.write("""Solo vamos a usar las 4 operaciones fundamentales: suma, resta, multiplicación y división. 

    En el caso de suma y resta las únicas opciones posibles son: + (ASCII Code 43) y - (ASCII Code 45), respectivamente.

    En el caso de multiplicación y división tendremos 2 opciones como sigue:""")

    st.subheader("Multiplicación")

    st.write("""Una × (ASCII Code 215) o un asterísco * (ASCII Code 42)""")

    st.image("src/img/mult2.png")


    st.subheader("División")

    st.write("""Un slash / (ASCII code 47) o el operando convencional ÷ (ASCII code 247)""")

    st.image("src/img/div1.png")


    st.subheader("Comentarios")

    st.subheader("Sobre las operaciones")

    st.write("""1. Asumimos que la aplicación siempre será usada por un agente honesto. No se debe validar para datos que no sean los referentes al modelo (aunque es un problema interesante de resolver)
    2. Somos consistentes en la entrada de cada canvas así como en el orden de las operaciones: de izquierda a derecha y con prioridad de operadores: ^, ( *, /), (+, -).""")

    st.subheader("Sobre la parte visual")

    st.write("""Escoger las secciones útiles de 02_Canvas.py y crear la vista referente a cada uno de los elementos de entrada:

    1. 3 Coeficientes
    2. 3 exponentes
    3. 2 operadores

    Para luego llamar a los modelos y evaluar la función.""")

def user_panel():
    # Esta sección de código debería ser st.write(Path("src/md/Objetivo.md").read_text())
    # Pero streamlit no soporta imágenes dentro de markdowns
    explanation()
    
    st.write(Path("src/md/Requerimientos.md").read_text())

    #######################################################
    #               INGRESAR CÓDIGO ACÁ                   #
    #######################################################    

def main():
    user_panel()

if __name__ == "__main__":
    main()