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
    let mut categories: Vec<Vec<MapEntry>> = Vec::new();

    for (index, line) in lines.iter().enumerate() {
        if line.contains("map") {
            let map_entry = parse_map_data(&lines, index + 1);
            categories.push(map_entry);
        }
    }

    return categories;
}

fn parse_string_to_numbers(line: &str) -> Vec<u32> {
    let mut number_list: Vec<u32> = Vec::new();
    let number_strings = line.trim().split(" ");

    for string in number_strings {
        if string == "" {
            continue;
        }

        let number = string
            .parse()
            .expect(&format!("String should be a number, got {string}"));

        number_list.push(number);
    }

    return number_list;
}

fn parse_map_data(lines: &Vec<&str>, initial_index: usize) -> Vec<MapEntry> {
    let mut entries: Vec<MapEntry> = Vec::new();

    for index in initial_index..lines.len() {
        let line = lines[index];

        if line == "" {
            break;
        }

        let numbers = parse_string_to_numbers(line);
        let map_entry = MapEntry {
            destination: numbers[0],
            source: numbers[1],
            range_length: numbers[2],
        };
        entries.push(map_entry);
    }

    return entries;
}

fn retrieve_location(seed_number: u32, categories: &Vec<Vec<MapEntry>>) -> u32 {
    let mut destination = seed_number;

    for map_entries in categories {
        destination = get_destination_number(destination, map_entries);
    }

    return destination;
}

fn get_destination_number(source: u32, map_entries: &Vec<MapEntry>) -> u32 {
    for map_entry in map_entries {
        if source > map_entry.source && source < map_entry.source + map_entry.range_length {
            return map_entry.destination + (source - map_entry.source);
        }
    }

    return source;
}
