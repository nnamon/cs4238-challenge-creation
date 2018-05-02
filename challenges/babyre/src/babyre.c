#include <stdio.h>
#include <string.h>

char * book1[] = {"rub", "tile", "dilute", "attention", "assertive", "shaft", "dish", "snake", "beg", "calf"};
char * book2[] = {"ignorant", "particular", "slime", "evening", "literature", "mark", "predict", "cat", "morning", "waiter"};
char * book3[] = {"pill", "provoke", "application", "extinct", "moving", "makeup", "whole", "thanks", "attic", "licence"};
char * book4[] = {"wind", "seat", "stunning", "polite", "joystick", "positive", "boom", "debate", "elephant", "candle"};
char * book5[] = {"aloof", "campaign", "purpose", "retired", "replace", "acquit", "respectable", "ex", "interface", "bottom"};
char * book6[] = {"infrastructure", "testify", "inhibition", "place", "garlic", "win", "bleed", "wrong", "stream", "ear"};
char * book7[] = {"rich", "ticket", "camera", "shrink", "tourist", "fall", "large", "terms", "ranch", "craftsman"};

int codes[] = {4, 9, 7, 3, 3, 7, 4};
char ** booksbook[] = {book1, book2, book3, book4, book5, book6, book7};

int main(int argc, char * argv[]) {

    if (argc < 8) {
        puts("Bad arguments.");
        return -1;
    }

    for (int i = 0; i < 7; i++) {
        if (strcmp(argv[i+1], booksbook[i][codes[i]])) {
            puts("Incorrect password.");
            return i;
        }
    }

    printf("Your password is %s-%s-%s-%s-%s-%s-%s.\n", argv[1], argv[2], argv[3], argv[4], argv[5], argv[6], argv[7]);
}
