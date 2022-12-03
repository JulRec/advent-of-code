with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:3])

lower_case_alphabet = [chr(i) for i in range(ord("a"), ord("z")+1)]
upper_case_alphabet = [i.upper() for i in lower_case_alphabet]
item_names = lower_case_alphabet + upper_case_alphabet
priorities = [i for i in range(1, len(item_names)+1)]

item_to_priority_mapping = {item_names[i]: priorities[i] for i in range(len(priorities))}
print(item_to_priority_mapping)


def split_rucksack(rucksack):
    half = len(rucksack) // 2
    first_half = rucksack[:half]
    second_half = rucksack[half:]
    assert(len(first_half) == len(second_half))
    return set(first_half), set(second_half)


def part_one(parsed_input):
    summed_priorities = 0
    for rucksack in parsed_input:
        first_half, second_half = split_rucksack(rucksack)
        intersecting_item = first_half.intersection(second_half).pop()
        priority = item_to_priority_mapping[intersecting_item]
        summed_priorities += priority

    print("Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?")
    print(summed_priorities)


part_one(parsed_input)


def find_badge(rucksacks):
    assert(len(rucksacks) == 3)
    r1, r2, r3 = [set(rucksack) for rucksack in rucksacks]
    badge = r1.intersection(r2, r3).pop()
    return badge


def part_two(parsed_input):
    summed_priorities = 0

    for i in range(0, len(parsed_input), 3):
        rucksacks = parsed_input[i:i+3]
        badge = find_badge(rucksacks)
        priority = item_to_priority_mapping[badge]
        summed_priorities += priority

    print("Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?")
    print(summed_priorities)


part_two(parsed_input)



