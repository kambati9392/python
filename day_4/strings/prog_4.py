
str1=input("Enter the string:::")
if len(str1)<3:
    print(str1)
else:
    if "ing" in str1:
        str1+="ly"
    else:
        str1+="ing"
    print(str1)