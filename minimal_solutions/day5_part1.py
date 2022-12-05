crates, moves = open('input_day5.txt', 'r').read().split('\n\n')
lane_list = [[] for _ in range(int(crates.split('\n')[-1].strip(' ')[-1]))]

for c in crates.split('\n')[:-1]:
    for x in range(1, int(crates.split('\n')[-1].strip(' ')[-1])+1):
        lane_list[x-1].append(f'   {c}'[x*4]) if f'   {c}'[x*4] != " " else 0

for line in moves.split('\n'):
    moves = [int(s) for s in line.split() if s.isdigit()]
    for index in range(moves[0]):
        r_crate, _ = lane_list[moves[1]-1][0], lane_list[moves[1]-1].pop(0)
        lane_list[moves[2]-1].insert(0, r_crate)

print(*[crate[0] for crate in lane_list])
