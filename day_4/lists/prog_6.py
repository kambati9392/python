# list1=[1,2,3,4,5,6,7,89,1,2,3,4,56]
# list2=sorted(list1)
# print(list2)
# list3=[]
# for item in list1:
#     if item in list3:
#         list2.remove(item)
#     else:
#         list3.append(item)
# print(list3)

# Function to remove duplicates from a list
def remove_duplicates(input_list):
    return list(set(input_list))

# Example list
input_list = [1, 2, 2, 3, 4, 4, 5, 5]

# Calling the function and printing the result
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)
