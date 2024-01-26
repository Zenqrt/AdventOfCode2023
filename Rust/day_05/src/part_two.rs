use std::fs;

struct ParsedDataResult {
    seed_numbers: Vec<NumberRange>,
    categories: Vec<Vec<MapEntry>>,
}

struct MapEntry {
    destination: u32,
    source: NumberRange,
    range_length: u32,
}

struct NumberRange {
    initial_num: u32,
    num_range: u32,
}

pub fn part_two(file_path: &str) -> u32 {
    let parsed_data = load_data(file_path);
    let locations = parsed_data
        .seed_numbers
        .iter()
        .map(|seed_number| retrieve_location(*seed_number, &parsed_data.categories));

    let min = locations
        .min()
        .expect("Should be able to find minimum value");

    return min;
}

fn load_data(file_path: &str) -> ParsedDataResult {
    let lines = fs::read_to_string(file_path).expect("Should be able to read file");
    let lines: Vec<&str> = lines.lines().collect();

    return ParsedDataResult {
        seed_numbers: retrieve_seed_numbers(&lines),
        categories: retrieve_categories(&lines),
    };
}

fn retrieve_seed_numbers(lines: &Vec<&str>) -> Vec<NumberRange> {
    let strings: Vec<&str> = lines[0].split(":").collect();
    let numbers = parse_string_to_numbers(strings[1]);

    let number_pairs = {
        let mut list: Vec<NumberRange> = Vec::new();

        for index in (0..numbers.len()).step_by(2) {
            list.push(NumberRange {
                initial_num: numbers[index],
                num_range: numbers[index + 1],
            });
        }

        list
    };

    return number_pairs;
}

fn retrieve_categories(lines: &Vec<&str>) -> Vec<Vec<MapEntry>> {
    lines
        .iter()
        .enumerate()
        .filter(|(_, line)| line.contains("map"))
        .map(|(index, _)| parse_map_data(&lines, index + 1))
        .collect()
}

fn parse_string_to_numbers(line: &str) -> Vec<u32> {
    line.trim()
        .split_whitespace()
        .filter_map(|string| string.parse().ok())
        .collect()
}

fn parse_map_data(lines: &Vec<&str>, initial_index: usize) -> Vec<MapEntry> {
    lines[initial_index..]
        .iter()
        .take_while(|line| !line.is_empty())
        .map(|line| {
            let numbers = parse_string_to_numbers(line);
            MapEntry {
                destination: numbers[0],
                source: numbers[1],
                range_length: numbers[2],
            }
        })
        .collect()
}

fn retrieve_location(seed_number: NumberRange, categories: &Vec<Vec<MapEntry>>) -> u32 {
    categories.iter().fold(seed_number, |dest, map_entries| {
        get_destination_number(dest, map_entries)
    })
}

fn get_destination_number(source: u32, map_entries: &Vec<MapEntry>) -> u32 {
    map_entries
        .iter()
        .find(|map_entry| {
            source > map_entry.source && source < map_entry.source + map_entry.range_length
        })
        .map_or(source, |map_entry| {
            map_entry.destination + (source - map_entry.source)
        })
}

#[cfg(test)]
mod tests {
    use super::part_two;

    const FILE_PATH: &str = "resources/test_input.txt";

    #[test]
    fn test_part_two() {
        let expected = 46;
        let actual = part_two(FILE_PATH);

        assert_eq!(expected, actual);
    }
}
