#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product


def process(A):
    for i in range(1, len(A)):
        p, c = A[i-1], A[i]
        if (p.islower() and c.isupper() and p.upper() == c) or \
           (p.isupper() and c.islower() and p.lower() == c):
            return A[:i-1] + A[i+1:]
    return None


def get_len(A):
    while True:
        n = process(A)
        if n:
            A = n
        else:
            break
    return len(A)


def main(A):
    print('Part 1', get_len(A))
    out = []
    for i in range(0, 26):
        c, C = chr(ord('a') + i), chr(ord('A') + i)
        A2 = A.replace(c, '').replace(C, '')
        l = get_len(A2)
        out.append(l)
        #print(i, l)
    print('Part 2', min(out))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = A.strip()
    main(A)
