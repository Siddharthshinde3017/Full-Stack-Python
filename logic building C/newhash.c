#include <stdio.h>

void  main() {
    int r, c;
    for (r = 1; r <= 4; r++) {
        for (c = 1; c <= 5; c++) {
            if (r == 1 || r == 4 || c == 1 || c == 5)
                printf("#");
            else
                printf(" ");
        }
        printf("\n");
    }
   
}
