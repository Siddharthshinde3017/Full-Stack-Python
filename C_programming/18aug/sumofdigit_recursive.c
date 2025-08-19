#include<stdio.h>

int sumOfdigits(int n){

    if(n==0){
        return 0;
    }
    else{ 
        // return n + sumOfdigits(n-1);
        int digit = n%10;
        return digit + sumOfdigits(n/10);
    }
}

void main(){
    printf("%d",sumOfdigits(123));
}