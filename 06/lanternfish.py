import numpy as np

with open("input.txt") as f:
    instructions_raw = f.read().split(",")

instructions = [int(instruction) for instruction in instructions_raw]
print(instructions)

part1 = False
if part1:
    days = 80
    today = instructions
    next_day = []

    for _ in range(days):
        for internal_timer in today:
            if internal_timer == 0:
                next_day.append(8)  # new fish is born
                next_day.append(6)  # reset internal timer

            else:
                next_day.append(internal_timer - 1)
        today = next_day
        next_day = []

    print(f"Counting {len(today)} fish.")

# part 2
# initialization
internal_timers = {str(i): 0 for i in range(9)}
for timer in instructions_raw:
    internal_timers[timer] += 1

print(internal_timers)
days = 256
for day in range(days):
    newborn_fish = internal_timers["0"]

    # move fish timers by one day
    internal_timers["0"] = internal_timers["1"]
    internal_timers["1"] = internal_timers["2"]
    internal_timers["2"] = internal_timers["3"]
    internal_timers["3"] = internal_timers["4"]
    internal_timers["4"] = internal_timers["5"]
    internal_timers["5"] = internal_timers["6"]
    internal_timers["6"] = internal_timers["7"]
    internal_timers["7"] = internal_timers["8"]

    # add baby-fish
    internal_timers["8"] = newborn_fish

    # reset parent fish
    internal_timers["6"] += newborn_fish

all_fish = sum([value for key, value in internal_timers.items()])
print(all_fish)

