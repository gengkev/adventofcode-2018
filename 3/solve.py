#!/usr/bin/env python3

import sys
import re
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]

def parse_claim(line):
    line = line.split()
    d = int(line[0].lstrip('#'))
    left, top = map(int, line[2].rstrip(':').split(','))
    width, height = map(int, line[3].split('x'))
    return d, left, top, width, height

def main(A):
    #A = [parse_claim(line) for line in A]
    A = [parse_ints(line) for line in A]
    grid = defaultdict(int)
    for claim in A:
        d, l, t, w, h = claim
        for i in range(h):
            for j in range(w):
                coords = (t+i, l+j)
                grid[coords] += 1

    count = 0
    for k, v in grid.items():
        if v >= 2:
            count += 1
    print('Part 1', count)

    for claim in A:
        d, l, t, w, h = claim
        has_overlap = False
        for i in range(h):
            for j in range(w):
                coords = (t+i, l+j)
                if grid[coords] > 1:
                    has_overlap = True
        if not has_overlap:
            print('Part 2', d)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        A = A.splitlines()
    else:
        A = open('input.txt').read()
        A = A.splitlines()
    main(A)
