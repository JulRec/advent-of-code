with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:3])

test_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

cards = {}
for line in parsed_input:
    card, numbers = line.split(":")
    card_id = int(card.split()[-1])
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = {int(number) for number in winning_numbers.split()}
    my_numbers = {int(number) for number in my_numbers.split()}
    print(winning_numbers, my_numbers)
    common_numbers = winning_numbers.intersection(my_numbers)
    print(common_numbers)
    cards[card_id] = list(common_numbers)


scored_points = []
for card_id, common_numbers in cards.items():
    if common_numbers:
        score = 2 ** (len(common_numbers) - 1)
        scored_points.append(score)

result = sum(scored_points)
print("Points worth in total", result)

number_of_cards = {card: 1 for card in cards}
for card_id, common_numbers in cards.items():
    bonus_cards = range(1, len(common_numbers) + 1)
    for i in bonus_cards:
        bonus_card_id = card_id + i
        # multiply by number of cards existing for actual card
        number_of_cards[bonus_card_id] += 1 * number_of_cards[card_id]

print(number_of_cards)
total_scratchcards = sum(number_of_cards.values())
print("Total scractchcards", total_scratchcards)
