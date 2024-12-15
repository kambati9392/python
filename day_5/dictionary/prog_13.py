
my_dict = {
    'a': [1, 2, 3],
    'b': [4, 5],
    'c': 'not a list',
    'd': [6, 7, 8, 9]
}

total_items = 0
for value in my_dict.values():
    if isinstance(value, list): 
        total_items += len(value)  

print("Total number of items in dictionary values that are lists:", total_items)
