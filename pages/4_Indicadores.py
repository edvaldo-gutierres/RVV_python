import streamlit as st;
import Controllers.IndicadorController as IndicadorController;
import models.indicador as indicador;
import pandas as pd;

st.markdown("# Indicadores ️:pencil:")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)


if add_selectbox == "Consultar":

    st.subheader(":blue[_Consultar Indicadores_]")

    with st.expander("Lista de Indicadores cadastrados"):
        Indicador_List = []

        for item in IndicadorController.Consultar():
            Indicador_List.append([item.codigo_indicador, item.nome_indicador, item.codigo_departamento,
                                   item.codigo_cargo, item.peso_indicador, item.inicio_vigencia, item.final_vigencia])

        df = pd.DataFrame(
            Indicador_List,
            columns=['Código do Indicador', 'Nome do Indicador', 'Código Departamento', 'Código Cargo', 'Peso Indicador',
                     'Início Vigência', 'Final Vigência'])
        df['Índice'] = df.index + 1
        df = df.set_index('Índice')
        st.dataframe(df, use_container_width=True)
