
# tuple1=(1,2,3,"ram","mohan")
# print("tuples--->",tuple1)
# a,b,c,d,e=tuple1

# print("a-->",a)
# print("b-->",b)
# print("c-->",c)
# print("d-->",d)
# print("e-->",e)

my_tuple = (1, 2, 3, 4, 5)
a, b, *rest = my_tuple

print("a =", a)        # Output: a = 1
print("b =", b)        # Output: b = 2
print("rest =", rest)  # Output: rest = [3, 4, 5]


my_tuple = (10, 20, 30, 40, 50, 60)

# Unpack with the * operator for the last elements
*rest, x, y = my_tuple

print("rest =", rest)  # All values except the last two
print("x =", x)        # Second to last value
print("y =", y)        # Last value
