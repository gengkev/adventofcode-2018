#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def main(A):
    A = list(map(int, A))
    print('Part 1', sum(A))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        A = A.split(', ')
    else:
        A = open('input.txt').read()
        A = A.splitlines()
    main(A)
