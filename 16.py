from data import inputGen

f = inputGen.getPuzzle(2021, 16)
file = f.input_data
file = file.split()[0]

table = dict()

for num in range(16):
    chars = '0123456789ABCDEF'
    table[chars[num]] = bin(num)[2:].zfill(4)

string = list(''.join([table[x] for x in file]))

result1 = 0

def get_result(nums, type_ID):
    if type_ID == 0:
        return sum(nums)
    elif type_ID == 1:
        res = 1
        for num in nums:
            res *= num
        return res
    elif type_ID == 2:
        return min(nums)
    elif type_ID == 3:
        return max(nums)
    elif type_ID == 5:
        return 1 if nums[0] > nums[1] else 0
    elif type_ID == 6:
        return 1 if nums[0] < nums[1] else 0
    elif type_ID == 7:
        return 1 if nums[0] == nums[1] else 0

def get_value(string):
    global result1
    result1 += int(''.join([string.pop(0) for _ in range(3)]).zfill(4), 2)
    type_ID = int(''.join([string.pop(0) for _ in range(3)]).zfill(4), 2)
    if type_ID != 4:
        nums = []
        I = string.pop(0)
        if I == '0':
            L = int(''.join([string.pop(0) for _ in range(15)]).zfill(4), 2)
            rest = [string.pop(0) for _ in range(L)]
            while rest:
                num, rest = get_value(rest)

                nums.append(num)
        else:
            L = int(''.join([string.pop(0) for _ in range(11)]).zfill(4), 2)
            for _ in range(L):
                num, string = get_value(string)
                nums.append(num)
        return (get_result(nums, type_ID), string)

    else:
        literal_value = ''
        trigger = True
        while trigger:
            trigger = False if string.pop(0) == '0' else True
            for _ in range(4):
                literal_value += string.pop(0)

        return (int(literal_value, 2), string)

result2, _ = get_value(string)


#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
