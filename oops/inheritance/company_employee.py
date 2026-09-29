class Company:
    def __init__(self):
        self.companyname=input("company name:")
        self.location=input("Location")
    def display_company(self):
        print(self.companyname,self.location)


class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=input("Employee id:")
        self.name=input("Employee name:")
        self.designation=input("Employee design:")
        self.salary=int(input("salary:"))
    def display_details(self):
        super().display_company()
        print(self.empid,self.name,self.designation,self.salary)
    def update_salary(self):
        self.salary=self.salary+self.salary *(10/100)
        print("incremented salary",self.salary)

e=Employee()
e.display_details()
e.update_salary()

