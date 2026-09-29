num=int(input("enter number:"))
length=1
square=num**2
if square %(10** length)==num:
    print("The number is automorphic")
else:
    print("Not automorphic")