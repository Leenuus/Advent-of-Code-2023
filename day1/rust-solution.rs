use std::fs::read_to_string;

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let digits: Vec<_> = line
                .chars()
                .enumerate()
                .filter_map(|(idx, c)| {
                    c.to_digit(10).map(|d| (idx, d))
                })
                .collect();
            let d1 = digits[0].1;
            let d2 = digits[digits.len() - 1].1;
            d1 * 10 + d2
        })
        .sum()
}

#[test]
fn test_part1() {
    const TEST1: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
    let actual = part1(TEST1);
    let expect = 142;
    assert_eq!(actual, expect);
}

fn part2(input: &str) -> u32 {
    const WORDS: [&str; 9] = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let mut res = 0;
    for line in input.lines() {
        // find digits
        let mut digits: Vec<_> = line
            .chars()
            .enumerate()
            .filter_map(|(idx, c)| {
                c.to_digit(10).map(|d| (idx, d))
            })
            .collect();
        // println!("line: {line}");
        // println!("digits1: {digits:?}");
        // find words
        for (n, &word) in WORDS.iter().enumerate() {
            digits.extend(
                line.match_indices(word)
                    .map(|(idx, _)| (idx, (n + 1) as u32)),
            );
        }
        // println!("digits2: {digits:?}");
        digits.sort_by(|&(idx1, _), &(idx2, _)| idx1.cmp(&idx2));
        let d1 = digits[0].1;
        let d2 = digits[digits.len() - 1].1;
        res += d1 * 10 + d2;
    }
    res
}

#[test]
fn test_part2() {
    const TEST2: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";
    let actual = part2(TEST2);
    let expect = 281;
    assert_eq!(actual, expect);
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let path = if args.len() == 2 { &args[1]} else { "./input.txt" };
    let input = read_to_string(path).unwrap_or_else(
        |_|  panic!("Can't find path {path}") 
    );

    // part1
    let part1_res = part1(&input);
    println!("Part1: {part1_res}");

    // part2
    let part2_res = part2(&input);
    println!("Part2: {part2_res}");
}
