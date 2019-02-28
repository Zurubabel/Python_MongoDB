import pyodbc

def retornar_conexao_sql():
    server = "DESKTOP-15TQLGD\SQLEXPRESS"
    database = "Estudo_MongoDB"
    username = "aula_mongodb"
    password = "abc123"
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()