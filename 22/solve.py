#!/usr/bin/env python3

import re
import sys
import functools
import heapq

is_sample = False

ROCKY = 0
WET = 1
NARROW = 2

NEITHER = 0
TORCH = 1
CLIMBING = 2


# global variables yay
depth = -1
target = None


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


@functools.lru_cache(maxsize=None)
def get_erosion(i, j):
    if (i, j) in [(0, 0), target]:
        index = 0
    elif i == 0:
        index = (j * 16807)
    elif j == 0:
        index = (i * 48271)
    else:
        index = get_erosion(i-1, j) * get_erosion(i, j-1)
    return (index + depth) % 20183


def get_region(pos):
    i, j = pos
    return get_erosion(i, j) % 3


def get_adj(pos):
    i, j = pos
    adj = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    return [
        (ni, nj) for ni, nj in adj
        if ni >= 0 and nj >= 0
    ]


def get_neighbors(node):
    pos, tool = node
    assert tool != get_region(pos)

    # Move to neighboring regions, keeping same tool
    out = []
    for npos in get_adj(pos):
        nregion = get_region(npos)
        if nregion != tool:
            out.append((1, (npos, tool)))

    # Stay in same region but switch tool
    for ntool in range(3):
        if ntool != tool and ntool != get_region(pos):
            out.append((7, (pos, ntool)))

    #print('get_neighbors', node, '->', out)
    return out


def dijkstra(source, goal):
    visited = {}
    q = []

    heapq.heappush(q, (0, source))

    while q:
        cost, cur = heapq.heappop(q)
        #print('dequeued', cost, pos, tool)

        if cur in visited:
            continue
        visited[cur] = cost

        if cur == goal:
            break

        for edge_cost, nxt in get_neighbors(cur):
            ncost = cost + edge_cost
            if nxt not in visited:
                #print('adding to queue', ncost, npos, ntool)
                heapq.heappush(q, (ncost, nxt))

    if not q:
        print('queue exited normally D:')
    return visited[goal]


def main(A):
    global depth, target
    A = A.splitlines()
    depth = parse_ints(A[0])[0]
    tj, ti = tuple(parse_ints(A[1]))
    target = (ti, tj)

    '''
    erosion = [[0 for _ in range(tj+1)] for _ in range(ti+1)]
    cost = 0
    for i in range(ti+1):
        for j in range(tj+1):
            if (i, j) in [(0, 0), (ti, tj)]:
                index = 0
            elif i == 0:
                index = (j * 16807)
            elif j == 0:
                index = (i * 48271)
            else:
                index = erosion[i-1][j] * erosion[i][j-1]
            erosion[i][j] = (index + depth) % 20183
            cost += (erosion[i][j] % 3)
            print(i, j, erosion[i][j])
    '''

    cost = 0
    for i in range(ti+1):
        for j in range(tj+1):
            cost += get_region((i, j))

    print('Part 1', cost)

    source = ((0, 0), TORCH)
    goal = (target, TORCH)
    cost = dijkstra(source, goal)

    print('Part 2', cost)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
