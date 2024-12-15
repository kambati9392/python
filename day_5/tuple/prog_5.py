
# tuple1=(1,2,3,"ram","mohan",1,2,3,"ram")
# print("tuples--->",tuple1)

# tup2=[]
# for item in tuple1:
#     item=str(item)
#     if item in tup2:
#         pass
#     else:
#         tup2.append(item)
# print(tup2)
# tup3=tuple(tup2)
# print(tup3)



# Define a tuple with repeated items
my_tuple = (10, 20, 30, 10, 40, 50, 20, 30, 10)

# Use a dictionary to count occurrences
from collections import Counter

# Count the occurrences of each item in the tuple
item_counts = Counter(my_tuple)

# Find items that are repeated
repeated_items = [item for item, count in item_counts.items() if count > 1]

# Print the results
print("Original tuple:", my_tuple)
print("Repeated items:", repeated_items)








# Define a tuple with repeated items
my_tuple = (10, 20, 30, 10, 40, 50, 20, 30, 10)

# Create an empty list to store repeated items
repeated_items = []

# Loop through the tuple to find duplicates
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

# Print the results
print("Original tuple:", my_tuple)
print("Repeated items:", repeated_items)
