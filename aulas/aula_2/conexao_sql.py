import pyodbc

server = "DESKTOP-15TQLGD\SQLEXPRESS"
database = "Estudo_MongoDB"
username = "aula_mongodb"
password = "abc123"
#string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
print(string_conexao)
conexao = pyodbc.connect(string_conexao)
cursor = conexao.cursor()

cursor.execute("Select * from Tbl_Teste")

for row in cursor:
    print(row)

conexao.close()