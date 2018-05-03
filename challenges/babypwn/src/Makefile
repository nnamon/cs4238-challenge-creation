CFLAGS?=-Wall
LIBS?=
all: babypwn

clean:
	rm -f babypwn *.o core core.*

authed: babyre.o
	${CC} ${CFLAGS} -o babypwn babypwn.o ${LIBS}
