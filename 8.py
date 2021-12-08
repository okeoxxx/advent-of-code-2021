from data import inputGen

f = inputGen.getPuzzle(2021, 8)
file = f.input_data
file = file.split()

result1 = 0

rows = []

while file:
    part1 = []
    for _ in range(10):
        part1.append(set(file.pop(0)))
    file.pop(0)
    part2 = []
    for _ in range(4):
        segment = file.pop(0)
        part2.append(set(segment))
        if len(segment) in [2,3,4,7]:
            result1 += 1
    rows.append([part1, part2])

result2 = 0
for row in rows:
    nums = dict()
    from5 = []
    from6 = []
    for seg in row[0]:
        if len(seg) == 2:
            nums[1] = seg
        elif len(seg) == 3:
            nums[7] = seg
        elif len(seg) == 4:
            nums[4] = seg
        elif len(seg) == 5:
            from5.append(seg)
        elif len(seg) == 6:
            from6.append(seg)
        else: 
            nums[8] = seg

    for seg in from6:
        if nums[4] - nums[1] <= seg:
            if nums[1] <= seg:
                nums[9] = seg
            else:
                nums[6] = seg
        else:
            nums[0] = seg
            
    for seg in from5:
        if nums[4] - nums[1] <= seg:
            nums[5] = seg
        else:
            if seg - nums[9]:
                nums[2] = seg
            else:
                nums[3] = seg
    output = ''
    for seg in row[1]:
        for i in range(10):
            if nums[i] == seg:
                output += str(i)
                break
    result2 += int(output)

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
