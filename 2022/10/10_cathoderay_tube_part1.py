with open("input.txt") as f:
    parsed_input = f.read().splitlines()


test = ["noop", "addx 3", "addx -5"]


X = 1
circles = 0
relevant_circles = [20, 60, 100, 140, 180, 220]
interesting_signal_strenghts = []

for line in parsed_input:
    # print("line", line, ", circles", circles,", X", X)
    if line == "noop":
        # wait for one circle
        circles += 1
        # print("line", line, ", circles", circles, ", X", X)
        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            print(
                "circle",
                circles,
                "has an X value of",
                X,
                "resulting in",
                signal_strength,
            )

    else:
        value = int(line.split()[1])
        circles += 1
        # print("line", line, ", circles", circles, ", X", X)

        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            print(
                "circle",
                circles,
                "has an X value of",
                X,
                "resulting in",
                signal_strength,
            )

        circles += 1
        # print("line", line, ", circles", circles, ", X", X)

        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            print(
                "circle",
                circles,
                "has an X value of",
                X,
                "resulting in",
                signal_strength,
            )

        X += value

print(
    "Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?"
)
print(sum(interesting_signal_strenghts))
