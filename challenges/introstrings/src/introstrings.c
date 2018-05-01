#include <stdio.h>
#include <string.h>

char * flag = "The password is: I_Hide_Qui3tly_In_this_Bin";

void do_secret(char * s) {
    strcpy(s, flag);
}

int main() {
    char secret[256];
    do_secret(secret);
    puts("Can you find the secret in me?");
}
