
int main(void) {
line5:
  var2 = 0;

line6:
  var5 = var2 | 65536;
  var2 = 4843319;

line8:
  var4 = var5 & 255;
  var2 = (var2 + var4) & 0xffffff;
  var2 = (var2 * 65899) & 0xffffff;

line13:
  if (256 > var5) {
    goto line28;
  }

line17:
  var4 = 0;

line18:
  var3 = (var4 + 1) * 256;

line20:
  if (var3 > var5) {
    goto line26;
  }

line24:
  var4 += 1;
  goto line18;

line26:
  var5 = var4;
  goto line8;

line28:
  if (var2 == var0) {
    exit(0);
  }
  goto line6;
}
