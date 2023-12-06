def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

cards = input()

def split_card(card):
    card = card.split(':')[1].strip()

    winning_numbers = card.split('|')[0].strip().split()
    winning_numbers = list(map(lambda x: int(x), winning_numbers))

    gambling = card.split('|')[1].strip().split()
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

