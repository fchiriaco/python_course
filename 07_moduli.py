import json

data = {
    "product": "Laptop",
    "price": 850,
    "tags": ["electronics", "portable"],
}

json_string = json.dumps(data, indent=2)
print(json_string)

parsed = json.loads(json_string)
print(parsed["product"])

with open("product.json", "w") as f:
    json.dump(data, f, indent=2)

with open("product.json", "r") as f:
    loaded = json.load(f)
    print(loaded)