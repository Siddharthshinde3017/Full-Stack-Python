#include<stdio.h>
#include<conio.h>
void main(){
    int start;
    int end;

    printf("Enter start :");
    scanf("%d", &start);

    printf("enter end: ");
    scanf("%d", &end);

    for (int i = start; i <= end ; i++)
    {
        printf("\t%d",i);
    }
}