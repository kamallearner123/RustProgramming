#include <stdio.h>
short main()
{
    short a=-100, b=-15;
    short c;
    c = (short) ((unsigned short)a/(unsigned short)b);
    prshortf("c=%d\n", c);
}
