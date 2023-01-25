d = dict(Pie = 100, Cookie = 300, Candies = 200)
s=''
sum = 0
while s!='stop':
  s = input()
  for i in d:
    if s == i:
        sum += d.get(s)

print(sum)