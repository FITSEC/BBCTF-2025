#include <stdio.h>
#include "out.c"

void func() {
  char buf[0x40];

  puts("\nBig Brother NEEDS YOU to give them your credit card number!");
  printf(">>> ");

  fgets(buf, 0x40, stdin);
  printf(buf);

  puts("Woah! You are missing those wacky numbers in the back. Enter NOW for FREE VBUCKS!");
  printf(">>> ");
  fgets(buf, 0x50, stdin);
}

int main() {
  printf("%s\n\n", img);
  puts("Big Brother needs to register you for 1000000 free vbucks!");
  puts("They only need just a bit of information first.");

  func();

  return 0;
}
