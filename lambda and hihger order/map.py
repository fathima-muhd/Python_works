# n=[1,2,3,4]
# print(list(map(lambda x:x**2,n)))
# print(tuple(map(lambda x:x**2,n)))
# print(set(map(lambda x:x**2,n)))


l=[{"name":"fathi","age":23,"email":"fm0909"},{"name":"farhah","age":23,"email":"farhah@gmail"}]
print(list(map(lambda l:l['email'],l)))