#Ask for the total price of the bill and also the count of diners and then calculate how much each person should pay

total_price=int(input("Enter total price:"))
Diners_count=int(input("enter the count of people:"))
amount=total_price/Diners_count
print(f"Everyone should pay Rs.{amount}")