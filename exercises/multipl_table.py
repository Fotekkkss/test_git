n = 8
row = ''
for i in range(1, 10):
    for j in range(1, 10):
        row += str(i) + '*' + str(j) + '=' + str(i*j) + '\t'
    print(row)
    row = ''
