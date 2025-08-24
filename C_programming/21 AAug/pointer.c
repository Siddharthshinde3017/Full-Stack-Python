#include<stdio.h>

void main 
(){
    int num = 10;
    int *p = &num;

    printf("\n%d",num);
    printf("\n%d", *p);
    printf("\n%d",p);


}