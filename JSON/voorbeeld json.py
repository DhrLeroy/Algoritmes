import json

data = {}

data["A"] = 1
data["B"] = 2
data["C"] = 3

with open("data.json", "w") as f:
    json.dump(data,f)

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
print(data["B"])