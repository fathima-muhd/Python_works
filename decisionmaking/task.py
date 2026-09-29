"""
n odd,print weird
n is even and inclusive range of 2 to 5,not weird
n is even and inclusive range of 6 to 20 ,weird
n is even and greater than 20,print not weird


"""
num=int(input("Enter number:"))
if num%2==1:
    print("Weird")
elif num%2==0 and num>=2 and num<=5:
    print("Not Weird")
elif num%2==0 and num>=6 and num<=20:
    print("Weird")
elif num%2==0 and num>20:
    print("Not weird")

"""
num=int(input("Enter number:"))
if num%2==0:  
    if num>=2 and num<=5:
    print(" Weird")
    elif num>=6 and num<=20:
    print("Not Weird")
    elif num%2==0 and num>20:
    print("Weird")
else:
    print("Not Weird)

"""