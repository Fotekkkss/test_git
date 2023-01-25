import random

play_again = 'y'
while play_again == 'y':
    randNumber = random.randint(1, 100)
    gssNumber = int(input('Guess a number form 1 to 100: '))

    while gssNumber != randNumber:
      if gssNumber < randNumber:
         print('Your number is lower')
      elif gssNumber > randNumber:
         print('Your number is higher')
      gssNumber = int(input('Guess a number form 1 to 100: '))
    if gssNumber == randNumber:
      print('You got it, it`s ', randNumber)
      play_again = input('Dou you want to play again? ')