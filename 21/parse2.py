#!/usr/bin/env python3

'''
An ElfCode to C transpiler.
Usage: python3 parse.py <elfcode_file>
The C program is printed to standard out.
'''

import sys

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

    # Extract ip_reg, parse rest of lines as instructions
    ip_reg = int(A[0].split()[1])
    A = A[1:]
    A = [parse_line(line) for line in A]

    # Set initial values of registers here
    initial_values = [0 for _ in range(NUM_REGS)]

    # Begin code generation!
    print('#include <stdio.h>')
    print('#include <stdbool.h>')
    print()
    print('int main(void) {')
    for i in range(NUM_REGS):
        print('  long long reg{} = {};'.format(
            i, generate_str('i', initial_values[i])))
    print()

    for i, line in enumerate(A):
        linestr = generate_line(i, *line)
        print('line{}:'.format(i))
        print('  {}'.format(linestr))
        print('  reg{}++;'.format(ip_reg))

        # Only break if we have to; otherwise fallthrough
        if linestr.startswith('reg{}'.format(ip_reg)):
            print('  goto jump;')
            print()

    print('jump:')
    print('  switch (reg{}) {{'.format(ip_reg))
    for i, _ in enumerate(A):
        print('  case {0}: goto line{0};'.format(i))
    print('  default:')
    print('    printf("Out of range: %lld\\n", reg{});'.format(ip_reg))
    print('    break;')
    print('  }')
    print()
    print('  return 0;')
    print('}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <elfcode_file>'.format(sys.argv[0]),
                file=sys.stderr)
        sys.exit(1)
    A = open(sys.argv[1]).read()
    main(A)
