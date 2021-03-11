# FOR LOOP:
list1 = ["Apple", 6, "Banana", 99, "Mango", 95.5, 100, -88, 0, 2, -50000, 10000]    # List created with Elements of Different Data Types

print("Elements Eligible: ")

for item in list1:
    if str(item).isnumeric() and item>6.0 :     # Checking if the element in the List is a Number greater than 6.0
        print(item,end = " ")

# WHILE LOOP:
while(True):    
    a = int(input("Enter a number: "))
    if(a>100):  
        print("\nCongratulations Number is greater than 100\nThank You for using the program")
        exit(0)
    print("\nNumber less than 100\n")
    continue    # Continues to the next iteration
    
    