from itertools import batched
from math import ceil

def get_input():
    return [line.strip() for line in open("day2/input.txt", "r").readlines()]

def processed_input():
    processed_ranges = list()
    for pair_string in get_input()[0].split(","):
        lower, upper = pair_string.split("-", 2)
        processed_ranges.append((lower, upper))
    return processed_ranges

def solution_one():
    invalid_id_total = 0
    for lower, upper in processed_input():
        for id in range(int(lower), int(upper)+1):
            if is_invalid(str(id)):
                invalid_id_total += id
    return invalid_id_total

def is_invalid(id):
    return len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]

def solution_two():
    invalid_id_total = 0
    for lower, upper in processed_input():
        for id in range(int(lower), int(upper)+1):
            if is_invalid_sol2(str(id)):
                invalid_id_total += id
    return invalid_id_total

def is_invalid_sol2(id):
    for repeat_len in range(1, (len(id) // 2) + 1):
        if len(id) % repeat_len != 0:
            continue
        if len(set(batched(id, repeat_len))) == 1:
            return True
    return False

if __name__ == "__main__":
    print("Advent of Code 2025: Day 2")
    print("Sol 1:", solution_one())
    print("Sol 2:", solution_two())
