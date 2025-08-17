#include<stdio.h>

void main(){
    int number, reverse, digit;
    number = 12345;
    while (number>0)
    {
        digit= number%10;
        reverse= reverse*10 + digit;
        number= number / 10;
    }
    printf("%d",reverse);
}