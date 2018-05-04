CFLAGS?=-Wall
LIBS?=
all: babypwn

clean:
	rm -f babypwn *.o core core.*

babypwn: babypwn.o
	${CC} ${CFLAGS} -o babypwn babypwn.o ${LIBS}
