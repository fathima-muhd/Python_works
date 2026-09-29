# A number thta has a factor of 1 and that number itself

number=4
for i in range(2,number):
    if number%i==0:
        print("not prime number")
        break #used to stop the entire for loop
    else:
        print("prime number")
        