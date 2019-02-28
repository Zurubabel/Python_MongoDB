#Exemplo MongoDB

# insert_one & insert_many()

from pymongo import MongoClient
client = MongoClient("localhost", 27017)

# Cria a Base de Dados
db = client.Aderbaldo
#db = client["Aderbaldo"]

# Inserindo dados
"""db.pessoas.insert_one({
    "id": 1,
    "Nome": "Juquinha",
    "Idade": 45
})"""

"""db.pessoas.insert_one({
    "id": 1,
    "Nome": "Juquinha",
    "Idade": 45,
    "filhos": ["Juninho", "Pedrinho", "Ze Capivara"]
})"""

db.pessoas.insert_many(
    [
        {
            "id": 5,
            "nome": "Pedrao"
         },
        {
            "indê": 7,
            "apelido": "Sebastião"
        }
    ]
)