import numpy as np

with open("input.txt") as f:
    instructions_raw = f.read().splitlines()

instructions = [instruction.split(" -> ") for instruction in instructions_raw]

coordinates = []
for line in instructions:
    x1, y1 = line[0].split(",")
    x2, y2 = line[1].split(",")
    coordinates.append([int(x1), int(y1), int(x2), int(y2)])

def calculate_points_on_line(line):
    x1, y1, x2, y2 = line
    x_shift = abs(x1 - x2)
    y_shift = abs(y1 - y2)
    x_min = x1 if x1 < x2 else x2
    y_min = y1 if y1 < y2 else y2

    points_on_line = []
    if x_shift and not y_shift:  # horizontal line
        for i in range(x_shift+1):
            points_on_line.append([x_min+i, y_min])

    elif y_shift and not x_shift:  # vertical line
        for i in range(y_shift+1):
            points_on_line.append([x_min, y_min+i])

    else:  # diagonal line
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        range_x = range(x1, x2 + step_x, step_x)
        range_y = range(y1, y2 + step_y, step_y)

        for i in range(x_shift + 1):
            points_on_line.append([range_x[i], range_y[i]])

    return points_on_line


covered_points = []
for line in coordinates:
    points = calculate_points_on_line(line)
    covered_points.extend(points)

points_to_count = np.array(covered_points)
unique, counts = np.unique(points_to_count, axis=0, return_counts=True)
print(len(unique[counts > 1]))


