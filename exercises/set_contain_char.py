inp = 'a i o p b a d y w w f w'
s = set(inp)
s.remove(' ')
count_of_w = 0
count_of_diff_of_w = 0
for i in s:
    if i == 'w':
        count_of_w += 1
    else:
        count_of_diff_of_w += 1

if count_of_w > 0:
    print(f'Set s contains {count_of_w} "w"')
else:
    print(f"Set s contains {count_of_diff_of_w} characters that different from 'w' ")