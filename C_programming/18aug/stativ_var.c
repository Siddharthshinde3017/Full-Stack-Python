#include<stdio.h>

// int num = 12;
// static int a = 21;

void test(){
    static int a = 12;
    int b= 10;

    a= a+b;
    b= b+a;

    printf("\n%d %d",a,b);

}
void main(){
    test();
    test();
}

