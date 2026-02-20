from mykvstore import KVStore
import os

uri = os.getenv("MONGO_URI")
if uri is None:
    print("Can't read `MONGO_URI` from environment varibles.")
    exit(1)

kvs = KVStore(uri)

# delete a non-existent entry will do nothing
del kvs["example"]
print(kvs["example"])  # None

# add entry
kvs["example"] = "hello, world!"
print(kvs["example"])  # {'_id': ObjectId('69989f97cb4dd1b2cf332613'), 'k': 'example', 'v': 'hello, world!'}

# update entry
kvs["example"] = "hello, new world!"  # {'_id': ObjectId('69989f97cb4dd1b2cf332613'), 'k': 'example', 'v': 'hello, new world!'}
print(kvs["example"])

# setting value to None is allowed
kvs["example"] = None
print(kvs["example"])  # {'_id': ObjectId('6998a0b913506d5a6033c688'), 'k': 'example', 'v': None}

# delete entry
del kvs["example"]
print(kvs["example"])  # None
