import random


play_game = 'y'
tries_counter = 0
start = 1
end = 100
answer = 'n'
while play_game == 'y':
    smallest = start
    largest = end
    guessed_number = int(input('Guess a number from 1 to 100: '))
    aiNumber = random.randint(start, end)
    print(aiNumber)
    answer = 'n'
    while answer != 'c':
        answer = input('Is it too large(L), too small(S) or correct(c)? ')
        if answer == 's':
            if aiNumber > start:
                smallest = aiNumber + 1
            aiNumber = random.randint(smallest, largest)
            print(aiNumber)
        elif answer == 'l':
            if aiNumber < end:
                largest = aiNumber - 1
            aiNumber = random.randint(smallest, largest)
            print(aiNumber)
    print(f'Your number is {guessed_number}')
    play_game = input('Continue? ')








