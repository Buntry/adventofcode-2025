from argparse import ArgumentParser
from itertools import combinations
from shapely.geometry import Polygon, box

def read_file(is_demo):
    file_name = "day9/input.txt" if not is_demo else "day9/demo-input.txt"
    return open(file_name, "r").read()

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--demo", "-d", action='store_true', help="Use demo input")
    return parser.parse_args()

def solution_one(args):
    lines = read_file(bool(args.demo)).split("\n")
    red_tiles = set()
    for line in lines:
        x, y = line.split(",", 2)
        x, y = int(x), int(y)
        red_tiles.add((x, y))
    
    tile_areas = dict()
    for tile_1, tile_2 in combinations(red_tiles, 2):
        rug_area = compute_rug_area(tile_1, tile_2)
        tile_areas[frozenset([tile_1, tile_2])] = rug_area
    
    descending_tile_areas = list(reversed(sorted(tile_areas.items(), key=lambda tile_area: tile_area[1])))
    return descending_tile_areas[0][1]


def compute_rug_area(tile_1, tile_2):
    tile_1_x, tile_1_y = tile_1
    tile_2_x, tile_2_y = tile_2
    return (1 + abs(tile_1_x - tile_2_x)) * (1 + abs(tile_1_y - tile_2_y))

def solution_two(args):
    lines = read_file(bool(args.demo)).split("\n")
    red_tiles = list()

    for line in lines:
        x, y = line.split(",", 2)
        x, y = int(x), int(y)
        red_tile = (x, y)
        red_tiles.append(red_tile)
    
    green_area = Polygon(red_tiles)

    tile_areas = dict()
    for tile_1, tile_2 in combinations(red_tiles, 2):
        rug_box = get_rug_as_box(tile_1, tile_2)
        if green_area.contains(rug_box):
            rug_area = compute_rug_area(tile_1, tile_2)
            tile_areas[frozenset([tile_1, tile_2])] = rug_area

    descending_tile_areas = list(reversed(sorted(tile_areas.items(), key=lambda tile_area: tile_area[1])))
    return descending_tile_areas[0][1]


def get_rug_as_box(tile_1, tile_2):
    min_x = min(tile_1[0], tile_2[0])
    min_y = min(tile_1[1], tile_2[1])
    max_x = max(tile_1[0], tile_2[0])
    max_y = max(tile_1[1], tile_2[1])
    return box(min_x, min_y, max_x, max_y)

if __name__ == "__main__":
    args = parse_args()
    #print("Solution 1: ", solution_one(args))
    print("Solution 2: ", solution_two(args))