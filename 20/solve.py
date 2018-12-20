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


def main(inp):
    inp = inp.strip().lstrip('^').rstrip('$')

    edges = defaultdict(set)
    positions = frozenset([(0, 0)])
    stack = []
    for i, c in enumerate(inp):
        #print('hello, char={}, positions={}, stack={}, edges={}'.format(
        #    c, set(positions), stack, edges))
        if c.isalpha():
            newpositions = []
            for pos in positions:
                npos = move(pos, c)
                edges[npos].add(pos)
                edges[pos].add(npos)
                newpositions.append(npos)
            positions = frozenset(newpositions)
        elif c == '(':
            stack.append((positions, frozenset()))
        elif c == '|':
            positions, old_acc = stack[-1]
            stack[-1] = positions, old_acc | positions
        elif c == ')':
            _, old_acc = stack.pop(-1)
            positions = old_acc | positions
        else:
            print('invalid char', c)
            assert False

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
