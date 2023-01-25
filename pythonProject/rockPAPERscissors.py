import random

user_choice = "null"
choice = "null"
player_choice = int(input("Enter a number. 1 - rock, 2 - paper, 3 - scissors:"))

rand_number = random.randint(1, 3)

if player_choice == 1:
    user_choice = "rock"
elif player_choice == 2:
    user_choice = "paper"
elif player_choice == 3:
    user_choice = "scissors"

if rand_number == 1:
    choice = "rock"
elif rand_number == 2:
    choice = "paper"
elif rand_number == 3:
    choice = "scissors"

if rand_number == player_choice:
    print("It`s a tie!")
elif player_choice == 1:
    if rand_number == 2:
        print(f"Computer won with {choice}")
    else:
        print(f"You win the {choice} with {user_choice}")
elif player_choice == 2:
    if rand_number == 1:
        print(f"You win {choice} with {user_choice}")
    else:
        print(f"You lose to the {choice}")
elif player_choice == 3:
    if rand_number == 2:
        print(f"You wint {choice} with {user_choice}")
    else:
        print(f"You lose to the {choice}")
