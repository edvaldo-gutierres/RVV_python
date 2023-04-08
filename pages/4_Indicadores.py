import streamlit as st;
import Controllers.IndicadorController as IndicadorController;
import models.indicador as indicador;
import pandas as pd;
import services.database as db;
import datetime


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


if add_selectbox == "Cadastrar":

    # Subtitulo
    st.subheader(":blue[_Cadastrar Indicador_]")

    # criar opções de Departamento e Cargo
    con_dpto = db.cnx.cursor()
    con_dpto.execute("SELECT CAST(d.Codigo_do_Departamento AS VARCHAR(10))+ ' - ' +  d.Nome_do_Departamento "
                     "FROM dbo.Departamento AS d")
    opcao_dpto = [row[0] for row in con_dpto.fetchall()]
    opcao_dpto_branco = [''] + opcao_dpto

    con_crg = db.cnx.cursor()
    con_crg.execute("SELECT CAST(c.Codigo_do_Cargo AS VARCHAR(10)) + ' - ' +  c.Nome_do_Cargo FROM dbo.Cargo AS c")
    opcao_crg = [row[0] for row in con_crg.fetchall()]
    opcao_crg_branco = [''] + opcao_crg


    min_date = datetime.date(year=1900, month=1, day=1)
    max_date = datetime.date(year=2050, month=12, day=31)


    #Cria formulário
    with st.form(key='include_indicador'):
        col1, col2 = st.columns(2)
        with col1:
            input_name = st.text_input(label="**Informe o Nome do Indicador**")
            input_cod_departamento = st.selectbox(label="**Informe o Departamento**", options=opcao_dpto_branco)
            input_inicio = st.date_input(label="**Informe Inicio Vigência**", min_value=min_date, max_value=max_date)
        with col2:
            input_peso = st.number_input(label="**Informe o Peso**", value=0.0, step=0.01)
            input_cod_cargo = st.selectbox(label="**Informe o código do Cargo**", options=opcao_crg_branco)
            # input_final = st.date_input(label="**Informe Final Vigência**", min_value=min_date, max_value=max_date)

        input_button_submit = st.form_submit_button("**Cadastrar**")

        if input_inicio is not None:
            inicio = input_inicio.strftime('%Y-%m-%d')

        cod_depart = input_cod_departamento.split('-')[0]
        cod_cargo = input_cod_cargo.split('-')[0]

    #Ação do Botão cadastrar
    if input_button_submit:
        IndicadorController.Incluir(indicador.Indicador(0, input_name, cod_depart, cod_cargo, input_peso, inicio))
        st.success("Indicador cadastrado com sucesso!!!")


    # Retorna tabela com os colaboradores cadastrados
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


if add_selectbox == "Alterar":

    st.subheader(":red[_Esse módulo foi desabilitado_]")


if add_selectbox == "Excluir":

    st.subheader(":blue[_Lista de Colaboradores Cadastrados_]")
    IndicadorController.Excluir_Form()