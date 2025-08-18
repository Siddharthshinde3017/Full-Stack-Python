#include<stdio.h>

int main(){
    int num; // 5 *4*3*2*1
    scanf("Enter number = %d",&num);
    int i;
    int result = 1; 

    for(i=; i>=1; i--){
        result = result*i;
        printf("\n%d",result);
    }
        // prinf("%d",num);


}