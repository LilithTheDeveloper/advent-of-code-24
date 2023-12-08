from functools import reduce

def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

inp = input()

time_total = int(inp[0].split(':')[1].replace(' ', ''))
distance = int(inp[1].split(':')[1].replace(' ', ''))

ways = 0
    
for i in range(0, time_total):
    charging_time = i 
    travel_distance = time_total - charging_time

    distance_travelled = charging_time * travel_distance

    if distance_travelled > distance:
        ways += 1

print(ways)
