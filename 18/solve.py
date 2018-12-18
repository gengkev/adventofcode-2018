#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


def next_grid(grid):
    N = len(grid)
    M = len(grid[0])
    def is_valid(p):
        i, j = p
        return 0 <= i < N and 0 <= j < M
    def get_nbrs(i, j):
        return filter(is_valid, [
            (i-1,j),(i+1,j),(i,j-1),(i,j+1),
            (i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1),
        ])
    def get_pos(i, j):
        if grid[i][j] == '.':
            cnt = len([nbr for nbr in get_nbrs(i, j)
                if grid[nbr[0]][nbr[1]] == '|'])
            return '|' if cnt >= 3 else '.'
        elif grid[i][j] == '|':
            cnt = len([nbr for nbr in get_nbrs(i, j)
                if grid[nbr[0]][nbr[1]] == '#'])
            return '#' if cnt >= 3 else '|'
        elif grid[i][j] == '#':
            cnt1 = len([nbr for nbr in get_nbrs(i, j)
                if grid[nbr[0]][nbr[1]] == '|'])
            cnt2 = len([nbr for nbr in get_nbrs(i, j)
                if grid[nbr[0]][nbr[1]] == '#'])
            return '#' if cnt1 >= 1 and cnt2 >= 1 else '.'

    new_grid = [[get_pos(i, j) for j in range(M)] for i in range(N)]
    return new_grid


def print_grid(grid):
    print('\n'.join(''.join(row) for row in grid))


def main(A):
    A = A.splitlines()
    visited_grids = {}
    scores = []

    for i in range(600):
        A = next_grid(A)
        #print('\ni = ', i)
        #print_grid(A)

        wooded = len([
            1 for i, j in product(range(len(A)), range(len(A[0])))
            if A[i][j] == '|'])
        lumber = len([
            1 for i, j in product(range(len(A)), range(len(A[0])))
            if A[i][j] == '#'])
        res = wooded * lumber

        Afreeze = tuple(map(tuple, A))
        if Afreeze in visited_grids:
            oldi = visited_grids[Afreeze]
            #print('already visited. current', i, oldi)
            break
        else:
            visited_grids[Afreeze] = i
        scores.append(wooded * lumber)

    target = 1000000000-1
    n = i - oldi
    t = oldi + (target - oldi) % n
    #print('scores[t] = ', scores[t], t, n)

    print('Part 1', scores[10-1])
    print('Part 2', scores[t])
    print(len(A), len(A[0]))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
