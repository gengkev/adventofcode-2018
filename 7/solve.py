#!/usr/bin/env python3

import re
import sys
import heapq
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False

def get_delay(i):
    if is_sample:
        return i + 1
    else:
        return i + 61

def parse_line(line):
    return ord(line[1]) - ord('A'), ord(line[7]) - ord('A')

'''
def visit(G, visited, out, n):
    #print('visited', n, sorted(G[n]))
    if visited[n]:
        return
    for m in sorted(G[n], reverse=True):
        visit(G, visited, out, m)
    out.append(n)
    visited[n] = True
    #print('done visiting', n)
'''

def has_incoming_edges(G, m):
    for u in range(len(G)):
        if m in G[u]:
            return True
    return False


def main(A):
    A = [line.split() for line in A]
    A = list(map(parse_line, A))

    N = 26
    G = [[] for _ in range(N)]
    Grev = [[] for _ in range(N)]
    S = set()
    for u, v in A:
        G[u].append(v)
        Grev[v].append(u)
        S |= {u, v}

    '''
    available = S
    for u, v in A:
        available -= {v}

    visited = [False for _ in range(N)]
    out = []
    out2 = []
    print(available)

    for i in sorted(available):
        print('STARTING TO VISIT', i)
        visit(G, visited, out, i)
        out2 += out[::-1]
        print(out)
        out = []
    '''

    available = set(n for n in S if not has_incoming_edges(G, n))
    out2 = []
    while available:
        n = min(available)
        available -= {n}
        out2.append(n)

        copy = G[n][:]
        for m in copy:
            G[n].remove(m)
            if not has_incoming_edges(G, m):
                available.add(m)



    res = [chr(n + ord('A')) for n in out2]
    res = ''.join(res)
    print('Part 1', res)


    available = set(S)
    nonfinished = set(S)
    def is_dep_satisfied(n):
        return all(i not in nonfinished for i in Grev[n])

    out2 = []
    workers = 2 if is_sample else 5
    w_occup = [0 for _ in range(workers)]
    finish_events = defaultdict(list)

    t = 0
    while nonfinished:
        for i in finish_events[t]:
            nonfinished -= {i}
            out2.append(i)
        nxtarr = sorted(i for i in available if is_dep_satisfied(i))
        #print('t =', t, 'nxtarr =', nxtarr)
        for i in nxtarr:
            d = get_delay(i)
            for w in range(workers):
                if w_occup[w] <= t:
                    #print('assigning i =', i, 'to worker', w)
                    # assign to worker
                    w_occup[w] = t + d
                    finish_events[t+d].append(i)
                    available -= {i}
                    assigned = True
                    break
        t += 1

    res = [chr(n + ord('A')) for n in out2]
    res = ''.join(res)
    #print('res', res)
    print('Part 2', t-1)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    A = A.splitlines()
    main(A)
