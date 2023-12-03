from functools import reduce
from pprint import pprint
def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

# Bag Contents
cube_red = 12
cube_green = 13
cube_blue = 14

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
games = input()
# [' 12 blue', ' 2 green, 13 blue, 19 red', ' 13 red, 3 green, 14 blue']
def get_game(game):
    game_prefix = game.split(': ')[0]
    game_id = game_prefix.split(' ')[1]
    sets = game.split(': ')[1].split(';')
    sets = list(map(lambda x: x.lstrip(), sets))

    possible = False
    for i in range(len(sets)):
        sets[i] = sets[i].split(', ')
        # print("--- SET ", i, " ---")
        for j in range(len(sets[i])):
            cube_red = 12
            cube_green = 13
            cube_blue = 14

            blues = 0
            reds = 0
            greens = 0
            if sets[i][j].find('blue') != -1:
                blues = int(sets[i][j].split(' ')[0])
            if sets[i][j].find('red') != -1:
                reds = int(sets[i][j].split(' ')[0])
            if sets[i][j].find('green') != -1:
                greens = int(sets[i][j].split(' ')[0])
            cube_red -= reds
            cube_green -= greens
            cube_blue -= blues

            if(cube_red < 0 or cube_green < 0 or cube_blue < 0):
                possible = False
                break
            else:
                possible = True
        if possible == False:
            break

        # print("--- END SET ", i, " ---")


    # if cube_red >= 0 and cube_green >= 0 and cube_blue >= 0:
    #     possible = True
        # print("Game ", game_id, " is possible")
        # print("Game ", game_id, " is not possible")
        # print("Cube Red left: ", cube_red)
        # print("Cube Green left: ", cube_green)
        # print("Cube Blue left: ", cube_blue)
    return (game_id, possible)

game_results = map(get_game, games)
sum = 0
for game in game_results:
    if game[1] == True:
        print("Game ", game[0], " is possible")
        sum += (int)(game[0])

print("Sum of possible games: ", sum)

