#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]


def main(A):
    #A = [line.split() for line in A]
    #A = [int(line) for line in A]
    #A = [parse_ints(line) for line in A]
    print('Part 1', sum(A))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        A = A.split(', ')
    else:
        A = open('input.txt').read()
        A = A.splitlines()
    main(A)
