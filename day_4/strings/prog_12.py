# str1=input("Enter the string")
# n=int(input("Enter the number with in length of given string"))
# list1=list(str1)
# print(list1)
# list2=[]
# for char in list1:
#     if n>0:
#       ct1=char.lower() 
#       list2.append(ct1)
#       n-=1
#     else:
#        list2.append(char)
# print(list2)
#------------------------------------#


def lowercase_first_n_chars(input_string, n):
    if n > len(input_string):
        n = len(input_string)
    result = input_string[:n].lower() + input_string[n:]
    
    return result
input_string = input("Enter a string: ")
n = int(input("Enter the number of characters to lowercase: "))

print("Result:", lowercase_first_n_chars(input_string, n))



#--------------------------#
str1="RAMMOHAN"
n=3
print(str1[:n].lower()+str1[n:])