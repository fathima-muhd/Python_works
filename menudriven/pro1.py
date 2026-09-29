def add():
    n1=int(input("enter n1:"))
    n2=int(input("Enter n2:"))
    print("sum is ",n1+n2)
def sub():
    n1=int(input("enter n1:"))
    n2=int(input("Enter n2:"))
    print("diff is ",n1-n2)
def mul():
    n1=int(input("enter n1:"))
    n2=int(input("Enter n2:"))
    print("prod is ",n1*n2)
def div():
    n1=int(input("enter n1:"))
    n2=int(input("Enter n2:"))
    print("div is ",n1/n2)
while(True): 
    print("1.Add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    else:
        exit()


