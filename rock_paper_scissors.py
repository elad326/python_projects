import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q for quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock - 0, paper - 1, scissors - 2

    computer_pick = options[random_number]

    print("computer choose", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you win!!")
        user_win += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_win += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_win += 1
        continue
    
    else:
        print("computer win")
        computer_win += 1
        continue

print("you won:", user_win, "computer win:", computer_win)
print("Goodbye!!")


    