list1=['ram','mohan','reddy','lokesh','eran']
n=int(input("Enter the number"))
for item in list1:
   item=str(item)
   if len(item)>n:
     print(item)