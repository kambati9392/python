import random
target=random.randrange(1,10)
guess_num=0
while target!=guess_num:
    guess_num=int(input("enter the number "))
    if target==guess_num:
        print("well guessed!!!")