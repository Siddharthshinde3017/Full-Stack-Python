#include<stdio.h>
void main(){
    int num1 = 10, num2 = 20;
    int *p1 = &num1;
    int *p2 = &num2;

    int result = *p1 + *p2;
    printf("result = %d\n", result);

    printf("value of p1 =%d\t value o p2 = %d\n",*p1,*p2);

    // swap
    *p1 =*p1 + *p2;
    *p2 =*p1-*p2;
    *p1 = *p1-*p2;

    // printf("%d\t %d",*p1,*p2);
    printf("After awaping value of p1 =%d\t After swaping value o p2 = %d\n",*p1,*p2);


}