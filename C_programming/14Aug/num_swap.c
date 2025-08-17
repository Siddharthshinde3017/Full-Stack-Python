#include<stdio.h>

void swap(int n1 , int n2){
    printf("\nnumber before swap n1 = %d and n2 = %d", n1, n2);

    // int temp;
    // temp = n1;           // with using temp variable
    // n1= n2;
    // n2= temp;

    n1=n1+n2;
    n2=n1-n2;
    n1 = n1-n2;

    printf("\nnumber after swap n1 = %d and n2 = %d", n1, n2);

}

void main(){
    // swap(20,30);
     swap(24,36);


}