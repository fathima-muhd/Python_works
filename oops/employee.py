class Employee:
    def __init__(self):
        print("Enter Employee details")
        self.name=input("name:")
        self.empid=int(input("empid:"))
        self.age=int(input("age:"))
        self.place=input("place:")
        self.salary=int(input("salary:"))
        self.designation=input("design:")
    def getsalary(self):
        print("salary:",self.salary)
    def showpersondetails(self):
        print("name:",self.name,"age:",self.age,self.place)

e1=Employee()
e2=Employee()
e1.getsalary()
e1.showpersondetails()
e2.getsalary()
e2.showpersondetails()

