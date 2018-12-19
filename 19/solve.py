#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


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

    while 0 <= reg[ip_reg] < len(A):
        line = A[reg[ip_reg]]
        op, a, b, c = line
        execute_op(reg, op, a, b, c)
        reg[ip_reg] += 1

    res = reg[0]
    print('Part 1', res)


    # Part 2
    reg = [0 for _ in range(6)]
    reg[0] = 1
    t = 0

    while 0 <= reg[ip_reg] < len(A): #and t < 2000:
        if reg[ip_reg] == 1:
            target_val = reg[2]
            break
        #if reg[ip_reg] == 7:
        #    print('hello', reg)
        line = A[reg[ip_reg]]
        op, a, b, c = line
        #if t % 1000000 == 0:
        #    print('\r', t, 'reg', reg, 'executing', op, a, b, c, end='')
        #print(t, reg[ip_reg], 'reg', reg, 'executing', op, a, b, c)
        execute_op(reg, op, a, b, c)
        reg[ip_reg] += 1
        t += 1

    # Sum factors of target_val
    res = 0
    for i in range(1, target_val+1):
        if target_val % i == 0:
            res += i
    print('Part 2', res)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
