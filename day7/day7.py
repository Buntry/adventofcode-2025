from argparse import ArgumentParser
from collections import defaultdict

def read_file(is_demo):
    file_name = "day7/input.txt" if not is_demo else "day7/demo-input.txt"
    return open(file_name, "r").read()

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--demo", "-d", action='store_true', help="Use demo input")
    return parser.parse_args()

def solution_one(args):
    lines = read_file(bool(args.demo)).split("\n")
    lines = [list(line) for line in lines]
    width = len(lines[0])

    beam_indices = set()
    beam_indices.add("".join(lines[0]).find("S"))

    splitter_count = 0
    
    for row in range(1, len(lines)):
        print(f"==== Row {row} =====")
        print(f"{beam_indices=}")
        print("\n".join("".join(line) for line in lines))

        new_beam_indices = set()
        remove_beam_indices = set()

        for beam_index in beam_indices:
            space = lines[row][beam_index]
            if space == ".":
                lines[row][beam_index] = "|"
            elif space == "^":
                splitter_count += 1
                if beam_index - 1 >= 0:
                    new_beam_indices.add(beam_index - 1)
                if beam_index + 1 < width:
                    new_beam_indices.add(beam_index + 1)
                remove_beam_indices.add(beam_index)
        
        print(f"{new_beam_indices=}")
        print(f"{remove_beam_indices=}")
        print(f"{splitter_count=}")

        for beam_index in remove_beam_indices:
            beam_indices.remove(beam_index)
        for beam_index in new_beam_indices:
            beam_indices.add(beam_index)
    return splitter_count
        
def solution_two(args):
    lines = read_file(bool(args.demo)).split("\n")
    lines = [list(line) for line in lines]
    width = len(lines[0])
    
    starting_beam_index = "".join(lines[0]).find("S")
    
    beam_timelines = defaultdict(int)
    beam_timelines[starting_beam_index] = 1
    
    for row in range(1, len(lines)):
        new_beam_timelines = defaultdict(int)
        remove_beam_indices = set()

        for beam_index in beam_timelines:
            space = lines[row][beam_index]
            num_timelines = beam_timelines[beam_index]
            if space == ".":
                lines[row][beam_index] = num_timelines
            elif space == "^":
                if beam_index - 1 >= 0:
                    new_beam_timelines[beam_index - 1] += num_timelines
                if beam_index + 1 < width:
                    new_beam_timelines[beam_index + 1] += num_timelines
                remove_beam_indices.add(beam_index)
        for beam_index in remove_beam_indices:
            del beam_timelines[beam_index]
        for beam_index in new_beam_timelines:
            beam_timelines[beam_index] += new_beam_timelines[beam_index]
        
        print(f"==== Row {row} =====")
        print(f"{beam_timelines=}")
        print("\n".join(" ".join((str(x) for x in line)) for line in lines))




    possible_timelines = 0
    for beam_index in beam_timelines:
        possible_timelines += beam_timelines[beam_index]
    return possible_timelines
    

if __name__ == "__main__":
    args = parse_args()
    # print("Solution 1: ", solution_one(args))
    print("Solution 2: ", solution_two(args))