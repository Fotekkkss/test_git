a1 = [1, 2, 3]
a2 = ['Mister', 'Sister']
a = a1 + a2
lenth_of_a1 = len(a1)
lenth_of_a2 = len(a2)
a.append(lenth_of_a1 + lenth_of_a2)
a.insert(0, lenth_of_a2*2)
a.extend(a1)
print(a)
