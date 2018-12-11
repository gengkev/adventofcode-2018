#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]


def get_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    power -= 5
    return power


def main(A):
    out = []
    for x in range(1, 301-3):
        for y in range(1, 301-3):
            pwr = 0
            for xx in range(3):
                for yy in range(3):
                    pwr += get_power(x+xx, y+yy, A)
            out.append((pwr, x, y))
    mpwr, mx, my = max(out)
    print('Part 1 {},{} (power={})'.format(mx, my, mpwr))

    base = [[get_power(x,y,A) for x in range(1,301)] for y in range(1,301)]
    pfx = [[0 for x in range(1,301)] for y in range(1,301)]
    pfx[0][0] = base[0][0]
    for x in range(1, 300):
        pfx[0][x] = pfx[0][x-1] + base[0][x]
    for y in range(1, 300):
        pfx[y][0] = pfx[y-1][0] + base[y][0]
    for y in range(1, 300):
        for x in range(1, 300):
            pfx[y][x] = pfx[y-1][x] + pfx[y][x-1] - pfx[y-1][x-1] + base[y][x]

    '''
    print('created pfx')

    print('BASE:')
    for y in range(10):
        print(base[y][:10])
    print('PREFIX:')
    for y in range(10):
        print(pfx[y][:10])
    '''

    def getpfx(y, x):
        if y < 0 or x < 0: return 0
        return pfx[y][x]
    def get_pwr(x, y, l):
        return getpfx(y+l-1, x+l-1) - getpfx(y+l-1, x-1) \
                - getpfx(y-1, x+l-1) + getpfx(y-1, x-1)
    assert get_pwr(0, 0, 1) == base[0][0]
    assert get_pwr(0, 0, 2) == base[0][0] + base[0][1] + base[1][0] + base[1][1]

    out2 = []
    for l in range(1,301):
        for x in range(300-l):
            for y in range(300-l):
                pwr = get_pwr(x, y, l)
                out2.append((pwr, x, y, l))
    mpwr, mx, my, msz = max(out2)
    print('Part 2 {},{},{} (power={})'.format(mx+1, my+1, msz, mpwr))






if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = int(A)
    main(A)
