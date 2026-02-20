# MyKVStore

A tiny key-value store backed by MongoDB, with dictionary-style access in Python.

## Features
- `kvs[key]` reads a value record from MongoDB.
- `kvs[key] = value` inserts or updates.
- `del kvs[key]` deletes by key (no error if missing).
- Uses a fixed database and collection name: `mykvstore`.

## Requirements
- Python 3.14+
- MongoDB connection URI
- Dependency: `pymongo>=4.16.0`

## Installation
### With uv (recommended)
```bash
uv sync
```

### With pip
```bash
pip install -e .
```

## Configuration
Set a MongoDB URI in `MONGO_URI`.

PowerShell:
```powershell
$env:MONGO_URI="mongodb+srv://<user>:<password>@<cluster-host>/"
```

Bash:
```bash
export MONGO_URI="mongodb+srv://<user>:<password>@<cluster-host>/"
```

## Quick Start
```python
from mykvstore import KVStore

kvs = KVStore("mongodb+srv://<user>:<password>@<cluster-host>/")

# Create
kvs["greeting"] = "hello"

# Read
print(kvs["greeting"])
# {'_id': ObjectId(...), 'k': 'greeting', 'v': 'hello'}

# Update
kvs["greeting"] = "hello again"

# Delete (safe if key does not exist)
del kvs["greeting"]
```

## Run the Example
```bash
uv run python examples/example.py
```

The example expects `MONGO_URI` to be set.

## API
### `KVStore(uri: str)`
Creates a client using the provided MongoDB URI and binds to:
- database: `mykvstore`
- collection: `mykvstore`

### `__getitem__(key)`
Returns `collection.find_one({"k": key})`.
- Returns a MongoDB document (including `_id`, `k`, `v`) when found.
- Returns `None` if missing.

### `__setitem__(key, value)`
- If key exists: updates `v` only.
- If key does not exist: inserts `{"k": key, "v": value}`.

### `__delitem__(key)`
Deletes one record matching the key. Missing keys are ignored.

## Notes
- Values are stored in field `v`; keys are stored in field `k`.
