try:
    num1=int(input("Number1="))
    num2=int(input("Number2="))
    sum=num1 + num2
    print("sum =",sum)
except ValueError as e:
    print(e)
    print(type(e))
except Exception as e:
    print(e)
    print(type(e))
finally:
    print("done")


