#!/usr/bin/env python3

import re
import sys
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product

is_sample = False


def main(A):
    target = list(map(int, str(A).strip()))
    A = int(A)

    recipes = [3, 7]
    a = 0
    b = 1

    while len(recipes) < A + len(target):
        s = list(map(int, str(recipes[a]+recipes[b])))
        recipes.extend(s)
        a = (a + 1 + recipes[a]) % len(recipes)
        b = (b + 1 + recipes[b]) % len(recipes)
        #print(a, b, recipes)

    res = [recipes[A+i] for i in range(len(target))]
    res = ''.join(map(str, res))
    print('Part 1', res)


    # reinitialize
    recipes = [3, 7]
    a = 0
    b = 1

    def check():
        base = len(recipes) - len(target)
        for j in range(len(target)):
            if recipes[base+j] != target[j]:
                return False
        return True

    while True:
        s = list(map(int, str(recipes[a]+recipes[b])))
        done = False
        for n in s:
            recipes.append(n)
            if check():
                done = True
                #print(recipes[-len(target):])
                break
        if done:
            break

        a = (a + 1 + recipes[a]) % len(recipes)
        b = (b + 1 + recipes[b]) % len(recipes)
    
    print('Part 2', len(recipes) - len(target))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
        A = open('sample.txt').read()
        is_sample = True
    else:
        A = open('input.txt').read()
    main(A)
