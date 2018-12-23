For Part 2, what I did was start with a bounding box covering all points,
then tile that box with points at a distance of `skip` from each other.
The number of bots in range is computed for each point, and then the
best-scoring points are selected. The process is repeated with a smaller
tiling in the neighborhood around those points.

There can be multiple best-scoring points, and it probably seems like a
good idea to check all of them. But even just randomly selecting one such
point still works!

No doubt this is because there are a lot of points that work and that give
the correct answer. If the input data were stricter this probably wouldn't
work at all.
