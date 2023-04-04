import streamlit as st;
import Controllers.ColaboradorController as ColaboradorController;
import models.departamento as departamento;
import pandas as pd


st.markdown("# Colaborador ️:couple:")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)


if add_selectbox == "Consultar":

    with st.expander("Lista de Colaboradores cadastrados"):
        Colaborador_List = []

        for item in ColaboradorController.Consultar():
            Colaborador_List.append([item.matricula_colaborador, item.nome_colaborador, item.sexo, item.cpf,
                                     item.data_nascimento, item.codigo_departamento, item.codigo_cargo,
                                     item.salario, item.status_colaborador])

        df = pd.DataFrame(
            Colaborador_List,
            columns=['Matrícula Colaborador', 'Nome Colaborador', 'Sexo', 'CPF', 'Data Nascimento', 'Código Departamento',
                     'Código Cargo', 'Salário', 'Status do Colaborador'])
        df['Índice'] = df.index + 1
        df = df.set_index('Índice')
        st.dataframe(df, use_container_width=True)