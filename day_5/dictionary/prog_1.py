# dict1={'a':1,'b':2,'c':4,'d':7}
# print(dict1)
# dict2=sorted(dict1)
# print(dict2)

# print(dict1['a'])

# dict1["e"]=2
# print(dict1)

# dict1.pop("e")
# print(dict1)

# del dict1["a"]
# print(dict1)


# for key, value in dict1.items():
#     print(key, value)


# print(dict1.keys())    # dict_keys(['name'])
# print(dict1.values())  # dict_values(['Alice'])
# print(dict1.items())   # dict_items([('name', 'Alice')])


# dict1.popitem()
# print(dict1)

# dict1.clear()
# print(dict1)  # Output: {}

# Sample dictionary
my_dict = {"apple": 50, "banana": 30, "cherry": 20, "date": 40}

# Sort the dictionary by value in ascending order
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted in Ascending Order:", sorted_asc)

# Sort the dictionary by value in descending order
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted in Descending Order:", sorted_desc)

