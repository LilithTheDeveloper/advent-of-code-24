def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))


inp = input()

times = inp[0].split(':')[1].split()
distance = inp[1].split(':')[1].split()

times = list(map(lambda x: int(x), times))
distance = list(map(lambda x: int(x), distance))

time_distance = list(zip(times, distance))

max_ways = []
for time_distance in time_distance:
    time_total = time_distance[0]
    distance = time_distance[1]

    ways = 0
    
    for i in range(0, time_total):
        charging_time = i 
        travel_distance = time_total - charging_time

        distance_travelled = charging_time * travel_distance

        if distance_travelled > distance:
            ways += 1
    max_ways.append(ways)

from functools import reduce
print(max_ways)

prod_ways = 0

for i in range(0, len(max_ways)):
    if i == 0:
        prod_ways = max_ways[i]
    else:
        prod_ways *= max_ways[i]

print("Maximum number of ways: ", prod_ways)



