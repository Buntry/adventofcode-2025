input_lines = [line.strip() for line in open("day1/input.txt", "r").readlines()]

dial_start = 50
dial_size = 100

current_dial_position = dial_start
total_rotations_end_at_zero = 0
total_rotation_clicks_at_zero = 0

for line in input_lines:
    direction, count = line[0], int(line[1:])
    if direction == "R":
        # cross zero as frequently as floor dial size division
        total_rotation_clicks_at_zero += (current_dial_position + count) // dial_size

        # move right
        current_dial_position = (current_dial_position + count) % dial_size
    elif direction == "L":
        # if we start at zero, we cross every full rotation
        if current_dial_position == 0:
            total_rotation_clicks_at_zero += count // dial_size
        # else if count would bring us beyond the threshold, every full rotation afterwards hits zero
        elif count >= current_dial_position:
            total_rotation_clicks_at_zero += 1 + ((count - current_dial_position) // dial_size)

        # move left
        current_dial_position = (current_dial_position - count) % dial_size

    if current_dial_position == 0:
        total_rotations_end_at_zero += 1

print("Solution 2:", total_rotations_end_at_zero)
print("Solution 2:", total_rotation_clicks_at_zero)
