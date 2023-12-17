import math as m
import re

with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:3])

rows = len(parsed_input)
columns = len(parsed_input[0])

chars = {
    (r, c): []
    for r in range(rows)
    for c in range(columns)
    if parsed_input[r][c] not in "01234566789."
}
print(chars)

for r, row in enumerate(parsed_input):
    print(r, row)
    for match in re.finditer(r"\d+", row):
        # use r in front of the string (= raw string) to state that \ is not meant as escape character
        # \d matches any digit from 0 to 9 in target string
        # the + indicates that number can contain at minimum one digit
        edge = {
            (r, c)
            for r in (r - 1, r, r + 1)
            for c in range(match.start() - 1, match.end() + 1)
        }

        for coordinate in edge:
            if coordinate in chars.keys():
                chars[coordinate].append(int(match.group()))

print(
    sum(sum(p) for p in chars.values()),
    sum(m.prod(p) for p in chars.values() if len(p) == 2),
)
