use std::{fs::read_to_string, ops::Range};
use regex::Regex;

#[allow(unused)]
const TEST: &str = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";

#[derive(Debug)]
struct Num{
    num: u32,
    row: usize,
    range: Range<usize>
}

#[derive(Debug)]
struct Symbols{
    s: String,
    row: usize,
    col: usize
}

fn parse(input: &str) -> (Vec<Num>, Vec<Symbols>){
    let num_pat = Regex::new(r"\d+").unwrap();
    let sym_pat = Regex::new(r"[^\d.]").unwrap();
    let mut nums = vec![];
    let mut symbols = vec![];

    for (row, line) in input.lines().enumerate(){
        nums.extend(
            num_pat.find_iter(line)
            .map(|m| {
                let num = m.as_str().parse::<u32>().unwrap();
                let range = m.range();
                Num {row, num, range}
        }));
        symbols.extend(
            sym_pat.find_iter(line)
            .map(|m| {
                let s = String::from(m.as_str());
                let col = m.start();
                Symbols { s, row, col}
            })
        )
    }

    (nums, symbols)
}

#[test]
fn test_parse() {
    let res = parse(TEST);
    println!("Result: {res:?}");
}

fn part1(input: &str) -> u32 {
    let (nums, symbols) = parse(input);
    let mut res = 0;
    for num in nums{
        let start = num.range.start.saturating_sub(1);
        for s in symbols.iter(){
            if (num.row as i64 - s.row as i64).abs() <= 1{
                if start <= s.col && s.col < num.range.end + 1{
                    res += num.num;
                    break;
                }
            }
        }
    }
    res
}

#[test]
fn test_part1() {
    const TEST1: &str = TEST;
    let actual = part1(TEST1);
    let expect = 4361;
    assert_eq!(actual, expect);
}

fn part2(input: &str) -> u32 {
    let (nums, symbols) = parse(input);
    let gears: Vec<_> = symbols.into_iter().filter(|s| s.s == "*").collect();
    let mut res = 0;
    for gear in gears{
        let mut count = 0;
        let mut ratio = 1;
        for num in nums.iter(){
            let start = num.range.start.saturating_sub(1);
            if (num.row as i64 - gear.row as i64).abs() <= 1{
                if start <= gear.col && gear.col < num.range.end + 1{
                    count += 1;
                    ratio *= num.num;
                }
            }
        }
        res += if count == 2 { ratio } else { 0 };
    }
    res
}

#[test]
fn test_part2() {
    const TEST2: &str = TEST;
    let actual = part2(TEST2);
    let expect = 467835;
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
