import pyodbc

server = 'localhost\\SQLEXPRESS'
database = 'rvv'
username = 'user_service_powerbi'
password = 'powerbi@12345'
cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnx.cursor()