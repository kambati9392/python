my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'e']
if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
