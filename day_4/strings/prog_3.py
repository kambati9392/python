str1=input("Enter the string")
list1=list(str1)
print(list1)
list2=[]
for char in list1:
    if char in list2:
        list2.append("$")
    else:
        list2.append(char)
print(list2)
result_string=''.join(list2)
