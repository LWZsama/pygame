list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
print(id(list1))
print(id(list2))

print(list1)
list2 = list1
list1.append(999)
print(id(list2),"\n",id(list1))