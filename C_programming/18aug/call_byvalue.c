#include<stdio.h>

void show(int num)
{
    printf("\nbefore adding num = %d",num);
    num= num +10;
    printf("\nafter adding  num = %d",num);

}

int main()
{
    int a = 10;

    printf("\nbefore adding a= %d",a);
    show(a);        // calling the value of a using the value of variable a
    printf("\nafter adding a= %d",a);
    return 0 ; 

}