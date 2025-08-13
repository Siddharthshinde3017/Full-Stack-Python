#include<stdio.h>
#include<conio.h>

void main(){
    // int num;
    // printf("Enter the number: ");
    // scanf("%d",&num);
    // // printf("Enteredd number is : %d", num);

    // if(num%2 == 0){
    //     printf("Number is Even");
    // }
    // else{
    //     printf("Number is Odd");

    // }
    

    char name[10];
    char city[10];

    printf("Enter the name:");
    scanf("%s", name);

    printf("\nEnter the city name : ");
    scanf("%s", city);

    printf("my name is %s, im from %s" , name , city);
}