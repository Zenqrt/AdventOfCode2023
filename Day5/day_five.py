def parse_string_into_ints(string: str) -> list[int]:
    number_list = []
    number_strings = string.strip().split(' ')

    for string in number_strings:
        if string != '':
            number_list.append(int(string))

    return number_list


def parse_seed_numbers(line: str) -> list[int]:
    string = line.split(':')[1]
    return parse_string_into_ints(string)


def parse_map(lines: list[str], starting_index: int) -> list[tuple[int, int, int]]:
    entries = []

    for index in range(starting_index, len(lines)):
        line = lines[index]

        if line == '\n':
            break

        numbers = parse_string_into_ints(line)
        entries.append((numbers[0], numbers[1], numbers[2]))

    return entries


def get_destinations_dict(map_entries: list[tuple[int, int, int]]) -> dict[int, int]:
    destinations_dict = {}

    for destination, source, range_length in map_entries:
        for offset in range(0, range_length):
            destinations_dict[source + offset] = destination + offset

    return destinations_dict


def get_destination_number(source_number: int, map_entries: list[tuple[int, int, int]]) -> int:
    for map_entry in map_entries:
        destination, source, range_length = map_entry

        if source < source_number < source + range_length:
            return destination + (source_number - source)

    return source_number


def part_one(input_file_path: str) -> int:
    map_entries = []

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        seed_numbers = parse_seed_numbers(lines[0])

        for index, line in enumerate(lines):
            if "map" in line:
                map_entry = parse_map(lines, index + 1)
                map_entries.append(map_entry)

    location_numbers: list[int] = []

    for seed_number in seed_numbers:
        destination_number = seed_number

        for map_entry in map_entries:
            destination_number = get_destination_number(destination_number, map_entry)

        location_numbers.append(destination_number)

    return min(location_numbers)


if __name__ == '__main__':
    part_one_answer = part_one(input_file_path="input.txt")
    print("Part one:", part_one_answer)
