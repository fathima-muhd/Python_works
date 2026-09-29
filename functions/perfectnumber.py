def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    print("perfect" if num==sum else "not perfect")
perfect(6)
    