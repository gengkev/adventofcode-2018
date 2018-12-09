#!/usr/bin/env python3

import re
import sys
from collections import deque


def parse_ints(text):
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]


def solve(players, marbles):
  A = deque([0])
  all_scores = [0 for _ in range(players)]

  for n in range(1, marbles):
    p = (n-1) % players
    #print('n =', n, 'p =', p)

    if n % 23 == 0:
      #print('HELLO', A)
      score = n
      A.rotate(7)
      score += A.popleft()
      #print('score', score)
      all_scores[p] += (score)

    else:
      #print(n, A)
      A.rotate(-2)
      A.appendleft(n)

  return max(all_scores)


def main(A):
  players, marbles = parse_ints(A)
  print('Part 1', solve(players, marbles))
  print('Part 2', solve(players, marbles * 100))


if __name__ == '__main__':
  if len(sys.argv) >= 2 and sys.argv[1].startswith('s'):
    A = open('sample.txt').read()
  else:
    A = open('input.txt').read()
  main(A)