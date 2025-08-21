#include<stdio.h>
#include<string.h>

void main (){
   char str11[20] = "hi ";
   char str12[20] = "helllo ";
   char str13[20] = "welcome ";
   char str14[20] = "good morning.";

   printf("\n%s", strcat(str11,str12));
   printf("\n%s", strcat(str13, str14));
    printf("\n%s", strcat(str11,str13));

}