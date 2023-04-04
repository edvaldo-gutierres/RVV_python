import pandas as pd
import streamlit as st
import Controllers.DepartamentoController as DepartamentoController
import models.departamento as departamento;


st.markdown("# Departamentos ️")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)


if  add_selectbox == "Cadastrar":

    #html_string = "<h3>Cadastrar Departamento</h3>"
    #st.markdown(html_string, unsafe_allow_html=True)
    st.subheader(":blue[_Cadastrar Departamento_]")

    with st.form(key='include_departament'):
        input_name = st.text_input(label="Informe o Nome do Departamento")
        input_status = st.selectbox("Selecione o Status",["Ativo","Inativo"])
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_status == "Ativo":
        ativo = 1
    else:
        ativo = 0

    if input_button_submit:
        DepartamentoController.Incluir(departamento.Departamento(0, input_name, ativo))
        st.success("Departamento cadastrado com sucesso!!!")

    with st.expander("Lista de Departamentos cadastrados"):
        Departament_List = []

        for item in DepartamentoController.Consultar():
            Departament_List.append([item.codigo_departamento, item.nome_departamento, item.status_departamento])

        df = pd.DataFrame(
            Departament_List,
            columns=['Codigo do Departamento', 'Nome do Departamento', 'Status do Departamento'])

        st.dataframe(df)



if  add_selectbox == "Excluir":

    st.subheader(":blue[_Lista de Departamentos Cadastrados_]")
    DepartamentoController.Excluir_Form()


if  add_selectbox == "Alterar":

    st.subheader(":blue[_Lista de Departamentos Cadastrados_]")
    DepartamentoController.Atualizar_Form()


if  add_selectbox == "Consultar":

    with st.expander("Lista de Departamentos cadastrados"):
        Departament_List = []

        for item in DepartamentoController.Consultar():
            Departament_List.append([item.codigo_departamento, item.nome_departamento, item.status_departamento])

        df = pd.DataFrame(
            Departament_List,
            columns=['Codigo do Departamento', 'Nome do Departamento', 'Status do Departamento'])

        st.dataframe(df)