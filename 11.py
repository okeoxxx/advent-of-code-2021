from data import inputGen

f = inputGen.getPuzzle(2021, 11)
file = f.input_data
file = file.split()
#file = ['5483143223','2745854711','5264556173','6141336146','6357385478','4167524645','2176841721','6882881134','4846848554','5283751526']
grid = []
while file:
    grid.append(list(map(int, list(file.pop(0)))))

def get_neigbors(point):
    x1,y1 = point
    neigbors = set()
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for dir in dirs:
        x2 = x1 + dir[0]
        y2 = y1 + dir[1]
        if 9 >= x2 >= 0 and 9 >= y2 >= 0 :
            neigbors.add((x2,y2))
    return neigbors


def tick(grid, counter):
    new_flashes = set()
    for y in range(10):
        for x in range(10):
            grid[y][x] += 1
            if grid[y][x] == 10:
                new_flashes.add((x,y))
    flashes = set()
    while new_flashes:
        flashes = flashes | new_flashes
        ls_flash = list(new_flashes)
        new_flashes = set()
        for point in ls_flash:
            for neigbor in get_neigbors(point):
                x,y = neigbor
                grid[y][x] += 1
                if grid[y][x] == 10:
                    new_flashes.add((x,y))
    for flash in flashes:
        x,y = flash
        grid[y][x] = 0
    return(grid, counter + len(flashes))

result1 = 0
for _ in range(100):
    grid, result1 = tick(grid, result1)

result2 = 100
while True:
    result2 += 1
    grid, counter = tick(grid, 0)
    if counter == 100:
        break

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
