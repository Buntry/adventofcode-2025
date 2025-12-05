from dataclasses import dataclass
from typing import Self
from sortedcontainers import SortedDict

def get_input():
    return [line.strip() for line in open("day5/input.txt", "r").readlines()]

@dataclass
class Range:
    low_inclusive: int
    high_inclusive: int

    def is_overlapping(self, other: Self) -> bool:
        return (self.high_inclusive >= other.low_inclusive 
                and other.high_inclusive >= self.low_inclusive)
    
    def extend_with_overlapping(self, other: Self) -> Self:
        return Range(min(self.low_inclusive, other.low_inclusive), max(self.high_inclusive, other.high_inclusive))
    
    def in_range(self, x: int) -> bool:
        return self.low_inclusive <= x and x <= self.high_inclusive
    
    def count(self) -> int:
        return self.high_inclusive - self.low_inclusive + 1

class MultiRange:
    def __init__(self):
        # always these ranges are non-overlapping
        self.ranges_by_lower = SortedDict()

    def add_range(self, a_range: Range):
        start_index = self.ranges_by_lower.bisect_right(a_range.low_inclusive) - 1
        start_index = max(start_index, 0)
        
        merged = a_range
        keys_to_remove = []
        
        keys = self.ranges_by_lower.keys()
        for index in range(start_index, len(keys)):
            key = keys[index]
            existing_range = self.ranges_by_lower[key]
            
            if merged.is_overlapping(existing_range):
                merged = merged.extend_with_overlapping(existing_range)
                keys_to_remove.append(key)
            elif existing_range.low_inclusive > merged.high_inclusive:
                # not possible to overlap
                break

        for key in keys_to_remove:
            del self.ranges_by_lower[key]
    
        self.ranges_by_lower[merged.low_inclusive] = merged

    def in_range(self, x: int) -> bool:
        idx = self.ranges_by_lower.bisect_right(x)
        if idx > 0:
            key = self.ranges_by_lower.keys()[idx - 1]
            return self.ranges_by_lower[key].in_range(x)
        return False
    
    def count(self) -> int:
        total = 0
        for a_range in self.ranges_by_lower.values():
            total += a_range.count()
        return total

def solution_one():
    fresh_id_ranges = MultiRange()
    finished_ranges = False

    total_fresh_ingredients = 0

    for line in get_input():
        if not finished_ranges:
            if line:
                lower, upper = line.split("-", 2)
                parsed_range = Range(int(lower), int(upper))
                fresh_id_ranges.add_range(parsed_range)
            else:
                finished_ranges = True
                continue
        else:
            ingredient_id = int(line)
            if fresh_id_ranges.in_range(ingredient_id):
                total_fresh_ingredients += 1
    return total_fresh_ingredients


def solution_two():
    fresh_id_ranges = MultiRange()

    for line in get_input():
        if not line:
            break
        lower, upper = line.split("-", 2)
        parsed_range = Range(int(lower), int(upper))
        fresh_id_ranges.add_range(parsed_range)
    
    return fresh_id_ranges.count()

if __name__ == "__main__":
    print("Solution 1:", solution_one())
    print("Solution 2:", solution_two())