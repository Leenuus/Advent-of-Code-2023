"""
[2023 day1 advent of code](https://adventofcode.com/2023/day/1)
Python solution
"""

import re
from operator import itemgetter
DEBUG = True

TEST1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def tests():
    print(part1(TEST1))
    print(part2(TEST2))


def findIterOverlapped(pattern: re.Pattern | str, string: str):
    res = []
    cur = 0
    while len(string):
        if m := re.search(pattern, string):
            # save the position in origin string and match string
            res.append((cur + m.start(), m.group()))
            # keep track of current pos in origin string
            cur += m.start() + 1
            # search from one character after the match's start
            string = string[m.start() + 1:]
        else:
            break
    return res if res else None

def part1(input: str):
    """simply find all digits and compose the first and the last one"""
    res = 0
    for line in input.splitlines():
        digits = tuple(map(int, re.findall(r'\d', line)))
        res += digits[0] * 10 + digits[len(digits) - 1]
    return res

def part2(input: str):
    res = 0
    pattern = re.compile(r'[\d]')
    word2digit = ['one','two','three','four','five','six','seven','eight','nine']
    pattern2 = re.compile('|'.join(word2digit))
    
    for line in input.splitlines():
        # find all digits written as digit
        nums = []
        if digits := re.finditer(pattern, line):
            nums.extend((d.start(), int(d.group())) for d in digits)

        # find all digits written in words
        # it may overlap so re.finditer doesn't work
        if digits := findIterOverlapped(pattern2, line):
            nums.extend((d[0], word2digit.index(d[1]) + 1) for d in digits)
        # print('nums:', nums)
        nums.sort(key=itemgetter(0))
        print('nums:', nums)
        res += nums[0][1] * 10 + nums[len(nums) - 1][1]
    return res

def main():
    if DEBUG:
        tests()
    else:
        with open('input.txt', 'r') as f:
            input = f.read()
        res1 = part1(input)
        res2 = part2(input)

        print('Part1:', res1)
        print('Part2:', res2)


if __name__ == '__main__':
    main()