# n1=int(input("enter the niumber "))
# n2=int(input("enter the number "))
# if n1>n2:
#     print(n1 )
# elif n2>n1:
#     print(n2)

# n1=int(input("enter the niumber "))
# n2=int(input("enter the number "))
# n3=int(input("enter the niumber "))
# # if n1>n2 and n1>n3:
#     print(n1)
# elif n2>n1 and n2>n3:
#     print(n2)
# else:
#     print(n3)
# big=n1
# if n2>big:
#     big=n2
# if n3>big:
#     big=n3
# print(big)

# n=int(input("enter the number "))
# if n>0:
#     print("positive number")
# else:
#     print("negitive number")

# n1=10
# n2=20
# if n1==n2:
#     print("equal")
# else:
#     print("not")

# p=20 
# c=30 
# h=70 
# d=40
# if p>=35 and c>=35 and h>=35 and d>=35:
#     print("pass")
# else:
#     print("fail")
# m=12
# if m<=12 or m>=1:
#    print("okey")
# else:
#    print("not matching")

# n=99
# if n>9 and n<100 or n<-9 and n>-100:
#     print("two digit")
# else:
#     print("nota two digit number")

# y=2028
# if y%4==0 and y%100!=0 or y%400==0:
#     print("leap year")
# else:
#     print("not a leap year")

# n1=2
# n2=2
# n3=1
# if n1==n2 or n1==n3 :
#     print("equal")
# elif n2==n1 or n2==n3:
#     print("equal")
# else:
#     print("not equal")

# n=2
# if n%3==0 and n%5==0:
#     print("sanju weds geetha")
# elif n%3==0:
#     print("sanju")
# elif n%5==0:
#     print("geetha")
# else:
#   print("breakup")

# d=21
# m=2
# y=2024
# if d>0 and d<32 and m>0 and m<13 and y>0 and y<2025:

# def max(n1,n2):
#     if n1>n2:
#         return n1
#     else:
#         return n2

# print(max(20,30))

def special(n):
    n1=n%10
    n2=n//10
    n3=n1+n2+n1*n2
    return n3==n
print(special(30))

mon=int
