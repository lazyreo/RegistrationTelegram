
from pymongo import MongoClient
from config import CLUSTER_ID

cluster = MongoClient(CLUSTER_ID)
register_bot_db = cluster["register_bot"]
users_collection = register_bot_db["users"]
users_collection.create_index("id")


def add_user(user: dict):
    if not is_exists(user["id"]):
        users_collection.insert_one(user)

def is_exists(user_id):
    r = users_collection.find_one({"id": user_id})
    return r is not None