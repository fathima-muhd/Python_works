#check if number is divisible by both 3 and 5
#check if number is either divisble by 3 or 5
#else print"not divisible byu 3 and 5"

num=int(input("enter number:"))
if num%5==0 and num%3==0:
    print("Is divisible by 3 and 5")
elif num%5==0 or num%3==0:
    print("Is divisible by either 3 or 5")
else:
    print("Not divisible by both 3 and 5")