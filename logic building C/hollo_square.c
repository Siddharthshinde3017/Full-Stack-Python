    #include <stdio.h>

    void main() {
        int r, c;

        for (r = 1; r < 5; r++) {
            for (c = 1; c < 6; c++) {
                if(r==1||r==4||c==1||c==5){
                    printf("*");
                }
                else{
                    printf(" ");
                }
                
            }
            printf("\n");  // Correct newline
        }
    }