#!/usr/bin/env python3

import copy
import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False
ELF_TEAM = 'E'


class CombatEnds(Exception):
    pass

class ElfDies(Exception):
    pass


def in_grid(grid, ignore, pos):
    N, M = len(grid), len(grid[0])
    i, j = pos
    return 0 <= i < N and 0 <= j < M \
            and grid[i][j] == '.' and pos not in ignore


def get_nbrs(grid, ignore, pos):
    i, j = pos
    D = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    out = [(i + di, j + dj) for di, dj in D]
    return [
        (ni, nj) for (ni, nj) in out
        if in_grid(grid, ignore, (ni, nj))
    ]


def shortest_path(grid, ignore, start, end):
    visited = {}
    q = deque()

    q.append(start)
    visited[start] = None

    while q and end not in visited:
        cur = q.popleft()
        for nbr in get_nbrs(grid, ignore, cur):
            if nbr not in visited:
                q.append(nbr)
                visited[nbr] = cur

    if end not in visited:
        return None

    out = []
    cur = end
    while cur is not None:
        out.append(cur)
        cur = visited[cur]

    return out[::-1]


def all_shortest_paths(grid, ignore, start):
    visited = {}
    q = deque()

    q.append(start)
    visited[start] = [start]

    while q:
        cur = q.popleft()
        for nbr in get_nbrs(grid, ignore, cur):
            if nbr not in visited:
                q.append(nbr)
                visited[nbr] = visited[cur] + [nbr]

    return visited


def move_unit(grid, units, unit):
    team, attackpwr, hp = units[unit]
    units_sans_moi = set(units.keys()) - {unit}
    #print('units_sans_moi', units_sans_moi)

    # Find all enemy units
    enemies = [
        ek for ek, ev in units.items()
        if ev[0] != team
    ]

    # Combat ends when no enemies
    if len(enemies) == 0:
        raise CombatEnds()

    #print('enemies', enemies)

    # Get in range squares (adj to enemy)
    in_range = []
    for eu in enemies:
        in_range.extend(get_nbrs(grid, units_sans_moi, eu))
    #print('in_range', in_range)

    # Get shortest path to each
    '''
    shortest_paths = []
    for cand in in_range:
        path = shortest_path(grid, units_sans_moi, unit, cand)
        if path is not None:
            shortest_paths.append((len(path), cand, path))
    '''
    spgraph = all_shortest_paths(grid, units_sans_moi, unit)
    shortest_paths = []
    for cand in in_range:
        if cand in spgraph:
            path = spgraph[cand]
            shortest_paths.append((len(path), cand, path))
    #print('shortest_paths', shortest_paths)

    # Can't move anywhere
    if len(shortest_paths) == 0:
        new_unit = unit

    else:
        # Find best path
        best_len, best_cand, best_path = min(shortest_paths)
        #print('best_len, best_cand, best_path', best_len, best_cand, best_path)

        # Best action is to do nothing
        if len(best_path) == 1:
            assert best_path[0] == unit
            new_unit = unit

        # Take first step in direction
        else:
            new_unit = best_path[1]
            #print('new_unit', new_unit)

            assert new_unit not in units_sans_moi
            units[new_unit] = units[unit]
            del units[unit]

    #print('> Unit at {} moved to {}, value {}'.format(
    #    unit, new_unit, (team, attackpwr, hp)))
    return new_unit


def attack_unit(grid, units, unit, raise_elf_dies):
    team, attackpwr, hp = units[unit]

    # find adjacent enemies
    targets = []
    for nbr in get_nbrs(grid, [], unit):
        if nbr in units:
            nteam, nattackpwr, nhp = units[nbr]
            if nteam != team:
                targets.append((nhp, nbr))

    if len(targets) > 0:
        _, target = min(targets)
        tteam, tattackpwr, thp = units[target]
        new_thp = thp - attackpwr

        # target dies
        if new_thp <= 0:
            #print('> Unit {} killed target {} {}'.format(
            #    unit, target, new_thp))
            del units[target]

            if tteam == ELF_TEAM and raise_elf_dies:
                raise ElfDies()

        else:
            #print('> Unit {} attacked target {} {}'.format(
            #    unit, target, new_thp))
            units[target] = (tteam, tattackpwr, new_thp)


def print_grid(grid, units):
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if (i, j) in units:
                team, _, _ = units[(i, j)]
                row.append(team)
            else:
                row.append(grid[i][j])
        print(''.join(row))


def step(grid, units, raise_elf_dies):
    #print('** BEGINNING STEP')
    unit_list = sorted(units.keys())
    elf_dies = False
    for unit in unit_list:
        if unit in units:
            new_unit = move_unit(grid, units, unit)
            attack_unit(grid, units, new_unit, raise_elf_dies)
        else:
            #print('unit already killed, cannot move: {}'.format(unit))
            pass

    #print('** PRINTING GRID')
    #print_grid(grid, units)

    if not units:
        print('units is empty lol')
        raise CombatEnds()

    return elf_dies


def play_game(grid, elf_attackpwr, raise_elf_dies):
    N, M = len(grid), len(grid[0])
    units = {}
    for i, j in product(range(N), range(M)):
        if grid[i][j] in 'GE':
            # i, j, unit team, attack power, HP
            team = grid[i][j]
            attackpwr = elf_attackpwr if team == ELF_TEAM else 3
            units[(i, j)] = (team, attackpwr, 200)
            grid[i][j] = '.'

    t = 0
    while True:
        try:
            step(grid, units, raise_elf_dies)
        except CombatEnds:
            #print('combat ends')
            break
        t += 1
    
    #print('full rounds completed', t)
    res_hp = sum(hp for _, _, hp in units.values())
    #print('sum of remaining hp', res_hp)

    res = t * res_hp
    return res



def main(A):
    grid = [list(line) for line in A.splitlines()]

    res = play_game(copy.deepcopy(grid), 3, False)
    print('Part 1', res)

    p = 4
    while True:
        try:
            #print('playing with p =', p)
            res = play_game(copy.deepcopy(grid), p, True)
        except ElfDies:
            p += 1
        else:
            print('Part 2', res)
            break


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
