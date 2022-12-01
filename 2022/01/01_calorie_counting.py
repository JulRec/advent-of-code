with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:30])

elfes_and_their_snacks = []
tmp = []

for i in range(len(parsed_input)):
    snack = parsed_input[i]

    # elf has finished it's list
    if len(snack) == 0:
        elfes_and_their_snacks.append(tmp)
        tmp = []

    else:
        tmp.append(float(snack))

print(elfes_and_their_snacks[:3])

calories_per_elf = [sum(snacks_per_elf) for snacks_per_elf in elfes_and_their_snacks]

elf_carrying_most_calories = max(calories_per_elf)
print("How many total Calories is the Elf carrying the most Calories carrying?")
print(elf_carrying_most_calories)

calories_per_elf_sorted = sorted(calories_per_elf, reverse=True)
print(calories_per_elf_sorted[:3])
print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
print(sum(calories_per_elf_sorted[:3]))