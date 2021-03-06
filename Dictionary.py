dict1 = { "Fruit":"Apple", "Furniture":"Bed", "Device":"iPad"}
print(dict1)

dict1["Language"] = "C++"
print(dict1)

dict1["Trash"] = "Negative"
print(dict1)

del dict1["Trash"]
print(dict1)

dict2 = dict1.copy()
print(dict2)

dict2["Electronics"] = "Fan"
print(dict2)

print(dict1)

print(dict1.get("Language"))    # Or print(dict1["Language"])
