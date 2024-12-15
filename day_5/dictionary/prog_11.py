my_list = [1, 2, 3, 4]
nested_dict = {}
#for item in my_list:
for item in reversed(my_list):
    nested_dict = {item: nested_dict}

print(nested_dict)
