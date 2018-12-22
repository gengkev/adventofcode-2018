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
    return cstr, rhs.strip()


def parse_line(line):
    line = line.split()
    op = line[0]
    a, b, c = map(int, line[1:])
    return op, a, b, c


def main(A):
    A = A.splitlines()

    # Extract ip_reg, parse rest of lines as instructions
    ip_reg = int(A[0].split()[1])
    ip_reg_var = generate_str('r', ip_reg)
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
        print('  long long {} = {};'.format(
            generate_str('r', i),
            generate_str('i', initial_values[i])))
    print()

    for i, line in enumerate(A):
        lhs, rhs = generate_line(i, *line)

        # On RHS, ip_reg can be substituted
        rhs = rhs.replace(ip_reg_var, generate_str('i', i))

        label = 'line{}:'.format(i)
        print('{:<10}'.format(label), end='')

        # If LHS is ip_reg, we need to jump
        if lhs == ip_reg_var:
            if 'reg' in rhs:
                print('{} = {} + 1;'.format(lhs, rhs))
                print('          goto jump;')
            else:
                # Immediate jump target
                target = eval(rhs.replace('LL', '')) + 1
                if 0 <= target < len(A):
                    print('goto line{};'.format(target))
                else:
                    print('printf("Out of range: {}\\n");'.format(target))
                    print('          return 0;')
            print()

        # Normal LHS <- RHS assignment
        else:
            print('{} = {};'.format(lhs, rhs))

    print('jump:')
    print('  switch ({}) {{'.format(ip_reg_var))
    for i, _ in enumerate(A):
        case_stmt = 'case {}:'.format(i)
        print('  {:<10}goto line{};'.format(case_stmt, i))
    print('  default:')
    print('    printf("Out of range: %lld\\n", {});'.format(ip_reg_var))
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
