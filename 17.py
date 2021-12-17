from data import inputGen

f = inputGen.getPuzzle(2021, 17)
file = f.input_data
file = file.split()

x1, x2 = map(int, file[2][2:-1].split('..'))
y1, y2 = map(int, file[3][2:].split('..'))

target = set()
for x in range(x1, x2+1):
    for y in range(y1, y2+1):
        target.add((x,y))

def get_trajectory(velocity):
    global result1
    points = [(0,0)]
    dx, dy = velocity
    while True:
        next_point = (points[-1][0]+dx, points[-1][1]+dy)
        if next_point in target:
            maximum = max(points, key=lambda x: x[1])[1]
            if maximum > result1:
                result1 = maximum
            return True
        elif next_point[0] > x2 or next_point[1] < y1:
            return False
        points.append(next_point)
        dx -= 1 if dx > 0 else 0
        dy -= 1

result1 = 0
result2 = 0

for x in range(x2+1):
    for y in range(y1,abs(y1)):
        if get_trajectory((x,y)):
            result2 += 1


#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
