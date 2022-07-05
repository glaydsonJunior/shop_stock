from database_connection import Crud_psql

database = input('Database: ')
user = input('User: ')
host = input('Host: ')
passwd = input('Password: ')
port = input('Port: ')
tabela = Crud_psql(user,host,passwd,database,port)
tabela.criar_tabela()
print("Tabela criada com sucesso!")
