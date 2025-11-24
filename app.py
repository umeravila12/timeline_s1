import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Modelo de Predicción para el abastecimiento periódico (modelo LSTM)")
st.write("Autor: Umer Avila - Avance01-Grupo03 | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")
# URLs de imágenes en GitHub
base_url = "https://raw.githubusercontent.com/umeravila12/timeline_s1/main/timeline_images/"
imagenes = {
   1: base_url + "timeline1.png",
   2: base_url + "timeline2.png",
   3: base_url + "timeline3.png",
   4: base_url + "timeline4.png",
   5: base_url + "timeline5.png"
}
# Slider
opcion = st.slider(
 "Selecciona un punto del timeline",
 min_value=1,
 max_value=5,
 value=1,
 step=1
)
# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)
if opcion == 1:
 st.info(" **1943 – La Neurona Formal** | Warren McCulloch y Walter Pitts publican el modelo de la Neurona MCP.")
if opcion == 2:
 st.info(" **1957 – La Invención del Perceptrón** | Frank Rosenblatt crea el Perceptrón.")
if opcion == 3:
 st.info(" **1986 – La Superación del Estancamiento con Retropropagación** | Geoffrey Hinton, David Rumelhart y Ronald Williams popularizan la Retropropagación.")
if opcion == 4:
 st.info(" **2009 – El Auge de las Redes Convolucionales (CNN) y GPUs** | Yann LeCun desarrolla LeNet-5 (1998) y el posterior uso de GPUs (a partir de 2009) para acelerar el entrenamiento.")
if opcion == 5:
 st.info(" **2012 – El Momento de AlexNet en ImageNet** | Alex Krizhevsky, Ilya Sutskever y Geoffrey Hinton (el equipo de AlexNet) ganan la competencia de reconocimiento visual ImageNet (ILSVRC) por un margen abrumador.")
