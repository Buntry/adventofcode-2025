input_lines = [line.strip() for line in open("day1/input.txt", "r").readlines()]

dial_start = 50
dial_size = 100

current_dial_position = dial_start
total_dials_points_at_zero_condition = 0
total_dials_crossing_zero_condition = 0

# sol 1

# for line in input_lines:
#     direction, count = line[0], int(line[1:])    
#     if direction == "R":
#         current_dial_position += count
#     elif direction == "L":
#         current_dial_position -= count
    
#     current_dial_position %= dial_size
#     if current_dial_position == 0:
#         total_dials_points_at_zero_condition += 1
# print("Solution 1:", total_dials_points_at_zero_condition)


# sol 2

for line in input_lines:
    direction, count = line[0], int(line[1:])
    
    if direction == "R":
        total_dials_crossing_zero_condition += (current_dial_position + count) // dial_size
        current_dial_position = (current_dial_position + count) % dial_size
    else:  # "L"
        if current_dial_position == 0:
            # Going left: we pass 0 every 100 clicks
            total_dials_crossing_zero_condition += count // dial_size
        elif count >= current_dial_position:
            # We'll pass through 0, then potentially more times
            total_dials_crossing_zero_condition += (count - current_dial_position) // dial_size + 1
        # else: count < current_dial_position, so we don't reach 0
        current_dial_position = (current_dial_position - count) % dial_size

print("Solution 2:", total_dials_crossing_zero_condition)
