#include<stdio.h>
#include<string.h>
struct student{
    int rollno[10];
    char name[30];
}s1;

void main(){
    // struct student s1;

    // s1.rollno = 101;
    // // s1.name = "abcd";
    // strcpy(s1.name,"abc");

    // printf("\nroll no :=%d", s1);
    // printf("\nname :=%s", s1);



    // user input

    printf("\nEnter the roll no:-");
    scanf("%d", &s1.rollno);

    printf("\nEnter the name: ");
    scanf("%s", s1.name);

    printf("\nrollno : = %d",s1.rollno);
    printf("\nname : = %s",s1.name);

}