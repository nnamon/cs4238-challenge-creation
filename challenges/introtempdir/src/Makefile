CFLAGS?=-Wall
LIBS?=
all: introtempdir

clean:
	rm -f introtempdir *.o core core.*

authed: introtempdir.o
	${CC} ${CFLAGS} -o introtempdir introtempdir.o ${LIBS}
