#sum of squareroot of even numbers and sum of square of odd numbers 1 to n

i=1
n=int(input("Enter n:"))
sumeven=0
sumodd=0
while(i<=n):
    if i%2==0:
        sumeven+=i**0.5
    else:
        sumodd+=i**2
    i+=1
print("sum is",sumeven)
print("sum of sqaure of odd numbers is",sumodd)