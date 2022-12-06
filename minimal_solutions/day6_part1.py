
data = open('input_day6.txt', 'r').read()
print([x for x in range(len(data)-4) if len(set(data[x:x+4])) == 4][0]+4)
