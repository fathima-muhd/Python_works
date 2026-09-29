class Parent:
    def m1(self):
        print("Method m1 from parent class")
    def m2(self):
        print("Method m2 from parent class")
# p=Parent()
# p.m1()
# p.m2()

class Child(Parent): #child inherited from parent
    def m1(self): #method overriding 
        super().m1()
        print("Method m1 from child class")
    def m3(self):
        print("Method m3 from child class")

c=Child()
c.m1() #child class called parent method
c.m2() #child class called paernt method
c.m3()
