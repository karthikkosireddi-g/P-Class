import json

j1 = '{"id" : 1, "name" : "AA"}' # JSON Data

print(type(j1))
print(j1)

myJSON = json.loads(j1)
print(type(myJSON))
print(myJSON["id"])
print(myJSON["name"])


# get JSON data from a file

f1 = open("I:\\Python\\Class2-Projects\\j1.json", "r")
myJSON2 = json.load(f1)
print(type(myJSON2))
print(myJSON2["id"])
print(myJSON2["name"])


