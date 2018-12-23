For Part 2, what I did was start with a bounding box covering all points,
then tile that box with points at a distance of `skip` from each other.
The number of bots in range is computed for each point, and then the
best-scoring points are selected. The process is repeated with a smaller
tiling in the neighborhood around those points.

There can be multiple points that all have the best score. It probably
seems like a good idea to check all of them: if there are multiple points
with 600 intersections, that doesn't imply each will have a point with
900 intersections in its neighborhood. But apparently it does, since even
just randomly selecting one of the best-scoring points seems to work!

No doubt this is because there are a lot of points that work and that give
the correct answer. If the input data were stricter that probably wouldn't
work. In fact there's no reason this algorithm should work at all, really,
since it's just sampling points and assuming the score of the neighborhood
around that points will be similar...
