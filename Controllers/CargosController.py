import services.database as db;
import models.cargos as cargo;
import streamlit as st;
import decimal

def Incluir(Cargo):
    count = db.cursor.execute("""
                            INSERT dbo.Cargo (Nome_do_Cargo,Status_do_Cargo,nivel_hierarquia)
                            VALUES(?,?,?)""", Cargo.nome_cargo, Cargo.status_cargo, Cargo.nivel).rowcount
    db.cnx.commit()


def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(c.Codigo_do_Cargo AS VARCHAR(10) ) AS Codigo_do_Cargo,
           c.Nome_do_Cargo,
           CASE
               WHEN c.Status_do_Cargo = 1 THEN
                   'Ativo'
               ELSE
                   'Inativo'
           END AS Status_do_Cargo,
           c.nivel_hierarquia
    FROM dbo.Cargo AS c;
    """)
    cargo_list = []

    for row in db.cursor.fetchall():
        cargo_list.append(cargo.Cargos(row[0], row[1], row[2], row[3]))

    return cargo_list


def Alterar(codigo_cargo,nome_cargo, status_cargo, nivel):

    if status_cargo == "Ativo":
        status_cargo = 1
    else:
        status_cargo = 0

    count = db.cursor.execute("""
             UPDATE dbo.Cargo
             SET  Nome_do_Cargo = ?, Status_do_Cargo = ?, nivel_hierarquia = ?
             WHERE Codigo_do_Cargo = ?""", nome_cargo, status_cargo, nivel, codigo_cargo).rowcount
    db.cnx.commit()


def Excluir(codigo_cargo):
    count = db.cursor.execute("""
                            DELETE FROM dbo.Cargo 
                            WHERE Codigo_do_Cargo = ?""", codigo_cargo).rowcount
    db.cnx.commit()


def Atualizar_Form():

    colms = st.columns((2, 3, 1.8, 2, 3, 2, 2.5,1.5))
    campos = ['Código', 'Cargo', 'Status', 'Nivel']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    min_nivel = '1'
    max_nivel = '100'
    Step = '1'

    for item in Consultar():
        cols = st.columns((2, 3, 1.8, 1, 3, 2, 2.5,1.5))
        col1, col2, col3, col4, col5, col6, col7, col8 = cols
        col1.write(item.codigo_cargo)
        col2.write(item.nome_cargo)
        col3.write(item.status_cargo)
        col4.write(item.nivel)
        novo_cargo = col5.text_input(":blue[Novo Cargo]", value=item.nome_cargo, key=f"{item.codigo_cargo}_nome")
        novo_status = col6.radio(":blue[Novo Status]", ["Ativo", "Inativo"],
                                     index=0 if item.status_cargo == "Ativo" else 1,
                                     key=f"{item.codigo_cargo}_status")
        novo_nivel = col7.number_input(":blue[Novo Nível]", value=int(item.nivel),
                                         key=f"{item.codigo_cargo}_salario",
                                         min_value=int(min_nivel), max_value=int(max_nivel), step=int(Step))
        button_space_atualizar = col8.empty()
        on_click_atualizar = button_space_atualizar.button("Ok", key=f"{item.codigo_cargo}_btnAtualizar")

def Excluir_Form():
    colms = st.columns((1, 2, 1, 2))
    campos = ['Código', 'Cargo', 'Status', 'Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        col1, col2, col3, col4 = st.columns((1, 2, 1, 2))
        col1.write(item.codigo_cargo)
        col2.write(item.nome_cargo)
        col3.write(item.status_cargo)
        button_space_excluir = col4.empty()
        on_click_excluir = button_space_excluir.button("Excluir", 'btnExcluir' + str(item.codigo_cargo), type="primary")


        if on_click_excluir:
            Excluir(item.codigo_cargo)
            button_space_excluir.button('Excluído', 'btnExclui' + str(item.codigo_cargo))
            st.write(':red[_Cargo excluído com sucesso!!!_]')