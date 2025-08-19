#include<stdio.h>

/*void main(){
    int num[2][2];
    num[0][0]=10;
    num[0][1]=20;
    num[1][0]=30;
    num[1][1]=40;

    printf("%d",num[1][1]);

}*/

// for taking user input

void main()
{
    int num[2][2];
    int i ,j;
    printf("Enter elements in arra: ");
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            scanf("%d",&num[i][j]);
        }

    }
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            printf("%d\t",num[i][j]);
        }
    printf("\n");
        

    }
}