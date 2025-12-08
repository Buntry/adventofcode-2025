from argparse import ArgumentParser
from itertools import combinations
from math import sqrt
from collections import defaultdict

def read_file(is_demo):
    file_name = "day8/input.txt" if not is_demo else "day8/demo-input.txt"
    return open(file_name, "r").read()

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--demo", "-d", action='store_true', help="Use demo input")
    return parser.parse_args()

def solution_one(args):
    lines = read_file(bool(args.demo)).split("\n")
    points = set()
    for line in lines:
        x, y, z = line.strip().split(",", 3)
        x, y, z = int(x), int(y), int(z)
        points.add((x, y, z))
    
    distances = dict()
    for p1, p2 in combinations(points, 2):
        distances[frozenset([p1, p2])] = distance_between_points(p1, p2)
    
    distance_items = sorted(distances.items(), key=lambda x: x[1])
    circuit_id_counter = -1
    
    points_by_circuit = defaultdict(set)
    connections_by_point = defaultdict(set)
    circuits_by_point = dict()

    limit = 1000 if not args.demo else 10

    for idx, distance_item in zip(range(0, limit), distance_items):
        points, distance = distance_item
        p1, p2 = tuple(points)

        # if both are connected already to the same circuit, nothing happens!
        if p1 in circuits_by_point and p2 in circuits_by_point \
            and circuits_by_point[p1] == circuits_by_point[p2]:
            continue

        # if neither are connected, connect them with a new circuit
        elif p1 not in circuits_by_point and p2 not in circuits_by_point:
            circuit_id_counter += 1
            
            points_by_circuit[circuit_id_counter].add(p1)
            points_by_circuit[circuit_id_counter].add(p2)

            connections_by_point[p1].add(p2)
            connections_by_point[p2].add(p1)

            circuits_by_point[p1] = circuit_id_counter
            circuits_by_point[p2] = circuit_id_counter

        # if both are connected by mismatching circuits, p2 and its connections merge with p1
        elif p1 in circuits_by_point and p2 in circuits_by_point:
            circuit_p1 = circuits_by_point[p1]
            circuit_p2 = circuits_by_point[p2]

            connections_by_point[p1].add(p2)
            connections_by_point[p2].add(p1)

            # merge all p2 circuits into p1
            for point_circuit_p2 in points_by_circuit[circuit_p2]:
                circuits_by_point[point_circuit_p2] = circuit_p1
                points_by_circuit[circuit_p1].add(point_circuit_p2)
            del points_by_circuit[circuit_p2]
        
        # if only pA is connected, merge pB into pA
        else:
            pa = p1 if p1 in circuits_by_point else p2
            pb = p1 if pa is p2 else p2

            circuit_pa = circuits_by_point[pa]

            connections_by_point[pa].add(pb)
            connections_by_point[pb].add(pa)
            
            points_by_circuit[circuit_pa].add(pb)
            circuits_by_point[pb] = circuit_pa

        print(f"Iter {idx} ===========")
        print(f"{points_by_circuit=}")
        print(f"{connections_by_point=}")
        print(f"{circuits_by_point=}")

    # sort the circuits by number of points
    circuit_points = sorted(points_by_circuit.items(), key=lambda points_by_circuit_item: len(points_by_circuit_item[1]))
    
    # get the 3 largest circuits by size, multiplying them together
    accumulator = 1
    for circuit_id, points in circuit_points[-3:]:
        accumulator *= len(points)
    return accumulator


def solution_two(args):
    lines = read_file(bool(args.demo)).split("\n")
    points = set()
    for line in lines:
        x, y, z = line.strip().split(",", 3)
        x, y, z = int(x), int(y), int(z)
        points.add((x, y, z))
    
    distances = dict()
    for p1, p2 in combinations(points, 2):
        distances[frozenset([p1, p2])] = distance_between_points(p1, p2)
    
    distance_items = sorted(distances.items(), key=lambda x: x[1])
    circuit_id = 0
    
    points_by_circuit = defaultdict(set)
    connections_by_point = defaultdict(set)
    circuits_by_point = dict()

    last_connection = None

    for idx, distance_item in enumerate(distance_items):
        points, _ = distance_item
        p1, p2 = tuple(points)

        # if both are connected already, nothing happens!
        if p1 in circuits_by_point and p2 in circuits_by_point:
            continue

        # if neither are connected, connect them with the same circuit
        elif p1 not in circuits_by_point and p2 not in circuits_by_point:
            points_by_circuit[circuit_id].add(p1)
            points_by_circuit[circuit_id].add(p2)

            connections_by_point[p1].add(p2)
            connections_by_point[p2].add(p1)
            last_connection = p1[0] * p2[0]

            circuits_by_point[p1] = circuit_id
            circuits_by_point[p2] = circuit_id
        
        # if only pA is connected, merge pB into pA
        else:
            pa = p1 if p1 in circuits_by_point else p2
            pb = p1 if pa is p2 else p2

            circuit_pa = circuits_by_point[pa]

            connections_by_point[pa].add(pb)
            connections_by_point[pb].add(pa)
            last_connection = pa[0] * pb[0]
            
            points_by_circuit[circuit_pa].add(pb)
            circuits_by_point[pb] = circuit_pa
    
    return last_connection
    
    

def distance_between_points(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)


if __name__ == "__main__":
    args = parse_args()
    #print("Solution 1: ", solution_one(args))
    print("Solution 2: ", solution_two(args))