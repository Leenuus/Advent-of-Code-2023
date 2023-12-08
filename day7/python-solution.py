"""
[2023 day7 advent of code](https://adventofcode.com/2023/day/7)
Python solution
"""

from functools import cmp_to_key

DEBUG = True

"""Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
"""

"""A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2"""

TEST = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def parse(input: str):
    res = []
    for line in input.splitlines():
        line = line.split(' ')
        hands = line[0]
        # deal with hands
        d = {}
        for card in hands:
            # higher card
            d[card] = d.setdefault(card, 0) + 1
        bid = int(line[1])
        res.append((d, bid, hands))
    return res

def handsRank(hands: dict[str, int]):
    if len(hands) == 1:
        return 7
    elif len(hands) == 2:
        hands = tuple(hands.values())
        # four of a kind
        if 1 in hands and 4 in hands:
            return 6
        # full horse
        elif 2 in hands and 3 in hands:
            return 5
    elif len(hands) == 3:
        hands = tuple(hands.values())
        # three of a kind
        if 3 in hands and 1 in hands:
            return 4
        # two pairs
        elif 2 in hands and 1 in hands:
            return 3
    elif len(hands) == 4:
        # one pair
        return 2
    else:
        # higher card
        return 1


def cardRank(card: str, part2: bool = False):
    match card:
        case 'A':
            return 10
        case 'K':
            return 9 
        case 'Q':
            return 8 
        case 'J':
            return 7  if part2 else -3
        case 'T': return 6  
        case '9': return 5  
        case '8':return 4    
        case '7':return 3  
        case '6':return 2  
        case '5':return 1  
        case '4':return 0  
        case '3':return -1  
        case '2': return -2
            


def tests():
    # res = parse(TEST)
    # print(res)
    print(part1(TEST))
    print(part2(TEST))

def sortFunction(a, b):
    ha = a[0]
    hb = b[0]
    if ha - hb == 0:
        for c1, c2 in zip(a[2], b[2]):
            res = cardRank(c1) - cardRank(c2)
            if res != 0:
                return res
    return ha - hb

def part1(input: str):
    hands = parse(input)
    # d, bids, hands
    # sort by comparing d
    hands = list((handsRank(hand[0]), hand[1], hand[2]) for hand in hands)
    # expect: 
    # [(2, 765, '32T3K'), (3, 220, 'KTJJT'), (3, 28, 'KK677'), (4, 684, 'T55J5'), (4, 483, 'QQQJA')]
    hands.sort(key=cmp_to_key(sortFunction))
    # print(hands)
    return sum(bid * rank for rank, bid in zip(range(1, len(hands) + 1), (hand[1] for hand in hands)))

def part2(input: str):
    # d, bids, hands
    hands = parse(input)

    def handsRankPart2(hands: dict[str, int]):
        # including J
        # try every case to get the most
        if 'J' in hands:
            # handsRank return 1 as smallest possible value
            rank = 0
            for i in range(1, hands['J'] + 1):
                for k in hands.keys():
                    h = dict(hands)
                    h[k] += i
                    h['J'] -= i
                    if h['J'] == 0:
                        h.pop('J')
                    try:
                        rank = max(handsRank(h), rank)
                    except TypeError:
                        print('rank: ', rank)
                        print('origin hands: ', hands)
                        print('modified hands: ', h)
            return rank
        # no J
        else:
            return handsRank(hands)

    hands = list((handsRankPart2(hand[0]), hand[1], hand[2]) for hand in hands)

    hands.sort(key=cmp_to_key(sortFunction))
    # print(hands)
    return sum(bid * rank for rank, bid in zip(range(1, len(hands) + 1), (hand[1] for hand in hands)))

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