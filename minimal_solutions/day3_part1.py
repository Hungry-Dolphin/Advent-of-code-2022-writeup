import string

sum_of_priority = 0
for b in open('input_day3.txt', 'r').read().split('\n'):
    item_type = str(list(set(b[:len(b)//2]) & set(b[len(b)//2:]))[0])
    sum_of_priority += string.ascii_letters.index(item_type) + 1

print(sum_of_priority)
