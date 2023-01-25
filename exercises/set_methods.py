a = set()
a1 = set()
a2 = set()
for i in range(100):
  if i%4==0 and i%5==0:
    a.add(i)
  if i%4==0:
    a1.add(i)
  if i%5==0:
    a2.add(i)

is_a_subset_a1 = a.issubset(a1)
is_a_subset_a2 = a.issubset(a2)
is_a_disjoint_a1 = a.isdisjoint(a1)
is_a_disjoint_a2 = a.isdisjoint(a2)
print(is_a_subset_a1)
print(is_a_subset_a2)
print(is_a_disjoint_a1)
print(is_a_disjoint_a2)
