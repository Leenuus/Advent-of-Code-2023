"""
[2023 day{{day}} advent of code](https://adventofcode.com/2023/day/{{day}})
Python solution
"""

PRODUCTION = False
DEBUG = True
INPUT_PATH = "./input.txt"

TEST = """"""

def tests():
    print(part1(TEST))
    print(part2(TEST))


def part1(input: str):
    """"""
    res = 0
    return res

def part2(input: str):
    """"""
    res = 0
    return res

def main():
    if DEBUG:
        tests()
    if PRODUCTION:
        with open(INPUT_PATH, 'r') as f:
            input = f.read()
        res1 = part1(input)
        res2 = part2(input)

        print('Part1:', res1)
        print('Part2:', res2)


if __name__ == '__main__':
    main()
