s = input()
s1 = s[::-1]
res = s1.replace(' ','')
res2 = s.replace(' ','')
print(res2 == res)