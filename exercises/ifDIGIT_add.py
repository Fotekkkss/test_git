sum = 0

n = int(input())
print('--------------')
while n>0:
    inpt = input()
    for i in inpt:
        if i.isdigit():
            dig_int = int(i)
            sum += dig_int
    n -= 1
print(sum)