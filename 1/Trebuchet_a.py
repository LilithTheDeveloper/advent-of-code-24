from functools import reduce

def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))


input = input()

def first_and_last_digit(line):
    digits = []
    for c in line:
        if(c.isdigit()):
            digits.append(c)
    if(len(digits) == 0):
        return 0
    combine = digits[0] + digits[-1] if len(digits) > 1 else digits[0] + digits[0]
    return combine 

def main():
    all_digits = map(first_and_last_digit, input) 
    sum = reduce(lambda x, y: int(x) + int(y), all_digits) 
    print(sum)

main()
