from data import inputGen

f = inputGen.getPuzzle(2021, 10)
file = f.input_data
file = file.split()

sus = {')':'(', '}':'{', ']':'[', '>':'<'}

valid = ['()', '[]', '{}', '<>']

def simplify(s):
    trigger = True
    while trigger:
        trigger = False
        for v in valid:
            if v in s:
                s = s.replace(v, '')
                trigger = True
                if not s:
                    return ''
    return s

invalid = ''
not_corrupted = []
for row in file:
    corrupted = False
    for i, ch in enumerate(row):
        if ch in sus:
            if row[i-1] == sus[ch]:
                continue
            else:
                txt = simplify(row[:i])
                if txt[-1] == sus[ch]:
                    continue
                else:
                    invalid += ch
                    corrupted = True
                    break
    if not corrupted:
        not_corrupted.append(simplify(row))


score = {')': 3, ']': 57, '}': 1197, '>': 25137}

result1 = 0
for a in invalid:
    result1 += score[a]

competition_results = []
score2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def count_score(s):
    r = 0
    for i in s[::-1]:
        r *= 5
        r += score2[i]
    return r

for row in not_corrupted:
    competition_results.append(count_score(row))
competition_results.sort()
while len(competition_results) > 1:
    competition_results.pop(0)
    competition_results.pop()
result2 = competition_results[0]


#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
