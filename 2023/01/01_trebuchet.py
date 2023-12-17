with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:30])


def extract_digits(line):
    numbers = [symbol for symbol in line if symbol.isdigit()]
    two_digit_number = int(numbers[0] + numbers[-1])
    return two_digit_number


def get_calibration_values(input):
    calibration_values = [extract_digits(line) for line in input]
    return calibration_values


print(f"Solution part 1 {sum(get_calibration_values(parsed_input))}")

test_input_part_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

SPELLED_OUT_TO_DIGIT = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eignt",
    "nine": "nine9nine",
}


def replace_spelled_out_digits(line):
    for spelled_out in SPELLED_OUT_TO_DIGIT:
        if spelled_out in line:
            digit = SPELLED_OUT_TO_DIGIT[spelled_out]
            line = line.replace(spelled_out, digit)
    return line


preprocessed_input_part_2 = [replace_spelled_out_digits(line) for line in parsed_input]

print(f"Solution part 2 {sum(get_calibration_values(preprocessed_input_part_2))}")
