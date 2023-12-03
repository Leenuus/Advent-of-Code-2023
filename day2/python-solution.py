"""
[2023 day2 advent of code](https://adventofcode.com/2023/day/2)
Python solution
"""

DEBUG = True

TEST = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def findall(s: str, sub: str):
    res = []
    idx = -1
    while True:
        idx = s.find(sub, idx + 1)
        if idx == -1 or idx >= len(s):
            break
        res.append(idx)
    return res


def tests():
    print(findall('oneone1one', 'one'))
    parseLine("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    parsed = parse(TEST)
    print('parsed:', parsed)
    print('part1: ', part1(TEST))

def parseLine(line: str):
    """return tuple (red the biggest, green the biggest, blue the biggest) from a game
    split into sets with separator ;
    split into colors with separator ,

    """
    sets = line[line.find(':') + 1:].split(';')
    red = 0
    blue = 0
    green = 0
    colors = []
    for s in sets:
        c = s.split(',')
        if DEBUG:
            print(c)
        colors.extend(c)
    if DEBUG:
        print(colors)
    for c in colors:
        # find red
        if c.find('red') != -1:
            red = max(int(c[1:c.find('red') - 1]), red)
            print('red: ', red)
            continue
        if c.find('green') != -1:
            green = max(int(c[1:c.find('green') - 1]), green)
            print('green: ', green)
            continue
        if c.find('blue') != -1:
            blue = max(int(c[1:c.find('blue') - 1]), blue)
            print('blue: ', blue)
            continue
    if DEBUG:
        print(red, green, blue)
    return red, green, blue

def parse(s: str):
    res = [parseLine(line) for line in s.splitlines()]
    return res

def part1(input: str):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    RED = 12
    GREEN = 13
    BLUE = 14
    games = parse(input)
    res = 0
    for i in range(len(games)):
        if games[i][0] <= RED and games[i][1] <= GREEN and games[i][2] <= BLUE:
            res += (i + 1)
    return res


def part2(input: str):
    """The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286."""
    games = parse(input)
    res = sum(game[0] * game[1] * game[2] for game in games)
    return res

def main():
    if DEBUG:
        tests()   
    with open(file='./input.txt', mode='r', encoding='utf8') as f:
        input = f.read()
    part1Res = part1(input)
    print('Part1:', part1Res)

    part2Res = part2(input)
    print('Part2:', part2Res)


if __name__ == '__main__':
    main()
