import pymongo

uri = "mongodb+srv://gabriel:290504ge@cluster0.jckct48.mongodb.net/"
client = pymongo.MongoClient(uri)
db = client.test
collection = db.my_collection

id1 = collection.insert_one({"x": 10}).inserted_id
id2 = collection.insert_one({"x": 8}).inserted_id
id3 = collection.insert_one({"x": 11}).inserted_id

print(f"IDs inseridos: {id1}, {id2}, {id3}")

doc = collection.find_one()
print("Documento encontrado:", doc)

print("Todos os valores de x:")
for item in collection.find():
    print(item["x"])

collection.create_index("x")
print("Índice criado em 'x'.")

print("Valores de x ordenados:")
for item in collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])

result = [item["x"] for item in collection.find().limit(2).skip(1)]
print("Resultado com limit=2 e skip=1:", result)
