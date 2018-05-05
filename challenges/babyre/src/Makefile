CFLAGS?=-Wall
LIBS?=
all: babyre

clean:
	rm -f babyre *.o core core.*

babyre: babyre.o
	${CC} ${CFLAGS} -o babyre babyre.o ${LIBS}
