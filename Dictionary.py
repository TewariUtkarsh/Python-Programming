dict1 = { "Fruit":"Apple", "Furniture":"Bed", "Device":"iPad"}  # Created a Dictionary
print(dict1)

dict1["Language"] = "C++"
print(dict1)

dict1["Trash"] = "Negative"
print(dict1)

del dict1["Trash"]  # Deleting element "Trash" from dict1
print(dict1)

dict2 = dict1.copy()    # Copying the content of Dict1 to Dict2
print(dict2)

dict2["Electronics"] = "Fan"    # Adding an Element in the Dictionary
print(dict2)

print(dict1)

print(dict1.get("Language"))    # Or print(dict1["Language"])
