#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "out.c"


char flag[] = "\x0f\x0f\x0e\x21\x13\x16\x5c\x3a\x09\x5c\x06\x5e\x3a\x62\x25\x5e\x3a\x0f\x61\x2b\x11\x3a\x62\x25\x5e\x14\x3a\x61\x1f\x5e\x3a\x0e\x25\x5c\x09\x29\x18";

unsigned char machine(char* command) {
  unsigned char regs[2];
  unsigned char rip = 0;

  while (rip < strlen(command)) {
    switch (*(command + rip)) {
      // mov reg, val
      case 1:
        if (*(command + rip + 1) > 2) {
          puts("PANIC 1");
          exit(-1);
        }

        regs[*(command + rip + 1) - 1] = *(command + rip + 2);
        rip += 3;
        
        break;

      // mov reg, reg
      case 2:
        if (*(command + rip + 1) > 2 || *(command + rip + 2) > 2) {
          puts("PANIC 2");
          exit(-1);
        }

        regs[*(command + rip + 1) - 1] = regs[*(command + rip + 2) - 1];
        rip += 3;

        break;

      // xor reg, reg
      case 3:
        if (*(command + rip + 1) > 2 || *(command + rip + 2) > 2) {
          puts("PANIC 3");
          exit(-1);
        }

        regs[*(command + rip + 1) - 1] ^= regs[*(command + rip + 2) - 1];
        rip += 3;

        break;

      // inc reg
      case 4:
        if (*(command + rip + 1) > 2) {
          puts("PANIC 4");
          exit(-1);
        }

        regs[*(command + rip + 1) - 1]++;
        rip += 2;

        break;

      // ret
      case 5:
        return regs[0];

      default:
        puts("PANIC D");
        exit(-1);
        break;
    }
  }

  return regs[0];
}

int main() {
  /*
   * mov reg[1], 0x67
   * inc reg[1]
   * mov reg[0], reg[1]
   * inc reg[0]
   * mov reg[1], <cur_char>
   * xor reg[1], reg[0]
   * mov reg[0], reg[1]
   * inc reg[0]
   * inc reg[0]
   * inc reg[0]
   * inc reg[0]
   * ret
   *
   * THIS IS TECHNICALLY JUST A (char ^ 0x69) + 4
   * */

  char final[128];
  char input[64];

  printf("%s\n", img);

  printf(">>> ");
  fgets(input, 62, stdin);
  *strchr(input, '\n') = 0;

  for (int i = 0; i < strlen(input); i++) {
    memset(final, 0, 128);

    char temp[] = "\x01\x02\x67\x04\x02\x02\x01\x02\x04\x01\x01\x02";

    strcat(final, temp);
    *(final + strlen(final)) = input[i];

    char temp2[] = "\x03\x02\x01\x02\x01\x02\x04\x01\x04\x01\x04\x01\x04\x01\x05";
    strcat(final, temp2);

    *(input + i) = machine(final);
  }

  if (strlen(flag) != strlen(input) || strcmp(flag, input)) {
    puts("Wrong input, sorry :(");

    exit(-1);
  }

  puts("Correct!");

  return 0;
}


