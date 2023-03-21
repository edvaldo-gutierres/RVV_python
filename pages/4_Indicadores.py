import streamlit as st
import time

st.markdown("# Indicadores ️:pencil:")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Inserir", "Alterar", "Excluir")
)

