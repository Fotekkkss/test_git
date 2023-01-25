
def get_avg(a_list):
    total = 0
    for mark in a_list:
        total += mark
    average = total/len(a_list)
    return average

def get_max(a_list):
    max_value = 0
    for mark in a_list:
        if mark > max_value:
            max_value = mark
    return max_value

mark_list = [[89, 78, 56, 79, 86, 72, 91, 63, 53],
              [68, 72, 73, 89, 74, 78],
              [97, 58, 72, 68, 81, 67, 93]]

avg_list = []
for group in mark_list:
    avg_value = get_avg(group)
    avg_list.append(avg_value)

max_avg = get_max(avg_list)
print("From " + str(len(mark_list)) + " schools avg is: " + str(max_avg))













