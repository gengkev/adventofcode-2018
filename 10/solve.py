#!/usr/bin/env python3

import re
import sys
import time
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def display_grid(grid):
    xs = [x for x,y in grid]
    ys = [y for x,y in grid]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    xlen = max_x-min_x+1
    ylen = max_y-min_y+1

    if ylen < 16:
        out = [
            ['.' for _ in range(min_x, max_x+1)]
            for _ in range(min_y, max_y+1)
        ]
        for x,y in grid:
            out[y-min_y][x-min_x] = '#'
        print('\n'.join(''.join(line) for line in out))
        return True
    else:
        return False


def get_grid_at_time(A, t):
    grid = set()
    for x0, y0, vx, vy in A:
        x, y = x0+vx*t, y0+vy*t
        grid.add((x, y))
    return grid


def main(A):
    A = [parse_ints(line) for line in A]
    i = 0
    good = False
    print('Part 1')
    while True:
        grid = get_grid_at_time(A, i)
        if display_grid(grid):
            print('Part 2', i)
            good = True
        elif good:
            break
        i += 1


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = A.splitlines()
    main(A)
