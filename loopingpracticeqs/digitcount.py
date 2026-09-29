num=int(input("Enter n="))
digit=0
count=0
while(num>0):
    digit=num%10
    if digit%2==0:
        count+=1
    num=num//10
print("count of even digits is ",count)