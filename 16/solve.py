#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]

line_pos = 0
def next_line(A):
    global line_pos
    line_pos += 1
    return A[line_pos-1]


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


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def parse_line(line):
    #return line.split()
    #return parse_ints(line)
    return line


def main(A):
    A = A.splitlines()
    rules = []

    opcodes = defaultdict(lambda: set(ALL_OPS))
    nonopcodes = defaultdict(lambda: set())

    three_or_more = 0
    while True:
        before = parse_ints(next_line(A))
        if not before: break
        opcode, a, b, c = parse_ints(next_line(A))
        after = parse_ints(next_line(A))
        rules.append((before, after, opcode, a, b, c))
        next_line(A)

    for before, after, opcode, a, b, c in rules:
        matching_opstrs = set()
        for tryopstr in ALL_OPS:
            reg = before[:]
            execute_op(reg, tryopstr, a, b, c)
            if reg == after:
                matching_opstrs.add(tryopstr)
            else:
                nonopcodes[tryopstr].add(opcode)
        if len(matching_opstrs) >= 3:
            three_or_more += 1
        opcodes[opcode] &= matching_opstrs

    res = three_or_more
    print('Part 1', res)

    #print(opcodes)
    #print(nonopcodes)

    a_opstr = dict()
    a_opcode = dict()

    def assign_op():
        for opstr in ALL_OPS:
            if opstr in a_opstr: continue
            result = []
            for opcode in range(16):
                if opcode in a_opcode: continue
                if opstr in opcodes[opcode] and opcode not in nonopcodes[opstr]:
                    result.append(opcode)
            assert len(result) > 0
            if len(result) == 1:
                opcode = result[0]
                #print('assigned', opstr, opcode)
                a_opstr[opstr] = opcode
                a_opcode[opcode] = opstr
                return True
        return False

    while assign_op():
        pass
    assert len(a_opstr) == 16
    #print(a_opstr)

    next_line(A)
    opmap = a_opcode
    reg = [0, 0, 0, 0]
    while True:
        try:
            line = next_line(A)
        except IndexError:
            break

        opcode, a, b, c = parse_ints(line)
        execute_op(reg, opmap[opcode], a, b, c)

    print('Part 2', reg[0])
if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
