#display bonus percentage 
#salary         Bonus
#50000          20%
#30000          10%
#Below 30000    5%

salary=int(input("enter salary:"))
if salary==50000:
    bonus=salary + salary *(20/100)
    print("bonus percentage is",bonus)
elif salary==30000:
    bonus=salary + salary *(10/100)
    print("bonus percentage is",bonus)
elif salary<30000:
    bonus=salary + salary *(5/100)
    print("bonus percentage is",bonus)
else:
    print("Thank you")