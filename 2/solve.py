#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def main(A):
    def has_two(line):
        return 2 in Counter(line).values()
    def has_three(line):
        return 3 in Counter(line).values()

    a = sum(int(has_two(line)) for line in A)
    b = sum(int(has_three(line)) for line in A)

    print('Part 1', a * b)

    def hamming_dist(uno, dos):
        return sum(int(a != b) for a, b in zip(uno, dos))
    def get_common(uno, dos):
        return ''.join(a for a, b in zip(uno, dos) if a == b)
    for uno, dos in combinations(A, 2):
        if hamming_dist(uno, dos) == 1:
            print('Part 2', get_common(uno, dos))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        A = A.splitlines()
    else:
        A = open('input.txt').read()
        A = A.splitlines()
    main(A)
