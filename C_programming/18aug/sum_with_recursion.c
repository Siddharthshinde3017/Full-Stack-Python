#include<stdio.h>

int sum(int num){
    if(num>0){
        return num + sum(num-1);
    }else{
        return 0;
    
    }
}

void main(){
    printf("%d",sum(10));
}