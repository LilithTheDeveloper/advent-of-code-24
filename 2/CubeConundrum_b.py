from functools import reduce
from pprint import pprint
def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

games = input()

def get_game(game):
    game_prefix = game.split(': ')[0]
    game_id = game_prefix.split(' ')[1]
    sets = game.split(': ')[1].split(';')
    sets = list(map(lambda x: x.lstrip(), sets))

    possible = False
    
    sum_powers = 0

    min_red = 0
    min_green = 0
    min_blue = 0
    for i in range(len(sets)):

        sets[i] = sets[i].split(', ')
        for j in range(len(sets[i])):

            blues = 0
            reds = 0
            greens = 0

            if sets[i][j].find('blue') != -1:
                blues = int(sets[i][j].split(' ')[0])
            if sets[i][j].find('red') != -1:
                reds = int(sets[i][j].split(' ')[0])
            if sets[i][j].find('green') != -1:
                greens = int(sets[i][j].split(' ')[0])

            if(blues > min_blue):
                min_blue = blues
            if(reds > min_red):
                min_red = reds
            if(greens > min_green):
                min_green = greens
    
    sum_powers = min_red * min_green * min_blue
    return sum_powers

game_results = map(get_game, games)
print("Sum of possible games: ", reduce(lambda x, y: x + y, game_results))
