from data import inputGen

f = inputGen.getPuzzle(2021, 1)
file = f.input_data
file = file.split()

result1 = 0
result2 = 0

while len(file) > 1:
    prev = int(file.pop(0))
    if prev < int(file[0]):
        result1 += 1
    if len(file) > 2:
        if prev < int(file[2]):
            result2 += 1

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
