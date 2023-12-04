"""
[2023 day4 advent of code](https://adventofcode.com/2023/day/4)
Python solution
"""

import re
from collections import deque

DEBUG = False

TEST = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def tests():
    print(part1(TEST)) # 13
    print(part2(TEST)) # 30


def parseLine(line: str):
    line = line[line.find(':') + 1:].split(' | ')
    pat = re.compile(r'\d+')
    winningNums = re.findall(pat, line[0])
    nums = re.findall(pat, line[1])
    if DEBUG:
        print("win: ", winningNums)
        print('nums: ', nums)
    return winningNums, nums

def countMatch(card):
    winningNums, nums = card
    count = len(set(winningNums) & set(nums))
    return count
    
def part1(input: str):
    """"""
    res = 0
    for line in input.splitlines():
        count = countMatch(parseLine(line))
        match count:
            case 0: points = 0
            case _: points =  2 ** (count - 1)
        res += points
    return res


def part2(input: str):
    """Process all of the original and copied scratchcards until no more scratchcards are won
    Data Flow:
        (cardId1, match1) -> [(cardId + 1, match2) ... (cardId + match, matchn)]
    """
    res = 0
    cards = [0 for _ in range(len(input.splitlines()) + 1)] 
    cardsToSpawn = [0] + [countMatch(parseLine(line)) for line in input.splitlines()]
    toCount = deque((id, canSpawn) for id, canSpawn in enumerate(cardsToSpawn, 0))
    if DEBUG:
        print(cards)
        print(toCount)
    while len(toCount):
        card = toCount.popleft()
        # spawn
        toCount.extend((card[0] + i, cardsToSpawn[card[0] + i]) for i in range(1, card[1] + 1))
        # count
        cards[card[0]] += 1
    if DEBUG:
        print('Scratch cards: ',cards)
    return sum(cards) - 1 # remove Card 0

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