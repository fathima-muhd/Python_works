num=int(input("Enter num:"))
digit=0
counteven=0
countodd=0
while(num>0):
    digit=num%10   #153%10 >>3    15%10>> 5     1%10>>0
    if digit%2==0:
        counteven+=1
    else:
        countodd+=1
    num=num//10     #153//10>> 15   15//10 >> 1     1//10 >>0
print("count of even is",counteven)
print("count of odd is",countodd)
