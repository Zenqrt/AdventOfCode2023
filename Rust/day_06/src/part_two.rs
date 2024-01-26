pub fn part_two(input_file_path: &str) -> usize {
    let lines = std::fs::read_to_string(input_file_path).expect("Failed to read file");
    let lines = lines.lines();

    let race_time = parse_numbers(lines.clone().nth(0).unwrap());
    let record_distance = parse_numbers(lines.last().unwrap());

    (0..=race_time).into_iter()
        .map(|hold_time| {calculate_distance(&hold_time, &race_time)})
        .filter(|distance| {*distance > record_distance})
        .count()
}

fn parse_numbers(line: &str) -> usize {
    let split_string = line.split_whitespace();

    split_string.skip(1)
        .map(|string| string.to_string())
        .collect::<Vec<String>>()
        .join::<&str>("")
        .parse::<usize>()
        .unwrap()
}

fn calculate_distance(hold_time: &usize, race_time: &usize) -> usize {
    let distance = hold_time * (race_time - hold_time);
    distance
} 

#[cfg(test)]
mod tests {
    use super::part_two;


    #[test]
    fn test_part_two() {
        let expected = 71503;
        let actual = part_two("test_input.txt");

        assert_eq!(expected, actual);
    }
}
