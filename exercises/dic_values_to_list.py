d = {'Adam':1000, 'Bobby':820, 'Garry':700, 'Eva':900}
print(d.get('Adam') + d.get('Eva'))
dic_to_list = []
for i in d.values():
    dic_to_list.append(i)
print(max(dic_to_list))
print(sum(dic_to_list))