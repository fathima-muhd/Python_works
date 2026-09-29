class Student:
    def __init__(self):
        self.rollno=int(input("roll no:"))
        self.name=input("Name:")
        self.marks=int(input("Marks:"))
    def updatemarks(self):
        newmark=int(input("marks:"))
        print("updated marks:",newmark)
    def display(self):
        print("roll no is",self.rollno)
        print("name is",self.name )
        print("marks is",self.marks)

l=[]
while(True):
    print("1.add student")
    print("2.update marks")
    print("3.dipslay student details")
    print("4.search student")
    print("5.delete student")
    print("6.exit")

    ch=int(input("Enter choice:"))

    if ch==1:
        s=Student()
        l.append(s)
    elif ch==2:
        rollno=int(input("roll no:"))
        for i in l:
            if i.rollno==rollno:
                i.updatemarks()
                break
        else:
            print("student does not exist")
    elif ch==3:
        if len(l)==0:
            print("No student record")
        else:
            for i in l:
                i.display()
    elif ch==4:
        rollno=int(input("enter roll no:"))
        for i in l:
            if i.rollno==rollno:
                print("student exist")
                break
        else:
            print("student does not exist")
    elif ch==5:
        rollno=int(input("rollno:"))
        for i in l:
            if rollno==i.rollno:
                l.remove(i)
                break
        else:
            print("student does not exist")
    else:
        exit()