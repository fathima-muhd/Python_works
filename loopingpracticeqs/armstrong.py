number=1534
n=number
sum=0
while(number>0):
    digit=number%10
    sum+=digit**3     #3**3 + 5**3 + 1**3
    number=number//10
if(sum==n):
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")
