import heapq

elf_rations = open('input_day1.txt', 'r').read().split('\n\n')
calorie_list = []

for elf in elf_rations:
    calorie_list.append(sum([int(x) for x in elf.split("\n")]))

top_3 = heapq.nlargest(3, calorie_list)
print(sum([int(x) for x in top_3]))
