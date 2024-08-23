from flask import Flask, jsonify, make_response, request
from bd import Campos

app = Flask('campos')

# PRIMEIRO METODO - VISUALIZAR OS DADOS (GET)
@app.route('/campos',methods=['GET'])
def get_campos():
 return Campos

#[GET/ID]
@app.route('/campos/<int:id>', methods=['GET'])
def get_campos_id(id):
 for campos in Campos:
  if campos.get('id') == id:
   return jsonify(campos)
 

# criar novo post [POST]
@app.route('/campos', methods=['POST'])
def criar_campos():
 campos = request.json
 Campos.append(campos)
 return make_response(
    jsonify(mensagem='campo cadastrado com sucesso!! ',
            campos=campos
            )
 )

#PUT - EDITAR DADOS
@app.route('/campos/<int:id>', methods=['PUT'])
def editar_campos_id(id):
 campos_alterar = request.get_json()
 for indice, campos in enumerate(Campos):
  if campos.get('id') == id:
   Campos[indice].update(campos_alterar)
   return jsonify(Campos[indice])

#delete
@app.route('/campos/<int:id>', methods=['DELETE'])
def excluir_campos(id):
 for indice, campos in enumerate(Campos):
  if campos.get('id') == id:
   del Campos[indice]
   return jsonify({"mensagem": "campos excluido com sucesso!! "})


app.run(port=5000, host='localhost')