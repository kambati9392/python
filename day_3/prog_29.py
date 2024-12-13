# n=int(input("Enter the number "))
# m=n-2
# for i in range(n):
#     if i==0 or i==1 or i==n-2 or i==n-1:
#         for j in range (m):
#             if j==0 or j==m-1:
#                print("*",end=" ")
#             else:
#                  print(" ",end=" ")
#     if i==3:
#         for j in range(m):
#             if j==2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     if i==2 or i==4:
#         for j in range(m):
#             if j==1 or j==m-2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()


n = int(input("Enter an odd number: "))

# Check if the number is odd
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(n):
        for j in range(n):
            # Print '*' when row index equals column index or their sum equals n-1
            if i == j or i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Move to the next line after each row
