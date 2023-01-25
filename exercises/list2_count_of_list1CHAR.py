a1 = [6, 5, 7, 8, 0, 100]
a2 = [100, 0, 8, 7, 5, 6]

for i in a1:
    count_of_char = a2.count(i)
    if count_of_char > 0:
        print(a2.index(i))
    else:
        break