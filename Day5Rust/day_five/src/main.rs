use std::fs;

struct ParsedDataResult {
    seed_numbers: Vec<u32>,
    categories: Vec<Vec<MapEntry>>,
}

struct MapEntry {
    destination: u32,
    source: u32,
    range_length: u32,
}

fn main() {
    let part_one_answer = part_one("src/res/input.txt");
    println!("Part one: {part_one_answer}");
}

fn part_one(file_path: &str) -> u32 {
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

fn retrieve_seed_numbers(lines: &Vec<&str>) -> Vec<u32> {
    let strings: Vec<&str> = lines[0].split(":").collect();
    return parse_string_to_numbers(strings[1]);
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

fn retrieve_location(seed_number: u32, categories: &Vec<Vec<MapEntry>>) -> u32 {
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
