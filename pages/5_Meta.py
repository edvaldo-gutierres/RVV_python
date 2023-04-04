import streamlit as st;
import Controllers.MetaController as MetaController;
import models.meta as meta;
import pandas as pd;

st.markdown("# Meta :spiral_calendar_pad: ️")
st.sidebar.markdown("###  Escolha uma opção! ")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    ("Consultar", "Cadastrar", "Alterar", "Excluir")
)


if add_selectbox == "Consultar":

    with st.expander("Lista de Metas cadastradas"):
        Meta_List = []

        for item in MetaController.Consultar():
            Meta_List.append([item.id_meta, item.matricula_colaborador, item.codigo_indicador, item.inicio_vigencia,
                              item.final_vigencia, item.valor_meta])

        df = pd.DataFrame(
            Meta_List,
            columns=['ID Meta', 'Matrícula do Colaborador', 'Código Indicador', 'Início Vigência', 'Final Vigência',
                     'Valor da Meta'])
        df['Índice'] = df.index + 1
        df = df.set_index('Índice')
        st.dataframe(df, use_container_width=True)