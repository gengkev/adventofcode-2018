#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

i = 0
blah = 0

def next_int(A):
    global i
    i += 1
    return A[i-1]


def parse_node(A):
    global blah
    metadata = []
    results = []

    nchild = next_int(A)
    nentries = next_int(A)
    for j in range(0, nchild):
        chld = parse_node(A)
        results.append(chld)
    for j in range(0, nentries):
        entry = next_int(A)
        metadata.append(entry)
        blah += entry

    if nchild == 0:
        return sum(metadata)
    else:
        out = 0
        for entry in metadata:
            if 0 <= entry-1 < nchild:
                out += results[entry-1]
        return out


def main(A):
    res = parse_node(A)
    print('Part 1', blah)
    print('Part 2', res)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = list(map(int, A.split()))
    main(A)
