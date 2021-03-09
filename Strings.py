
# Strings:
a = " Hello User!r!r "
print(a)

# Operations that can be performed on strings:
# 1.Length 
print("\nLength of the String:",len(a))
# 2.Convert string to Lower 
print("\nConverting string to lower case:",a.lower())
# 3.Convert string to Upper
print("\nConvreting string to upper case:",a.upper())
# 4.Stripping Ends of thr String
print("\nStripping the String:",a.strip())
# 5.Replace anything in the String
print("\nReplace ! in the string:",a.replace("!",". How you doing??"))
# 6.Split function for String 
print("\nSplitting the String:",a.split('!'))

name = "harry"
print("\n\nName:", name[0].upper()+name[1:])
str1 = "Hello"
str2 = int(42.5)
print(str1,str2)

# Another example of String Slicing
str1 = "Hello World Hello"
print(str1[::-1])
print(str1.find("Hello"))
