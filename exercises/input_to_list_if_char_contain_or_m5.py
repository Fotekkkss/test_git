lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()
    if len(ele) > 5 or 'G' in ele:
        lst.append(ele)

print(lst)