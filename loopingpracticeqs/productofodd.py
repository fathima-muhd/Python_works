#product of odd digits
num=int(input("enter number="))
digit=0
product=1
while(num>0):
    digit=num%10
    if digit%2!=0:
        product*=digit
    num=num//10
print("product of odd digits is ",product)
