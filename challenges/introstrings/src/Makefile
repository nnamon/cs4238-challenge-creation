CFLAGS?=-Wall
LIBS?=
all: introstrings

clean:
	rm -f introstrings *.o core core.*

introstrings: introstrings.o
	${CC} ${CFLAGS} -o introstrings introstrings.o ${LIBS}
