with open("input.txt") as f:
    parsed_input = f.read()


def find_marker(stream, number_of_unique_characters):
    for i in range(len(stream)):
        potential_start_of_packet_marker = stream[i:i+number_of_unique_characters]
        complete_marker_index = i + number_of_unique_characters
        if len(set(potential_start_of_packet_marker)) == number_of_unique_characters:
            print(f"Found marker: {potential_start_of_packet_marker} after {complete_marker_index} signs")
            break


# part one
find_marker(parsed_input, 4)

# part two
find_marker(parsed_input, 14)