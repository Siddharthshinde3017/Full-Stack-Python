#include<stdio.h>

void evenodd(int *ptr)
{
    if(*ptr%2 ==0)
    {
        printf("even");
    }
    else{
        printf("odd");
    }
}
void main(){
    int num = 10;
    evenodd(&num);
}