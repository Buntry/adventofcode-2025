import re

def get_input():
    return [line.strip() for line in open("day6/input.txt", "r").readlines()]

def process_input():
    matrix = []
    ops = None
    for line in get_input():
        line_parts = re.split(r'\s+', line)
        if line_parts[0].isdigit():
            matrix.append(list(map(int, line_parts)))
        else:
            ops = line_parts
    return matrix, ops

def solution_one():
    total = 0
    matrix, ops = process_input()
    for idx, op in enumerate(ops):
        is_mult = op == "*"
        accumulator = int(is_mult)
        for row in range(0, len(matrix)):
            x = matrix[row][idx]
            if is_mult:
                accumulator *= x
            else:
                accumulator += x
        total += accumulator
    return total

def solution_two():
    file = open("day6/input.txt", "r").read()

    file_lines = file.split("\n")
    file_height = len(file_lines)
    file_width = len(file_lines[-1])

    total = 0
    
    for op_match in re.finditer(r'\*|\+', file_lines[-1]):
        col = op_match.start(0)
        op_parsing = True

        is_mult = file_lines[-1][col] == "*"
        accumulator = int(is_mult)

        while op_parsing and col < file_width:
            digit_str = ""
            for row in range(0, file_height - 1):
                digit_str += file_lines[row][col]
            digit_str = digit_str.strip()
            if digit_str:
                x = int(digit_str)
                if is_mult:
                    accumulator *= x
                else:
                    accumulator += x
                col += 1
            else:
                op_parsing = False
        total += accumulator
        
    return total





if __name__ == "__main__":
    #print("Solution 1: ", solution_one())
    print("Solution 2: ", solution_two())


