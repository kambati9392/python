# lastNum=False
# midnum=False
# firstNum=False
def evennum():
    for i in range(100,401):
    #    count=0
    #    for j in str(i):
    #        if int(j)%2==0:
    #         count+=1
    #    if count==len(str(i)):
    #        print(i)
         if all(int(j) % 2 == 0 for j in str(i)):
            print(i)
print(evennum())            