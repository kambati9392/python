# arr1=[1,2,3,4,5,6]
# print(arr1)
# print(arr1[2])
# print(arr1[:5])
# print(arr1[4:])

#if we want to store only integers
import array
int_arr1=array.array('i',[11,22,33,44,55,66,77,88,99,00])
print(int_arr1)

print(int_arr1[0])
print(int_arr1[6])
print(int_arr1[5])
print(int_arr1[4])
print(int_arr1[3])

for i in range(len(int_arr1)):
    print(int_arr1[i])