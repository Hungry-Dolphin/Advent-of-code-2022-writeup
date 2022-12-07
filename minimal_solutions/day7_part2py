cwd_list, files = list(), dict()
for line in open('input_day7.txt', 'r').read().split('\n'):
    if line.startswith('$ cd /'):
        cwd_list.append('/')
    elif line.startswith('$ cd ..'):
        cwd_list.pop()
    elif line.startswith('$ cd '):
        cwd_list.append(f'/{line.split(" ")[-1]}')
    elif line[0].isnumeric():
        for index in range(len(cwd_list)):
            path, size = ''.join(cwd_list[:index+1]), int(line.split(" ")[0])
            if path in files:
                files.update({f'{path}': f'{int(files[path])+size}'})
            else:
                files[path] = f'{size}'


to_make_free = 30000000 - (70000000 - int(files['/']))
print(min([int(v) for v in files.values() if int(v) > to_make_free]))
