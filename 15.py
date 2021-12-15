from data import inputGen

f = inputGen.getPuzzle(2021, 15)
file = f.input_data
file = file.split()

grid = []
while file:
    grid.append(list(map(int, list(file.pop(0)))))
    
def get_neighbour_points(point, grid):
    x,y = point
    points = set()
    for x2, y2 in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
        if x2 in [-1,len(grid)] or y2 in [-1,len(grid)]:
            continue
        else:
            points.add((x2,y2))
    return points

def visit(point, grid, visited, paths, results):
    visited.add(point)
    results[point] = paths[point]
    del paths[point]
    for p in get_neighbour_points(point, grid):
        distance = grid[p[1]][p[0]] + results[point]
        if p in visited:
            continue
        elif p in paths:
            if paths[p] > distance:
                paths[p] = distance
        else:
            paths[p] = distance

def get_result(grid):
    visited = set()
    results = dict()
    paths = {(0,0):0}

    while (len(grid)-1,len(grid)-1) not in visited:
        next_point = min(paths, key=paths.get)
        visit(next_point, grid, visited, paths, results)

    return results[(len(grid)-1,len(grid)-1)]

result1 = get_result(grid)

new_grid = []
for i in range(5):
    for row in grid:
        new_grid.append([])
        for j in range(5):
            for num in row:
                new_num = num + i + j
                if new_num > 9:
                    new_num -= 9
                new_grid[-1].append(new_num)

result2 = get_result(new_grid)

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
