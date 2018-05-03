#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "art.h"

void get_shell() {
    system("/bin/sh");
}

void vuln() {
    unsigned long long canary_val = 0;
    char buffer[256];
    asm("mov %%fs:0x28, %0" :"=r"(canary_val));
    printf("Overflow? [%llu]: ", canary_val);
    read(0, buffer, 512);
    puts("Overflow!");
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    puts(art);
    puts("Can you get a shell?");
    vuln();
    puts("Goodbye!");
}
