"""
[2023 day9 advent of code](https://adventofcode.com/2023/day/9)
Python solution
"""

import re
from typing import Iterable


PRODUCTION = True
DEBUG = True
INPUT_PATH = "./input.txt"

TEST = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def parse(input: str):
    # Don't forget there are negative numbers in input file but not in test cases given
    pat = re.compile(r'-?\d+')
    return tuple(tuple(int(d) for d in pat.findall(line)) for line in input.splitlines())

def partition(seq: Iterable, length: int = 1, step: int = 1):
    """divide `seq` into pairs"""
    res = []
    seq = tuple(seq)
    for i in range(0, len(seq) - 1, step):
        res.append(seq[i:i+length])
    return iter(res)


def tests():
    print(part1(TEST))
    print(part2(TEST))


def part1(input: str):
    res = 0

    records = parse(input)
    for r in records:
        a = [r]
        while True:
            b = a[len(a) - 1]
            # compute next history adding the last elements of all arrays
            res += b[len(b) - 1]
            # break when the generated array has only 0
            if all(map(lambda x: x == 0, b)):
                break
            b = tuple(map(lambda x: x[1] - x[0],
                    partition(b, 2, 1)))
            a.append(b)
    
    return res


def part2(input: str):
    res = 0

    records = parse(input)
    for r in records:
        a = [r]
        # `c` stores the result of a line of record
        c = 0
        flip = 1
        while True:
            b = a[len(a) - 1]
            # In fact, add number in the front of every history means:
            # In Lisp: (-a (- b (- c (- d 0))))
            # In Math: a - (b - (c - (d - 0)))
            # a - b + c - d
            # where a, b, c, d is the first element of every level
            c += flip * b[0]
            flip *= -1
            # break when the generated array has only 0
            if all(map(lambda x: x == 0, b)):
                break
            b = tuple(map(lambda x: x[1] - x[0],
                    partition(b, 2, 1)))
            a.append(b)
        res += c
    
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
