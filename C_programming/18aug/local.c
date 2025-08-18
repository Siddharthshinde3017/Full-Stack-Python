#include<stdio.h>

void test(){  
    int num = 110; // local variable - local variables are used within a block of code we cannot use it in another block
    printf("%d", num);
}
void demo(){
    // printf("%d",num);// gives us error 
}

void main(){
    test();
    demo();
}