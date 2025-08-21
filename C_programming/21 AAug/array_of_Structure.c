// #include<stdio.h>

// struct student
// {
//     int rollno;
//     char name[30];
// }s[5];

// void main(){
//     printf("Enter details of student");
//     for(int i =0; i <5;i++){

//         printf("\nenter roll no: ");
//         scanf("%d",&s[i].rollno);

//         printf("\nenter name:-");
//         scanf("%s", &s[i].name);
//     }
//     for (int i = 0; i <5; i++)
//     {
//         printf("\nrollno is :%d",s[i].rollno);
//         printf("\nname is :-%s",s[i].name);
//     }
    
    
// }

#include <stdio.h>

struct student {
    int rollno;
    char name[30];
} s[5];

int main() {
    printf("Enter details of 5 students:\n");

    for (int i = 0; i < 5; i++) {
        printf("\nEnter roll no: ");
        scanf("%d", &s[i].rollno);

        printf("Enter name: ");
        scanf("%s", s[i].name); 
    }

    
    for (int i = 0; i < 5; i++) {
        printf("Roll No: %d\n", s[i].rollno);
        printf("Name   : %s\n", s[i].name);

    }

    return 0;
}

