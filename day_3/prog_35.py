str1=input("Enter the string")
has_digit=False
for char in str1:
    if char.isdigit():      #if '0' <= char <= '9':
          has_digit=True    #if char.isdigit():
      
if  has_digit:
     print("not string")
else:
     print("string")