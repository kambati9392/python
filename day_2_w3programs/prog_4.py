n=int(input("enter the number "))
sp=n
st=n-1
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    # for k in range(sp):
    #     print(" ",end=" ")
    #     sp-=1
    print()
for r in range(n):
    for l in range(st):
      print("*",end=" ")
    st-=1
    print()
    

    
