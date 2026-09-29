#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

try:
    d={"name":"arun","age":23,"place":"ekm"}
    k=input("Enter a key to find the value: ")
    print(d[k])
except KeyError:
    print("Key Error")