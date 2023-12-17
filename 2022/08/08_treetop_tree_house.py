import numpy as np


with open("test_input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input)

raw_map = []
for row in parsed_input:
    fields = [int(height) for height in row]
    raw_map.append(fields)

map = np.array(raw_map)
print(map)
# visible_tree_map = np.zeros(map.shape, dtype=int)
# print(visible_tree_map)


def count_visible_trees(row):
    counter = 0
    for i in range(len(row - 1)):
        tree = row[i]
        predecessors = row[:i]
        tree_bigger_than_predecessors = predecessors < tree
        print(predecessors, tree, predecessors < tree)

        if tree_bigger_than_predecessors.all():
            print("counting", tree)
            counter += 1

    return counter


"""
visible_trees = 0
for row in map:
    #print(row)
    visible_trees += count_visible_trees(row)
    #print(np.flip(row))
    visible_trees += count_visible_trees(np.flip(row))
    #break
    print()


# transpose map to get columns
for row in map.T:
    #print(row)
    visible_trees += count_visible_trees(row)
    #print(np.flip(row))
    visible_trees += count_visible_trees(np.flip(row))
    #break
"""


def draw_visible_tree_in_map(row):
    visible_trees_in_row = np.zeros(row.shape, dtype=int)
    for i in range(len(row - 1)):
        tree = row[i]
        predecessors = row[:i]
        tree_bigger_than_predecessors = predecessors < tree
        # print(predecessors, tree, predecessors < tree)

        if tree_bigger_than_predecessors.all():
            visible_trees_in_row[i] = 1

    return visible_trees_in_row


# concat the np arrays with or to get the 1 at the right place
rows, cols = map.shape
print(rows, cols)


visible_tree_map_left = np.zeros(map.shape, dtype=int)
visible_tree_map_right = np.zeros(map.shape, dtype=int)
for i in range(rows):
    row = map[i]
    # print(row)
    visible_trees = draw_visible_tree_in_map(row)
    visible_tree_map_left[i] = visible_trees

    visible_trees = draw_visible_tree_in_map(np.flip(row))
    visible_tree_map_right[i] = np.flip(visible_trees)

# print(visible_tree_map_left)
# print(visible_tree_map_right)


visible_tree_map_from_top = np.zeros(map.shape, dtype=int)
visible_tree_map_from_bottom = np.zeros(map.shape, dtype=int)
for i in range(cols):
    # transpose map to get columns
    row = map.T[i]
    # print(row)
    visible_trees = draw_visible_tree_in_map(row)
    visible_tree_map_from_top[i] = visible_trees

    visible_trees = draw_visible_tree_in_map(np.flip(row))
    visible_tree_map_from_bottom[i] = np.flip(visible_trees)

# print(visible_tree_map_from_top.T)
# print(visible_tree_map_from_bottom.T)

visible_tree_map = (
    visible_tree_map_left
    + visible_tree_map_right
    + visible_tree_map_from_top.T
    + visible_tree_map_from_bottom.T
)

print(visible_tree_map)


print("Consider your map; how many trees are visible from outside the grid?")
print(np.count_nonzero(visible_tree_map))


## part 2
# for each value check all neighbors

scenic_scores = np.zeros(map.shape, dtype=int)
# then get max value

"""
for i in range(rows):
    for j in range(cols):
        #tree = map[i, j]
        # to the left
        left = 0
        for l in range(i):
            next_tree = map[i -l, j]
            
        
        i_tmp = i
        while i_tmp > 0:
            next_tree = map[i_tmp-1, j]
            if next_tree
        
        # to the right
        right = 0
        
        # to the top
        top = 0
        
        # to the bottom
        bottom = 0
"""


# die karte so slicen, dass mein baum die Ecke ist


def count_visible_trees(row):
    # assuming data is provided in the form of yyy where x is the location for the tree house left to the is the rest of the row.
    # e.g.  xyyy
    counter = 1

    if len(row) == 1:
        return 1

    for i in range(len(row) - 1):
        # next tree is bigger, we can't see it
        if row[i] >= row[i + 1]:
            counter += 1
            return counter

        else:
            counter += 1


score_left = np.zeros(map.shape, dtype=int)
# check out view to the left
for row in map:
    # slice the rows
    row = np.flip(row)
    row_score = 0
    for i in range(1, len(row)):
        print(row)
        tmp_row = row[:i]
        print(tmp_row)
        score = count_visible_trees(tmp_row)
        print(score)
    break

    # print(row)


input_file = open("input.txt", "r")
# input_file = open('input/input_test.txt', 'r')

tree_heights = np.array(
    [[int(i) for i in line.strip()] for line in input_file], dtype=object
)
scenic_scores = dict()

width = tree_heights.shape[0]
height = tree_heights.shape[1]

for i in range(width):
    for j in range(height):
        N_sum, S_sum, E_sum, W_sum = (0, 0, 0, 0)
        for N in reversed(range(0, j)):
            N_sum += 1
            if tree_heights[i, j] <= tree_heights[i, N]:
                break
        for S in range(j + 1, height):
            S_sum += 1
            if tree_heights[i, j] <= tree_heights[i, S]:
                break
        for W in reversed(range(0, i)):
            W_sum += 1
            if tree_heights[i, j] <= tree_heights[W, j]:
                break
        for E in range(i + 1, width):
            E_sum += 1
            if tree_heights[i, j] <= tree_heights[E, j]:
                break
        # print((i, j), 'N:', N_sum, 'S:', S_sum, 'W:', W_sum, 'E:', E_sum)
        scenic_scores[(i, j)] = N_sum * S_sum * W_sum * E_sum

print(max(scenic_scores.values()))
