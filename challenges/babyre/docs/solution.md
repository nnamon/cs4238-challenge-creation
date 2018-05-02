# SOLUTION

The binary keeps a few dictionaries to look up the right sequence of code
words.

```c
char * book1[] = {"rub", "tile", "dilute", "attention", "assertive", "shaft", "dish", "snake", "beg", "calf"};
char * book2[] = {"ignorant", "particular", "slime", "evening", "literature", "mark", "predict", "cat", "morning", "waiter"};
char * book3[] = {"pill", "provoke", "application", "extinct", "moving", "makeup", "whole", "thanks", "attic", "licence"};
char * book4[] = {"wind", "seat", "stunning", "polite", "joystick", "positive", "boom", "debate", "elephant", "candle"};
char * book5[] = {"aloof", "campaign", "purpose", "retired", "replace", "acquit", "respectable", "ex", "interface", "bottom"};
char * book6[] = {"infrastructure", "testify", "inhibition", "place", "garlic", "win", "bleed", "wrong", "stream", "ear"};
char * book7[] = {"rich", "ticket", "camera", "shrink", "tourist", "fall", "large", "terms", "ranch", "craftsman"};

int codes[] = {4, 9, 7, 3, 3, 7, 4};
char ** booksbook[] = {book1, book2, book3, book4, book5, book6, book7};
```

The `codes` array contains a list of correct indices and `booksbooks` array
contains an array of dictionaries. To get the right sequence, simply look up
the corret index for the corresponding dictionary.

The binary uses `strcmp` to check that the user input in the arguments matches
the right code words.

```c
    for (int i = 0; i < 7; i++) {
        if (strcmp(argv[i+1], booksbook[i][codes[i]])) {
            puts("Incorrect password.");
            return i;
        }
    }
```

Thus, the player can debug binary and break on the strcmp call to get the right
code word for each iteration.

```shell
(gdb) br *0x000000000040062e
Breakpoint 1 at 0x40062e
(gdb) r 1 2 3 4 5 6 7
Starting program: /vagrant/challenges/babyre/src/babyre 1 2 3 4 5 6 7

Breakpoint 1, 0x000000000040062e in main ()
(gdb) info reg
rax            0x7fffffffe7ba	140737488349114
rbx            0x0	0
rcx            0x8	8
rdx            0x400762	4196194
rsi            0x400762	4196194
rdi            0x7fffffffe7ba	140737488349114
rbp            0x7fffffffe450	0x7fffffffe450
rsp            0x7fffffffe430	0x7fffffffe430
r8             0x400730	4196144
r9             0x7ffff7de7ab0	140737351940784
r10            0x846	2118
r11            0x7ffff7a2d740	140737348032320
r12            0x4004c0	4195520
r13            0x7fffffffe530	140737488348464
r14            0x0	0
r15            0x0	0
rip            0x40062e	0x40062e <main+120>
eflags         0x212	[ AF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) x/s $rsi
0x400762:	"assertive"
(gdb) x/s $rdi
0x7fffffffe7ba:	"1"
(gdb)
```

The first code word is 'assertive'. We simply repeat this for all of the
code words.

Solving the binary:

```shell
$ ./babyre assertive waiter thanks polite retired wrong tourist; echo $?
Your password is assertive-waiter-thanks-polite-retired-wrong-tourist.
```


