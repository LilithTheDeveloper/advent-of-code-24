from pprint import pprint
import prettytable as pt
import numpy as np

def input():
    with open('input.txt') as f:
        lines = f.readlines()
    return list(map(lambda x: x.strip(), lines))

fields = input()

DEST_START='DEST_START'
DEST_END='DEST_END'
SRC_START='SRC_START'
SRC_END='SRC_END'
RANGE='RANGE'
START='START'
END='END'


def get_map_index(fields, map_name):
    start = -1
    end = -1
    for i in range(1, len(fields)):
        if(fields[i] == map_name):
            start = i+1
            break

    for i in range(start, len(fields)):
        if(fields[i] == ''):
            end = i
            break

    return start, end

def get_maps(fields, map_name):
    map_index = get_map_index(fields, map_name)
    map_lines = fields[map_index[0]:map_index[1]]
    return list(map(lambda x: x.split(), map_lines))

def categorize_maps(maps):
    categorized_maps = []
    for map in maps:
        categorized_map = {}
        categorized_map.update(DEST_START=int(map[0]))
        categorized_map.update(DEST_END=int(map[0])+int(map[2])-1)
        categorized_map.update(SRC_START=int(map[1]))
        categorized_map.update(SRC_END=int(map[1])+int(map[2])-1)
        categorized_map.update(RANGE=int(map[2]))
        categorized_maps.append(categorized_map)
    categorized_maps.sort(key=lambda x: x.get(SRC_START))
    return categorized_maps

seed_to_soil = categorize_maps(get_maps(fields, 'seed-to-soil map:'))
soil_to_fertilizer = categorize_maps(get_maps(fields, 'soil-to-fertilizer map:'))
fertilizer_to_water = categorize_maps(get_maps(fields, 'fertilizer-to-water map:'))
water_to_light = categorize_maps(get_maps(fields, 'water-to-light map:'))
light_to_temperature = categorize_maps(get_maps(fields, 'light-to-temperature map:'))
temperature_to_humidity = categorize_maps(get_maps(fields, 'temperature-to-humidity map:'))
humidity_to_location = categorize_maps(get_maps(fields, 'humidity-to-location map:'))

seeds = list(map(lambda x: int(x), fields[0].split(' ')[1:]))

def categorize_seeds(seeds):
    categorized_seeds = []
    for i in range(0, len(seeds)-1, 2):
        categorized_seed = {}
        start = seeds[i]
        rng = seeds[i+1]
        end = start + rng - 1
        categorized_seed.update(START=start)
        categorized_seed.update(END=end)
        categorized_seed.update(RANGE=rng)
        categorized_seeds.append(categorized_seed)
    return categorized_seeds

seed_ranges = categorize_seeds(seeds)

def get_seed_src_range(start, end, seed_to_soil_map):
    for map in seed_to_soil_map:
        src_start = map.get(SRC_START)
        src_end = map.get(SRC_END)
        print(start, end, src_start, src_end)
        if(start >= src_start and end <= src_end):
            return map
    print(f"No map found for seed range {start} -> {end}")
    return None

seed_to_soil_ranges = []
for map in seed_ranges:
    ranges = get_seed_src_range(map.get(START), map.get(END), seed_to_soil)
    seed_to_soil.append(ranges)


# def select_map(source, maps):
#     for map in maps:
#         src_start = map.get(SRC_START)
#         src_end = map.get(SRC_END)
#         if(source >= src_start and source <= src_end):
#             return map
#     # print("No map found for source: ", source)
#     return None

# Any source numbers that aren't mapped correspond to the same destination number. 
# So, seed number 10 corresponds to soil number 10.

def get_dest(src_x)

# def get_dest(source, map):
#     src_start = map.get(SRC_START)
#     dest_start = map.get(DEST_START)
#     diff = source - src_start
#     dest = dest_start + diff
#     return dest

# def map_src_to_dst(source, map):
#     if(map == None):
#         return source
#     dest = get_dest(source, map)
#     return dest
#
# table = pt.PrettyTable()
# table.field_names = ["Seed", "Soil", "Fertilizer", "Water", "Light", "Temperature", "Humidity", "Location"]
#
# for seed in seeds:
#     seed_destinations = map_src_to_dst(seed, select_map(seed, seed_to_soil))
#     soil_destinations = map_src_to_dst(seed_destinations, select_map(seed_destinations, soil_to_fertilizer))
#     fertilizer_destinations = map_src_to_dst(soil_destinations, select_map(soil_destinations, fertilizer_to_water))
#     water_destinations = map_src_to_dst(fertilizer_destinations, select_map(fertilizer_destinations, water_to_light))
#     light_destinations = map_src_to_dst(water_destinations, select_map(water_destinations, light_to_temperature))
#     temperature_destinations = map_src_to_dst(light_destinations, select_map(light_destinations, temperature_to_humidity))
#     humidity_destinations = map_src_to_dst(temperature_destinations, select_map(temperature_destinations, humidity_to_location))
#
#     table.add_row([seed, seed_destinations, soil_destinations, fertilizer_destinations, water_destinations, light_destinations, temperature_destinations, humidity_destinations])
#
# table.sortby = "Location"
# # print(table)
#     
#
