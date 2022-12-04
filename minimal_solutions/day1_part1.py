elf_rations = open('input_day1.txt', 'r').read().split('\n\n')
# One liner for tryhards
print(max([sum([int(x) for x in elf.split("\n")]) for elf in elf_rations]))

# Bit more normal solution
calorie_list = []

for elf in elf_rations:
    calorie_list.append(sum([int(x) for x in elf.split("\n")]))

print(max(calorie_list))
