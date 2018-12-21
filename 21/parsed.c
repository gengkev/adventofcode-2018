#include <stdio.h>
#include <stdbool.h>

bool visited[0x1000000];
long long last_visited = -1;

int main(void) {
  //long long reg0 = 0LL;
  long long reg1 = 0LL;
  long long reg2 = 0LL;
  long long reg3 = 0LL;
  long long reg4 = 0LL;
  long long reg5 = 0LL;

  bool done = false;
  while (!done) {
    switch (reg1) {
    case 0:
      reg2 = 123LL;
      reg1++;

    case 1:
      reg2 = reg2 & 456LL;
      reg1++;

    case 2:
      reg2 = reg2 == 72LL;
      reg1++;

    case 3:
      reg1 = reg2 + reg1;
      break;

    case 4:
      reg1 = 0LL;
      break;

    case 5:
      reg2 = 0LL;
      reg1++;

    case 6:
      reg5 = reg2 | 65536LL;
      reg1++;

    case 7:
      reg2 = 4843319LL;
      reg1++;

    case 8:
      reg4 = reg5 & 255LL;
      reg1++;

    case 9:
      reg2 = reg2 + reg4;
      reg1++;

    case 10:
      reg2 = reg2 & 16777215LL;
      reg1++;

    case 11:
      reg2 = reg2 * 65899LL;
      reg1++;

    case 12:
      reg2 = reg2 & 16777215LL;
      reg1++;

    case 13:
      reg4 = 256LL > reg5;
      reg1++;

    case 14:
      reg1 = reg4 + reg1;
      break;

    case 15:
      reg1 = reg1 + 1LL;
      break;

    case 16:
      reg1 = 27LL;
      break;

    case 17:
      reg4 = 0LL;
      reg1++;

    case 18:
      reg3 = reg4 + 1LL;
      reg1++;

    case 19:
      reg3 = reg3 * 256LL;
      reg1++;

    case 20:
      reg3 = reg3 > reg5;
      reg1++;

    case 21:
      reg1 = reg3 + reg1;
      break;

    case 22:
      reg1 = reg1 + 1LL;
      break;

    case 23:
      reg1 = 25LL;
      break;

    case 24:
      reg4 = reg4 + 1LL;
      reg1++;

    case 25:
      reg1 = 17LL;
      break;

    case 26:
      reg5 = reg4;
      reg1++;

    case 27:
      reg1 = 7LL;
      break;

    case 28:
      //reg4 = reg2 == reg0;
      reg4 = 0;

      /* BEGIN ANSWER-PRINTING */

      // Hash collision means we'll never terminate from now on
      if (visited[reg2]) {
        printf("Part 2 %lld\n", last_visited);
        done = true;
        break;
      }

      // First time we've reached this point
      if (last_visited == -1) {
        printf("Part 1 %lld\n", reg2);
      }

      visited[reg2] = true;
      last_visited = reg2;

      /* END ANSWER-PRINTING */
      reg1++;

    case 29:
      reg1 = reg4 + reg1;
      break;

    case 30:
      reg1 = 5LL;
      break;

    default:
      printf("Out of range: %lld\n", reg1);
      done = true;
    }
    reg1++;
  }
  return 0;
}
