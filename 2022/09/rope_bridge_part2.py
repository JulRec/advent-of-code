import numpy as np

with open("test_input.txt") as f:
    parsed_input = f.read().splitlines()


def move_one_step(direction, head_position, tail_position, is_head=False):
    if direction == "R":
        if is_head:
            # only use head always, move all other parts only when the distance says so
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
        if is_head:
            # only use head always, move all other parts only when the distance says so
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
        if is_head:
            # only use head always, move all other parts only when the distance says so
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
        if is_head:
            # only use head always, move all other parts only when the distance says so
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

    return total_dist


# field = np.zeros((1000, 1000), dtype=int)
# where position 0 ist the head and position 9 is the tail
# rope_positions = {str(i): np.array([500, 500], dtype=int) for i in range(10)}

# setup for testing
field = (
    np.zeros((5, 6), dtype=int) + 100
)  # todo delete the -1 afterwards, only used for better visibility
rope_positions = {str(i): np.array([4, 0]) for i in range(10)}
# field[rope_positions["9"][0], rope_positions["9"][1]] += 1

print(field)

for line in parsed_input:
    direction, steps = line.split()
    print(f"--------- next line {direction, steps} ------------")
    for i in range(int(steps)):
        for r in range(9):
            # handle each part of the rope as head + tail combo, update counter only if tail did something
            head_position = rope_positions[str(r)]
            tail_position = rope_positions[str(r + 1)]
            # print(f"rope positions {str(r)} as head and {str(r+1)} as tail", "head position", head_position, "tail position", tail_position)
            if r == 0:
                move_one_step(direction, head_position, tail_position, is_head=True)
            else:
                move_one_step(direction, head_position, tail_position)

            # print("head position", head_position, "tail position", tail_position)
            # print("")
            # for now mark everything for debugging
            field[rope_positions[str(r)][0], rope_positions[str(r)][1]] = r
            field[rope_positions[str(r + 1)][0], rope_positions[str(r + 1)][1]] = r + 1
        print(field)

        # mark tail position
        # field[rope_positions["9"][0], rope_positions["9"][1]] += 1
        # print(field)
        # field = np.zeros((5, 6), dtype=int) + 100  # todo delete the -1 afterwards, only used for better visibility


# if there is a gap, let it move to the previous part position?
