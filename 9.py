from data import inputGen

f = inputGen.getPuzzle(2021, 9)
file = f.input_data
file = file.split()

grid = []
while file:
    grid.append(list(map(int, file.pop(0))))

def get_neighbour_points(x,y):
    return [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]

def get_neighbour(point):
    x,y = point
    if x in [-1,100] or y in [-1,100]:
        return 9
    else:
        return grid[y][x]

def basin(x,y):
    points = {(x,y)}
    new_points = set()
    trigger = True
    while trigger:
        new_points = set()
        trigger = False
        for p in points:
            for point in get_neighbour_points(p[0],p[1]):
                if point in points:
                    continue
                elif get_neighbour(point) == 9:
                    continue
                else:
                    trigger = True
                    new_points.add(point)
        points = points | new_points
    return len(points)

result1 = 0
basins = []
for y,row in enumerate(grid):
    for x, num in enumerate(row):
        neighbours = []
        for point in get_neighbour_points(x,y):
            neighbours.append(get_neighbour(point))
        if num < sorted(neighbours)[0]:
            result1 += num + 1
            basins.append(basin(x,y))

basins.sort()
result2 = 1
for _ in range(3):
    result2 *= basins.pop()

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
