CFLAGS?=-Wall
LIBS?=
all: fourbytewrite

clean:
	rm -f fourbytewrite *.o core core.*

fourbytewrite: fourbytewrite.o
	${CC} ${CFLAGS} -o fourbytewrite fourbytewrite.o ${LIBS}
