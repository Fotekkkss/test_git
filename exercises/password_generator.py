import random

def get_char(char_list, number):
    templist = []
    for i in range(number):
        templist.append(random.choice(char_list))
    return templist

while True:
    num_chars = int(input('NUmber of characers: '))
    num_isupper = int(input("How many uppercase letters: "))
    num_islower = int(input("How many lowercase letters: "))
    num_digits = int(input('How many digits: '))
    num_symb = int(input('How many symbols: '))
    if num_chars < num_isupper + num_islower + num_digits + num_symb:
        print('Too much characters!')
    else:
        break

upper_list = [chr(i) for i in range(65, 65+26)]
upper_char = get_char(upper_list, num_isupper)
lower_list = [chr(i) for i in range(97, 97+26)]
lower_char = get_char(lower_list, num_islower)
digit_list = [str(i) for i in range(0, 10)]
digit_char = get_char(digit_list, num_digits)
symb_list = [chr(i) for i in range(32, 48)]
symb_list += [chr(i) for i in range(58, 65)]
symb_list += [chr(i) for i in range(91, 97)]
symb_list += [chr(i) for i in range(123, 127)]
symb_char = get_char(symb_list, num_symb)

num_unfilled = num_chars - num_isupper - num_islower - num_digits - num_symb
whole_list = upper_list + lower_list + digit_list + symb_list
remaining_chars = get_char(whole_list, num_unfilled)



password = upper_char + lower_char + digit_char + symb_char + remaining_chars
random.shuffle(password)

password = ''.join(password)

print(password)












