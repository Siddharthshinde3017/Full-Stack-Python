#include<stdio.h>
#include<conio.h>
void main(){
    int num;
    int choise;
    printf("Enter the number : ");
    scanf("%d",&num);
    printf("\nEnter your choise: ");
    scanf("%d",&choise);
    if(choise == 1){
        if (num%2==0)
        {
            printf("number is Even");
        }
        else{
            printf("Number is odd");
        }
    }
    else if (choise==2)
    {
        if (num>0)
        {
            printf("number is positive");
        }
        else if(num<0)
        {
            printf("Number is negative");
        }
        else{
            printf("number is neither positive nor negative ");
        }        
    }
}