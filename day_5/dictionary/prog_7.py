dict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 40, 6: 70, 7: 70, 8: 90, 9: 90}
dict2=set()
for value in dict1.values():
     dict2.add(value)
print(dict2)