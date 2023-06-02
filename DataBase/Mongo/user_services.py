import pymongo
from uuid import uuid4
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/"


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
        dbConnection.insert_one({"username": username, "password": password})
    except Exception as error:
        print(error)


def find_user(username):
    return dbConnection.find_one({"username": username})


def update_user(username, updated_data):
    pass


if __name__ == "__main__":
    ObjectId
    # insert_user("Ashkan", "1234")
    # print(find_user("Ashkan"))
    print(ObjectId())
