import pprint as pp
def input():

    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

cards = input()

def split_card(idx, card):
    prefix = card.split(':')[0].split(' ')[1]    
    card = card.split(':')[1].strip()

    winning_numbers = card.split('|')[0].strip().split()
    winning_numbers = list(map(lambda x: int(x), winning_numbers))

    scratch_numbers = card.split('|')[1].strip().split()
    scratch_numbers = list(map(lambda x: int(x), scratch_numbers))

    matching_numbers = 0

    for i in range(0, len(scratch_numbers)):
        if scratch_numbers[i] in winning_numbers:
            matching_numbers += 1

    return matching_numbers 

def get_prefix(card):
    prefix = card.split(':')[0].split()
    prefix = prefix[1]
    return prefix

winners = []
stored_cards = [1 for i in range(0, len(cards))]

for i, card in enumerate(cards):
    winners.append(split_card(i, card))

for i in range(0, len(winners)):
    cards_copied = []
    for j in range(1, winners[i]+1):
        current_card_amount = stored_cards[i]
        stored_cards[i+j] += current_card_amount
        cards_copied.append(i+j+1)

print(sum(stored_cards))
