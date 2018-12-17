#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def parse_line(gridx, gridy, line):
    a, b = line.split(', ')
    if a[0] == 'x':
        x = parse_ints(a)[0]
        y0, y1 = parse_ints(b)
        for y in range(y0, y1+1):
            gridx[x].add(y)
            gridy[y].add(x)
    else:
        assert a[0] == 'y'
        y = parse_ints(a)[0]
        x0, x1 = parse_ints(b)
        for x in range(x0, x1+1):
            gridx[x].add(y)
            gridy[y].add(x)


# greatest element of A less than x
def lower_bound(A, x):
    return max([val for val in A if val < x], default=float('inf'))
def upper_bound(A, x):
    return min([val for val in A if val > x], default=float('-inf'))


def fill_water(gridx, gridy, ew, source_x, source_y, min_y, max_y):
    #print('\nHELLO fill_water', source_x, source_y)
    water = 0
    t = 0
    while True:
        #print('hello world, water is', water)
        base_y = upper_bound(gridx[source_x], source_y)
        if base_y == float('-inf'):
            break
        #print('base_y is', base_y)

        # check if bounded on l, r
        level_y = base_y - 1
        base_xl = lower_bound(gridy[level_y], source_x)
        base_xr = upper_bound(gridy[level_y], source_x)
        bounded = base_xl < source_x < base_xr
        if level_y == source_y:
            #print('BLAH BLAH level_y == source_y', level_y, source_y)
            bounded = False

        if bounded:
            for x in range(base_xl+1, base_xr):
                bounded = bounded and x in gridy[base_y]

        if bounded:
            #print('bounded lr: source {},{}'.format(source_x, source_y))
            #print('  base_y {} level_y {} base_xl {} base_xr {}'.format(
            #    base_y, level_y, base_xl, base_xr))

            for x in range(base_xl+1, base_xr):
                gridx[x].add(level_y)
                gridy[level_y].add(x)
                water += 1
        else:
            #print('uh oh, unbounded')

            # try to find new sources
            new_sources = []
            extra_water = 0

            if level_y == source_y:
                new_sources.append((source_x, source_y-1))

            # extra water to left
            x = source_x - 1
            while x not in gridy[level_y] and x in gridy[base_y]:
                if (x, level_y) not in ew:
                    ew.add((x, level_y))
                    extra_water += 1
                x -= 1
            if x not in gridy[level_y]:
                if (x, level_y) not in ew:
                    ew.add((x, level_y))
                    extra_water += 1
                new_sources.append((x, level_y))
            #print('extra_water to left', extra_water)

            # extra water to right
            x = source_x + 1
            while x not in gridy[level_y] and x in gridy[base_y]:
                if (x, level_y) not in ew:
                    ew.add((x, level_y))
                    extra_water += 1
                x += 1
            if x not in gridy[level_y]:
                if (x, level_y) not in ew:
                    ew.add((x, level_y))
                    extra_water += 1
                new_sources.append((x, level_y))

            #print('extra water', extra_water)
            for y in range(source_y+1, base_y):
                if (source_x, y) not in ew and y >= min_y:
                    ew.add((source_x, y))
                    extra_water += 1
            #print(source_y, base_y)

            #print('extra water', extra_water)
            water += extra_water
            return water, new_sources

        t += 1

    extra_water = 0
    for y in range(source_y+1, max_y+1):
        if (source_x, y) not in ew and y >= min_y:
            ew.add((source_x, y))
            extra_water += 1
    #print('NO BOTTOM, extra_water', extra_water)
    water += extra_water
    return water, []


def main(A):
    A = A.splitlines()
    gridx = defaultdict(set)
    gridy = defaultdict(set)
    for line in A:
        parse_line(gridx, gridy, line)
    min_y, max_y = min(gridy), max(gridy)
    min_x, max_x = min(gridx), max(gridx)
    gridx_original = dict((k, set(v)) for k, v in gridx.items())

    # find space for water
    sources = [(500, 0)]
    ew = set()
    visited_sources = set()
    water = 0

    def print_grid():
        for y in range(0, max_y+1):
            out = []
            for x in range(min_x-1, max_x+2):
                #if source_x == x and source_y == y:
                #    out.append('+')
                if x in gridx_original and y in gridx_original[x]:
                    out.append('#')
                elif y in gridx[x]:
                    out.append('~')
                elif (x, y) in ew:
                    out.append('|')
                else:
                    out.append('.')
            print(''.join(out))

    while sources:
        source = sources.pop(0)
        if source in visited_sources:
            #print('VISITED, NO, BAD', source)
            continue
        visited_sources.add(source)
        source_x, source_y = source
        if source_y > max_y:
            #print('bad', source_y)
            raise ValueError()
        new_water, new_sources = fill_water(
            gridx, gridy, ew, source_x, source_y, min_y, max_y
        )

        #print('DONE:', new_water, new_sources)
        water += new_water
        sources.extend(new_sources)

    print_grid()

    '''
    #print('pre adjustment', water)
    # stop double counting
    adjustment = 0
    for y in range(0, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in ew and y in gridx[x]:
                adjustment += 1
    print('lol adjustment', adjustment)
    water -= adjustment
    print('water', water)
    '''

    new_water = 0
    still_water = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x-1, max_x+2):
            if x in gridx_original and y in gridx_original[x]:
                pass
            elif y in gridx[x]:
                new_water += 1
                still_water += 1
            elif (x, y) in ew:
                new_water += 1
    #print('new water', new_water)
    #assert new_water == water
    water = new_water

    print('Part 1', water)
    print('Part 2', still_water)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
