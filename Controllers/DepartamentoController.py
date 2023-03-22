import services.database as db;
import models.departamento as dpto;
import streamlit as st;
import time;

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


def Alterar(nome_departamento, status_departamento):


    count = db.cursor.execute("""
             UPDATE FROM dbo.Departamento
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


def Alterar_Excluir():
    colms = st.columns((1, 2, 1, 2, 1))
    campos = ['Código', 'Departamento', 'Status', 'Excluir', 'Alterar']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        col1, col2, col3, col4, col5 = st.columns((1, 2, 1, 2, 1))
        col1.write(item.codigo_departamento)
        col2.write(item.nome_departamento)
        col3.write(item.status_departamento)
        button_space_excluir = col4.empty()
        on_click_excluir = button_space_excluir.button("Excluir", 'btnExcluir' + str(item.codigo_departamento))
        button_space_alterar = col5.empty()
        on_click_alterar = button_space_alterar.button("Alterar", 'btnAlterar' + str(item.codigo_departamento))

        if on_click_excluir:
            Excluir(item.codigo_departamento)
            button_space_excluir.button('Excluído', 'btnExclui' + str(item.codigo_departamento))
            st.write(':red[_Departamento excluído com sucesso!!!_]')

        if on_click_alterar:
            Alterar(item.nome_departamento,item.status_departamento)
            st.experimental_set_query_params(codigo=[item.codigo_departamento])
            st.write(":blue[_Departamento alterado com sucesso!!!_]")
