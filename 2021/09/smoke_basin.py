import numpy as np

with open("testinput.txt") as f:
    instructions_raw = f.read().splitlines()

array = np.array([[int(number) for number in row] for row in instructions_raw])
y_max = array.shape[0]
x_max = array.shape[1]

def get_adjacent_indices(x, y):
    indices = []
    if x > 0:
        indices.append([x - 1, y])
    if x < x_max - 1:
        indices.append([x + 1, y])
    if y > 0:
        indices.append([x, y - 1])
    if y < y_max - 1:
        indices.append([x, y + 1])
    return indices


low_points = []
for y in range(y_max):
    for x in range(x_max):
        adjacent_indices = get_adjacent_indices(x, y)
        adjacent_values = [array[y, x] for x, y in adjacent_indices]
        if array[y, x] < min(adjacent_values):
            low_points.append([x, y])

risk_levels = [1 + array[y, x] for x, y in low_points]
print(f"Part 1 sum of the risk levels is {sum(risk_levels)}")

def get_adjacent_basin_indices(x, y):
    adjacent_indices = get_adjacent_indices(x, y)
    basin_indices = [[x, y] for x, y in adjacent_indices if y < 9]
    return basin_indices


for point in low_points:
    # extend all points until they reach a 9
    pass




