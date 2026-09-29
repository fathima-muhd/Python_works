#set the total to zero to start with.
# while the total is 50 or less,ask the user to input a number.
# Then add the number to the total.if the total is over 50 print the total
total=0
while(total<=50):
    n=int(input("enter n:"))
    total=total+n
print("Total is",total)