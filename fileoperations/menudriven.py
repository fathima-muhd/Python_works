def file_read():
    filename=input("enter the filename: ")
    f=open(filename,"r")
    content=f.read()
    print(content)
    f.close()

def file_write():
    filename=input("Enter the filename: ")
    f=open(filename,"w")
    content=input("Enter the content: ")
    f.write(content)
    f.close()
    
def file_append():
    filename=input("Enter the filename: ")
    f=open(filename,"a")
    content=input("Enter the content: ")
    f.write(content)
    f.close()

def file_search():
    filename = input("Enter the filename: ")
    search = input("Enter the word to search: ")
    f = open(filename, "r")
    content = f.read()
    if search in content:
        print("Word found")
    else:
        print("Word not found")
    f.close()

# def file_search():
#     filename=input("Enter the filename: ")
#     f=open(filename,"r")
#     print(f.tell())
#     f.seek(0)
#     f.close()

def file_delete():
    import os
    filename=input("Enter the filename: ")
    os.remove(filename)
    print("file is deleted")

def file_exit():
    exit()

while(True):# infinite loop
    print("1. Read 2. Write 3. Append 4. Search 5. Delete 6. Exit")
    ch=int(input("Enter your choice: "))

    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    elif ch==6:
        file_exit()
    else:
        print("invalid choice")