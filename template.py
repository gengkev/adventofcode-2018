#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def parse_line(line):
    #return line.split()
    #return parse_ints(line)
    return line


def main(A):
    A = A.splitlines()
    A = [parse_line(line) for line in A]
    
    res = 0
    print('Part 1', res)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
