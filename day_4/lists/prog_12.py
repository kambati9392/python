list1=[1,2,3,4]
list2=[1,3,4,5,6,7]
list3=[]
for item in list2:
    if item not in list1:
        list3.append(item)
print(list3)


difference = [item for item in list1 if item not in list2]