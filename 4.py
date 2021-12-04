import copy
from data import inputGen

f = inputGen.getPuzzle(2021, 4)
file = f.input_data
file = file.split()

nums = file.pop(0)
tables = []
while file:
    table = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(file.pop(0))
        table.append(row)
    
    copy_table = copy.deepcopy(table)
    
    for _ in range(5):
        col = []
        for row in copy_table:
            col.append(row.pop(0))
        table.append(col)
    tables.append(table)

max = len(tables)

played = set()
for num in nums.split(','):
    played.add(num)
    trigger = False
    for_remove = []
    for t in tables:
        all = set()
        for row in t:
            all = all | set(row)
            if len(set(row) - played) == 0:
                trigger = True
        if trigger:
            trigger = False
            for_remove.append(t)
            if len(tables) == max:
                unmarked = all - played
                result1 = 0
                for n in unmarked:
                    result1 += int(n)
                result1 *= int(num)
    if for_remove:
        for i in for_remove:
            tables.remove(i)
        for_remove = []
    if not tables:
        unmarked = all - played
        result2 = 0
        for n in unmarked:
            result2 += int(n)
        result2 *= int(num)
        break

'''
f.answer_a = result1
f.answer_b = result2
'''
print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
