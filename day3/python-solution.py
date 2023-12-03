"""
[2023 day3 advent of code](https://adventofcode.com/2023/day/3)
Python solution
"""

TEST = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

DEBUG = True

def tests():
    # res = parse(TEST)
    # part1(TEST)
    # part2(TEST)
    pass

def parse(input: str):
    nums = []
    symbols = []
    lines = input.splitlines()
    for row in range(len(lines)):
        line = lines[row]
        i = 0
        while i < len(line):
            if line[i].isdigit():
                # get the digit and its spanning coordinates
                start = i
                while i+1 < len(line) and line[i + 1].isdigit():
                    i = i + 1 
                end = i
                num = line[start:end + 1]
                if DEBUG:
                    print('num: ', num)
                num = int(num)
                nums.append((num, tuple((row, col) for col in range(start, end + 1) )))
            else:
                # get symbols and its coordinate
                if not line[i].isdigit() and line[i] != '.' :
                    symbols.append(((row, i), line[i]))
                else:
                    pass
            i = i + 1
    if DEBUG:
        print('nums:', nums)
        print('symbols:', symbols)
    return nums, symbols
    

def part1(input: str):
    """The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)"""
    nums, symbols = parse(input)
    symbolsCors = tuple(s[0] for s in symbols)
    print(symbolsCors)
    res = 0

    def foundOne(numCors, symbolsCors):
        for n in numCors:
            for s in symbolsCors:
                x = abs(n[0] - s[0])
                y = abs(n[1] - s[1])
                if x <= 1 and y<=1:
                    return True
        return False
        
    for num in nums:
        if foundOne(num[1], symbolsCors):
            res += num[0]
    if DEBUG:
        print('result: ', res)
    return res

def part2(input: str):
    """The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any `*` symbol that is adjacent to exactly **two** part numbers. Its gear ratio is the result of multiplying those two numbers together.
    This time, you need to find the gear ratio of every gear and **add** them all up so that the engineer can figure out which gear needs to be replaced."""
    nums, symbols = parse(input)
    res = 0
    gears = tuple(
        map(lambda x: x[0],
            filter(lambda x: x[1] == '*', symbols)
        ))
    if DEBUG:
        print(gears)

    def getGearRatio(gear, nums):
        # num: (n, ( (x, y) ...) )
        # gear: (x, y)
        count = 0
        res = 1
        for num in nums:
            for cor in num[1]:
                x = abs(gear[0] - cor[0])
                y = abs(gear[1] - cor[1])
                if x <= 1 and y<= 1:
                    count += 1
                    res *= num[0]
                    break
        if count == 2:
            return res
        else:
            """gear without 2 part numbers has gear ratio 0"""
            return 0
        
    for g in gears:
        # find two adj part numbers
        res += getGearRatio(g, nums)
    if DEBUG:
        print(res)
    return res

def main():
    if DEBUG:
        tests()
    with open('./input.txt', 'r', encoding='utf8') as f:
        input = f.read()
    print('Part1: ', part1(input))
    print('Part2: ', part2(input))

if __name__ == '__main__':
    main()