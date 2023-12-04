### Debugging Shenanigans

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

# def is_tuple_key_in_map(coordinate, lst):
#     for item in lst:
#         if coordinate in item:
#             return True
#     return False

def print_gears_by_character(input, lines, special_coordinates):
    print(special_coordinates)
    for i in range(0, lines):
        for j in range(0, len(input[i])):
            if (i,j) in special_coordinates:
                 print(Colors.RED + input[i][j] + Colors.RESET, end='')
            elif(special_coordinates.get((i,j)) is not None):
                print(Colors.BLUE+ input[i][j] + Colors.RESET, end='')
            else:
                print(input[i][j], end='')
        print()


def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

input = input()

#Valid symbols for gears

def print_gears(input, lines):
    for i in range(0, lines):
        print(input[i])

#Get the square at the given coordinates
#y - the line number
#x - the character number
def get_square(input, y,x):
    return input[y][x]

def get_coordinate_of_numbers(input):
    coordinates = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] in symbols:
                coordinates.append((i,j))
    return coordinates

def replace_at(input, y, x, symbol):
    input[y] = input[y][:x] + symbol + input[y][x+1:]
    return input

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

    return merged_neighbours 
#
# neighbours = {}
# neighbours.update(get_neighbours(input, 0, 9))
# neighbours.update(get_neighbours(input, 3, 25))
# neighbours.update(get_neighbours(input, 3, 15))
# neighbours.update(get_neighbours(input, 3, 19))
#
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@'] 

def traverse_machine(input):
    valid_digits = []
    for i in range(0, len(input)):
        current_digit = []
        valid_digit = False
        for j in range(0, len(input[i])):
            if input[i][j] in numbers:
                current_digit.append(input[i][j])
                neigbours = get_neighbours(input, i, j)
                for key, value in neigbours.items():
                    if value in symbols:
                        valid_digit = True
            elif input[i][j] not in numbers: 
                if valid_digit:
                    valid_digits.append(int(''.join(current_digit)))
                    valid_digit = False
                current_digit = []
           
            # THE EDGE CASE OF 4 GEARS GYAT
            if len(input[i]) - 1 == j:
                if valid_digit:
                    valid_digits.append(int(''.join(current_digit)))
                    valid_digit = False
                current_digit = []
    return valid_digits


valid_gears = traverse_machine(input)
print("Length: " + str(len(input)))
print("Valid gears: " + str(len(valid_gears)))
print("Sum: " + str(sum(valid_gears)))

# gear_set = set(valid_gears)
#
## highlight all nubmers
#
# new_lines = []

# import re
# for line in input:
#     for number in gear_set:
#         pos = line.find(str(number))
#         pattern = re.compile(rf'\b{number}\b')
#         line = pattern.sub(f"{Colors.GREEN}{number}{Colors.RESET}", line)
#     new_lines.append(line)
#
# print_gears(new_lines, len(new_lines))

# print("Valid gears: " + str(valid_gears))
# sum = sum(valid_gears)
# print("Sum: " + str(sum))
# V

