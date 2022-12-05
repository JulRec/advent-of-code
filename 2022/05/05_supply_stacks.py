with open("input.txt") as f:
    parsed_input = f.read().splitlines()

parsed_state = parsed_input[:8]
parsed_steps = parsed_input[10:]
cleaned_steps = [(step.split()[1], step.split()[3], step.split()[5]) for step in parsed_steps]


def setup_initial_state(parsed_state):
    initial_state = {str(i): [] for i in range(1, 10)}

    for row in reversed(parsed_state):
        n = 4
        split_row = [row[i:i+n] for i in range(0, len(row), n)]
        clean_row = [row.strip() for row in split_row]
        for i in range(len(clean_row)):
            container = clean_row[i]

            if (len(container)) > 0:
                container_letter = container[1]
                initial_state[str(i+1)].append(container_letter)

            else:
                #print(f"Skipped {container}.")
                pass

    return initial_state


def part_one(initial_state, steps):
    # index 0 = bottom container, highest index = top container
    for step in steps:
        # move x from y to z
        mov, fro, to = step
        for _ in range(int(mov)):
            container = initial_state[fro].pop()
            initial_state[to].append(container)

    print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
    top_containers = [crates[-1] for _, crates in initial_state.items()]
    print("".join(top_containers))


def part_two(initial_state, steps):
    # index 0 = bottom container, highest index = top container
    for step in steps:
        # move x from y to z
        mov, fro, to = step
        mov = int(mov)
        containers = initial_state[fro]
        staying_containers = containers[:-mov]
        moving_containers = containers[-mov:]
        initial_state[fro] = staying_containers
        initial_state[to].extend(moving_containers)


    print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
    top_containers = [crates[-1] for _, crates in initial_state.items()]
    print("".join(top_containers))


state = setup_initial_state(parsed_state)
part_one(state, cleaned_steps)

state = setup_initial_state(parsed_state)
part_two(state, cleaned_steps)
