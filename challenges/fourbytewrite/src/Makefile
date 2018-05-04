CFLAGS?=-Wall
LIBS?=
all: fourbytewrite

clean:
	rm -f fourbytewrite *.o core core.*

authed: babyre.o
	${CC} ${CFLAGS} -o fourbytewrite fourbytewrite.o ${LIBS}
