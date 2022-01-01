from data import inputGen

f = inputGen.getPuzzle(2021, 20)
file = f.input_data
file = file.split()

table = file.pop(0)

grid = []

while file:
    row = file.pop(0)
    grid.append([])
    for ch in row:
        if ch == '.':
            grid[-1].append('0')
        else:
            grid[-1].append('1')

def extend_grid(grid, background):
    size = len(grid) + 2
    new_grid = []
    new_grid.append([background]*size)
    for row in grid:
        new_grid.append([background]+row+[background])
    new_grid.append([background]*size)
    return new_grid

def determine_pixel(grid, x, y, background):
    binary = ''
    for point in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
        x2,y2 = point
        if len(grid) in point or x2 < 0 or y2 < 0:
            binary += background
        else:
            binary += grid[y2][x2]
    return True if table[int(binary, 2)] == '#' else False

def tick(grid, count):
    background = '1' if count % 2 == 1 else '0'
    grid = extend_grid(grid, background)
    next_grid = []
    for y in range(len(grid)):
        next_grid.append([])
        for x in range(len(grid)):
            if determine_pixel(grid, x, y, background):
                next_grid[-1].append('1')
            else:
                next_grid[-1].append('0')
    return next_grid

def get_result(grid):
    res = 0
    for row in grid:
        res += row.count('1')
    return res

for num in range(50):
    grid = tick(grid, num)
    if num == 1:
        result1 = get_result(grid)

result2 = get_result(grid)

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
