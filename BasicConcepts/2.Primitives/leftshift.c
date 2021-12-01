#include <stdio.h>
int main()
{
    unsigned long int a = 10;
    unsigned int b = 100;

    for(unsigned int i=1; i<=b; i++)
    {
        printf("a>> %d = %lu\n",i, a<<i);
    }
}
