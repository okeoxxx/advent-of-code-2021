from data import inputGen

f = inputGen.getPuzzle(2021, 2)
file = f.input_data
file = file.split()

x = 0
y1 = 0
y2 = 0
aim = 0

while file:
    dir = file.pop(0)
    num = int(file.pop(0))
    if dir == 'forward':
        x += num
        y2 += aim * num
    elif dir == 'down':
        y1 += num
        aim += num
    elif dir == 'up':
        y1 -= num
        aim -= num

result1 = x * y1
result2 = x * y2

f.answer_a = result1
f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
