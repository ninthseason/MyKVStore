from pymongo import MongoClient
from importlib.util import find_spec
import os

class KVStore:
    def __init__(self, uri: str | None = None) -> None:
        """Initialize KVStore with a MongoDB URI.

        If `uri` is `None`, this method resolves `MONGO_URI` in order from:
        1. The local environment variable.
        2. Google Colab secrets. (When in google colab environment)
        """
        if uri is None:
            uri = self.default_uri()
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

    @staticmethod
    def default_uri() -> str:
        uri = os.getenv("MONGO_URI")
        if uri is None and find_spec("google") is not None:  # in google colab
            from google.colab import userdata  # type: ignore
            uri = userdata.get("MONGO_URI")
        if uri is None:
            raise RuntimeError("Can't get default uri from `MONGO_URI` environment variable or `MONGO_URI` google colab secrets.")
        return uri
