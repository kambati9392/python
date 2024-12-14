# import array
# arr1=array.array('i',[1,2,3,4,5,62,3,4,5,6,7])
# ele=4
# first_acc=arr1.index(ele)
# arr1.pop(first_acc)
# print(arr1)

arr1 = [1, 2, 3, 4, 5, 62, 3, 4, 5, 6, 7]
ele = 4

# Remove the first occurrence directly
if ele in arr1:
    arr1.remove(ele)

print(arr1)
