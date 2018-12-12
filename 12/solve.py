#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]


def parse_line(line):
    left, right = line.split(' => ')
    return (left, right)


def get_surrounding(state, i):
    return ''.join(
            state.get(j, '.')
            for j in range(i-2,i+3)
        )

def next_gen(A, state):
    min_x, max_x = min(state), max(state)
    return {i: A[get_surrounding(state, i)]
            for i in range(min_x-2, max_x+2)}


def count_state(state):
    return sum(k for k, v in state.items() if v == '#')


def main(A):
    initial_state = list(A[0].lstrip('initial state: '))
    #print(initial_state)
    A = dict(parse_line(line) for line in A[2:])
    #print(A)

    state = dict(enumerate(initial_state))
    for t in range(20):
        state = next_gen(A, state)
    res = count_state(state)
    print('Part 1', res)

    state = dict(enumerate(initial_state))
    for t in range(2000):
        state = next_gen(A, state)
        #print(t+1, count_state(state))

    # Linear interpolation after 1000 steps
    cnt_1000 = count_state(state)
    state = next_gen(A, state)
    cnt_1001 = count_state(state)
    delta = cnt_1001 - cnt_1000
    res = cnt_1000 + delta * (50000000000 - 1000)
    print('Part 2', res)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
    else:
        A = open('input.txt').read()
    A = A.splitlines()
    main(A)
