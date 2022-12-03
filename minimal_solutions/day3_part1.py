import string

backpacks = open('input_day3.txt', 'r').read().split('\n')
sum_of_priority = 0

for back_p in backpacks:
    first_half, second_half = back_p[:len(back_p)//2], back_p[len(back_p)//2:]
    item_type = str(list(set(first_half) & set(second_half))[0])
    sum_of_priority += string.ascii_letters.index(item_type) + 1

print(sum_of_priority)
