polls = ['Ben', 'Andy', 'Ben', 'Andy', 'Carol', 'Carol', 'Carol', 'Andy', 'Ben', 'Andy', 'Carol', 'Andy', 'Carol']

candidates = []

votes = []

for i in polls:
    if i not in candidates:
        candidates.append(i)
        votes.append(1)
    else:
        candi_index =  candidates.index(i)
        votes[candi_index] += 1

max_vote = 0
max_candi = []

for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        candidate = candidates[i]
        max_candi = []
        max_candi.append(candidate)
    elif votes[i] == max_vote:
        candidate = candidates[i]
        max_candi.append(candidate)

print('Highest: ')
print(*max_candi, sep='\n')
print('Each has ' + str(max_vote) + ' votes.')











