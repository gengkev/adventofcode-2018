The second part was a bit silly. I realized there was no way I would be
able to run 50 billion iterations with my Python script, or even with a
C program. So there must be some other way to compute the result.

I ended up printing out the counts for each time and what do you know,
it converges to a linear trend after a while. (How this is possible, I am
not sure, but what luck!) So we can get the count for 50 billion generations
through linear interpolation.

I did the linear interpolation in a Python shell, the code for that was
written after getting the star. :)
