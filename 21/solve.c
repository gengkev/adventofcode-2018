#include <stdio.h>
#include <stdbool.h>

bool visited[0x1000000];
long long last_visited = -1;

int main(void) {
  long long var2 = 0;

  while (true) {
    long long var5 = var2 | 65536;
    var2 = 4843319;

    while (true) {
      var2 = (var2 + (var5 & 255)) & 0xffffff;
      var2 = (var2 * 65899) & 0xffffff;

      if (var5 < 256) {
        break;
      }

      var5 = var5 / 256;
    }

    //if (var2 == var0) {
    //  break;
    //}

    /* BEGIN ANSWER-PRINTING */

    // Hash collision means we'll never terminate from now on
    if (visited[var2]) {
      printf("Part 2 %lld\n", last_visited);
      break;
    }

    // First time we've reached this point
    if (last_visited == -1) {
      printf("Part 1 %lld\n", var2);
    }

    visited[var2] = true;
    last_visited = var2;

    /* END ANSWER-PRINTING */
  }

  return 0;
}
