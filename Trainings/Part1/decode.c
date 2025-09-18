#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char **argv)
{
	int arg = 1;
	char *decoded = malloc(strlen(argv[arg])/2+1);
	int j = 0;
	printf("Arg %d = %s\n", argc, argv[arg]);

	for (int i=0; i<strlen(argv[arg]); i=i+2) {
		if ((argv[arg][i] <= 'z') && (argv[arg][i]>= 'a'))
		{
			decoded[j] = argv[arg][i];
			j++;
		}
	}
	printf("j=%d", j);

	decoded[j] = 0;

	printf("Decoded = %s\n", decoded);
}
