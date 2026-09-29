#wap to check if a number is positive or negative

num=int(input("Enter number:"))
if num>0:
    print("Positive")
elif num==0:
    print(f"{num} is neither positive nor negative")
else:
    print("Negative")