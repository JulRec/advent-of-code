with open("test_input.txt") as f:
    parsed_input = f.read().splitlines()


def is_sprite_visible(circle, x):
    if circle in [x - 1, x, x + 1]:
        return True

    return False


def update_screen(screen, circle):
    screen[circle] = "#"
    return screen


X = 1
circles = 0
relevant_circles = [20, 60, 100, 140, 180, 220]
interesting_signal_strenghts = []
screen = ["." for i in range(40)]

for line in parsed_input:
    # print("line", line, ", circles", circles,", X", X)
    if line == "noop":
        # wait for one circle
        circles += 1

        # print("line", line, ", circles", circles, ", X", X)
        # screen_temp = ["." for i in range(40)]
        # screen_temp[X-1] = "#"
        # screen_temp[X] = "#"
        # screen_temp[X+1] = "#"
        # print(screen_temp)

        if is_sprite_visible(circles, X):
            screen = update_screen(screen, circles)

        if circles % 40 == 0:
            print(screen)
            # reset screen and circles for next circle
            screen = ["." for i in range(40)]
            # circles = 0

        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            # print("circle", circles, "has an X value of", X, "resulting in", signal_strength)

    else:
        value = int(line.split()[1])
        circles += 1

        # print("line", line, ", circles", circles, ", X", X)
        # screen_temp = ["." for i in range(40)]
        # screen_temp[X-1] = "#"
        # screen_temp[X] = "#"
        # screen_temp[X+1] = "#"
        # print(screen_temp)

        if is_sprite_visible(circles, X):
            screen = update_screen(screen, circles)

        if circles % 40 == 0:
            print(screen)
            # reset screen and circles for next circle
            screen = ["." for i in range(40)]
            # circles = 0

        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            # print("circle", circles, "has an X value of", X, "resulting in", signal_strength)

        circles += 1

        # print("line", line, ", circles", circles, ", X", X)
        # screen_temp = ["." for i in range(40)]
        # screen_temp[X-1] = "#"
        # screen_temp[X] = "#"
        # screen_temp[X+1] = "#"
        # print(screen_temp)

        if is_sprite_visible(circles, X):
            screen = update_screen(screen, circles)

        if circles % 40 == 0:
            print(screen)
            # reset screen and circles for next circle
            screen = ["." for i in range(40)]
            # circles = 0

        if circles in relevant_circles:
            signal_strength = circles * X
            interesting_signal_strenghts.append(signal_strength)
            # print("circle", circles, "has an X value of", X, "resulting in", signal_strength)

        X += value

print(
    "Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?"
)
print(sum(interesting_signal_strenghts))


print(50 % 40)
