def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

input = input()


print(input[0][2])

for i, line in enumerate(input):
    for j, char in enumerate(line):
        print(f"y: {i}, x: {j}, char: {char}")
    
