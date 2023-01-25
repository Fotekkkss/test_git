car_plates = ['AB1234', 'CD5678', 'EF901', 'GH234', 'JK567', 'LM901']

odd_days = ['MO', 'WE', 'FR']
even_days = ['TU', 'TH', 'SA']
pass_list = []

today = input('Enter day of a week (SUnday to SAturday): ')
for i in car_plates:
    last_digit = int(i[-1])
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(i)
    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(i)
    elif today == 'SU':
        pass_list.append(i)
print(*pass_list, sep='\n')




















