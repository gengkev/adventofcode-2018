#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False

def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]

NUM_REGS = 6

ARITH_OPS = {
    'add': '+',
    'mul': '*',
    'ban': '&',
    'bor': '|',
}

SET_OP = 'set'

CMP_OPS = {
    'gt': '>',
    'eq': '==',
}


def generate_str(type_, val):
    if type_ == 'r':
        assert 0 <= val < NUM_REGS
        return 'reg{}'.format(val)
    elif type_ == 'i':
        return '{}LL'.format(val)
    elif type_ == 'n':
        return ''
    else:
        assert False


def generate_line(lineno, op, a, b, c):
    if op[:3] in ARITH_OPS:
        atype = 'r'
        btype = op[3]
        opstr = ARITH_OPS[op[:3]]

    elif op[:3] == SET_OP:
        atype = op[3]
        btype = 'n'
        opstr = ''

    elif op[:2] in CMP_OPS:
        atype = op[2]
        btype = op[3]
        opstr = CMP_OPS[op[:2]]

    else:
        assert False

    astr = generate_str(atype, a)
    bstr = generate_str(btype, b)
    cstr = generate_str('r', c)

    rhs = '{} {} {}'.format(astr, opstr, bstr)
    return '{} = {};'.format(cstr, rhs.strip())


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

    print('#include <stdio.h>')
    print('#include <stdbool.h>')
    print()
    print('int main(void) {')
    for i in range(NUM_REGS):
        print('  long long reg{} = 0;'.format(i))
    print()
    print('  bool done = false;')
    print('  while (!done) {')
    print('    switch (reg{}) {{'.format(ip_reg))

    for i, line in enumerate(A):
        linestr = generate_line(i, *line)
        print('    case {}:'.format(i))
        print('      {}'.format(linestr))
        print('      break;')

    print('    default:')
    print('      printf("Out of range: %lld\\n", reg{});'.format(ip_reg))
    print('      done = true;')
    print('    }')
    print('    reg{}++;'.format(ip_reg));
    print('  }')
    print('  return 0;')
    print('}')


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
