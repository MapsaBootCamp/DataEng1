import pymongo
from uuid import uuid4


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ml-test"]
mycollection = mydb["users-info"]

user_info = {"userId": str(uuid4()), "name": "Ashkan", "age": 20, "friends": ["Asghar", "Akbar"]}

# mycollection.insert_one(user_info)
mycollection.update_many({"name": "Ashkan"}, {"$set": {"age": 32}})