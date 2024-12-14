list1=input("enter the numbersss").split()
evenct=0
oddct=0
for num in list1:
    num=int(num)
    if num%2==0:
        evenct+=1
    else:
        oddct+=1
print(evenct)
print(oddct)