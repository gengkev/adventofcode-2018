#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

'''
    0
3       1
    2
'''

# always (y,x) order
DIRECTIONS = [
    (-1,  0),  # up
    ( 0,  1),   # right
    ( 1,  0),   # down
    ( 0, -1),  # left
]

def char_to_direction(c):
    if c == '<': return 3
    elif c == '>': return 1
    elif c == '^': return 0
    elif c == 'v': return 2
    assert False


def move_direction(a, d):
    y, x = a
    dy, dx = DIRECTIONS[d]
    return y+dy, x+dx


def tick(grid, carts):
    height = len(grid)
    width = len(grid[0])
    ncarts = dict()
    cart_list = list(sorted(carts.keys()))
    skipcarts = set()
    crashes = []
    for i,(y,x) in enumerate(cart_list):
        if (y,x) in skipcarts:
            #print('skip cart', (y,x))
            continue
        d, t = carts[(y, x)]
        ny, nx = move_direction((y,x), d)
        assert 0 <= ny < height, ny
        assert 0 <= nx < width, nx
        if (ny,nx) in ncarts or \
                (ny,nx) in carts and i <= cart_list.index((ny,nx)):
            # crash
            #print('crash {},{}'.format(nx, ny))
            crashes.append((ny, nx))
            if (ny,nx) in ncarts:
                del ncarts[(ny, nx)]
            skipcarts.add((ny, nx))
            continue
        nd = d
        nt = t
        if grid[ny][nx] == '\\':
            if d in (1, 3):
                nd = (d + 1) % 4
            else:
                nd = (d - 1) % 4
        elif grid[ny][nx] == '/':
            if d in (1, 3):
                nd = (d - 1) % 4
            else:
                nd = (d + 1) % 4
        elif grid[ny][nx] == '+':
            nd = (d - 1 + t) % 4
            nt = (t + 1) % 3
        ncarts[(ny, nx)] = (nd, nt)
    return crashes, ncarts


def main(A):
    A = [list(line) for line in A]
    height = len(A)
    width = len(A[0])

    # initialize cart state
    carts = dict()
    for y,x in product(range(height), range(width)):
        if A[y][x] in '<>^v':
            carts[(y, x)] = (char_to_direction(A[y][x]), 0)
            if A[y][x] in '<>': A[y][x] = '-'
            else:               A[y][x] = '|'

    #for y in range(height):
    #    print(''.join(A[y]))

    t = 0
    part1 = False
    while True:
        #print(t, carts)
        crashes, carts = tick(A, carts)

        # for part 1 print first crash
        if not part1 and len(crashes) > 0:
            y, x = crashes[0]
            print('Part 1 {},{}'.format(x,y))
            part1 = True

        # break if one cart left
        if len(carts) == 1:
            break

        t += 1

    # for part 2 print last cart left
    y, x = list(carts.keys())[0]
    print('Part 2 {},{}'.format(x,y))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = A.splitlines()
    main(A)
