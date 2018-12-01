#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def main(A):
    A = list(map(int, A))
    print('Part 1', sum(A))

    x = defaultdict(int)
    s = 0

    while True:
        for i in A:
            x[s] += 1
            #print('s', s, 'x[s]', x[s])
            if x[s] == 2:
                print('Part 2', s)
                return
            s += i


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read().split(', ')
    else:
        A = open('input.txt').read().splitlines()
    main(A)
