# list=[1,1,2,3,4]
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)

# print(new)

#remove the duplicates by converting in to set
list=[1,1,2,3,4]
print(set(list))

#intersectiojn and union

l1=[12,23,45,56]
l2=[12,23,78,90]
print(set(l1).intersection(set(l2)))
print(set(l1).union(set(l2)))