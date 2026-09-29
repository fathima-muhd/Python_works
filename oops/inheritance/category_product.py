#single inheritance
class Category:
    def __init__(self):
        self.categoryname=input("category name:")
    def show_category(self):
        print("category is",self.categoryname)
    
class Product(Category):
    def __init__(self): 
        super().__init__()
        self.product=input("product:")
        self.price=int(input("Price:"))
        self.quantity=int(input("quantity:"))
    def total_price(self):
        self.total_price=self.price*self.quantity
        print("total price:",self.total_price)

p=Product()
p.show_category()
p.total_price()