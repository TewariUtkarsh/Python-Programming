print("\nWelcome to Program demonstrating about Lists in Python: ")

x = input("\nEnter the elements separted by commas:\n")
lst = list(x.split(","))    # Spliting string input, x, thus converting a List 

print("\nList entered: ",lst)

p = int(input("\nEnter the Index for Insertion: "))
x = input("Enter the element to be inserted: ")
lst.insert(p,x)     # Inserting element x at index p

print("\nList after Insertion: ",lst)

p = int(input("\nEnter the Index at which you have to perform removal: "))
lst.pop(p-1)        # Deleting the element at the last index

print("\nList after Removal: ",lst)

lst.sort()          # Sorting the List
print(f"\nSorted List: {lst}")

# print(f"\nElement: {lst[8]}")
