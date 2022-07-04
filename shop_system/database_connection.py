import psycopg2
class Crud_psql:
    def __init__(self,username,host,password,database,port):
        self.username = username
        self.host = host
        self.password = password
        self.database = database
        self.port = port

    #Cria a tabela produtos
    def criar_tabela(self):
        with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
            comandos = banco.cursor()
            comandos.execute(''' create table Produtos(nome text PRIMARY KEY,preco numeric not null,estoque integer not null) ''')
            banco.commit()
    #Adicionar produto
    def add_produto(self, name,price,stock):
        try:
            with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
                comandos = banco.cursor()
                comandos.execute(f" INSERT INTO produtos(nome,preco,estoque) values ('{name}',{price},{stock}); ")
                banco.commit()
        except:
            return "Produto ja cadastrado"


    #Ver todos os produtos
    def ver_produtos(self):
        try:
            with psycopg2.connect(f'dbname=ShopDatabase user=postgres password=tscwindows host=localhost port=5432') as banco:
                comandos = banco.cursor()
                comandos.execute(f'SELECT * FROM produtos')
                viwer = comandos.fetchall()
                return viwer
        except IndexError:
            return 'Nenhum produto cadastrado'

    #Filtrar produtos pelo o nome
    def produtos_nome(self, name):
            with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
                comandos = banco.cursor()
                comandos.execute(f"select nome,preco,estoque from produtos where nome like '{name}%' ")
                viwer = comandos.fetchall()
                if len(viwer) != 0:
                    return viwer
                else:
                    return "Nenhum produto encontrado"


    #Limpar a tabela inteira
    def limpar_tabela(self):
        with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
            comandos = banco.cursor()
            comandos.execute('delete from produtos where preco > -1;')
            banco.commit()

    #Função de remover produtos
    def remover_produto(self,nome):
        with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
            comandos = banco.cursor()
            comandos.execute(f"delete from produtos where nome='{nome}' ")
    #Função de compra de produtos
    def compra(self, nome,quantidade):
        with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
            comandos = banco.cursor()
            comandos.execute(f"select estoque from produtos where nome like '{nome}' ")
            quantidade_estoque = comandos.fetchone()
            compras = quantidade_estoque[0]+quantidade
            comandos.execute(f" UPDATE produtos SET estoque = {compras} where nome='{nome}' ")

    #Função de venda de produtos
    def venda(self, nome,quantidade):
        with psycopg2.connect(f'dbname={self.database} user={self.username} password={self.password} host={self.host} port={self.port}') as banco:
            comandos = banco.cursor()
            comandos.execute(f"select estoque from produtos where nome like '{nome}' ")
            quantidade_estoque = comandos.fetchone()
            compras = quantidade_estoque[0]-quantidade
            comandos.execute(f" UPDATE produtos SET estoque = {compras} where nome='{nome}' ")