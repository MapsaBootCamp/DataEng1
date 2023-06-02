import pymongo
from uuid import uuid4
from bson.objectid import ObjectId
from dataclasses import dataclass
from typing import Dict

uri = "mongodb://localhost:27017/"


@dataclass
class User:
    username: str
    password: str
    age: int = None
    address: str = None


@dataclass
class UpdateUser:
    age: int = None
    address: str = None


def get_db_connection(db_name, collection_name,  uri=uri):
    myclient = pymongo.MongoClient(uri)
    mydb = myclient[db_name]
    mycollection = mydb[collection_name]
    return mycollection


dbConnection = get_db_connection("ml-test", "users-info")


def insert_user(username, password):
    try:
        # password should be hashed
        if dbConnection.find_one({"username": username}):
            raise Exception("cheninn useri darim!")
        user = User(username, password)
        dbConnection.insert_one(user.__dict__)
    except Exception as error:
        print(error)


def find_by_username_regex(re_):
    return dbConnection.find({"username": {"$regex": re_}})


def find_user(username):
    return dbConnection.find_one({"username": username})


def update_user(username, updated_data: Dict):
    try:
        query = {"username": username}
        old_user = find_user(username)
        new_user = UpdateUser(**updated_data)
        new_user_full_data = dict(new_user.__dict__)
        for key, val in old_user.items():
            if key != "_id":
                if key not in updated_data.keys():
                    new_user_full_data[key] = val
        dbConnection.update_one(query, {"$set": new_user_full_data})
    except Exception as error:
        print(error)


if __name__ == "__main__":
    # addresses = ["Tehran", "Shiraz", "Esfahan", "Gilan"]
    # for i in range(100):
    #     address = addresses[i // 25]
    #     update_user(f"Ashkan{i}", {"address": address})
    # insert_user("Asghar", "1234")
    # user = find_user("Ashkan")
    # users = find_by_username_regex(r"^S")
    # print([user for user in users])
    # update_user("Ashkan0", {"address": "Kermanshah", "age": 32})
    # dbConnection.insert_one({"username": "A", "friends": ["B", "C", "D"]})
    print(list(dbConnection.aggregate(
        [{"$group": {"_id": "$address", "mean_age": {"$avg": "$age"}}}])))
