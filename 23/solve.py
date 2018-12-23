#!/usr/bin/env python3

import re
import sys
import random
from itertools import product

is_sample = False


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'-?\d+', text)]


def get_dist(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def parse_line(line):
    x, y, z, r = parse_ints(line)
    return ((x, y, z), r)


def main(A):
    A = A.splitlines()
    A = [parse_line(line) for line in A]

    def get_radius(robot):
        pos, r = robot
        return r

    def is_in_range(robot, pos):
        robot_pos, r = robot
        return get_dist(robot_pos, pos) <= r

    strongest = max(A, key=get_radius)
    others = [
        robot for robot in A
        if is_in_range(strongest, robot[0])
    ]

    res = len(others)
    print('Part 1', res)


    overall_best_score = (0, 0)

    def try_area(area, old_skip):
        nonlocal overall_best_score

        # score = (num_in_range, -dist_to_origin)
        best_score = (0, 0)
        best_points = []

        for pos in area:
            num_in_range = len([
                1 for robot in A
                if is_in_range(robot, pos)
            ])
            mine = (num_in_range, -get_dist(pos, (0,0,0)))
            if mine > best_score:
                best_score = mine
                best_points = [pos]
                #print('new best score', best_score)
            elif mine == best_score:
                best_points.append(pos)

        #print('best_score', best_score)

        if best_score > overall_best_score:
            overall_best_score = best_score

        if old_skip == 1:
            #print('returning from try_area, skip == 1')
            return

        radius = old_skip
        skip = max(radius // 2, 1)  # smaller divisor is faster!!

        # Only examine one point...??
        # They are all tied, but this is a bit questionable
        # Seems to work though, even when randomly picked!
        for guess in [random.choice(best_points)]:
            area = product(*[
                range(guess[i] - radius, guess[i] + radius + skip + 1, skip)
                for i in range(3)
            ])
            #print('try_area, radius={}, skip={}, guess={}'.format(
            #    radius, skip, guess))
            try_area(area, skip)


    # initial area covers all given points
    xs = sorted(set([p[0] for p,r in A]))
    ys = sorted(set([p[1] for p,r in A]))
    zs = sorted(set([p[2] for p,r in A]))

    skip = 100000000
    area = product(
        range(min(xs), max(xs)+1, skip),
        range(min(ys), max(ys)+1, skip),
        range(min(zs), max(zs)+1, skip),
    )
    try_area(area, skip)
    print('Part 2', -overall_best_score[1])


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
