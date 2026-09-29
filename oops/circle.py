class Circle:
    def __init__(self):
        self.radius=float(input("radius:"))
    def getarea(self):
        self.area = 3.14*self.radius**2
        print(self.area)
    def getperimeter(self):
        self.perimeter=2*3.14*self.radius
        print(self.perimeter)
c1=Circle()
c1.getarea()
c1.getperimeter()
c2=Circle()
c2.getarea()
c2.getperimeter()