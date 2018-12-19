Part 1 was pretty straightforward implementation based on Day 16.

Part 2... first I tried converting it into C code, which took quite a good
while, expectedly. Somewhere along the way I noticed, with confirmation
from printing some outputs, that lines 17+ were only used for an
initialization phase, and the preceding lines were the actual meat of the
problem. 

After a while it became obvious it was checking for factors of the number
in register 2 by brute-forcing all combinations of factors in registers
1 and 5. I tried entering the number of factors and thereby wasted around
10 crucial minutes. But in fact, it was the
[sum of all factors](https://www.wolframalpha.com/input/?i=sum+of+all+divisors+of+10551376)
that I needed to complete my quest...

Afterwards I wrote some code to automatically detect when the target
number was computed, and find all factors in Python, which feels relatively
nice and clean.
