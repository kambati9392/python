n=5
for i in range(n):
    if i==0:
        for j in range(n):
           print("*",end=" ")
    else:
        for j in range(n):
            if j==n//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()