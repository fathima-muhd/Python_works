#ask the user to enter a number.Keep asking until they enter a vlue over 5 
# and then display the message "the last number you entered was {number} and stop the program"

n=int(input("n:"))
while(n<=5):
    n=int(input("n:"))   
print("the last number you entered was" ,n)