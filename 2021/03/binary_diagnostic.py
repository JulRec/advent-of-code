import math
import numpy as np


with open("input.txt") as f:
    instructions_raw = f.read().splitlines()

instructions_prepared = np.array([[int(bit) for bit in binary_number] for binary_number in instructions_raw])

height, width = instructions_prepared.shape
most_common_bit_threshold = int(height/2)

ones_per_column = np.count_nonzero(instructions_prepared, axis=0)
column_thresholds = ones_per_column - most_common_bit_threshold  # positive value -> 1, negative value -> 0
print(column_thresholds)
gamma = np.where(column_thresholds > 0, 1, 0)
epsilon = np.where(column_thresholds < 0, 1, 0)
print(f"  gamma = {gamma} \nepsilon = {epsilon}")

exponent = 2 ** np.arange(width-1, -1, -1)
print(exponent)
gamma_rate = np.sum(exponent * gamma)
epsilon_rate = np.sum(exponent * epsilon)
print(f"Calculated power consumption is {gamma_rate * epsilon_rate}, correct answer of part 1 is 841526.")

# part 2
# consider first bit of those numbers
# keep numbers selected by bit critera for the type of rating
# if there is only 1 number left, stop and return value
def calculate_gamma(instructions_prepared):
    height, width = instructions_prepared.shape
    most_common_bit_threshold = int(math.ceil(height / 2))  # round up when dealing with odd numbers

    ones_per_column = np.count_nonzero(instructions_prepared, axis=0)
    column_thresholds = ones_per_column - most_common_bit_threshold  # positive value -> 1, negative value -> 0
    print(column_thresholds)
    gamma = np.where(column_thresholds >= 0, 1, 0)  # use >= to map equal number of occurance to 1 to keep values with a one when there is a tie
    return gamma

instructions = instructions_prepared.tolist()

for column in range(width):
    gamma = calculate_gamma(np.array(instructions))
    bit_criteria = gamma[column]
    print(f"Calculated gamma {gamma}, column {column}, using bit_criteria {bit_criteria}")

    instructions = [row for row in instructions if row[column] == bit_criteria]
    print(instructions)
    if len(instructions) == 1:
        print(f"Found rating {instructions}")
        break

oxygen_generator_rating = np.sum(exponent * np.array(instructions))
print(oxygen_generator_rating)

def calculate_epsilon(instructions_prepared):
    height, width = instructions_prepared.shape
    most_common_bit_threshold = int(math.ceil(height / 2))  # round up when dealing with odd numbers

    ones_per_column = np.count_nonzero(instructions_prepared, axis=0)
    column_thresholds = ones_per_column - most_common_bit_threshold  # positive value -> 1, negative value -> 0
    #TODO pick the value that occurs the least often 
    print("ones_per_column", ones_per_column, "column_thresholds", column_thresholds)
    #epsilon = np.where(column_thresholds <= 1, 0, 1)  # use < to map equal number of occurance to 0 to keep values with a 0 when there is a tie
    epsilon = np.where(ones_per_column < most_common_bit_threshold, 1, 0)
    return epsilon

instructions = instructions_prepared.tolist()
for column in range(width):
    epsilon = calculate_epsilon(np.array(instructions))
    bit_criteria = epsilon[column]
    print(f"Calculated epsilon {epsilon}, column {column}, using bit_criteria {bit_criteria}")

    instructions = [row for row in instructions if row[column] == bit_criteria]
    print(instructions)
    if len(instructions) == 1:
        print(f"Found rating {instructions}")
        break

co2_scrubber_rating = np.sum(exponent * np.array(instructions))
print(co2_scrubber_rating)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f"Calculated life_support_rating = {life_support_rating}")  # correct answer is 4790390