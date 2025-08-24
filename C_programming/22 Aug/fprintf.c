#include<stdio.h>
void main(){
    FILE *p;
    p = fopen("file.txt","w");
    fprintf(p,"hello");
    fclose(p);
}