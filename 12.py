from data import inputGen
import copy
f = inputGen.getPuzzle(2021, 12)
file = f.input_data
file = file.split()

paths = []

dirs = dict()
for row in file:
    x, y = row.split('-')
    if 'start' in row:
        if x == 'start':
            paths.append([x,y])
        else:
            paths.append([y,x])
    elif 'end' in row:
        if x == 'end':
            dirs.setdefault(y, [])
            dirs[y].append(x)
        else:
            dirs.setdefault(x, [])
            dirs[x].append(y)
    else:
        dirs.setdefault(y, [])
        dirs.setdefault(x, [])
        dirs[y].append(x)
        dirs[x].append(y)

paths2 = copy.deepcopy(paths)

result1 = 0
while paths:
    new_paths = []
    for p in paths:
        for d in dirs[p[-1]]:
            if d == 'end':
                result1 += 1
            elif d.islower() and d in p:
                continue
            else:
                new_paths.append(p + [d])
    paths = copy.deepcopy(new_paths)

def may_not_visit(path):
    visited_twice = False
    small_caves = []
    for cave in path[1:]:
        if cave.islower():
            small_caves.append(cave)
            if small_caves.count(cave) > 1:
                if not visited_twice:
                    visited_twice = True
                else:
                    return True
    return False


result2 = 0
while paths2:
    new_paths = []
    for p in paths2:
        for d in dirs[p[-1]]:
            if d == 'end':
                result2 += 1
            elif d.islower() and may_not_visit(p + [d]):
                continue
            else:
                new_paths.append(p + [d])
    paths2 = copy.deepcopy(new_paths)

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
