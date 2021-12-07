from data import inputGen

f = inputGen.getPuzzle(2021, 7)
file = f.input_data
file = file.split(',')
file = list(map(int, file))

fuel = len(file) * max(file)
for num in range(max(file)):
    new_fuel = 0
    for n in file:
        new_fuel += abs(num - n)
        if new_fuel > fuel:
            break
    if new_fuel < fuel:
        fuel = new_fuel
    else:
        break
result1 = fuel

def sum_row(n):
    return n * (n + 1) // 2

fuel = len(file) * sum_row(max(file))
for num in range(max(file)):
    new_fuel = 0
    for n in file:
        new_fuel += sum_row(abs(num - n))
        if new_fuel > fuel:
            break
    if new_fuel < fuel:
        fuel = new_fuel
    else:
        break
result2 = fuel

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
