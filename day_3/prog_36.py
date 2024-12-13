x=int(input("Enter the number "))
y=int(input("Enter the number "))
z=int(input("Enter the number "))
if x==y==z:
    print("equi")
elif x==y or y==z or z==x :
    print("iso")
else:
    print("scalan")