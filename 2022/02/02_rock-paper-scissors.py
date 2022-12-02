with open("input.txt") as f:
    parsed_input = f.read().splitlines()

print(parsed_input[:30])


mapping_opponent = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

mapping_for_me = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

mapping_strategy = {
    "X": "lost",
    "Y": "draw",
    "Z": "won"
}

# if opponent picks key, select value to win
winning_mapping = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

# if opponent picks key, select value to loose
loosing_mapping = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


score_mapping = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lost": 0,
    "draw": 3,
    "won": 6
}

def rock_paper_scissors_score(player1_pick, player2_pick):
    """
    Calculate score for player1

    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lost": 0,
    "draw": 3,
    "won": 6

    """
    result = score_mapping[player1_pick] - score_mapping[player2_pick]

    if result == 0:
        score = score_mapping["draw"]

    elif result == -2 or result == 1:
        score = score_mapping["won"]

    elif result == 2 or result == -1:
        score = score_mapping["lost"]

    return score_mapping[player1_pick] + score


def total_score_part1(parsed_input):
    total_score = 0

    for i in range(len(parsed_input)):
        round = parsed_input[i]
        opponent_pick, my_pick = round.split()
        opponent = mapping_opponent[opponent_pick]
        myself = mapping_for_me[my_pick]
        score = rock_paper_scissors_score(myself, opponent)
        total_score += score

    print("Part 1: What would your total score be if everything goes exactly according to your strategy guide?")
    print(total_score)

total_score_part1(parsed_input)


def follow_strategy(opponent, strategy):
    if strategy == "draw":
        my_pick = opponent

    elif strategy == "lost":
        my_pick =loosing_mapping[opponent]

    elif strategy == "won":
        my_pick = winning_mapping[opponent]

    score_by_game_strategy = score_mapping[strategy]
    score_by_picked_sign = score_mapping[my_pick]
    score = score_by_game_strategy + score_by_picked_sign
    return score


def score_part_2(parsed_input):
    total_score = 0

    for i in range(len(parsed_input)):
        round = parsed_input[i]
        opponent_pick, my_strategy = round.split()
        opponent = mapping_opponent[opponent_pick]
        strategy = mapping_strategy[my_strategy]
        score = follow_strategy(opponent, strategy)
        total_score += score

    print("Part 2: what would your total score be if everything goes exactly according to your strategy guide?")
    print(total_score)

score_part_2(parsed_input)

