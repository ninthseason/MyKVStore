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
print(kvs["example"])  # hello, world!

# update entry
kvs["example"] = "hello, new world!"  # hello, new world!
print(kvs["example"])

# setting value to None is allowed, in MongoDB the value will be `null`
kvs["example"] = None
print(kvs["example"])  # None

# delete entry
del kvs["example"]
print(kvs["example"])  # None
