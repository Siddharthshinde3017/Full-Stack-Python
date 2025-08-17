#include<stdio.h>

void main(){
    int number, sum, digit;
    number = 121;
    while (number>0)
    {
        digit = number%10;// digit = 1
        sum = digit+sum;// sum=1
        number= number/10;//num=12

    }
    printf("%d",sum);
}