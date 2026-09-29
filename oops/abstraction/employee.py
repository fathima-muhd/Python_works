#an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.
from abc import ABC,abstractmethod
class Employee(ABC):

    def __init__(self):
        self.name=input("name=")
        self.age=int(input("age="))
        self.empid=int(input("empid="))

    @abstractmethod
    def calculate_salary(self):
        pass
class Fulltimeemployee(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.salary=int(input("salary="))
    def calculate_salary(self):
        print("full time monthly salary=",self.salary)

f=Fulltimeemployee()
f.calculate_salary()

class PartTimeEmployee(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.salary=int(input("salary="))
        self.hours=int(input("Hours worked per month="))
    def calculate_salary(self):
        salary=self.hours*self.salary
        print("Part time salary =",salary)

p=PartTimeEmployee()
p.calculate_salary()