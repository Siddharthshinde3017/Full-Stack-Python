# include<stdio.h>
void main(){
    int r,c;
    int Alp='a';
    for(r=1;r<4;r++){
        for(c=1;c<4;c++){
            printf("%c",Alp);
            Alp++;
        }printf("\n");
    }
}