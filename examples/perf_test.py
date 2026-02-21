import time
from mykvstore import KVStore

kvs = KVStore()

start_time = time.time()
for i in range(100):
    kvs[i] = i
end_time = time.time()

print(f"Inserting 100 entries uses {end_time - start_time}s")
# Inserting 100 entries uses 9.00014591217041s