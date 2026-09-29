#sum of numbers divisible by 3 and 5 from 1 to 30
i=1
sum=0
while(i<=30):
    if i%5==0 and i%3==0:
        sum+=i
    i+=1
print("sum of numbers which are divisible by 3 and 5 are",sum)