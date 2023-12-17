import numpy as np

with open("test_input.txt") as f:
    parsed_input = f.read().splitlines()


def move_one_step(direction):
    if direction == "R":
        head_position[1] += 1
        distance = calculate_distance(head_position, tail_position)
        if distance == 2:
            # tail mimics the heads movement
            tail_position[1] += 1
        elif distance == 3:
            # tail needs to make a diagonal step
            tail_position[1] += 1
            tail_position[0] = head_position[0]

    elif direction == "L":
        head_position[1] -= 1
        distance = calculate_distance(head_position, tail_position)
        if distance == 2:
            # tail mimics the heads movement
            tail_position[1] -= 1
        elif distance == 3:
            # tail needs to make a diagonal step
            tail_position[1] -= 1
            tail_position[0] = head_position[0]

    elif direction == "D":
        head_position[0] += 1
        distance = calculate_distance(head_position, tail_position)
        if distance == 2:
            # tail mimics the heads movement
            tail_position[0] += 1
        elif distance == 3:
            # tail needs to make a diagonal step
            tail_position[0] += 1
            tail_position[1] = head_position[1]

    elif direction == "U":
        head_position[0] -= 1
        distance = calculate_distance(head_position, tail_position)
        if distance == 2:
            # tail mimics the heads movement
            tail_position[0] -= 1
        elif distance == 3:
            # tail needs to make a diagonal step
            tail_position[0] -= 1
            tail_position[1] = head_position[1]


def calculate_distance(head, tail):
    dist = head - tail
    total_dist = abs(dist[0]) + abs(dist[1])

    if abs(dist[0]) == 1 and abs(dist[1]) == 1:
        # don't move even if it is diagonal
        total_dist -= 1

    if dist[0] != 0 and dist[1] != 0:
        # diagonal
        # total_dist += 1  # <-- not sure if we need taht
        pass

    # print(head, tail, "dist", dist, "total dist", total_dist)
    return total_dist


# setup for testing
field = np.zeros((5, 6), dtype=int)

head_position = np.zeros(2, dtype=int)
tail_position = np.zeros(2, dtype=int)

head_position[0] = 4
tail_position[0] = 4
field[tail_position[0], tail_position[1]] += 1
print(field)

# setup for part one
field = np.zeros((1000, 1000), dtype=int)
head_position = np.array([500, 500], dtype=int)
tail_position = np.array([500, 500], dtype=int)


def solve_part_one(parsed_input):
    for line in parsed_input:
        direction, steps = line.split()
        print(f"--------- next line {direction, steps} ------------")
        for i in range(int(steps)):
            move_one_step(direction)
            # mark tail position
            field[tail_position[0], tail_position[1]] += 1
            # print(field)

    print("How many positions does the tail of the rope visit at least once?")
    print(np.count_nonzero(field))


## part 2
field = np.zeros((1000, 1000), dtype=int)
# where position 0 ist the head and position 9 is the tail
rope_positions = {str(i): np.array([500, 500], dtype=int) for i in range(10)}

# setup for testing
field = np.zeros((5, 6), dtype=int)
rope_positions = {str(i): np.array([4, 0]) for i in range(10)}
field[rope_positions["9"]] += 1


# field[tail_position[0], tail_position[1]] += 1
print(field)

for line in parsed_input:
    direction, steps = line.split()
    print(f"--------- next line {direction, steps} ------------")
    for i in range(int(steps)):
        move_one_step(direction)
        # mark tail position
        field[tail_position[0], tail_position[1]] += 1
        # print(field)
