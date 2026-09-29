#Ask the user to enter three numbers and add the first two number and multiply the total by the third number
#Display the answer as "The answer is [answer]"

number_1=int(input("Enetr first number:"))
number_2=int(input("Enter the second number:"))
number_3=int(input("Enter the third number:"))
total =number_1+ number_2
answer=total * number_3
print(f"The answer is {answer}")