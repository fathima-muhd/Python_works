f1=open("f1.txt","a+")
print("First file pointer position:",f1.tell())   #Tells the position of file pointer
f1.write("python")
print("file pointer position after appending:",f1.tell())   #Tells the position of file pointer
f1.seek(0)     #change the file pointer position
print("after file pointer position change:",f1.tell())  
print(f1.read())
f1.close()