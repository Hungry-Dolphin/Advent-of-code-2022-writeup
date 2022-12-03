import string

backpacks = open('input_day3.txt', 'r').read().split('\n')
sum_of_priority = 0

for index in range(0, len(backpacks), 3):
    group = backpacks[index:index + 3]
    item_type = str(list(set(group[0]) & set(group[1]) & set(group[2]))[0])
    sum_of_priority += string.ascii_letters.index(item_type) + 1

print(sum_of_priority)
