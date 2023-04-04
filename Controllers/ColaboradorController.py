import services.database as db;
import models.colaborador as colaborador;
import streamlit as st;
import decimal

def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(c.Matricula_do_Colaborador AS VARCHAR(10)) AS Matricula_do_Colaborador,
           c.Nome_do_Colaborador,
           c.Sexo,
           c.CPF,
           c.Data_Nascimento,
           CAST(c.Codigo_do_Departamento AS VARCHAR(10)) AS Codigo_do_Departamento,
           CAST(c.Codigo_do_Cargo AS VARCHAR(10)) AS Codigo_do_Cargo,
           c.Salario,
           CASE
               WHEN c.Status_do_Colaborador = 1 THEN
                   'Ativo'
               ELSE
                   'Inativo'
           END Status_do_Colaborador
    FROM dbo.Colaborador AS c
    """)
    colaborador_list = []

    for row in db.cursor.fetchall():
        colaborador_list.append(colaborador.Colaborador(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                        row[7], row[8]))

    return colaborador_list


def Incluir(colaborador):
    count = db.cursor.execute("""
                            INSERT INTO dbo.Colaborador (
                                Nome_do_Colaborador,
                                Sexo,
                                CPF,
                                Data_Nascimento,
                                Codigo_do_Departamento,
                                Codigo_do_Cargo,
                                Salario,
                                Status_do_Colaborador
                            )
                            VALUES(?,?,?,?,?,?,?,?)""", colaborador.nome_colaborador, colaborador.sexo, colaborador.cpf,
                              colaborador.data_nascimento, colaborador.codigo_departamento, colaborador.codigo_cargo,
                              colaborador.salario, colaborador.status_colaborador).rowcount
    db.cnx.commit()


def Alterar(matricula_colaborador,nome_colaborador, salario, status_colaborador):

    if status_colaborador == "Ativo":
        status_colaborador = 1
    else:
        status_colaborador = 0

    count = db.cursor.execute("""
             UPDATE dbo.Colaborador
             SET  Nome_do_Colaborador = ?, Salario = ?, Status_do_Colaborador = ?
             WHERE Matricula_do_Colaborador = ?""", nome_colaborador, salario, status_colaborador, matricula_colaborador).rowcount
    db.cnx.commit()


def Excluir(matricula_colaborador):
    count = db.cursor.execute("""
                            DELETE FROM dbo.Colaborador 
                            WHERE Matricula_do_Colaborador = ?""", matricula_colaborador).rowcount
    db.cnx.commit()


def Atualizar_Form():

    # Ajuste a largura da página
    # st.set_page_config(page_title="Alterar Colaborador", layout="wide",
    #                    initial_sidebar_state="expanded", width=1200)

    colms = st.columns((2, 3, 3, 2, 4, 2))
    campos = ['Matrícula', 'Colaborador']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    min_salario = decimal.Decimal('1000.00')
    max_salario = decimal.Decimal('1000000.00')
    Step = decimal.Decimal('100.00')

    for item in Consultar():
        cols = st.columns((2, 3, 3, 2, 4, 2))
        # col1, col2, col3, col4, col5, col6, col7, col8 = cols
        col1, col2, col5, col6, col7, col8 = cols
        col1.write(item.matricula_colaborador)
        col2.write(item.nome_colaborador)
        # col3.write(item.salario)
        # col4.write(item.status_colaborador)
        novo_nome = col5.text_input(":blue[Novo Nome]", value=item.nome_colaborador,
                                            key=f"{item.matricula_colaborador}_nome")
        novo_status = col6.radio(":blue[Novo Status]", ["Ativo", "Inativo"],
                                     index=0 if item.status_colaborador == "Ativo" else 1,
                                     key=f"{item.matricula_colaborador}_status")
        novo_salario = col7.number_input(":blue[Novo Salário]", value=float(item.salario),
                                         key=f"{item.matricula_colaborador}_salario",
                                         min_value=float(min_salario), max_value=float(max_salario), step=float(Step))
        button_space_atualizar = col8.empty()
        on_click_atualizar = button_space_atualizar.button("Ok", key=f"{item.matricula_colaborador}_btnAtualizar",
                                                           type="primary")

        if on_click_atualizar:
            Alterar(item.matricula_colaborador, novo_nome, novo_salario, novo_status)
            button_space_atualizar.button('Feito!', key=f"{item.matricula_colaborador}_btnAtualizado")
            st.write(f':green[_Colaborador {item.matricula_colaborador} atualizado com sucesso!!!_]')


def Excluir_Form():
    colms = st.columns((1, 2, 1, 2))
    campos = ['Matrícula', 'Colaborador', 'Status', 'Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        col1, col2, col3, col4 = st.columns((1, 2, 1, 2))
        col1.write(item.matricula_colaborador)
        col2.write(item.nome_colaborador)
        col3.write(item.status_colaborador)
        button_space_excluir = col4.empty()
        on_click_excluir = button_space_excluir.button("Excluir", key=f"{item.matricula_colaborador}_btnExcluir",
                                                       type="primary")


        if on_click_excluir:
            Excluir(item.matricula_colaborador)
            button_space_excluir.button('Excluído', key=f"{item.matricula_colaborador}_btnExcluido")
            st.write(':red[_Colaborador excluído com sucesso!!!_]')