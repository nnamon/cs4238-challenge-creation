#include <stdio.h>

char * key = "\x3f\x13\xba\xb8\xda\xf6\x63\xb6\x8a\x72\xff\x69\x2c\x0b\x33\x1f\xec\xee\x3f\x62\x95\x46\xef\xd7\xf9\x61\xfe\xc5\x1d\xfa\x5d\x7d\xe4\x4e\xfe\x07";
char * encrypted = "\x66\x7c\xcf\xca\xfa\x86\x02\xc5\xf9\x05\x90\x1b\x48\x2b\x5a\x6c\xd6\xce\x5e\x3d\xfd\x29\x82\xb2\xa6\x0e\x98\x9a\x64\xca\x28\x0f\xbb\x21\x89\x69";

int main() {
    char flag[37] = {0};
    for (int i = 0; i < 36; i++) {
        flag[i] = key[i] ^ encrypted[i];
    }

    puts("Hello, I will create a file called 'password.txt' in this directory.");

    FILE *fp;
    fp = fopen("password.txt","w");
    if (!fp) {
        puts("Unable to open file for writing. Are you sure you have permissions?");
    }

    fprintf(fp, "%s", flag);
    puts("Successfully written!");

    fclose(fp);
}
