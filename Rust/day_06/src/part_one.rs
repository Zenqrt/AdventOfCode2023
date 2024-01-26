pub fn part_one(input_file_path: &str) -> usize {
    let lines = std::fs::read_to_string(input_file_path).expect("Failed to read file");
    let lines = lines.lines();

    let race_times = parse_numbers(lines.clone().nth(0).unwrap());
    let record_distances = parse_numbers(lines.last().unwrap());

    race_times.into_iter()
        .zip(record_distances.into_iter())
        .map(|(race_time, record_distance)| {
            (0..=race_time).into_iter()
                .map(|hold_time| {calculate_distance(&hold_time, &race_time)})
                .filter(|distance| {*distance > record_distance})
                .count()
        })
        .product()
}

fn parse_numbers(line: &str) -> Vec<u32> {
    let split_string = line.split_whitespace();

    split_string.into_iter().skip(1)
        .map(|string| string.parse::<u32>().expect("Failed to parse string to int"))
        .collect()
}

fn calculate_distance(hold_time: &u32, race_time: &u32) -> u32 {
    let distance = hold_time * (race_time - hold_time);
    distance
} 

#[cfg(test)]
mod tests {
    use super::part_one;


    #[test]
    fn test_part_one() {
        let expected = 288;
        let actual = part_one("test_input.txt");

        assert_eq!(expected, actual);
    }
}
