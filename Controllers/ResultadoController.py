import services.database as db;
import models.resultado as resultado;

def Consultar():
    db.cursor.execute(""" 
    SELECT CAST(r.id_resultado AS VARCHAR(10)) AS id_resultado,
           CAST(r.Matricula_do_Colaborador AS VARCHAR(10)) AS Matricula_do_Colaborador,
           CAST(r.Codigo_do_Indicador AS VARCHAR(10)) AS Codigo_do_Indicador,
           r.Competencia,
           r.Valor_do_Resultado
    FROM dbo.Resultado AS r
    """)

    resultado_list = []

    for row in db.cursor.fetchall():
        resultado_list.append(resultado.Resultado(row[0], row[1], row[2], row[3], row[4]))

    return resultado_list