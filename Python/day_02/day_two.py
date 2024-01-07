def _extract_game_info(string: str) -> [str]:
    split_string = string.split(":")
    return split_string[1].strip().split(";")


def _is_game_possible(round_strings: [str], expected_reds: int, expected_greens: int, expected_blues: int) -> bool:
    for round_string in round_strings:
        cube_strings = round_string.split(",")

        for cube_string in cube_strings:
            cube_split_string = cube_string.strip().split(" ")
            cube_amount = int(cube_split_string[0])
            cube_color = cube_split_string[1]

            if (cube_color == 'red' and cube_amount > expected_reds) or \
                    (cube_color == 'green' and cube_amount > expected_greens) or \
                    (cube_color == 'blue' and cube_amount > expected_blues):
                return False

    return True


def part_one(input_file_path: str, expected_reds: int, expected_greens: int, expected_blues: int) -> int:
    total_game_ids = 0

    with open(input_file_path, 'r') as file:
        for line in file.readlines():
            round_strings = _split_string_into_rounds(line)
            game_id = int(split_string[0].split(" ")[1])
            possible_game = _is_game_possible(round_strings, expected_reds, expected_greens, expected_blues)

            if possible_game:
                total_game_ids += game_id

    return total_game_ids


def _should_be_minimum(color_amount: int, current_min: int) -> bool:
    return current_min is None or color_amount > current_min


def _retrieve_minimum_colors_of_rounds(round_strings: [str]) -> (int, int, int):
    red = None
    green = None
    blue = None

    for round_string in round_strings:
        cube_strings = round_string.split(',')

        for cube_string in cube_strings:
            cube_split_string = cube_string.strip().split(" ")
            cube_amount = int(cube_split_string[0])
            cube_color = cube_split_string[1]

            if cube_color == 'red' and _should_be_minimum(cube_amount, red):
                red = cube_amount
            elif cube_color == 'green' and _should_be_minimum(cube_amount, green):
                green = cube_amount
            elif cube_color == 'blue' and _should_be_minimum(cube_amount, blue):
                blue = cube_amount

    return red, green, blue


def part_two(input_file_path: str) -> int:
    power_set_sum = 0

    with open(input_file_path, 'r') as file:
        for line in file.readlines():
            split_string = line.split(":")
            round_strings = split_string[1].strip().split(";")

            min_red, min_green, min_blue = _retrieve_minimum_colors_of_rounds(round_strings)

            power_set = min_red * min_green * min_blue
            power_set_sum += power_set

    return power_set_sum


if __name__ == '__main__':
    input_file = "input.txt"

    total_game_ids = part_one(input_file, expected_reds=12, expected_greens=13, expected_blues=14)
    print(f"Part one: {total_game_ids}")

    total_power_set = part_two(input_file)
    print(f"Part two: {total_power_set}")
