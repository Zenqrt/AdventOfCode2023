def parse_number_string(number_string: str) -> list[int]:
    number_list = []

    for string in number_string.strip().split(' '):
        if string != '':
            number_list.append(int(string))

    return number_list


def parse_card_numbers(line: str) -> tuple[list[int], list[int]]:
    numbers_split_string = line.split(':')[1].split("|")  # Gets the two string of numbers

    return parse_number_string(numbers_split_string[0]), parse_number_string(numbers_split_string[1])


def part_one(input_file_path: str) -> int:
    # create total points worth int
    # read input file and convert it into array (you don't need the "Card 1:" info)
    #
    # for each card:
    # create two arrays(lists): winning numbers and card numbers
    # create points worth int
    # for each card number, check if card number is present in winning numbers.
    # if so, if points worth is 0, set to 1, else double the number
    # at end of loop, add points worth to total points worth

    total_points_worth = 0

    with open(input_file_path, 'r') as file:
        card_array = [parse_card_numbers(line) for line in file.readlines()]

    for winning_numbers, card_numbers in card_array:
        points_worth = 0

        for card_number in card_numbers:
            if card_number in winning_numbers:
                points_worth = 1 if points_worth == 0 else points_worth * 2

        total_points_worth += points_worth

    return total_points_worth


if __name__ == '__main__':
    part_one_answer = part_one("input.txt")
    print("Part one:", part_one_answer)
