import pymongo
from uuid import uuid4
from bson.objectid import ObjectId
from dataclasses import dataclass
from typing import Dict

uri = "mongodb://localhost:27017/"


def get_db_connection(db_name, collection_name,  uri=uri):
    myclient = pymongo.MongoClient(uri)
    mydb = myclient[db_name]
    mycollection = mydb[collection_name]
    return mycollection


dbConnection = get_db_connection("ml-test", "carts")


# dbConnection.insert_one(
#     {"userId": ObjectId("6479b7aede2b41b5155b4520"), "products": []})


print(list(dbConnection.aggregate([{"$lookup": {"from": "users-info",
                                                "localField": "userId", "foreignField": "_id", "as": "user_info"}}])))
