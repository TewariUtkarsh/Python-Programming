myCars = ("Toyota","Mercedes","BMW","Audi","BMW")     #Tuple declared 
print("\nTuple: ",myCars)

# Tuple has only 2 built in functions:

# 1.count()- To count the number of Element ,that is passed as the Parameter, in the Tuple
print("\nNumber of times BMW is present in the Tuple: ",myCars.count("BMW")) 
print("Number of times Audi is present in the Tuple: ",myCars.count('Audi'))

# 2.index()- Returns the Index of the Element that is passed as an Arguement
print("\nToyota is present at index ",myCars.index("Toyota"))

print(f"\nTuple: {myCars}")
