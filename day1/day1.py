from itertools import combinations
import math

entries = open('./input.txt', 'r').readlines()
entries = [int(x) for x in entries]

def solve_day1(entries, size):
    for comb in combinations(entries, size):
        if sum(comb) == 2020:
            return math.prod(comb)

print('Part 1: {0}'.format(solve_day1(entries, 2)))
print('Part 2: {0}'.format(solve_day1(entries, 3)))
