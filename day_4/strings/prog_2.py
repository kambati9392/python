# from  collections import Counter 
str1=input("enter the string")
# freq=Counter(str1)
# print(freq)

freq={}
for char in str1:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)