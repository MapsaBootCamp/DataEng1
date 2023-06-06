import json
from pymongo import MongoClient

client = MongoClient("localhost:27017")
db = client["restaurant_db"]

data = []

with open("restaurants.json", "r") as f:
    for elm in f.readlines():
        data.append(json.loads(elm))


db.restaurants.insert_many(data)

client.close()
