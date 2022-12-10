data = open('input_day8.txt', 'r').read().split('\n')
vis = 0

for r_in, line in enumerate(data):
    # Check edges
    if r_in == 0 or r_in+1 == len(data):
        vis += len(line)
        continue

    for c_in, tree in enumerate(line):
        # Check edges
        if c_in == 0 or c_in+1 == len(line):
            vis += 1
            continue

        # Check if visable
        size = int(tree)
        if size > int(max(line[c_in+1:])) or size > int(max(line[:c_in])):
            vis += 1
            continue
        top = list()
        bottom = list()
        for index, line2 in enumerate(data):
            if index < r_in:
                top.append(int(line2[c_in]))
            elif index > r_in:
                bottom.append(int(line2[c_in]))
        if size > max(bottom) or size > max(top):
            vis += 1
            continue

print(vis)
