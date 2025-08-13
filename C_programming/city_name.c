#include<stdio.h>
#include<conio.h>

void main(){
     char name[10];
    char city[10];

    // printf("Enter the name:");
    // scanf("%s", &name);

    // printf("\nEnter the city name : ");
    // scanf("%s", &city);

    printf("\nEnter the name and city"); // here we take input name and city in one line
    scanf("%s%s",&name,&city);

    printf("my name is %s, im from %s" , name , city);
    // return 0;
}
