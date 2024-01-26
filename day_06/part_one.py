def calculate_distance(hold_time: int, race_time: int) -> int:
    speed = hold_time
    remaining_time = race_time - hold_time

    distance = speed * remaining_time
    print(f"Distance: {distance}")
    return distance


def parse_numbers(line: str) -> list[int]:
    split_str = line.split()

    return [int(split_str[i]) for i in range(1, len(split_str))]


def part_one(input_file_path: str) -> int:
    wins_product = 1
    times = []
    distances = []

    with open(input_file_path) as file:
        lines = file.readlines()

        times = parse_numbers(lines[0])
        distances = parse_numbers(lines[1])

    for race_time, record_distance in zip(times, distances):
        possible_wins = 0

        for hold_time in range(0, race_time + 1):
            distance = calculate_distance(hold_time, race_time)

            if distance > record_distance:
                possible_wins += 1

        wins_product *= possible_wins

    return wins_product


if __name__ == "__main__":
    part_one_answer = part_one("input.txt")
    print("Part one:", part_one_answer)
