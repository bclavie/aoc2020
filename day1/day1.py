from itertools import combinations
import math

def solve_day1(entries, size):
    return math.prod([x for x in combinations(entries, size) if sum(x) == 2020][0])
    # for comb in combinations(entries, size):
    #     if sum(comb) == 2020:
    #         return math.prod(comb)

if __name__ == '__main__':
    entries = open('./input.txt', 'r').readlines()
    entries = [int(x) for x in entries]
    print('Part 1: {0}'.format(solve_day1(entries, 2)))
    print('Part 2: {0}'.format(solve_day1(entries, 3)))
