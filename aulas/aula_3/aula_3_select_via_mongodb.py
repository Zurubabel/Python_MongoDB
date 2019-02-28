#Importando pymongo MongoClient
from pymongo import MongoClient

#client = MongoClient("base de dados", "port")
client = MongoClient("localhost", 27017)

#print(client.list_database_names())

#client.base de dados

db = client.Estudo_MongoDB

# Inserindo valores
#(1),(12), (500), (-222)
db.teste.insert_one({
    "bala": "Juquinha"
})

""""db.teste.insert_many(
    [
        {"id": 1},
        {"id": 12},
       {"id": 500},
        {"id": -222}
    ]
)
"""
