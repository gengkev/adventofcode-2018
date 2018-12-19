#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main() {
  long long reg[6] = {0};
  reg[0] = 1;

line0:
  goto line17;

line1:
  reg[1] = 1;
line2:
  reg[5] = 1;

line3:
  reg[3] = reg[1] * reg[5];

line4:
  reg[3] = (reg[3] == reg[2]) ? 1 : 0;
  if (reg[3] == 1) {
    printf("hello at line4, [%lld, %lld, %lld, %lld, n/a, %lld]\n",
        reg[0], reg[1], reg[2], reg[3], reg[5]);
    reg[0] = reg[1] + reg[0];
  }
  reg[5] = reg[5] + 1;

line9:
  reg[3] = (reg[5] > reg[2]) ? 1 : 0;
  if (reg[3] == 0) {
    goto line3;
  }
  reg[1] = reg[1] + 1;

line13:
  reg[3] = (reg[1] > reg[2]) ? 1 : 0;
  if (reg[3] == 0) {
    goto line2;
  }
  printf("and that's the end\n");
  exit(0);

line17:
  reg[2] = reg[2] + 2;
  reg[2] = reg[2] * reg[2];
  reg[2] = 19 * reg[2];
  reg[2] = reg[2] * 11;

line21:
  reg[3] = reg[3] + 6;
  reg[3] = reg[3] * 22;
  reg[3] = reg[3] + 8;
  reg[2] = reg[2] + reg[3];

line25:
  switch (reg[0]) {
  case 0:
    goto line26;
  case 1:
    goto line27;
  case 2:
    goto line28;
  case 3:
    goto line29;
  case 4:
    goto line30;
  case 5:
    goto line31;
  case 6:
    goto line32;
  case 7:
    goto line33;
  case 8:
    goto line34;
  case 9:
    goto line35;
  default:
    printf("failed to jump, reg[0] = %lld\n", reg[0]);
    exit(0);
  }
line26:
  goto line0;
line27:
  reg[3] = 27;
line28:
  reg[3] = reg[3] * 28;
line29:
  reg[3] = 29 + reg[3];
line30:
  reg[3] = 30 * reg[3];
line31:
  reg[3] = reg[3] * 14;
line32:
  reg[3] = reg[3] * 32;
line33:
  reg[2] = reg[2] + reg[3];
line34:
  reg[0] = 0;
line35:
  goto line1;
}

