from functools import reduce
def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

input = input()

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = '*'

def print_gears(input, lines):
    for i in range(0, lines):
        print(input[i])

#Get the square at the given coordinates
#y - the line number
#x - the character number
def get_square(input, y,x):
    return input[y][x]

def get_neighbours(input, y, x):
    neighbours = []
    if x > 0:
        neighbour = {(y, x-1): get_square(input, y, x-1)}
        neighbours.append(neighbour)
    if x < len(input[y]) - 1:
        neighbour = {(y, x+1): get_square(input, y, x+1)}
        neighbours.append(neighbour)
    if y > 0:
        neighbour = {(y-1, x): get_square(input, y-1, x)}
        neighbours.append(neighbour)
    if y < len(input) - 1:
        neighbour = {(y+1, x): get_square(input, y+1, x)}
        neighbours.append(neighbour)
    if x > 0 and y > 0:
        neighbour = {(y-1, x-1): get_square(input, y-1, x-1)}
        neighbours.append(neighbour)
    if x > 0 and y < len(input) - 1:
        neighbour = {(y+1, x-1): get_square(input, y+1, x-1)}
        neighbours.append(neighbour)
    if x < len(input[y]) - 1 and y > 0:
        neighbour = {(y-1, x+1): get_square(input, y-1, x+1)}
        neighbours.append(neighbour)
    if x < len(input[y]) - 1 and y < len(input) - 1:
        neighbour = {(y+1, x+1): get_square(input, y+1, x+1)}
        neighbours.append(neighbour)

    merged_neighbours = {}

    for d in neighbours:
        merged_neighbours.update(d)
        #if value of key is not a number then remove it
        for key, value in d.items():
            if value not in numbers:
                del merged_neighbours[key]

    return merged_neighbours 

def construct_number(y,x, input):
    left_most = x

    while get_square(input, y, left_most) in numbers and left_most >= 0:
        left_most -= 1

    number = '' 
    for i in range(left_most+1, len(input[y])):
        if get_square(input, y, i) not in numbers:
            break
        number += get_square(input, y, i)

    return number

def traverse_machine(input):
    gear_parts = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if(input[i][j] == symbol):
                neighbours = get_neighbours(input, i, j)
                adjacent_numbers = []
                for key, value in neighbours.items():
                    adjacent_numbers.append(construct_number(key[0], key[1], input))
                unique_numbers = list(set(adjacent_numbers))
                gear_parts.append(unique_numbers)
    filtered_gear_parts = []
    for gear_part in gear_parts:
        if len(gear_part) == 2:
            filtered_gear_parts.append(gear_part)
    return filtered_gear_parts 

gear_parts = traverse_machine(input)
sum = 0

for gear_part in gear_parts:
    sum += reduce(lambda x, y: int(x) * int(y), gear_part)

print(sum)
