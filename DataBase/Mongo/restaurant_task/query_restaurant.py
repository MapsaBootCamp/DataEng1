from pymongo import MongoClient
import re

client = MongoClient("localhost:27017")
db = client["restaurant_db"]

# Q1
# for data in db.restaurants.find().limit(5):
#     print(data)
#     print("-" * 100)

# Q2
# count = 0
# for data in db.restaurants.find(
#         {
#             "$or": [
#                 {"cuisine": {"$regex": re.compile(r"^B", re.IGNORECASE)}},
#                 {"address.street": re.compile(r"^m", re.IGNORECASE)}]
#         },
#         {"_id": 0, "cuisine": 1,  "address": 1, "borough": 1}).limit(50):
#     print(data)
#     print(count)
#     count += 1
#     print("-" * 100)


# Q3
# for data in db.restaurants.find(
#     {"grades": {"$elemMatch": {"score": {"$gt": 90}}}},
#         # {
#         #     "grades.score": {"$gt": 90}
#         # },
#         {"restaurant_id": 1, "grades": 1}):
#     print(data)
#     print("-" * 100)

# count = 0
# for data in db.restaurants.aggregate(
#         [
#             {"$unwind": "$grades"},
#             {"$group": {"_id": "$restaurant_id", "total": {"$sum": "$grades.score"}}},
#             {"$match": {"total": {"$gt": 90}}}
#         ]):
#     print(data)
#     print(count)
#     count += 1
#     print("-" * 100)


# print(db.restaurants.find_one({"restaurant_id": "40398434"}))

# print(db.restaurants.count_documents({"grades.grade": "A"}))

# Q7
# for data in db.restaurants.aggregate(
#         [
#             {"$unwind": "$grades"},
#             {"$match": {"grades.grade": "A"}},
#             {"$group": {"_id": "$cuisine", "count": {"$sum": 1}}},
#         ]):
#     print(data)
#     print("-" * 100)


# print(len(list(db.restaurants.aggregate(
#     [
#         {"$unwind": "$grades"},
#         {"$match": {"grades.grade": "A", "restaurant_id": "30075445"}},
#     ]))))


# for data in db.restaurants.aggregate([
#     {"$match": {"grades": {"$elemMatch": {"grade": "A"}}}},
#     {"$group": {"_id": "$restaurant_id", "count": {"$sum": 1}}}
# ]):
#     print(data)
#     print("-" * 100)

# for data in db.restaurants.aggregate([
#     {"$group": {"_id": "$restaurant_id", "count": {"$sum": 1}}},
#     {"$match": {"count": {"$gt": 2}}}
# ]):
#     print(data)
#     print("-" * 100)

# print(db.restaurants.find_one({"restaurant_id": "40398434"}))

# for data in db.restaurants.aggregate([
#         {
#             "$unwind": "$grades"
#         },
#         {
#         "$project": {
#             "date": {"$toDate": "$grades.date"},
#             # "year": {"$year": {"$toDate": "$grades.date"}}
#             }
#         }]):
#     print(data)
#     print("-" * 100)


client.close()
