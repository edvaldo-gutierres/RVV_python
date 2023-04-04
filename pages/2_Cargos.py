import streamlit as st;
import Controllers.CargosController as CargoController;
import models.cargos as cargos;
import pandas as pd

st.markdown("# Cargos ️:pencil:")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)

if  add_selectbox == "Cadastrar":

    st.subheader(":blue[_Cadastrar Cargo_]")

    with st.form(key='include_cargo'):
        input_name = st.text_input(label="Informe o Nome do Cargo")
        input_status = st.selectbox("Selecione o Status",["Ativo","Inativo"])
        input_nivel = st.number_input('Informe o Níve Hierarquico', step=1)
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_status == "Ativo":
        ativo = 1
    else:
        ativo = 0

    if input_button_submit:
        CargoController.Incluir(cargos.Cargos(0, input_name, ativo, input_nivel))
        st.success("Cargo cadastrado com sucesso!!!")


    with st.expander("Lista de Cargos cadastrados"):
        Cargo_List = []

        for item in CargoController.Consultar():
            Cargo_List.append([item.codigo_cargo, item.nome_cargo, item.status_cargo, item.nivel])

        df = pd.DataFrame(
            Cargo_List,
            columns=['Codigo do Cargo', 'Nome do Cargo', 'Status do Cargo', 'Nivel Hieraquia'])

        st.dataframe(df)



if  add_selectbox == "Consultar":

    st.subheader(":blue[_Consultar Cargos_]")

    with st.expander("Lista de Cargos cadastrados"):
        Cargo_List = []

        for item in CargoController.Consultar():
            Cargo_List.append([item.codigo_cargo, item.nome_cargo, item.status_cargo, item.nivel])

        df = pd.DataFrame(
            Cargo_List,
            columns=['Codigo do Cargo', 'Nome do Cargo', 'Status do Cargo', 'Nível do Cargo'])
        df['Índice'] = df.index + 1
        df = df.set_index('Índice')
        st.dataframe(df)


if add_selectbox == "Alterar":

    st.subheader(":blue[_Lista de Cargos Cadastrados_]")
    CargoController.Atualizar_Form()


if add_selectbox == "Excluir":

    st.subheader(":blue[_Lista de Cargos Cadastrados_]")
    CargoController.Excluir_Form()