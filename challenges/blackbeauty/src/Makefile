CFLAGS?=-Wall
LIBS?=
all: blackbeauty

clean:
	rm -f blackbeauty *.o core core.*

blackbeauty: blackbeauty.o
	${CC} ${CFLAGS} -o blackbeauty blackbeauty.o ${LIBS}
