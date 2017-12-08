/* loader.c */

/* TODO: Include appropriate headers */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    /* TODO: Declare an array large enough to hold the raw bytes. 
	Raw bytes are best stored in byte-addressable arrays. Pick the appropriate type. Call it "raw_bytes"*/
    /* TODO: Declare a function pointer type that matches the calc function's type. Call it  "Calc_fptr" */
    unsigned char raw_bytes[1024];
    typedef int (*Calc_fptr)(char, int, int);

    FILE *fp;
    unsigned int i = 0;
    long fSize;
    Calc_fptr calculator;

    /* TODO if number of arguments is not 4 (5 including program name)
		print ("Usage %s <filename> <uint> <operation> <uint>\n", argv[0]) and exit */
    if (argc != 5) {
        printf("Usage %s <filename> <uint> <operation> <uint>\n", argv[0]);
        return 0;
    }

    /* TODO: Open and read the binary file into raw_bytes. Use fopen and fread. */

    fp = fopen(argv[1], "rb");
    fseek(fp, 0, SEEK_END);
    fSize = ftell(fp);
    //printf("%d\n", fSize);
	rewind(fp);
    fread(raw_bytes, sizeof(unsigned char), fSize, fp);
    //for (int k = 0; k <= 99; k++) {
    //    printf("%02x", raw_bytes[k]);
    //}

    calculator = (Calc_fptr)raw_bytes;
    /* TODO: Print the result. Refer to sample input and output. */
    i = (*calculator)(argv[3][0], atoi(argv[2]), atoi(argv[4]));
    printf("%d %c %d = %d\n", atoi(argv[2]), argv[3][0], atoi(argv[4]), i);
    return 0;
}
