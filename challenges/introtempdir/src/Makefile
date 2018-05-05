CFLAGS?=-Wall
LIBS?=
all: introtempdir

clean:
	rm -f introtempdir *.o core core.*

introtempdir: introtempdir.o
	${CC} ${CFLAGS} -o introtempdir introtempdir.o ${LIBS}
