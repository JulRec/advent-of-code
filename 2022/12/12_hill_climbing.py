import numpy as np

with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[0])

field = []

for line in parsed_input:
    letters = [letter for letter in line]
    field.append(letters)

print(field[0])
