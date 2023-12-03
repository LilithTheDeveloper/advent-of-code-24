from functools import reduce

input_file = 'input.txt'

def get_number_in_string(string):
    number_words = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            }

    for number_word in number_words:
        if string.startswith(number_word):
            return number_words[number_word]
    return 0

def first_and_last_digit(line):
    digits = []
    for i, c in enumerate(line):
        if(c.isdigit()):
            digits.append(c)
        else:
            number = get_number_in_string(line[i:])
            if(number != 0):
                digits.append(str(number))
    if(len(digits) == 0):
        return 0
    combine = digits[0] + digits[-1] if len(digits) > 1 else digits[0] + digits[0]
    return combine 

def ginput():
    with open(input_file) as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

def main():
    input = ginput()
    all_digits = map(first_and_last_digit, input) 
    sum = reduce(lambda x, y: int(x) + int(y), all_digits) 
    print(sum)
    pass

if __name__ == "__main__":
    main()
