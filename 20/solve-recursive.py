#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


DIRECTIONS = {
    'E': (0, 1),
    'W': (0, -1),
    'N': (-1, 0),
    'S': (1, 0),
}


# all-pairs shortest paths
def bfs(edges, start):
    visited = {}
    q = deque()

    visited[start] = 0
    q.append(start)

    while q:
        cur = q.popleft()
        for nbr in edges[cur]:
            if nbr not in visited:
                visited[nbr] = visited[cur] + 1
                q.append(nbr)

    return visited


def move(pos, c):
    #print('move({}, {})'.format(pos, c))
    i, j = pos
    ni, nj = DIRECTIONS[c]
    return (i+ni, j+nj)


def recurse(next_char, edges, initial_positions):
    positions = initial_positions
    acc = set()

    while True:
        c = next_char()
        if c.isalpha():
            newpositions = []
            for pos in positions:
                npos = move(pos, c)
                edges[npos].add(pos)
                edges[pos].add(npos)
                newpositions.append(npos)
            positions = frozenset(newpositions)
        elif c == '(':
            positions = recurse(next_char, edges, positions)
        elif c == '|':
            acc.update(positions)
            positions = initial_positions
        elif c == ')':
            acc.update(positions)
            break
        else:
            assert False

    return frozenset(acc)


def main(inp):
    # append ) to ensure recurse exits
    inp = inp.strip().lstrip('^').rstrip('$') + ')'

    i = 0
    def next_char():
        nonlocal i
        i += 1
        return inp[i-1]

    initial_positions = frozenset([(0, 0)])
    edges = defaultdict(set)
    recurse(next_char, edges, initial_positions)

    dists = bfs(edges, (0, 0))
    res = max(dists.values())
    print('Part 1', res)

    res = len([v for v in dists.values() if v >= 1000])
    print('Part 2', res)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
