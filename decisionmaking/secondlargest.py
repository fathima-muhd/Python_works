#second largest
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
num3=int(input("Enter number:"))
if num1>num2 and num1<num3 or num1>num3 and num1<num2:
    print(f"{num1} is sec_largest")
elif num2>num1 and num2<num3 or num2>num3 and num2<num1:
    print(f"{num2} is sec_largest")
else:
    print(f"{num3} is sec_largest")