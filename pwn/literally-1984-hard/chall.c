#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "img.c"

char flag[64];

void menu() {
  puts("===================================");
  puts("1. Send a funny message");
  puts("2. Print something funny and quirky");
  puts("3. Exit");
  puts("===================================");
}

void funny_message() {
  char buf[16];

  puts("Announce to the world how funny you are with a message");
  printf(">>> ");

  fgets(buf, 32, stdin);
}

void print_stuff(char* str) {
  char temp[64];

  strcpy(temp, str);

  for (int i = 0; i < 10; i++) {
    printf("%s ", temp);
  }

  putchar(10);
}

int main() {
  FILE* fd = fopen("flag.txt", "r"); 
  char choice[8];

  fgets(flag, 64, fd);

  printf("%s\n\nMy son, Aiden, is the comedian of the family! He is literally obsessed with making jokes about the movie 1984 and they are HILARIOUS!!!\n\n", img);

  while (1) {
    menu();
    printf(">>> ");
    fgets(choice, 4, stdin);

    switch(atoi(choice)) {
      case 1:
        funny_message();
        break;

      case 2:
        print_stuff("literally 1984");
        break;

      case 3:
        exit(0);
        break;
    }
  }

  return 0;
}
