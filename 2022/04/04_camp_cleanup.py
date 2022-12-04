with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:3])

preprocessed_input = [line.split(",") for line in parsed_input]
print(preprocessed_input[:3])

def get_range_from_assignment(assignment):
    elf1, elf2 = assignment
    sections_elf1 = elf1.split("-")
    sections_elf2 = elf2.split("-")
    section_range_elf1 = set([i for i in range(int(sections_elf1[0]), int(sections_elf1[1])+1)])
    section_range_elf2 = set([i for i in range(int(sections_elf2[0]), int(sections_elf2[1]) + 1)])
    return section_range_elf1, section_range_elf2


def part_one(preprocessed_input):
    complete_overlaps = 0
    for assignment in preprocessed_input:
        section_range_elf1, section_range_elf2 = get_range_from_assignment(assignment)
        intersecting_sections = section_range_elf1.intersection(section_range_elf2)

        if len(intersecting_sections) == len(section_range_elf1) or len(intersecting_sections) == len(section_range_elf2):
            complete_overlaps += 1

    print("In how many assignment pairs does one range fully contain the other?")
    print(complete_overlaps)


part_one(preprocessed_input)


def part_two(preprocessed_input):
    overlaps = 0
    for assignment in preprocessed_input:
        section_range_elf1, section_range_elf2 = get_range_from_assignment(assignment)
        intersecting_sections = section_range_elf1.intersection(section_range_elf2)

        if len(intersecting_sections) > 0:
            overlaps += 1

    print("In how many assignment pairs do the ranges overlap?")
    print(overlaps)


part_two(preprocessed_input)
