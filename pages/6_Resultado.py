import streamlit as st;
import Controllers.ResultadoController as ResultadoController;
import models.resultado as resultado;
import pandas as pd

st.markdown("# Resultado :trophy: ️")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)


if add_selectbox == "Consultar":

    st.subheader(":blue[_Consultar Resultados_]")

    with st.expander("Lista de Resultados cadastrados"):
        Resultado_List = []

        for item in ResultadoController.Consultar():
            Resultado_List.append([item.id_resultado, item.matricula_colaborador, item.codigo_indicador,
                                   item.competencia, item.valor_resultado])

        df = pd.DataFrame(
            Resultado_List,
            columns=['ID Resultado', 'Matrícula do Colaborador', 'Código Indicador', 'Competência', 'Valor da Meta'])
        df['Índice'] = df.index + 1
        df = df.set_index('Índice')
        st.dataframe(df, use_container_width=True)