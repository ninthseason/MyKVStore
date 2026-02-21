from pymongo import MongoClient
import os

class KVStore:
    def __init__(self, uri: str | None = None) -> None:
        if uri is None:
            uri = os.getenv("MONGO_URI")
            if uri is None:
                raise RuntimeError("Argument `uri` does not specify and can't read `MONGO_URI` from environment variables.")
        self.client = MongoClient(uri)
        self.db = self.client.get_database("mykvstore")
        self.collection = self.db.get_collection("mykvstore")


    def __getitem__(self, key) -> dict | None:
        e = self.collection.find_one({"k": key})
        return None if e is None else e["v"]

    
    def __setitem__(self, key, value):
        if self[key] is not None:
            self.collection.update_one({"k": key}, {"$set": {"v": value}})
        else:
            self.collection.insert_one({"k": key, "v": value})

    def __delitem__(self, key):
        self.collection.delete_one({"k": key})