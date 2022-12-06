
data = open('input_day6.txt', 'r').read()
print([x for x in range(len(data)-14) if len(set(data[x:x+14])) == 14][0]+14)
