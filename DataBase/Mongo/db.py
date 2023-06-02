import pymongo
from uuid import uuid4

uri = "mongodb://localhost:27017/"

def get_db_connection(db_name, collection_name,  uri = uri):
    myclient = pymongo.MongoClient(uri)
    mydb = myclient[db_name]
    mycollection = mydb[collection_name]
    return mycollection

