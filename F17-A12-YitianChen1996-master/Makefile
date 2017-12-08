all: loader hellosh

loader: loader.c
	gcc loader.c -W -z execstack -std=c99 -m32 -o loader

hellosh: hellosh_defines.c hellosh_defines.h hellosh.c
	gcc hellosh_defines.c hellosh.c -std=c99 -o hellosh

.PHONY: clean
clean:
	rm -f loader hellosh
	rm -f *.o
	rm -f *~ \#*\# *.swp
