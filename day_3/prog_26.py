n=5
m=n+2
for i in range(m):
    if i==0 or i==m-1 or i==m//2:
        for j in range(0,n):
            print("*",end=" ")
    elif i==m//2-1 or i==m//2-2:
        for j in range(n):
            if j==0:
              print("*",end=" ")
            else:
               print(" ",end=" ")
    elif i==m//2+1 or i==m//2+2:
        for j in range(n):
            if j==n-1:
              print("*",end=" ")
            else:
               print(" ",end=" ")
    
    print()
        
