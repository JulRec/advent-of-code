with open("input.txt") as f:
    instructions_raw = f.read().splitlines()

horizontal_position = 0
depth = 0

for instruction in instructions_raw:
    direction, distance_raw = instruction.split()
    distance = int(distance_raw)
    if direction == "forward":
        horizontal_position += distance
    elif direction == "down":
        depth += distance
    elif direction == "up":
        depth -= distance

print(f"Part 1 answer: {horizontal_position * depth}")
# correct answer part 1 = 1924923

# part 2
horizontal_position = 0
depth = 0
aim = 0

for instruction in instructions_raw:
    direction, distance_raw = instruction.split()
    distance = int(distance_raw)
    if direction == "forward":
        horizontal_position += distance
        depth += (aim * distance)
    elif direction == "down":
        aim += distance
    elif direction == "up":
        aim -= distance

print(f"Part 2 answer: {horizontal_position * depth}")
# correct answer part 2 = 1982495697
