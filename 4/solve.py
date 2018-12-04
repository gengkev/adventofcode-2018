#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]


def main(A):
    A = [line.split() for line in A]

    # m[min_]
    m = Counter()
    # c[gnum][min_]
    c = defaultdict(Counter)
    # part2[(gnum, min_)]
    part2 = Counter()

    gnum = -1
    i = 0
    while i < len(A):
        line = A[i]
        if line[2].startswith('Guard'):
            gnum = int(line[3].lstrip('#'))
        elif line[2] == 'falls':
            start = parse_ints(line[1])[1]
            nline = A[i+1]
            end = parse_ints(nline[1])[1]
            for j in range(start, end):
                c[gnum][j] += 1
                part2[(gnum, j)] += 1
            m.update({gnum: end-start})
            i += 1
        else:
            assert False, line
        i += 1

    gnum, time = m.most_common(1)[0]
    #print(gnum, time)
    min_, _ = c[gnum].most_common(1)[0]
    #print(min_)
    print('Part 1', gnum * min_)

    (gnum, min_), _ = part2.most_common(1)[0]
    #print(gnum, min_)
    print('Part 2', gnum * min_)




if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        A = A.splitlines()
    else:
        A = open('input.txt').read()
        A = A.splitlines()
    A.sort()
    main(A)
