# import array
# # from collections import Counter
# arr1=[1,2,3,4,5,6,7,8,9,2,4,6,8,9,1,4,5,6,,7,9,2,3,4,6,]
# print(arr1)
# element=2
# count=arr1.count(2)
# print(count)

import array
arr1=[1,2,3,4,5,1,2,3,4,5,6,7,89]
ele_ct={}
for ele in arr1:
    if ele in ele_ct:
        ele_ct[ele]+=1
    else:
        ele_ct[ele]=1
print(ele_ct)

