import services.database as db;

def Incluir(Departamento):
    count = db.cursor.execute("""
                                INSERT dbo.Departamento (Nome_do_Departamento,Status_do_Departamento)
                                VALUES(?,?)""",Departamento.nome_departamento,Departamento.status_departamento).rowcount
    db.cnx.commit()
