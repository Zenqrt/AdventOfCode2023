use part_one::part_one;
use part_two::part_two;

mod part_one;
mod part_two;

fn main() {
    let part_one_answer = part_one("input.txt");
    let part_two_answer = part_two("input.txt");

    println!("Part one: {part_one_answer}");
    println!("Part two: {part_two_answer}");
}


