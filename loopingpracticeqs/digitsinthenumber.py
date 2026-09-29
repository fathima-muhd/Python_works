n=int(input("Enter n:"))
count=0   
while(n>0):
    n=n//10     #153//10   15//10    1//10 >>>> 1  5  3
    count+=1
print("count is",count)
