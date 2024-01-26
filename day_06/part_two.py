def calculate_distance(hold_time: int, race_time: int) -> int:
    speed = hold_time
    remaining_time = race_time - hold_time

    return speed * remaining_time


def parse_numbers(line: str) -> int:
    split_str = line.split()
    number_str = ''.join(split_str[i] for i in range(1, len(split_str)))

    return int(number_str)


def part_two(input_file_path: str) -> int:
    with open(input_file_path) as file:
        lines = file.readlines()

        race_time = parse_numbers(lines[0])
        record_distance = parse_numbers(lines[1])

    possible_wins = 0

    for hold_time in range(0, race_time + 1):
        distance = calculate_distance(hold_time, race_time)

        if distance > record_distance:
            possible_wins += 1

    return possible_wins


if __name__ == "__main__":
    part_two_answer = part_two("input.txt")
    print("Part one:", part_two_answer)
