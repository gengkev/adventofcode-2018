I was affected by the
[issue with this problem](https://www.reddit.com/r/adventofcode/comments/a3kr4r/2018_day_6_solutions/eb76843/)
for both Part 1 and 2, which is why I didn't get on the scoreboard, and
which is why there's a lot of debugging code where I'm trying to figure
out what I did wrong :(

For this problem I just used a brute force approach, iterating through
all x and y coordinates in a 2D range enclosing all input coordinates.
For part 1, I ran with two different ranges, so that any ranges with
infinite area would change in size, and I could get rid of them by
taking a set intersection.
