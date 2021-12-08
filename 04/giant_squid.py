import numpy as np

with open("input.txt") as f:
    instructions_raw = f.read().split("\n\n")

numbers_raw = instructions_raw[0]
numbers = [int(number) for number in numbers_raw.split(",")]
print(numbers)


class Board:
    def __init__(self, board):
        self.board = board
        self.win = False
        self.score = 0

    def update_called_numbers(self, called_number):
        self.board = np.ma.masked_where(self.board == called_number, self.board)

    def check_win_condition(self):
        horizontal = np.ma.getmask(np.sum(self.board, axis=0))
        vertical = np.ma.getmask(np.sum(self.board, axis=1))
        if np.sum(horizontal) or np.sum(vertical):
            self.win = True

    def calculate_score(self):
        self.score = np.sum(self.board)


all_boards = []
for i in range(1, len(instructions_raw)):
    instruction = instructions_raw[i]
    rows = instruction.splitlines()
    cols = [col.split() for col in rows]
    board = np.array(cols).astype(int)
    all_boards.append(Board(board))

# part 1
game_over = False
for number in numbers:
    for board in all_boards:
        board.update_called_numbers(number)
        board.check_win_condition()
        if board.win:
            board.calculate_score()
            sum_of_unmarked_numbers = board.score
            score = number * sum_of_unmarked_numbers
            print(f"Achieved final score {score} with number {number} x {sum_of_unmarked_numbers}")
            game_over = True
            break
    if game_over:
        break

# part 2
winner_scores = []
for number in numbers:
    for board in all_boards:
        if not board.win:
            board.update_called_numbers(number)
            board.check_win_condition()
            if board.win:
                board.calculate_score()
                sum_of_unmarked_numbers = board.score
                score = number * sum_of_unmarked_numbers
                print(f"Achieved final score {score} with number {number} x {sum_of_unmarked_numbers}")
                winner_scores.append(score)

print(f"We loose when we pick the board with score {winner_scores[-1]}")
