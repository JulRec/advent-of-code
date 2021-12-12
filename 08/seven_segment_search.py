with open("input.txt") as f:
    instructions_raw = f.read().splitlines()

signal_patterns = [line.split(" | ")[0].split(" ") for line in instructions_raw]
output_values = [line.split(" | ")[1].split(" ") for line in instructions_raw]

# part 1
digit_count = 0
for line in output_values:
    for digit in line:
        digit_length = len(digit)
        if digit_length == 2 or digit_length == 3 or digit_length == 4 or digit_length == 7:
            digit_count += 1

print(f"Part 1 counts {digit_count} digits with unique patterns.")

# part 2
length_to_digit_mapping = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


decoded_outputs = []
for i in range(len(signal_patterns)):
    line = signal_patterns[i]
    segments_mapping = {}
    len5 = []
    len6 = []

    for digit in line:
        digit_length = len(digit)
        digit_as_set = set(list(digit))

        # uniques
        if digit_length == 2:
            segments_mapping["1"] = digit_as_set
        elif digit_length == 3:
            segments_mapping["7"] = digit_as_set
        elif digit_length == 4:
            segments_mapping["4"] = digit_as_set
        elif digit_length == 7:
            segments_mapping["8"] = digit_as_set

        # mulitples
        elif digit_length == 5:
            len5.append(digit_as_set)
        elif digit_length == 6:
            len6.append(digit_as_set)

    for digit in len5:
        four_without_one = segments_mapping["4"].difference(segments_mapping["1"])
        #print(segments_mapping["4"], "without", segments_mapping["1"], "is", four_without_one)

        if len(digit.intersection(segments_mapping["1"])) == 2:
            segments_mapping["3"] = digit
        elif len(digit.intersection(four_without_one)) == 2:
            segments_mapping["5"] = digit
        else:
            segments_mapping["2"] = digit

    for digit in len6:
        if digit.issuperset(segments_mapping["4"]):
            segments_mapping["9"] = digit
        elif digit.issuperset(segments_mapping["1"]):
            segments_mapping["0"] = digit
        else:
            segments_mapping["6"] = digit

    output = ""
    for digit in output_values[i]:
        digit_as_set = set(list(digit))
        for key, value in segments_mapping.items():
            if digit_as_set == value:
                output += key
    decoded_outputs.append(int(output))

print(f"Part 2 sum of decoded outputs is {sum(decoded_outputs)}.")


