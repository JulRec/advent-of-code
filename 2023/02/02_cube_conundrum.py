import numpy as np

with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:3])

test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

MAX_NUMBER_OF_CUBES = {"red": 12, "green": 13, "blue": 14}


def prepare_input(line):
    number_of_cubes_per_color = {}
    game_name, sets_of_cubes = line.split(":")
    sets_of_cubes = sets_of_cubes.split(";")
    game_id = int(game_name.split()[-1])
    print(sets_of_cubes)
    for draw in sets_of_cubes:
        draw = draw.split(",")
        # print(draw)
        for color in draw:
            amount, color = color.strip().split()
            # print(amount, color)
            if color in number_of_cubes_per_color:
                number_of_cubes_per_color[color].append(int(amount))
            else:
                number_of_cubes_per_color[color] = [int(amount)]
    return game_id, number_of_cubes_per_color


def solve_part_one(parsed_input):
    possible_game_ids = []

    for line in parsed_input:
        game_id, number_of_cubes_per_color = prepare_input(line)
        print(number_of_cubes_per_color)
        game_possible = True
        for color, number_of_cubes in number_of_cubes_per_color.items():
            print(f"Max number of cubes for {color}", max(number_of_cubes))
            if max(number_of_cubes) > MAX_NUMBER_OF_CUBES[color]:
                game_possible = False
        print("game possible", game_possible)
        if game_possible:
            possible_game_ids.append(game_id)

    print("Sum of possible game IDs", sum(possible_game_ids))


# solve_part_one(parsed_input)


def solve_part_two(parsed_input):
    all_sets_powers = []
    for line in parsed_input:
        _, number_of_cubes_per_color = prepare_input(line)
        fewest_number_of_cubes = []
        for color, number_of_cubes in number_of_cubes_per_color.items():
            print(f"Max number of cubes for {color}", max(number_of_cubes))
            fewest_number_of_cubes.append(max(number_of_cubes))
        set_power = np.prod(fewest_number_of_cubes)
        print("set_power", set_power)
        all_sets_powers.append(set_power)

    print("Sum of all sets powers", sum(all_sets_powers))


solve_part_two(parsed_input)
