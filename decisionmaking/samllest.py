#smallest among 3
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
num3=int(input("Enter number:"))
if num1<num2 and num1<num3:
    print(f"{num1} is smallest")
elif num2<num1 and num2<num3:
    print(f"{num2} is smallest")
else:
    print(f"{num3} is smallest")