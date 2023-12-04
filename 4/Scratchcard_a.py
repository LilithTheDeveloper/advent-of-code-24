def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

cards = input()

# Card   1: 43 19 57 13 44 22 29 20 34 33 | 34 68 13 38 32 57 20 64 42  7 44 54 16 51 33 85 43 24 86 93 83 29 25 19 22
def split_card(card):
    prefix = card.split(':')[0].split(' ')[1]    
    card = card.split(':')[1].strip()

    winning_numbers = card.split('|')[0].strip().split(' ')
    winning_numbers = [i for i in winning_numbers if i != '']
    winning_numbers = list(map(lambda x: int(x), winning_numbers))

    gambling = card.split('|')[1].strip().split(' ')
    gambling = [i for i in gambling if i != '']
    gambling = list(map(lambda x: int(x), gambling))

    points = 0

    for i in range(0, len(gambling)):
        if gambling[i] in winning_numbers:
            if(points == 0):
                points = 1
            else:
                points *= 2

    return points

sum = 0
for card in cards:
    sum += split_card(card)
print(sum)

