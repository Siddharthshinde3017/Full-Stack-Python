#include<stdio.h>
void main(){
    int numbers[5];
    int i , sum=0;

    printf("\nEnter your array element :");
    for(i=0;i<5;i++){

        scanf("%d",&numbers[i]);
        sum = sum+ numbers[i];
    }
    printf("sum = %d",sum);
}