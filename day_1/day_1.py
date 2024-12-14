# # import random
# # ram_at_position=0
# # n=0
# # def die():
# #     n=random.randrange(1,6)
# #     return n 
# # print(die())
# # l=[2,4]
# # s=[3,6]

# # n=1234
# # reverse=0
# # while n>0:
# #     t1=n%10
# #     reverse=reverse*10+t1
# #     n=n//10
# # print(reverse)


# # n1=int(input("enter a number"))
# # # n2=int(input("enter the number"))

# # print(n1*n1)

# # n1=float(input("enter the number"))
# # n2=float(input("enter the number"))
# # sum=n1+n2
# # print(sum/2)
# # n=int(input("enter the number  "))
# # for i in range (n):
# #     for i in range (n):
# #         print(n,end=" ")
# #     print()
# n=int(input("enter the number"))
# st=1
# sp=n-1
# for i in range (n):
#     for i in range (st):
#       print("*",end=" ")
#       st+=1
#     print()
#     for i in range (sp):
#         print(" ")
#         sp-=1
#     print()
       
# n = int(input("Enter the number of rows: "))
# for i in range(n, 0, -1):
#     print("*"*i)
# n=5
# num=1
# for i in range (1,n+1):
#     for t in range (1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()
# n=5
# for i in range (1,n+1):
#     print(" " * (n-i) , str(i) * (2*i-1))

# n=10
# m=1
# while n>0:
#     print(m)
#     m+=1
#     n-=1
#n=int(input("enter the number "))
# sum=0
# while n>0:
#    sum=sum+n
#    n-=1
# print(sum)
# t=1
# prod=0
# i=1
# while i<=10:
#     prod=0
#     prod=n*i
#     print(n," * ", i , "=", prod)
#     i+=1
#     # ten-=1

# for i in range (1,11):
#     print(n,"*",i, "=",n*i)



# n=int(input("enter the number "))
# a=0
# for i in range(1,n+1):
    
#     for k in range(0,i):
#          print(a,end=" ")
#          a+=1
#     for j in range(1,n-i):
#          print(" ",end=" ")
#     print()

# n=54321
# ct=0
# while n>0:
#     n%10
#     ct+=1
#     n=n//10
# print(ct)
  
# list1=[1,2,3,4,5,6777,7]
# for i in range (len(list1)-1,-1,-1):
#     print(list1[i])
# print("done")

# for i in range (-10 , 0):
#     print(i)


# for i in range (2,100):
#     ct=0
#     for j in range (1,i+1):
#        if i%j==0:
#            ct+=1
#     if ct==2:
#        print(i)
# n=10
# prod=1
# for i in range (3,0, -1):
#     prod=prod*i
# print(prod)   

# n1=0
# n2=1
# n=0
# for i in range (10):
#     n=n1+n2
#     print(n1+n2)
#     n1=n2
#     n2=n


# n=int(input("enter the number "))
# for i in range (n):
#     match n:
#         case 1:
#           print("manoj")
#         case 2:
#           print("ram")
#         case 3:
#           print("lokesh")
#         case 4:
#           print("reddy")

# n1=10
# n2=20
# n=n1+n2
# print("n2","=",n-n2,"n1","=",n-n1)

# str1=input("enter the string")
# vowels="aeiouAEIOU  "
# vowel_count=0
# for i in str1:
#     if i in vowels
#         vowel_count+=1
     
    
# num=int(input("enter the number "))
# for i in range(2 , num+1):
#     ct=0
#     for j in range (1,i+1):       
#         if i%j==0:
#             ct+=1      
#     if ct==2:
#        print(i)


# n1=30
# n2=40
# for i in range(int(n2/2),0,-1):
#     if n1%i==0 and n2%i==0:
#         print(i)
#         break