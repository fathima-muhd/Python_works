# wap to calculate the bike tax 
# if the price of the bike is above 100000 add tax of 12% alongwith price to total
# if the  price of the bike is above or equal to 50k and 
# less than or equal to 100000 add tax of 7%
# if the price is below 50k add 5% tax to it

price=int(input('Enter price:'))
if price>100000:
    tax=price+price*0.12
    print("Bike tax is",tax)
elif price>=50000 and price<=100000:
    tax=price+price*0.07
    print("Bike tax is",tax)
else:
    tax=price+price*0.05
    print("Bike tax is",tax)
