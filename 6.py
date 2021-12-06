import copy
from data import inputGen

f = inputGen.getPuzzle(2021, 6)
file = f.input_data
file = file.split(',')
file = map(int, file)
fish = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for num in file:
    fish[num] += 1

result1 = 0
for _ in range(256):
    if _ == 80:
        for num in range(9):
            result1 += fish[num]
    new = fish[0]
    for num in range(8):
        fish[num] = fish[num+1]
    fish[6] += new
    fish[8] = new

result2 = 0
for num in range(9):
    result2 += fish[num]

'''
f.answer_a = result1
f.answer_b = result2
'''
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
