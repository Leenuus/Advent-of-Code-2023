"""
[2023 day8 advent of code](https://adventofcode.com/2023/day/8)
Python solution
"""

from __future__ import annotations
import re
from math import gcd
from typing import NamedTuple
DEBUG = True

TEST1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


class Node(NamedTuple):
    Name: str
    left: str
    right: str

def tests():
    res = parse(TEST1)
    print('t1: ', res)
    res = parse(TEST2)
    print('t2: ', res)
    res = part1(TEST1)
    print('t1: ', res)
    res = part1(TEST2)
    print('t2: ', res)
    res = part2(TEST3)
    print(res)


def parse(input: str):
    pat = re.compile(r'([A-Z\d]{3}) = \(([A-Z\d]{3}), ([A-Z\d]{3})\)')
    lines = input.splitlines()
    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        a = pat.match(lines[i]).group(1)
        b = pat.match(lines[i]).group(2)
        c = pat.match(lines[i]).group(3)
        nodes[a] = Node(a, b, c)
    return instructions, nodes

def part2(input: str):
    instructions, nodes = parse(input)
    starts = tuple(filter(lambda k: k.endswith('A'), nodes.keys()))
    print('start positions: ', starts)
    ends = tuple(filter(lambda k: k.endswith('Z'), nodes.keys()))
    print('end positions: ', ends)
    steps = []
    for pos in starts:
        step = 0
        while True:
            for ins in instructions:
                if ins == 'L':
                    pos = nodes[pos].left
                elif ins == 'R':
                    pos = nodes[pos].right
                step += 1
                if pos in ends:
                    break
            if pos in ends:
                break
        steps.append(step)
    print(steps)
    lcm = 1
    for s in steps:
        lcm = lcm * s // gcd(lcm, s)
    return lcm
        
def part1(input: str):
    instructions, nodes = parse(input)
    positions = 'AAA'
    step = 0
    while True:
        for ins in instructions:
            if ins == 'L':
                positions = nodes[positions].left
            elif ins == 'R':
                positions = nodes[positions].right
            step += 1
            if positions == 'ZZZ':
                break
        if positions == 'ZZZ':
            break
    return step

def main():
    production = True
    if DEBUG:
        tests()
    if production:
        with open('input.txt', 'r') as f:
            input = f.read()
        res1 = part1(input)
        res2 = part2(input)

        print('Part1:', res1)
        print('Part2:', res2)


if __name__ == '__main__':
    main()