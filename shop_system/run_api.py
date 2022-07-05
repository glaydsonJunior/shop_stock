from database_connection import Crud_psql
from flask import Flask, jsonify,request

database = input('Database: ')
user = input('User: ')
host = input('Host: ')
passwd = input('Password: ')
port = input('Port: ')
tabela = Crud_psql(user,host,passwd,database,port)

app = Flask(__name__)

@app.route('/all_products')
def home():
    response = []
    for i in tabela.ver_produtos():
        response.append({'name':i[0],'price':i[1],'stock:':i[2]})
    return jsonify(response)


@app.route('/search')
def search():
    filtro = request.args.get("name")
    response = []
    for i in tabela.produtos_nome(filtro):
        response.append({'name':i[0],'price':i[1],'stock':i[2]})
    return jsonify(response)

@app.route('/add_product', methods=['POST'])
def add():
    receive_json = request.get_json()
    tabela.add_produto(receive_json["name"],receive_json["price"],receive_json["stock"])
    return jsonify(receive_json)

@app.route('/del_product', methods=['DELETE'])
def deletar():
    nome = request.args.get("name")
    tabela.remover_produto(nome)
    return jsonify({'result':'produto deletado com sucesso'})

@app.route('/market', methods=['PUT'])
def market():
    receive_json = request.get_json()
    if receive_json['action'] == 'sell':
        tabela.venda(receive_json['name'],int(receive_json['quantity']))
        return jsonify({'result':'quantidade do produto alterado com sucesso'})
    elif receive_json['action'] == 'buy':
        tabela.compra(receive_json['name'],int(receive_json['quantity']))
        return jsonify({'result':'sucess'})
    else:
        return jsonify({'result':'this action does not exist use buy or sell'})


if __name__ == '__main__':
    app.run()
