n1=int(input("enter the number n1 "))
n2=int(input("enter the number n2 "))
n3=int(input("enter the number n3 "))

if n1<n2 and n3>n2 or n1>n2 and n3<n2 :
    print("median :", n2)
elif n2<n1 and n3>n1 or n2>n1 and n3<n1:
    print("median : ",n1)
else:
    print("median : ",n3)