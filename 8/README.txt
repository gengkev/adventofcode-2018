I think the key for this problem was

1. developing an interface to just get the next integer available in the
   sequence (similar to cin in C++), as opposed to iterating through an
   array of input;
2. using recursion to take advantage of that interface to process child
   nodes correctly without getting a massive headache.
