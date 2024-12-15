# from collections import Counter
# string1="rammohanreddy"
# #for char in string1:
# ct=Counter(string1)
# print(ct)

str1="rammohan reddy"
dict1={}
for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
print(dict1)