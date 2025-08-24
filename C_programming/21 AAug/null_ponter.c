#include<stdio.h>

void main(){
    int * ptr = NULL;
    int num = 10;
    ptr = &num;

    if (ptr == NULL) //(ptr=='\0')
    {
        printf("nullp pointer");
    }
    else{
        printf("%d",*ptr);
    }
    
}