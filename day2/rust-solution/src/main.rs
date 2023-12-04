use std::fs::read_to_string;
use regex::Regex;

#[allow(unused)]
const TEST: &str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

struct Colors{
    red: u32,
    green: u32,
    blue: u32
}

fn parse_line(line: &str) -> Colors{
    let (mut red, mut green, mut blue) = (0, 0, 0);
    let bl_pat = Regex::new(r"(\d+) blue").unwrap();
    let re_pat = Regex::new(r"(\d+) red").unwrap();
    let gr_pat = Regex::new(r"(\d+) green").unwrap();
    for res in bl_pat.captures_iter(line){
        let a = res.get(1).unwrap().as_str().parse::<u32>().unwrap();
        blue = std::cmp::max(a, blue);
    }
    for res in gr_pat.captures_iter(line){
        let a = res.get(1).unwrap().as_str().parse::<u32>().unwrap();
        green = std::cmp::max(a, green);
    }
    for res in re_pat.captures_iter(line){
        let a = res.get(1).unwrap().as_str().parse::<u32>().unwrap();
        red = std::cmp::max(a, red);
    }
    Colors {red, green, blue}
}

fn part1(input: &str) -> usize {
    const RED: u32 = 12;
    const GREEN: u32 = 13;
    const BLUE: u32 = 14;
    input.lines()
    .map(parse_line)
    .enumerate()
    .filter(
        |(_, colors)| 
        colors.blue <= BLUE && colors.red <= RED && colors.green <= GREEN
        )
    .map(|(idx, _)| idx + 1)
    .sum()
}

#[test]
fn test_part1() {
    const TEST1: &str = TEST;
    let actual = part1(TEST1);
    let expect = 8;
    assert_eq!(actual, expect);
}

fn part2(input: &str) -> u32 {
    input.lines()
    .map(parse_line)
    .map(|Colors { red, green, blue}| red * green * blue)
    .sum()
}

#[test]
fn test_part2() {
    const TEST2: &str = TEST;
    let actual = part2(TEST2);
    let expect = 2286;
    assert_eq!(actual, expect);
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let path = if args.len() == 2 { &args[1]} else { "../input.txt" };
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