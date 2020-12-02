from collections import Counter
from operator import xor

def solve_day2(entries):
    valid_count_p1, valid_count_p2 = 0, 0
    for entry in entries:
        words = entry.strip().split()
        min_char, max_char = [int(x) for x in words[0].split('-')]
        policy_char = words[1][0]
        password = words[2]
        counts = Counter(password)
        if min_char <= counts[policy_char] <= max_char:
            valid_count_p1 += 1
        if xor((password[min_char-1] == policy_char), (password[max_char-1] == policy_char)):
            valid_count_p2 += 1
    
    return valid_count_p1, valid_count_p2


if __name__ == '__main__':
    entries = open('./input.txt', 'r').readlines()
    print('Part 1: {0}\nPart 2: {1}'.format(*solve_day2(entries)))