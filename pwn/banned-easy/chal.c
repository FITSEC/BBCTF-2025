#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "img.c"

char message[16];
char ban[32];

void menu() {
  puts("==========================");
  puts("1. Complain");
  puts("2. Send a mean message to Big Brother");
  puts("3. Exit");
  puts("==========================");
}

int main() {
  char choice[8];

  strcpy(ban, "TAXIDERMY A CAT INTO A DRONE");

  while (1) {
    printf("%s\n\t\tYOU SHALL NOT %s\n\n", img, ban);

    if (!strcmp(ban, "LOSE")) {
      FILE* file = fopen("flag.txt", "r");
      char flag[64];
      fgets(flag, 64, file);

      printf("%s\n", flag);
    }

    menu();
    printf(">>> ");
    fgets(choice, 4, stdin);

    switch(atoi(choice)) {
      case 1:
        puts("THIS IS NOT FAIR!!!!\n\n");
        break;

      case 2:
        fgets(message, 64, stdin); 
        *strchr(message, '\n') = 0;
        break;

      case 3:
        exit(0);
        break;
    }
  }

  return 0;
}
