class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(self.name,self.age)
p1=Person(n="arun",a=23)
p1.show()
p2=Person(n="amal",a=34)
p2.show()