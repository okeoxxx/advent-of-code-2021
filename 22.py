from data import inputGen

f = inputGen.getPuzzle(2021, 22)
file = f.input_data
file = file.split()
#file = ['on','x=10..12,y=10..12,z=10..12','on','x=11..13,y=11..13,z=11..13','off', 'x=9..11,y=9..11,z=9..11','on', 'x=10..10,y=10..10,z=10..10']

def parse(text):
    x, y, z = text.split(',')
    x1, x2 = map(int, x[2:].split('..'))
    y1, y2 = map(int, y[2:].split('..'))
    z1, z2 = map(int, z[2:].split('..'))
    return x1, x2, y1, y2, z1, z2

turned_on = set()

while file:
    switch = file.pop(0)
    x1, x2, y1, y2, z1, z2 = parse(file.pop(0))
    nums = [x1, x2, y1, y2, z1, z2]
    if min(nums) < -50 or max(nums) > 50:
        continue
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                if switch == 'on':
                    turned_on.add((x,y,z))
                else:
                    turned_on.discard((x,y,z))

    

result1 = len(turned_on)

result2 = 0

f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
