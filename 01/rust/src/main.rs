pub fn main() {
    let elves = include_str!("../../input").split("\n\n");
    let mut calorie_totals = vec![];
    for elf in elves {
        let total_calories = elf
            .split('\n')
            .take_while(|l| !l.is_empty())
            .fold(0, |a, b| a + b.parse::<i32>().unwrap());
        calorie_totals.push(total_calories);
    }
    calorie_totals.sort_by(|a, b| b.cmp(a));
    println!("part 1: {}", calorie_totals[0]);
    println!("part 2: {}", calorie_totals[..3].iter().sum::<i32>());
}
