class Student:
    def __init__(self):
        self.name=input("name:")
        self.rollno=int(input("roll no:"))
        self.mark1=int(input("mark1:"))
        self.mark2=int(input("mark2:"))
        self.mark3=int(input("mark3:"))
    def display(self):
        print("roll no:",self.rollno)
        print("total mark:",self.mark1+self.mark2+self.mark3)
s1=Student()
s2=Student()
s1.display()
s2.display()
