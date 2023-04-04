import services.database as db;
import models.cargos as cargo;

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