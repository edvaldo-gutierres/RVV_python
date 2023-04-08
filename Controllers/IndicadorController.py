import services.database as db;
import models.indicador as indicador;
import streamlit as st

def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(i.Codigo_do_Indicador AS VARCHAR(10)) AS Codigo_do_Indicador,
           i.Nome_do_Indicador,
           CAST(i.Codigo_do_Departamento AS VARCHAR(10)) AS Codigo_do_Departamento,
           CAST(i.Codigo_do_Cargo AS VARCHAR(10)) AS Codigo_do_Cargo,
           i.Peso_do_Indicador,
           i.Inicio_Vigencia,
           i.Final_Vigencia
    FROM dbo.Indicadores AS i
    """)

    indicador_list = []

    for row in db.cursor.fetchall():
        indicador_list.append(indicador.Indicador(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    return indicador_list


def Incluir(indicador):
    count = db.cursor.execute("""
                            INSERT INTO dbo.Indicadores
                            (
                                Nome_do_Indicador,
                                Codigo_do_Departamento,
                                Codigo_do_Cargo,
                                Peso_do_Indicador,
                                Inicio_Vigencia
                            )
                            VALUES(?,?,?,?,?)""", indicador.nome_indicador, indicador.codigo_departamento,
                              indicador.codigo_cargo, indicador.peso_indicador, indicador.inicio_vigencia).rowcount
    db.cnx.commit()


def Alterar(codigo_indicador,peso_indicador, inicio, final):

    count = db.cursor.execute("""
             UPDATE dbo.Indicadores
             SET  Peso_do_Indicador = ?, Inicio_Vigencia = ?, Final_Vigencia = ?
             WHERE Codigo_do_Indicador = ?""", peso_indicador, inicio, final, codigo_indicador).rowcount
    db.cnx.commit()


def Excluir(codigo_indicador):
    count = db.cursor.execute("""
                            DELETE FROM dbo.Indicadores
                            WHERE Codigo_do_Indicador = ?""", codigo_indicador).rowcount
    db.cnx.commit()




def Excluir_Form():
    colms = st.columns((1.2, 2, 2.2, 2, 1, 2, 1, 2))
    campos = ['Código', 'Indicador', 'Departamento', 'Cargo', 'Peso', 'Inicio', 'Final']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in Consultar():
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1.2, 2, 2.2, 2, 1, 2, 1, 2))
        col1.write(item.codigo_indicador)
        col2.write(item.nome_indicador)
        col3.write(item.codigo_departamento)
        col4.write(item.codigo_cargo)
        col5.write(round(item.peso_indicador,2))
        col6.write(item.inicio_vigencia)
        col7.write(item.final_vigencia)
        button_space_excluir = col8.empty()
        on_click_excluir = button_space_excluir.button("Excluir", 'btnExcluir' + str(item.codigo_indicador),
                                                       type="primary")


        if on_click_excluir:
            Excluir(item.codigo_indicador)
            button_space_excluir.button('Excluído', 'btnExclui' + str(item.codigo_indicador))
            st.write(':red[_Indicador excluído com sucesso!!!_]')