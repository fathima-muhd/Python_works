class Person:
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("roll no:"))
        self.course=input('course:')
        self.mark=int(input("marks:"))
    def show(self):
        super().show()
        print(self.rollno,self.course,self.mark)
    def updatemark(self):
        self.mark=int(input("new marks:"))
    

s=Student()  
s.show()
s.updatemark()
#if we dont create init() in child class it will go to the init( ) of parent class
#otherwise it will go the child class
#if we need to call both init() use super() in child init()

    