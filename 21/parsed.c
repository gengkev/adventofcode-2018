#include <stdio.h>
#include <stdbool.h>

bool visited[0x1000000];
long long last_visited = -1;

int main(void) {
  //long long reg0 = 0;
  long long reg1 = 0;
  long long reg2 = 0;
  long long reg3 = 0;
  long long reg4 = 0;
  long long reg5 = 0;

  bool done = false;
  while (!done) {
    switch (reg1) {
    case 0:
      reg2 = 123;
      break;
    case 1:
      reg2 = reg2 & 456;
      break;
    case 2:
      reg2 = reg2 == 72;
      break;
    case 3:
      reg1 = reg2 + reg1;
      break;
    case 4:
      reg1 = 0;
      break;
    case 5:
      reg2 = 0;
      break;
    case 6:
      reg5 = reg2 | 65536;
      break;
    case 7:
      reg2 = 4843319;
      break;
    case 8:
      reg4 = reg5 & 255;
      break;
    case 9:
      reg2 = reg2 + reg4;
      break;
    case 10:
      reg2 = reg2 & 16777215;
      break;
    case 11:
      reg2 = reg2 * 65899;
      break;
    case 12:
      reg2 = reg2 & 16777215;
      break;
    case 13:
      reg4 = 256 > reg5;
      break;
    case 14:
      reg1 = reg4 + reg1;
      break;
    case 15:
      reg1 = reg1 + 1;
      break;
    case 16:
      reg1 = 27;
      break;
    case 17:
      reg4 = 0;
      break;
    case 18:
      reg3 = reg4 + 1;
      break;
    case 19:
      reg3 = reg3 * 256;
      break;
    case 20:
      reg3 = reg3 > reg5;
      break;
    case 21:
      reg1 = reg3 + reg1;
      break;
    case 22:
      reg1 = reg1 + 1;
      break;
    case 23:
      reg1 = 25;
      break;
    case 24:
      reg4 = reg4 + 1;
      break;
    case 25:
      reg1 = 17;
      break;
    case 26:
      reg5 = reg4;
      break;
    case 27:
      reg1 = 7;
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

      break;
    case 29:
      reg1 = reg4 + reg1;
      break;
    case 30:
      reg1 = 5;
      break;
    default:
      printf("Out of range: %lld\n", reg1);
      done = true;
    }
    reg1++;
  }
  return 0;
}
