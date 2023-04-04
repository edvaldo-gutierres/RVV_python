import services.database as db;
import models.meta as meta;

def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(m.id_meta AS VARCHAR(10)) AS id_meta,
           CAST(m.Matricula_do_Colaborador AS VARCHAR(10)) AS Matricula_do_Colaborador,
           CAST(m.Codigo_do_Indicador AS VARCHAR(10)) AS Codigo_do_Indicador,
           m.Inicio_Vigencia,
           m.Final_Vigencia,
           m.Valor_da_Meta
    FROM dbo.Meta AS m
    """)

    meta_list = []

    for row in db.cursor.fetchall():
        meta_list.append(meta.Meta(row[0], row[1], row[2], row[3], row[4], row[5]))

    return meta_list