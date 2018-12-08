#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def generate_blah(A, extra):
    closest = defaultdict(int)
    xs = [x for x,y in A]
    ys = [y for x,y in A]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    diff_x = (max_x - min_x)*extra
    diff_y = (max_y - min_y)*extra
    start_x, end_x = min_x - diff_x, max_x + diff_x
    start_y, end_y = min_y - diff_y, max_y + diff_y
    #print(min_x, max_x, min_y, max_y)
    #print(start_x, end_x, start_y, end_y)

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            blah = [(p, dist(p, (x,y))) for p in A]
            pc, c = min(blah, key=lambda t:t[1])
            count = 0
            for (p,d) in blah:
                if d == c:
                    count += 1
            if count == 1:
                closest[pc] += 1
    #print('end')
    assert set(closest.keys()) - set(A) == set()
    '''
    for x, y in A:
        if x in (min_x, max_x) or y in (min_y, max_y):
            print('deleting', (x,y), closest[(x,y)])
            del closest[(x,y)]
    '''
    return closest.values()


def get_total_dist(A, pt):
    return sum(dist(c, pt) for c in A)


def part2(A, extra, target):
    xs = [x for (x,y) in A]
    ys = [y for (x,y) in A]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    cnt = 0
    for x in range(min_x - extra, max_x + extra + 1):
        for y in range(min_y - extra, max_y + extra + 1):
            if get_total_dist(A, (x,y)) < target:
                cnt += 1

    return cnt


def main(A):
    A = [tuple(map(int, line.split(', '))) for line in A]

    uno = generate_blah(A, 1)
    dos = generate_blah(A, 2)
    #tres = generate_blah(A, 4)

    #print('uno', sorted(uno))
    #print('dos', sorted(dos))
    #print('tres', sorted(tres))
    #print('uno&dos', sorted(set(uno)&set(dos)))
    #print('uno&dos&tres', sorted(set(uno)&set(dos)&set(tres)))
    #print('len(uno&dos&tres)', len(sorted(set(uno)&set(dos)&set(tres))))
    #print('len(A)', len(A))

    result = set(uno) & set(dos)
    print('Part 1', max(result))

    if is_sample:
        target = 32
    else:
        target = 10000

    #print('Part 2', part2(A, 0, target))
    print('Part 2', part2(A, target//100, target))
    #print('Part 2', part2(A, target//10, target))

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        is_sample = True
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = A.splitlines()
    main(A)
