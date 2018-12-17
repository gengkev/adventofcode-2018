Well this wasn't great. The code I wrote is pretty terrible and probably
doesn't work correctly in general. But at least it's pretty fast: 0.3s
in pypy3 if the call to `print_grid()` is removed :D

The basic idea is that the `fill_water` fills water starting at a source
position. It finds the base that the water will fall to, then checks if the
water is bounded at that point. If so, it adds the water positions to the
grid. Rinse and repeat.

The first time I got stuck was when I needed to backtrack upwards. In the
code this happens when the start-position has the same y-coordinate as
`level_y`, which is the current y-coordinate that we are filling.

It was hard to figure out what the problem even was, but I made a function
to print the grid, which helped a lot. When doing so, I made a set `ew` to
store all possible flowing-water positions (which might later become
still-water).

I resolved the problem by enqueueing the position immediately above the
current start position, to check later on, whenever I detected that
situation. Since flowing-water positions could later become still-water,
my old way of tracking water became more complex.

However I realized that if I can print the grid, then I can count properly.
So I just reused the same code I used to print the grid, but for counting
instead.

The final hour was wasted due to issues with the grid dimensions. First,
I didn't realize that you could have water flowing in columnx `min_x-1` and
`max_x+1` where `min_x` and `max_x` are the min/max positions of clay.

Next, I didn't realize that you shouldn't count water below `min_y`; I had
started counting at `0`, which is the y-coordinate of the source.
Unfortunately the sample was constructed such that I wouldn't find this
issue. That wasted a lot of time.

Anyway, the code is very bad, and I know the functions `lower_bound` and
`upper_bound` have the wrong names, and poor API design...
