#include<stdio.h>
#include<string.h>

void main(){
    char ch1 [50] = "hello";
    char ch2 [50] = "wrldf";
    char ch3 [50];
    
    // strlen 
    printf("Lenth = %d",strlen(ch1));

    int length = strlen(ch1);
    printf("\nLenth = %d",length);



    // strcpy()
    strcpy(ch3,ch2);
    printf("\n%s",ch3);



    // strcat 
    strcat(ch1,ch2);
    printf("\n%s ",ch1);

    // strcmp
    // printf("\n%d",strcmp("hello","hello"));
    if(strcmp(ch1,ch2)==0)
    {
        printf("\nEqual");

    }
    else{
        printf("\nNot equal");
    }

    // strrev 
    printf("\n%s",strrev(ch1));

    //strlwr strupr
    printf("\n%s",strlwr(ch2));
    printf("\n%s",strupr(ch2));


}