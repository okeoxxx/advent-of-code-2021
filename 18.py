from data import inputGen
import copy
f = inputGen.getPuzzle(2021, 18)
file = f.input_data
file = file.split()

def make_list(num):
    ls = []
    for ch in num:
        if ch in '0123456789':
            if ls and isinstance(ls[-1], int):
                ls[-1] = ls[-1] * 10 + int(ch)
            else:
                ls.append(int(ch))
        else:
            ls.append(ch)
    return ls

def addition(num1, num2):
    return ['['] + num1 + [','] + make_list(num2) + [']']

def pre_reduce(num):
    trigger = True
    while trigger:
        trigger = False
        depth = 0
        last_num_index = 0
        new_num = []
        while num:
            part = num.pop(0)
            if part == '[':
                depth += 1
                if depth == 5:
                    trigger = True
                    if isinstance(new_num[last_num_index], int):
                        new_num[last_num_index] += num.pop(0)
                    else:
                        num.pop(0)
                    num.pop(0)
                    x = num.pop(0)
                    num.pop(0)
                    new_num.append(0)
                    for i, ch in enumerate(num):
                        if isinstance(ch, int):
                            num[i] += x
                            break
                    new_num += num
                    num = copy.deepcopy(new_num)
                    break
            elif part == ']':
                depth -= 1
            elif isinstance(part, int):
                last_num_index = 0
            new_num.append(part)
            last_num_index -= 1
    return new_num

def reduce(num):
    trigger = True
    while trigger:
        trigger = False
        depth = 0
        last_num_index = 0
        new_num = []
        while num:
            part = num.pop(0)
            if part == '[':
                depth += 1
                if depth == 5:
                    trigger = True
                    if isinstance(new_num[last_num_index], int):
                        new_num[last_num_index] += num.pop(0)
                    else:
                        num.pop(0)
                    num.pop(0)
                    x = num.pop(0)
                    num.pop(0)
                    new_num.append(0)
                    for i, ch in enumerate(num):
                        if isinstance(ch, int):
                            num[i] += x
                            break
                    new_num += num
                    num = copy.deepcopy(new_num)
                    break
            elif part == ']':
                depth -= 1
            elif isinstance(part, int):
                last_num_index = 0
                if part > 9:
                    trigger = True
                    x = part // 2
                    y = part - x
                    new_num += make_list('[{},{}]'.format(x,y)) + num
                    num = copy.deepcopy(new_num)
                    break
            new_num.append(part)
            last_num_index -= 1
    return new_num

def get_magnitude(num):
    depth = 0
    index_point = 0
    for i, part in enumerate(num):
        if part == '[':
            depth += 1
        elif part == ',' and depth == 1:
            index_point = i
        elif part == ']':
            depth -= 1
            if depth == 0 and index_point:
                x = num[1:index_point]
                x = 3*get_magnitude(x) if '[' in x else 3*x[0]
                y = num[index_point+1:i]
                y = 2*get_magnitude(y) if '[' in y else 2*y[0]
                return x + y

def get_num(x, y):
    return reduce(pre_reduce(addition(x, y)))


result2 = 0
for i, x in enumerate(file[:-1]):
    for y in file[i+1:]:
        for couple in [(x,y), (y,x)]:
            num = get_num(make_list(couple[0]), couple[1])
            res = get_magnitude(num)
            if res > result2:
                result2 = res


num = make_list(file.pop(0))
while file:
    num = get_num(num, file.pop(0))

result1 = get_magnitude(num)

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
