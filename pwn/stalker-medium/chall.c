#include <stdio.h>
#include <stdlib.h>

__attribute__((naked)) void gadgets() {
  asm volatile ("pop %rdi ; ret");
}

void SNITCHSNITCHSNITCH(long long alice) {
  FILE* charlie = fopen("flag.txt", "r");

  if (alice != 0xcafebabe) {
    puts("Fake info...");

    exit(-1);
  }

  char bob[64];
  fgets(bob, 64, charlie);

  printf("%s\n", bob);
}

void house() {
  char alice[16];
  
  puts("You have entered the house...");
  puts("As you look around the corner, you see him with some illegal substance 0xcafebabe!!!");
  puts("YOU MUST SNITCH!!!");
  printf(">>> ");

  fgets(alice, 64, stdin);
}

void start() {
  char alice[16];

  puts("You are suspecting your neighbor is against Big Brother!");
  puts("As a responsible citizen, it is your duty to find more about it. YOU MUST STALK HIM!");
  puts("\nAttempt to enter the house...");
  printf(">>> ");

  fgets(alice, 38, stdin);
}

int main() {
  start();

  return 0;
}
