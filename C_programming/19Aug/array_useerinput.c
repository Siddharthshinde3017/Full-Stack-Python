#include<stdio.h>
void main(){
    int numbers[5];
    int i ;

    printf("\nEnter your array element :");
    for(i=0;i<5;i++){

        scanf("%d",&numbers[i]);

    }
    for(i=0;i<5;i++){

        printf("\t%d",numbers[i]);

    }
}