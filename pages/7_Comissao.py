import streamlit as st

st.markdown("# Comissão ️:scroll:")

# Using object notation
add_selectbox = st.radio(
    "Qual operação você deseja realizar?",
    ("Calcular", "Excluir Cálculo")
)

if add_selectbox == 'Calcular':
    st.write('You selected Calcular.')
else:
    st.write("You didn\'t select Excluir Cálculo.")