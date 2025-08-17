#include<stdio.h>
void main()
{
    int i=1;
    // while (i<=10)
    // {
    //     printf("%d",i);
    // }
    // sum of number//
    int numbr, digit , sum;
    numbr = 123456;
    while (numbr>0)
    {
        digit =numbr%10;
        sum = sum+ digit;
        numbr = numbr/10;

    }
    printf("%d", sum);
    
    
}