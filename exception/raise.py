try:
    n=int(input("number="))
    if n<0:
        raise ValueError("Number should be positive")
except ValueError as e:
    print(e)
else:
    print(n)
 