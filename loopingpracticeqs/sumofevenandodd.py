#sum of even and product of odd numbers from 1 to n
i=1
n=int(input("Enter n:"))
sum=0
product=1
while(i<=n):
    if i%2==0:
        sum+=i
    else:
        product*=n
    i+=1
print("sum is",sum)
print("product is",product)