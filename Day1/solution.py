import re

digit_strings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def retrieve_digit(text: str) -> int:
    return int(text) if text.isdigit() else digit_strings[text]


def retrieve_calibration_value(calibration_input: str) -> int:
    digit_search = re.finditer(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", calibration_input.lower())
    match_list = [match.group(1) for match in digit_search]

    first_digit = retrieve_digit(match_list[0])
    last_digit = retrieve_digit(match_list[-1])

    return first_digit * 10 + last_digit


def sum_calibration_values(values: list[int]) -> int:
    return sum(values)


if __name__ == '__main__':
    calibration_document = "calibration_document.txt"

    with open(calibration_document, 'r') as document:
        calibration_values = list(map(retrieve_calibration_value, document))

    calibration_value_sum = sum_calibration_values(calibration_values)
    print(calibration_values)
    print(f"The sum of the calibration values is: {calibration_value_sum}")
