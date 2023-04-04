import streamlit as st;
import Controllers.ColaboradorController as ColaboradorController;
import models.colaborador as colaborador;
import pandas as pd;
import services.database as db;
import datetime


st.markdown("# Colaborador ️:couple:")
st.sidebar.markdown("###  Escolha uma opção! ")

# Define as opções do selectbox
options = ("Consultar", "Cadastrar", "Alterar", "Excluir")

# Cria caixa de seleção da barra lateral
add_selectbox = st.sidebar.selectbox(
    "Qual operação você deseja realizar?",
    options,
    index=0 # define "Consultar" como padrão
)


# Define as funções para cada opção

if add_selectbox == "Consultar":

    st.subheader(":blue[_Consultar Colaborador_]")
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


if add_selectbox == "Cadastrar":

    # Subtitulo
    st.subheader(":blue[_Cadastrar Colaborador_]")

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
    with st.form(key='include_colaborador'):
        col1, col2 = st.columns(2)
        with col1:
            input_name = st.text_input(label="**Informe o Nome do Colaborador**")
            input_cpf = st.text_input(label="**Informe o CPF do Colaborador** (Ex.: 111.111.111-11)")
            input_cod_departamento = st.selectbox(label="**Informe o Departamento**", options=opcao_dpto_branco)
            input_salario = st.number_input(label="**Informe o Salário**", value=0.0, step=100.00)
        with col2:
            input_sexo = st.selectbox("**Selecione o Sexo**", ["Selecione","Masculino", "Feminino"])
            input_dtnasc = st.date_input(label="**Informe a data de nascimento**", min_value=min_date, max_value=max_date)
            input_cod_cargo = st.selectbox(label="**Informe o código do Cargo**", options=opcao_crg_branco)
            input_status = st.selectbox("**Selecione o Status**", ["Selecione","Ativo", "Inativo"])
        input_button_submit = st.form_submit_button("**Cadastrar**")

    # Ajusta dados para insert no banco
    if input_status == "Ativo":
        ativo = 1
    else:
        ativo = 0

    if input_sexo == "Masculino":
        sexo = 'M'
    else:
        sexo = 'F'

    if input_dtnasc is not None:
        data_nasc = input_dtnasc.strftime('%Y-%m-%d')

    cod_depart = input_cod_departamento.split('-')[0]
    cod_cargo = input_cod_cargo.split('-')[0]

    #Ação do Botão cadastrar
    if input_button_submit:
        ColaboradorController.Incluir(colaborador.Colaborador(0, input_name, sexo, input_cpf, data_nasc,
                                                              cod_depart, cod_cargo, input_salario,
                                                              ativo))
        st.success("Colaborador cadastrado com sucesso!!!")


    #Retorna tabela com os colaboradores cadastrados
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


if add_selectbox == "Alterar":

    st.subheader(":blue[_Lista de Colaboradores Cadastrados_]")
    ColaboradorController.Atualizar_Form()


if add_selectbox == "Excluir":

    st.subheader(":blue[_Lista de Colaboradores Cadastrados_]")
    ColaboradorController.Excluir_Form()