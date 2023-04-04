import services.database as db;
import models.departamento as dpto;


def Incluir(Departamento):
    count = db.cursor.execute("""
                            INSERT dbo.Departamento (Nome_do_Departamento,Status_do_Departamento)
                            VALUES(?,?)""", Departamento.nome_departamento, Departamento.status_departamento).rowcount
    db.cnx.commit()


def Excluir(codigo_departamento):
    count = db.cursor.execute("""
                            DELETE FROM dbo.Departamento 
                            WHERE Codigo_do_Departamento = ?""", codigo_departamento).rowcount
    db.cnx.commit()


def Alterar(codigo_departamento,nome_departamento, status_departamento):

    if status_departamento == "Ativo":
        status_departamento = 1
    else:
        status_departamento = 0

    count = db.cursor.execute("""
             UPDATE dbo.Departamento
             SET  Nome_do_Departamento = ?, Status_do_Departamento = ?
             WHERE Codigo_do_Departamento = ?""", nome_departamento, status_departamento, codigo_departamento).rowcount
    db.cnx.commit()


def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(d.Codigo_do_Departamento AS VARCHAR(10)) AS Codigo_do_Departamento,
           d.Nome_do_Departamento,
           CASE
            WHEN d.Status_do_Departamento = 1 THEN 'Ativo'
            ELSE 'Inativo'
           END AS Status_do_Departamento
    FROM dbo.Departamento AS d
    """)
    departament_list = []

    for row in db.cursor.fetchall():
        departament_list.append(dpto.Departamento(row[0], row[1], row[2]))

    return departament_list


def Excluir_Form():
    colms = st.columns((1, 2, 1, 2))
    campos = ['Código', 'Departamento', 'Status', 'Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        col1, col2, col3, col4 = st.columns((1, 2, 1, 2))
        col1.write(item.codigo_departamento)
        col2.write(item.nome_departamento)
        col3.write(item.status_departamento)
        button_space_excluir = col4.empty()
        on_click_excluir = button_space_excluir.button("Excluir", 'btnExcluir' + str(item.codigo_departamento))


        if on_click_excluir:
            Excluir(item.codigo_departamento)
            button_space_excluir.button('Excluído', 'btnExclui' + str(item.codigo_departamento))
            st.write(':red[_Departamento excluído com sucesso!!!_]')


import streamlit as st

def Atualizar_Form():

    colms = st.columns((1, 2, 1, 2, 1, 2, 1))
    campos = ['Código', 'Departamento', 'Status']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        cols = st.columns((1, 2, 1, 2, 1, 2))
        col1, col2, col3, col4, col5, col6 = cols
        col1.write(item.codigo_departamento)
        col2.write(item.nome_departamento)
        col3.write(item.status_departamento)
        novo_departamento = col4.text_input(":blue[Novo Departamento]", value=item.nome_departamento,
                                            key=f"{item.codigo_departamento}_nome")
        novo_status = col5.radio(":blue[Novo Status]", ["Ativo", "Inativo"],
                                     index=0 if item.status_departamento == "Ativo" else 1,
                                     key=f"{item.codigo_departamento}_status")
        button_space_atualizar = col6.empty()
        on_click_atualizar = button_space_atualizar.button("Atualizar", key=f"{item.codigo_departamento}_btnAtualizar")

        if on_click_atualizar:
            Alterar(item.codigo_departamento, novo_departamento, novo_status)
            button_space_atualizar.button('Atualizado', key=f"{item.codigo_departamento}_btnAtualizado")
            st.write(f':green[_Departamento {item.codigo_departamento} atualizado com sucesso!!!_]')



