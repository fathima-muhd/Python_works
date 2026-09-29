from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("length="))
        self.breadth=int(input("breadth="))
    def get_area(self):
        print("area of rectangle is",self.length*self.breadth)
    def get_perimeter(self):
        print("Perimeter of rectangle is",2*(self.length+self.breadth))

r=Rectangle()
r.get_perimeter()
r.get_area()

class Square(Shape):
    def __init__(self):
            self.side=int(input("side="))
    def get_area(self):
        print("area of square is",self.side*self.side)
    def get_perimeter(self):
        print("Perimeter of square is",4*self.side)

s=Square()
s.get_perimeter()
s.get_area()
