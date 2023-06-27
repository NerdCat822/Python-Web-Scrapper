import random

print("Welcome to Python Casino")
pc_choice = random.randint(1, 50)
playing = True
while playing:
    user_choice = int(input("Choose number."))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower! Computer chose", pc_choice)
    elif user_choice < pc_choice:
        print("Higher! Computer chose", pc_choice)
