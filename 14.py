from data import inputGen
import copy

f = inputGen.getPuzzle(2021, 14)
file = f.input_data
file = file.split()

initial = file.pop(0)
polymer = dict()
rules = dict()
counter = dict()

while file:
    x = file.pop(0)
    file.pop(0)
    y = file.pop(0)
    rules[x] = [x[0]+y, y + x[1]]
    polymer[x] = 0
    counter[y] = 0

empty_polymer = copy.deepcopy(polymer)

for i in range(len(initial)-1):
    polymer[initial[i:i+2]] +=1

def step(polymer):
    new_polymer = copy.deepcopy(empty_polymer)
    for part in polymer:
        for rule in rules[part]:
            new_polymer[rule] += polymer[part]

    return new_polymer

def get_result(polymer, counter):
    counter[initial[0]] +=1
    counter[initial[-1]] +=1

    for part in polymer:
        for element in part:
            counter[element] += polymer[part]

    return (max(counter.values()) - min(counter.values())) // 2

for i in range(40):
    if i == 10:
        result1 = get_result(polymer, copy.deepcopy(counter))
    polymer = step(polymer)

result2 = get_result(polymer, copy.deepcopy(counter))

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
