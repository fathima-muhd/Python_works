# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
try:
    filename=input("enter the filename: ")
    f=open(filename,"r")
    content=f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("File Not Found Error")