import copy
from data import inputGen

f = inputGen.getPuzzle(2021, 5)
file = f.input_data
file = file.split()
copy_file = copy.deepcopy(file)
points = set()
multipoints = set()
while file:
    x1, y1 = map(int, file.pop(0).split(','))
    file.pop(0)
    x2, y2 = map(int, file.pop(0).split(','))
    if x1 == x2:
        if y1 > y2:
            for y in range(y2, y1 + 1):
                if (x1, y) in points:
                    multipoints.add((x1, y))
                points.add((x1, y))
        else:
            for y in range(y1, y2 + 1):
                if (x1, y) in points:
                    multipoints.add((x1, y))
                points.add((x1, y))
    elif y1 == y2:
        if x1 > x2:
            for x in range(x2, x1 + 1):
                if (x, y1) in points:
                    multipoints.add((x, y1))
                points.add((x, y1))
        else:
            for x in range(x1, x2 + 1):
                if (x, y1) in points:
                    multipoints.add((x, y1))
                points.add((x, y1))
result1 = len(multipoints)

points = set()
multipoints = set()
while copy_file:
    x1, y1 = map(int, copy_file.pop(0).split(','))
    copy_file.pop(0)
    x2, y2 = map(int, copy_file.pop(0).split(','))
    if x1 == x2:
        if y1 > y2:
            for y in range(y2, y1 + 1):
                if (x1, y) in points:
                    multipoints.add((x1, y))
                points.add((x1, y))
        else:
            for y in range(y1, y2 + 1):
                if (x1, y) in points:
                    multipoints.add((x1, y))
                points.add((x1, y))
    elif y1 == y2:
        if x1 > x2:
            for x in range(x2, x1 + 1):
                if (x, y1) in points:
                    multipoints.add((x, y1))
                points.add((x, y1))
        else:
            for x in range(x1, x2 + 1):
                if (x, y1) in points:
                    multipoints.add((x, y1))
                points.add((x, y1))
    else:
        if y1 > y2:
            if x1 > x2:
                for i, y in enumerate(range(y2, y1 + 1)):
                    if (x2 + i, y) in points:
                        multipoints.add((x2 + i, y))
                    points.add((x2 + i, y))
            else:
                for i, y in enumerate(range(y2, y1 + 1)):
                    if (x2 - i, y) in points:
                        multipoints.add((x2 - i, y))
                    points.add((x2 - i, y))
        else:
            if x1 > x2:
                for i, y in enumerate(range(y1, y2 + 1)):
                    if (x1 - i, y) in points:
                        multipoints.add((x1 - i, y))
                    points.add((x1 - i, y))
            else:
                for i, y in enumerate(range(y1, y2 + 1)):
                    if (x1 + i, y) in points:
                        multipoints.add((x1 + i, y))
                    points.add((x1 + i, y))
result2 = len(multipoints)

'''
f.answer_a = result1
f.answer_b = result2
'''
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
