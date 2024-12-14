list1=['abc','aba','1221',345,676,66]

for item in list1:
    item=str(item)
    if len(item)>2:
        if item[0]==item[-1]:
            print(item)

# list1=[232,345]
# print(len(list[0]))