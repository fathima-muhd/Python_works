class Person:
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
    def show(self):
        print(self.name,self.age)
p1=Person()
p2=Person()
p1.show()
p2.show()