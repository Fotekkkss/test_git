s =  'Good,Day,Mister,Anderson'
a = []
a = s.split(',')
b = []
for i in a:
    if i.find('e') != -1:
        b.append(i)
print(b)