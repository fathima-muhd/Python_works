class Book:
    def __init__(self):
        print("enter the details:")
        self.title=input("title:")
        self.author=input("author:")
        self.languages=input("lang:")
        self.price=int(input("price:"))
        self.pages=int(input("pages:"))
    def gettitle(self):
        print(self.title)
    def getauthor(self):
            print(self.author)
    def getprice(self):
            print(self.price)
    print("updated value")
    def settitle(self):
        self.title=input("new title:")
        self.gettitle()
    def setauthor(self):
        self.author=input("new author:")
        self.getauthor()
    def setprice(self):
        self.price=input("new price:")
        self.getprice()
        



    
b1=Book()
b2=Book()
b1.gettitle()
b1.getauthor()
b1.getprice()

b2.gettitle()
b2.getauthor()
b2.getprice()

b1.settitle()
b1.setauthor()
b1.setprice()



b2.settitle()
b2.setauthor()
b2.setprice()

