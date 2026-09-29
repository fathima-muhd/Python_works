def func(s):
    new={}
    for i in s:
        new[i]=s.count(i)
    return new
print(func("hello"))