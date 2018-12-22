#include <stdio.h>
#include <stdbool.h>

bool visited[0x1000000];
long long last_visited = -1;

int main(void) {
  // long long reg0 = 0LL;
  long long reg1 = 0LL;
  long long reg2 = 0LL;
  long long reg3 = 0LL;
  long long reg4 = 0LL;
  long long reg5 = 0LL;

line0:    reg2 = 123LL;
line1:    reg2 = reg2 & 456LL;
line2:    reg2 = reg2 == 72LL;
line3:    reg1 = reg2 + 3LL + 1;
          goto jump;

line4:    goto line1;

line5:    reg2 = 0LL;
line6:    reg5 = reg2 | 65536LL;
line7:    reg2 = 4843319LL;
line8:    reg4 = reg5 & 255LL;
line9:    reg2 = reg2 + reg4;
line10:   reg2 = reg2 & 16777215LL;
line11:   reg2 = reg2 * 65899LL;
line12:   reg2 = reg2 & 16777215LL;
line13:   reg4 = 256LL > reg5;
line14:   reg1 = reg4 + 14LL + 1;
          goto jump;

line15:   goto line17;

line16:   goto line28;

line17:   reg4 = 0LL;
line18:   reg3 = reg4 + 1LL;
line19:   reg3 = reg3 * 256LL;
line20:   reg3 = reg3 > reg5;
line21:   reg1 = reg3 + 21LL + 1;
          goto jump;

line22:   goto line24;

line23:   goto line26;

line24:   reg4 = reg4 + 1LL;
line25:   goto line18;

line26:   reg5 = reg4;
line27:   goto line8;

line28:   //reg4 = reg2 == reg0;
          reg4 = 0;

          /* BEGIN ANSWER-PRINTING */

          // Hash collision means we'll never terminate from now on
          if (visited[reg2]) {
            printf("Part 2 %lld\n", last_visited);
            return 0;
          }

          // First time we've reached this point
          if (last_visited == -1) {
            printf("Part 1 %lld\n", reg2);
          }

          visited[reg2] = true;
          last_visited = reg2;

          /* END ANSWER-PRINTING */

line29:   reg1 = reg4 + 29LL + 1;
          goto jump;

line30:   goto line6;

jump:
  switch (reg1) {
  case 0:   goto line0;
  case 1:   goto line1;
  case 2:   goto line2;
  case 3:   goto line3;
  case 4:   goto line4;
  case 5:   goto line5;
  case 6:   goto line6;
  case 7:   goto line7;
  case 8:   goto line8;
  case 9:   goto line9;
  case 10:  goto line10;
  case 11:  goto line11;
  case 12:  goto line12;
  case 13:  goto line13;
  case 14:  goto line14;
  case 15:  goto line15;
  case 16:  goto line16;
  case 17:  goto line17;
  case 18:  goto line18;
  case 19:  goto line19;
  case 20:  goto line20;
  case 21:  goto line21;
  case 22:  goto line22;
  case 23:  goto line23;
  case 24:  goto line24;
  case 25:  goto line25;
  case 26:  goto line26;
  case 27:  goto line27;
  case 28:  goto line28;
  case 29:  goto line29;
  case 30:  goto line30;
  default:
    printf("Out of range: %lld\n", reg1);
    break;
  }

  return 0;
}
