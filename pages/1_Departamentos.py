import streamlit as st
import Controllers.DepartamentoController as DepartamentoController
import models.departamento as departamento

st.markdown("# Departamentos ️")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar","Cadastrar", "Alterar", "Excluir")
)


if  add_selectbox == "Cadastrar":

    #html_string = "<h3>Cadastrar Departamento</h3>"
    #st.markdown(html_string, unsafe_allow_html=True)

    st.subheader(":blue[_Cadastrar Departamento_]")

    with st.form(key='include_departamento'):
        input_name = st.text_input(label="Informe o Nome do Departamento")
        input_status = st.selectbox("Selecione o Status",["Ativo","Inativo"])
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_status == "Ativo":
        ativo = 1
    else:
        ativo = 0

    if input_button_submit:
        departamento.nome_departamento = input_name
        departamento.status_departamento = ativo

        DepartamentoController.Incluir(departamento)

        st.success("Departamento cadastrado com sucesso!!!")





