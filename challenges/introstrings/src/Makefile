CFLAGS?=-Wall
LIBS?=
all: introstrings

clean:
	rm -f introstrings *.o core core.*

authed: introstrings.o
	${CC} ${CFLAGS} -o introstrings introstrings.o ${LIBS}
