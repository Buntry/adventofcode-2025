def get_input():
    return [list(line.strip()) for line in open("day4/input.txt", "r").readlines()]

def grid_neighbor_positions(row, col, width, height):
    relative_shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for shift_row, shift_col in relative_shifts:
        new_row = row + shift_row
        new_col = col + shift_col

        if new_row < 0 or new_row >= height:
            continue
        elif new_col < 0 or new_col >= width:
            continue

        yield new_row, new_col 

def solution_one():
    grid = get_input()
    height = len(grid)
    width = len(grid[0])

    total_paper_rolls_with_three_or_less = 0

    for row in range(0, height):
        for col in range(0, width):

            # skip if not a paper roll
            if grid[row][col] != "@":
                continue

            total_paper_rolls = 0
            for neighbor_row, neighbor_col in grid_neighbor_positions(row, col, width, height):
                if grid[neighbor_row][neighbor_col] == "@":
                    total_paper_rolls += 1

            if total_paper_rolls <= 3:
                total_paper_rolls_with_three_or_less += 1
    return total_paper_rolls_with_three_or_less

def solution_two():
    grid = get_input()
    height = len(grid)
    width = len(grid[0])

    total_paper_rolls_with_three_or_less = 0

    current_iter_rolls = None
    iteration_counter = 0
    while current_iter_rolls != 0:
        iteration_counter += 1
        current_iter_rolls = 0
        for row in range(0, height):
            for col in range(0, width):

                # skip if not a paper roll
                if grid[row][col] != "@":
                    continue

                total_paper_rolls = 0
                for neighbor_row, neighbor_col in grid_neighbor_positions(row, col, width, height):
                    if grid[neighbor_row][neighbor_col] == "@":
                        total_paper_rolls += 1

                if total_paper_rolls <= 3:
                    grid[row][col] = "x"
                    current_iter_rolls += 1
        total_paper_rolls_with_three_or_less += current_iter_rolls 
    return total_paper_rolls_with_three_or_less

if __name__ == "__main__":
    print("Solution 1: ", solution_one())
    print("Solution 2: ", solution_two())