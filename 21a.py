from data import inputGen

f = inputGen.getPuzzle(2021, 21)
file = f.input_data
file = file.split()

player1 = [0, int(file[4])]
player2 = [0, int(file[9])]

dice = 0
rolls_counter = 0

def get_sum():
    suma = 0
    global rolls_counter
    global dice
    for _ in range(3):
        rolls_counter += 1
        dice += 1
        if dice > 100:
            dice -= 100
        suma += dice
    return suma

while player1[0] < 1000 and player2[0] < 1000:
    for p in [player1, player2]:
        position = p[1] + get_sum()
        while position > 10:
            position -= 10
        p[0] += position
        p[1] = position
        if p[0] >= 1000:
            break
    
result1 = player1[0] * rolls_counter if player2[0] >= 1000 else player2[0] * rolls_counter
result2 = 0

#f.answer_a = result1
#f.answer_b = result2

print('Solution 1st part:', result1)
print('Solution 2nd part:', result2)
