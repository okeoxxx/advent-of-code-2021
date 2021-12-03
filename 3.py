from data import inputGen

f = inputGen.getPuzzle(2021, 3)
file = f.input_data
file = file.split()

max = len(file)
counter = [0] * 12

for byte in file:
    for i, bit in enumerate(byte):
        if bit == '1':
            counter[i] += 1

gamma = ''
epsilon = ''

for num in counter:
    if num > max - num:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

result1 = int(gamma, 2) * int(epsilon, 2)

def rating_selector(nums, index, co2=0):
    x = []
    y = []
    for n in nums:
        if n[index] == '1':
            x.append(n)
        else:
            y.append(n)

    if len(x) >= len(y):
        return x if co2 == 0 else y
    else:
        return y if co2 == 0 else x

def rater(file, co2=0):
    bits = file[:]
    i = 0
    while len(bits) > 1:
        bits = rating_selector(bits, i, co2)
        i += 1
    return bits[0]


result2 = int(rater(file), 2) * int(rater(file, co2=1), 2)
'''
f.answer_a = result1
f.answer_b = result2
'''
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
