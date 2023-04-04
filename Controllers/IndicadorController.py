import services.database as db;
import models.indicador as indicador;

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

