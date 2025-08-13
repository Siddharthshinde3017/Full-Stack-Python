// we can use ternery operaor in used in the code to simplify the if else statment 
#include<stdio.h>
#include<conio.h>

void main(){
    int a ;
    printf("Enter the number :" );
    scanf("%d",a);
    // ()? operation1 : operation2
    (a % 2 == 0)? printf("number is even"): printf("number is odd");

}