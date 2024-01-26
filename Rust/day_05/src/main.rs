use part_one::part_one;

use crate::part_two::part_two;

mod part_one;
mod part_two;

fn main() {
    let path = "resources/input.txt";

    let part_one_answer = part_one(path);
    println!("Part one: {part_one_answer}");

    let part_two_answer = part_two(path);
    println!("Part two: {part_two_answer}");
}
