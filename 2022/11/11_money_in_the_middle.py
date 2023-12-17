import numpy as np

with open("test_input.txt") as f:
    parsed_input = f.read().splitlines()


class Monkey:
    def __init__(
        self,
        items,
        worry_level,
        worry_level_multiplier,
        divisor,
        true_choice,
        false_choice,
    ):
        self.items = items
        # todo add worry level instruction
        self.worry_level = worry_level
        self.worry_level_multiplier = worry_level_multiplier
        self.divisor = divisor
        self.true_choice = true_choice
        self.false_choice = false_choice

    def update_worry_level(self):
        print(f"Monkey inspects an item with a worry level of {self.worry_level}.")
        self.worry_level *= self.worry_level_multiplier
        print(
            f"Worry level is multiplied by {self.worry_level_multiplier} to {self.worry_level}."
        )

    def get_next_monkey_for_item(self):
        item = self.items.pop(0)

        self.worry_level = np.floor(self.worry_level / 3)
        print(
            f"Monkey gets bored with item. Worry level is divided by 3 to {self.worry_level}."
        )

        if self.worry_level // self.divisor == 0:
            print(f"Current worry level is divisible by {self.divisor}.")
            monkey = self.true_choice

        else:
            print(f"Current worry level is not divisible by {self.divisor}.")
            monkey = self.false_choice

        print(f"Item with worry level {self.worry_level} is thrown to monkey {monkey}.")
        return item, monkey


def init_monkeys(parsed_input):
    monkeys = {}

    for i in range(0, len(parsed_input), 7):
        print(parsed_input[i])
        items = parsed_input[i + 1].split(":")[-1].split(",")
        items = [int(i) for i in items]
        print(items)
        worry_level_instruction = parsed_input[i + 2].split("=")[-1]
        print(worry_level_instruction)
        # worry_level_multiplier,
        # divisor,
        # true_choice,
        # false_choice

    return monkeys


init_monkeys(parsed_input)
