class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def is_intersecting(self, other) -> bool:
        return self.start < other.end and self.end > other.start

    def __str__(self):
        return f"({self.start}..{self.end})"

    def __repr__(self):
        return self.__str__()


class MapEntry:
    def __init__(self, destination: int, source: int, range_length: int):
        self.destination = destination
        self.source = source
        self.range_length = range_length


def parse_string_into_ints(string: str) -> list[int]:
    number_list = []
    number_strings = string.strip().split(' ')

    for string in number_strings:
        if string != '':
            number_list.append(int(string))

    return number_list


def parse_seed_ranges(line: str) -> list[Range]:
    string = line.split(':')[1]
    numbers = parse_string_into_ints(string)
    pairs = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]

    return [Range(pair[0], pair[0] + pair[1]) for pair in pairs]


def parse_map(lines: list[str], starting_index: int) -> list[MapEntry]:
    entries = []

    for index in range(starting_index, len(lines)):
        line = lines[index]

        if line == '\n':
            break

        numbers = parse_string_into_ints(line)
        entries.append(MapEntry(numbers[0], numbers[1], numbers[2]))

    return entries


def get_destinations_dict(map_entries: list[tuple[int, int, int]]) -> dict[int, int]:
    destinations_dict = {}

    for destination, source, range_length in map_entries:
        for offset in range(0, range_length):
            destinations_dict[source + offset] = destination + offset

    return destinations_dict


def get_destination_range(source_ranges: list[Range], map_entries: list[MapEntry]) -> list[Range]:
    ranges = []

    for map_entry in map_entries:
        entry_range = Range(map_entry.source, map_entry.source + map_entry.range_length)

        for source_range in source_ranges:
            if source_range.is_intersecting(entry_range):
                print(f"{source_range} intersects with {entry_range}")

                if source_range.start < entry_range.start:
                    start_destination = source_range.start
                else:
                    start_offset = source_range.start - map_entry.source
                    start_destination = map_entry.destination + start_offset

                if source_range.end > entry_range.end:
                    end_destination = source_range.end
                else:
                    end_offset = map_entry.range_length - ((map_entry.source + map_entry.range_length) - source_range.end)
                    end_destination = map_entry.destination + end_offset

                ranges.append(Range(start_destination, end_destination))

    return source_ranges if len(ranges) == 0 else ranges


def part_two(input_file_path: str) -> int:
    map_entries = []

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        seed_ranges = parse_seed_ranges(lines[0])

        for index, line in enumerate(lines):
            if "map" in line:
                map_entry = parse_map(lines, index + 1)
                map_entries.append(map_entry)

    location_numbers: list[int] = []
    ranges: list[Range] = []

    for seed_range in seed_ranges:
        destination_range = [seed_range]

        for index, map_entry in enumerate(map_entries):
            print("Operaiton")
            destination_range = get_destination_range(destination_range, map_entry)
            ranges += destination_range
            print("Destination:", destination_range)

        print("\n\nFinal Destination Range:", ranges)

        # location_numbers.append(destination_range)

    return min(list(map(lambda r: r.start, ranges)))


if __name__ == '__main__':
    part_two_answer = part_two(input_file_path="input.txt")
    print("Part two:", part_two_answer)
