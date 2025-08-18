#include<stdio.h>

int main(){
    int num; // 5 *4*3*2*1
    printf("Enter the Number\n");
    scanf("%d",&num);
    int i;
    int result = 1; 

    for(i=num; i>=1; i--){
        result = result*i;
          printf("\n%d",result);
    }
         


}