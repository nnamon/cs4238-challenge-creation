#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "art.h"

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    puts(art);
    system("/usr/games/cowsay \"Can you find the shell?\"");

    char * cow_buffer = malloc(12);
    memset(cow_buffer, 0, 12);
    read(0, cow_buffer, 12);
    void * ptr;

    memcpy(&ptr, cow_buffer + 4, 4);
    memcpy(ptr, cow_buffer + 8, 4);

    free(cow_buffer);
}
