def is_starting_digit(line: list[str], column_index: int) -> bool:
    return (line[column_index].isnumeric() and column_index == 0) or (line[column_index].isnumeric() and not line[column_index - 1].isnumeric())


def get_digit_string(line: list[str], starting_index: int) -> str:
    digit_string = ""
    line_length = len(line)

    for index in range(starting_index, line_length):
        digit_string += line[index]

        next_index = index + 1
        if next_index >= line_length or not line[next_index].isnumeric():
            return digit_string


def parse_digit_string(digit_string: str) -> tuple[int, int]:
    return int(digit_string), len(digit_string)


def has_symbol(input_array: list[list[str]], row_index: int, column_index: int, digit_count: int) -> bool:
    for y in range(-1, 2):
        look_y = row_index + y

        if look_y >= len(input_array) or look_y < 0:
            continue

        for x in range(-1, digit_count + 1):
            look_x = column_index + x

            if look_x >= len(input_array[look_y]) or look_x < 0:
                continue

            character = input_array[look_y][look_x]

            if not character.isdigit() and character != '.':  # if symbol
                return True
    return False


def part_two(input_file_path: str) -> int:
    # check if digit is the start of a number (no digits behind it)
    # if so, locate digit string in line from starting digit index
    # parse into number and digit count
    # check for symbol around each number using the digit count as size and current position (row, column)
    # If symbol found, add to sum digit, else do nothing and continue.
    sum_digits = 0

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        input_array = [[char for char in line.removesuffix("\n")] for line in lines]

        for row_index, line in enumerate(input_array):
            for column_index, char in enumerate(line):
                if is_starting_digit(line, column_index):
                    digit_string = get_digit_string(line, column_index)
                    full_number, digit_count = parse_digit_string(digit_string)

                    if has_symbol(input_array, row_index, column_index, digit_count):
                        sum_digits += full_number

    return sum_digits


if __name__ == '__main__':
    part_two_answer = part_two("input.txt")
    print("Part two:", part_two_answer)
