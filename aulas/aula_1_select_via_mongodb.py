from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.pessoas

db.pessoas.insert_one({
    "nome": "Zurubabel",
    "idade": 31
})

print(client.list_database_names())