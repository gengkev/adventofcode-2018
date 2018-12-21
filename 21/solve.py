#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False
MAX_STEPS = 1000

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


ALL_OPS = [
    'addr', 'addi',
    'mulr', 'muli',
    'banr', 'bani',
    'borr', 'bori',
    'setr', 'seti',
    'gtir', 'gtri', 'gtrr',
    'eqir', 'eqri', 'eqrr',
]

def execute_op(reg, op, a, b, c):
    def get_sec():
        if op[3] == 'r':
            return reg[b]
        elif op[3] == 'i':
            return b
        else:
            assert False

    if op[:3] == 'add':
        reg[c] = reg[a] + get_sec()
    if op[:3] == 'mul':
        reg[c] = reg[a] * get_sec()
    if op[:3] == 'ban':
        reg[c] = reg[a] & get_sec()
    if op[:3] == 'bor':
        reg[c] = reg[a] | get_sec()
    if op[:3] == 'set':
        reg[c] = a if op[3] == 'i' else reg[a]
    if op == 'gtir':
        reg[c] = 1 if a > reg[b] else 0
    if op == 'gtri':
        reg[c] = 1 if reg[a] > b else 0
    if op == 'gtrr':
        reg[c] = 1 if reg[a] > reg[b] else 0
    if op == 'eqir':
        reg[c] = 1 if a == reg[b] else 0
    if op == 'eqri':
        reg[c] = 1 if reg[a] == b else 0
    if op == 'eqrr':
        reg[c] = 1 if reg[a] == reg[b] else 0


def parse_line(line):
    line = line.split()
    op = line[0]
    a, b, c = map(int, line[1:])
    return op, a, b, c


def main(A):
    A = A.splitlines()
    ip_reg = parse_ints(A[0])[0]
    A = A[1:]
    A = [parse_line(line) for line in A]

    # Part 1
    reg = [0 for _ in range(6)]
    visited = [False for _ in range(2**24)]
    last_visited = None

    while 0 <= reg[ip_reg] < len(A):
        line = A[reg[ip_reg]]
        op, a, b, c = line

        #print('t', t, 'ip', reg[ip_reg], line, reg)
        if reg[ip_reg] == 28:
            #print(t, 'hello from line 28', reg)

            if visited[reg[2]]:
                print('Part 2', last_visited)
                break

            if last_visited is None:
                print('Part 1', reg[2])

            visited[reg[2]] = True
            last_visited = reg[2]

        execute_op(reg, op, a, b, c)
        reg[ip_reg] += 1


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
