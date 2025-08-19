#include<stdio.h>
int swap(int*a,int*b){
    *a = *a+*b;
    *b = *a-*b;
    *a = *a-*b;
    // int temp;
    // temp = *a;
    // *a = *b;
    // *b = temp;

    // printf("%d %d", *a, *b);
}
void main(){
        int c = 10;
        int d = 20 ;

        swap(&c,&d);

        printf("the number afrer swaping are c= %d d = %d",c,d);
}