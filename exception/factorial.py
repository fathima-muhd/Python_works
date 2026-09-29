import math
while(True):
    try:
        num=int(input("number="))
        print(math.factorial(num))
        break
    except ValueError:
        print("Value error")

