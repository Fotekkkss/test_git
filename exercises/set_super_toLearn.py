s1 = {90, 100, 70, -100}
s2 = {92, 100, 500, 19}
s3 = {88, 100, -100, 83, 71}
res_union = s1.union(s2, s3)
print(res_union)
res_dif = s3.difference(s1)
print(res_dif)
res_super = s1.intersection(s2 - s3)
print(res_super)