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

line0:
  reg2 = 123LL;
  reg1++;
line1:
  reg2 = reg2 & 456LL;
  reg1++;
line2:
  reg2 = reg2 == 72LL;
  reg1++;
line3:
  reg1 = reg2 + reg1;
  reg1++;
  goto jump;

line4:
  reg1 = 0LL;
  reg1++;
  goto jump;

line5:
  reg2 = 0LL;
  reg1++;
line6:
  reg5 = reg2 | 65536LL;
  reg1++;
line7:
  reg2 = 4843319LL;
  reg1++;
line8:
  reg4 = reg5 & 255LL;
  reg1++;
line9:
  reg2 = reg2 + reg4;
  reg1++;
line10:
  reg2 = reg2 & 16777215LL;
  reg1++;
line11:
  reg2 = reg2 * 65899LL;
  reg1++;
line12:
  reg2 = reg2 & 16777215LL;
  reg1++;
line13:
  reg4 = 256LL > reg5;
  reg1++;
line14:
  reg1 = reg4 + reg1;
  reg1++;
  goto jump;

line15:
  reg1 = reg1 + 1LL;
  reg1++;
  goto jump;

line16:
  reg1 = 27LL;
  reg1++;
  goto jump;

line17:
  reg4 = 0LL;
  reg1++;
line18:
  reg3 = reg4 + 1LL;
  reg1++;
line19:
  reg3 = reg3 * 256LL;
  reg1++;
line20:
  reg3 = reg3 > reg5;
  reg1++;
line21:
  reg1 = reg3 + reg1;
  reg1++;
  goto jump;

line22:
  reg1 = reg1 + 1LL;
  reg1++;
  goto jump;

line23:
  reg1 = 25LL;
  reg1++;
  goto jump;

line24:
  reg4 = reg4 + 1LL;
  reg1++;
line25:
  reg1 = 17LL;
  reg1++;
  goto jump;

line26:
  reg5 = reg4;
  reg1++;
line27:
  reg1 = 7LL;
  reg1++;
  goto jump;

line28:
  //reg4 = reg2 == reg0;
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
  reg1++;
line29:
  reg1 = reg4 + reg1;
  reg1++;
  goto jump;

line30:
  reg1 = 5LL;
  reg1++;
  goto jump;

jump:
  switch (reg1) {
  case 0: goto line0;
  case 1: goto line1;
  case 2: goto line2;
  case 3: goto line3;
  case 4: goto line4;
  case 5: goto line5;
  case 6: goto line6;
  case 7: goto line7;
  case 8: goto line8;
  case 9: goto line9;
  case 10: goto line10;
  case 11: goto line11;
  case 12: goto line12;
  case 13: goto line13;
  case 14: goto line14;
  case 15: goto line15;
  case 16: goto line16;
  case 17: goto line17;
  case 18: goto line18;
  case 19: goto line19;
  case 20: goto line20;
  case 21: goto line21;
  case 22: goto line22;
  case 23: goto line23;
  case 24: goto line24;
  case 25: goto line25;
  case 26: goto line26;
  case 27: goto line27;
  case 28: goto line28;
  case 29: goto line29;
  case 30: goto line30;
  default:
    printf("Out of range: %lld\n", reg1);
    break;
  }

  return 0;
}
