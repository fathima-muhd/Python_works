#count of odd numbers which are not div by  from 1 to 50
i=1
count=0
while(i<=50):
    if i%2!=0 and i%7!=0:
        count+=1
    i+=1
print("count is",count)