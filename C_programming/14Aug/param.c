#include<stdio.h>

void evenodd(int num){
    if(num%2==0){
        printf("even num : %d", num);
    }
    else{
        printf("odd num : %d", num);
    }
}

void main(){
    evenodd(5);
    evenodd(26);
}