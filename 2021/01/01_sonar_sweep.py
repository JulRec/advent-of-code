with open("input.txt") as f:
    measurements_raw = f.read().splitlines()

measurements_prepared = [int(measurement) for measurement in measurements_raw]
print(f"Found {len(measurements_prepared)} measurements.")


# part 1 - detect one increase, right answer = 1624
def calculate_measurement_increments(measurements):
    larger_measurements = 0

    for i in range(len(measurements)-1):
        if measurements[i] < measurements[i+1]:
            larger_measurements += 1

    return larger_measurements


print(f"Solution part 1: {calculate_measurement_increments(measurements_prepared)}")

# part 2 - detect increase over three values, right answer = 1653
measurements_over_3_values = [sum(measurements_prepared[i:i + 3]) for i in range(len(measurements_prepared) - 2)]
print(f"Solution part 2: {calculate_measurement_increments(measurements_over_3_values)}")
