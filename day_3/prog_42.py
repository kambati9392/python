list1=input("Enter the numbers  ").split()
sum=0
svg=0
for i in list1:
    i=int(i)
    sum=sum+i
avg=sum//len(list1)
print(sum , avg )