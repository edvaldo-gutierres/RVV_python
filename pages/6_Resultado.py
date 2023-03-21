import streamlit as st

st.markdown("# Resultado :trophy: ️")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Inserir", "Alterar", "Excluir")
)
