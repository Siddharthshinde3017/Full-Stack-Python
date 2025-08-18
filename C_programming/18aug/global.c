#include<stdio.h>

int num = 10;
void test(){
    int num= 50 ; //  this modifies the value of num and saves the value within the test function
    printf("%d",num);

}

void demo(){
    printf("%d", num);
}

void main(){
    test();
    demo();

}
// # imp question difference between local and global variable with example

