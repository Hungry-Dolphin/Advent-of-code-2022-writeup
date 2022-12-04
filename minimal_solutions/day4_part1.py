count = 0
for pair in open('input_day4.txt', 'r').read().split('\n'):
    elf1, elf2 = pair.split(',')

    r1 = list(range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1))
    r2 = list(range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1))

    count += 1 if all(x in r1 for x in r2) or all(x in r2 for x in r1) else 0

print(count)
