a1 = ('Cat', 'Dog', 'Cow', 'Sheep')
a2 = (30.5, 100.1, 90.3, 72.7)
n = min(len(a1), len(a2))
animals = {}
for i in range(0, n):
    animals.update({a1[i] : a2[i]})

print(animals)