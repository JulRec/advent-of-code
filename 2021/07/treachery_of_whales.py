import numpy as np

with open("input.txt") as f:
    instructions_raw = f.read().split(",")

instructions = [int(instruction) for instruction in instructions_raw]

positions = np.array(instructions)
position_min = positions.min()
position_max = positions.max()

# part 1
min_fuel_cost = np.infty
for distance in range(position_min, position_max+1):
    costs = np.absolute(positions - distance)
    costs_for_all_moves = np.sum(costs)
    if costs_for_all_moves < min_fuel_cost:
        min_fuel_cost = costs_for_all_moves

print(f"Part 1: minimum fuel cost is {min_fuel_cost}.")

# part 2
min_fuel_cost = np.infty
for distance in range(position_min, position_max+1):
    costs = np.absolute(positions - distance).tolist()
    crab_engineering_costs = [sum(list(range(1, cost+1))) for cost in costs]

    costs_for_all_moves = sum(crab_engineering_costs)
    if costs_for_all_moves < min_fuel_cost:
        min_fuel_cost = costs_for_all_moves

print(f"Part 2: minimum fuel cost is {min_fuel_cost}.")

