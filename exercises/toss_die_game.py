import random

start_place = 0
end_place = 40
user_place = 0
comp_place = 0
user_win = False
comp_win = False
quit_game = False

while not user_win or not comp_win:
    user_input = input("Enter 't' to toss or die, or 'q' to end: ")
    if user_input == 'q':
        quit_game = True
        break
    if user_input == 't':
        user_move = random.randint(1, 6)
        user_place += user_move
        print('You move for ' + str(user_move) + ' steps')
        if user_place > end_place:
            overshoot = user_place - end_place
            user_place = end_place - overshoot
        print('Now you are at position ' + str(user_place))
        if user_place == end_place:
            user_win = True
            break
    comp_move = random.randint(1, 6)
    comp_place += comp_move
    print('Computer moves for ' + str(comp_move) + ' steps')
    if comp_place > end_place:
        overshoot = comp_place - end_place
        comp_place = end_place - overshoot
    print('Computer is at position ' + str(comp_place))
    if comp_place == end_place:
        comp_win = True
        break

if quit_game:
    print('You need ' + str(end_place - user_place) + ' steps to win')
elif user_win:
    print('You win!')
elif comp_win:
    print('Computer wins!')

















