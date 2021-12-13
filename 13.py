from data import inputGen

import matplotlib.pyplot as plt

f = inputGen.getPuzzle(2021, 13)
file = f.input_data
file = file.split()

points = set()
folds = []

while file:
    row = file.pop(0)
    if row in ['fold', 'along']:
        continue
    elif row[0] in 'xy':
        folds.append(row)
    else:
        x,y = map(int, row.split(','))
        points.add((x,y))

def fold_it(points, fold):
    new_points = set()
    ch, num = fold.split('=')
    num = int(num)
    for p in points:
        x, y = p
        if ch == 'x':
            if x > num:
                x = 2*num - x
        if ch == 'y':
            if y > num:
                y = 2*num - y
        new_points.add((x,y))
    return new_points

points = fold_it(points, folds.pop(0))
result1 = len(points)

for fold in folds:
    points = fold_it(points, fold)

plt.scatter(*zip(*points))
plt.show()

result2 = 'RPCKFBLR'

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
