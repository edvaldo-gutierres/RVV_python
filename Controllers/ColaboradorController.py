import services.database as db;
import models.colaborador as colaborador;

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