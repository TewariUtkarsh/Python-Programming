def getdata():  # Function Created
    '''This is the function to get the input from User'''   # Doc Strint Created
    getdata.name = input("Enter your Name: ")
    getdata.age = int(input("Enter your Age: "))
    getdata.prof = input("Enter your Profession: ")

def dispdata():
    print("\n\nName:",getdata.name,"\nAge:",getdata.age,"\nProfession:",getdata.prof,"\n\nThank You!!")

# print("Welcome\n")
# getdata()
# dispdata()
print(getdata.__doc__)  # To Display Doc String