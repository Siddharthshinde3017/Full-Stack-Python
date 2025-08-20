#include<stdio.h>

void main(){
    int num[5]={10, 20, 30, 40, 50};
    int i ;
    for ( i = 0; i < 5; i++)
    {
       printf("%d\t",num[i]);
    }
   printf("\n");
    for ( i = 4; i >=0; i--)
    {
        printf("%d\t",num[i]);
    }
    
    
    // printf("");
}