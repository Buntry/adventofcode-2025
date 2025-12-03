from math import pow
from functools import lru_cache

def get_input():
    return [line.strip() for line in open("day3/input.txt", "r").readlines()]

def solution_one():
    total_joltage = 0
    for line in get_input():
        total_joltage += max_joltage(line)
    return total_joltage

def solution_two():
    total_joltage = 0
    for line in get_input():
        total_joltage += max_joltage(line, num_batteries=12)
    return total_joltage


def max_joltage(batteries, num_batteries=2):

    # cumulative_joltage[b][p] represents the way to pick the best b batteries from position p onwards
    cumulative_joltage = [[0 for _ in range(0, len(batteries))] for _ in range(0, num_batteries+1)]

    for battery_count in range(0, num_batteries+1):
        # we don't really care about zero batteries
        if battery_count == 0:
            continue
        
        # if there is only 1 battery to choose, take the maximum from position p onwards
        if battery_count == 1:
            for p in reversed(range(0, len(batteries))):
                if p+1 == len(batteries):
                    cumulative_joltage[1][p] = int(batteries[p])
                else:
                    cumulative_joltage[1][p] = max(cumulative_joltage[1][p+1], int(batteries[p]))
        else:
            for pos in reversed(range(0, len(batteries))):
                # No more room for remaining batteries
                remaining_battery_count = len(batteries) - pos
                if battery_count > remaining_battery_count:
                    cumulative_joltage[battery_count][pos] = 0
                    continue

                # best joltage at position
                best_joltage_at_pos = None

                # joltage if we take this battery
                joltage_with_take = (int(batteries[pos]) * int(pow(10, battery_count-1))) + cumulative_joltage[battery_count-1][pos+1]
                
                # determine if we must take this battery, otherwise get the skip value
                if battery_count == remaining_battery_count:
                    best_joltage_at_pos = joltage_with_take
                else:
                    joltage_with_skip = cumulative_joltage[battery_count][pos+1]
                    best_joltage_at_pos = max(joltage_with_take, joltage_with_skip)

                cumulative_joltage[battery_count][pos] = best_joltage_at_pos
    
    return cumulative_joltage[num_batteries][0]

if __name__ == "__main__":
    print("Solution 1", solution_one())
    print("Solution 2", solution_two())