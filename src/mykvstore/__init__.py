from pymongo import MongoClient

class KVStore:
    def __init__(self, uri: str) -> None:
        self.client = MongoClient(uri)
        self.db = self.client.get_database("mykvstore")
        self.collection = self.db.get_collection("mykvstore")


    def __getitem__(self, key) -> dict | None:
        return self.collection.find_one({"k": key})

    
    def __setitem__(self, key, value):
        if self[key] is not None:
            self.collection.update_one({"k": key}, {"$set": {"v": value}})
        else:
            self.collection.insert_one({"k": key, "v": value})

    def __delitem__(self, key):
        self.collection.delete_one({"k": key})