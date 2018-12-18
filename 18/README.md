I think my code always ends up as some weird mixture of imperative/C-like,
Pythonic (list comprehensions), and functional style, or rather just
whatever the first thing I think of is. This is sometimes a liability:
one of my bugs this time was mixing up i and j in the list comprehension
to create `new_grid`, since I'm always used to writing i before j. Oops.

Related to that, I always try to use (y, x) since that's the same as (i, j),
except when parsing input. Since the AOC style always has the origin in the
top left, that helps avoid confusion (except that input coordinates are
often provided in the (x, y) order).

The other bug I had was computing the correct index corresponding to
the target (1 billion) once a cycle in grid states was detected, since
I mixed up `oldi` and `i`. I also got bitten by an off-by-one similar to
one in a previous day which I avoided then. Oof.
