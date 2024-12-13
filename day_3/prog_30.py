n=10
sp=n-2
for i in range(1):
    for j in range(n):
        print("*",end=" ")
    print()
for k in range(sp):
    for l in range(sp):
        print(" ",end=" ")
    sp-=1
    for m in range(1):
        print("*",end=" ")
    print()
for i in range(1):
    for j in range(n):
        print("*",end=" ")
    