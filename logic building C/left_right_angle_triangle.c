//     *
//    **
//   ***
//  ****   

// # include<stdio.h>
// void main(){
//     int r,c,s;
    
//     for (r=1;r<5;r++){
//         for(s=1;s<=5-r;s++){
//             printf(" ");
//         }

//         for(c=1;c<=r;c++){
//             printf("*");
            
//         }
//         printf("\n");
//     }
// }



// for printiting pattern of 1
//     1
//    11
//   111
//  1111

// # include<stdio.h>
// void main(){
//     int r,c,s;
    
//     for (r=1;r<5;r++){
//         for(s=1;s<=5-r;s++){
//             printf(" ");
//         }

//         for(c=1;c<=r;c++){
//             printf("1");
            
//         }
//         printf("\n");
//     }
// }


// for printing 01
//    0
//   11
//  000
// 1111


// # include<stdio.h>
// void main(){
//     int r,c,s;
    
//     for (r=1;r<5;r++){
//         for(s=1;s<=5-r;s++){
//             printf(" ");
//         }

//         for(c=1;c<=r;c++){
//             if (r%2 == 0){
//                 printf("1");
//             }
//             else{
//                 printf("0");
//             }
            
//         }
//         printf("\n");
//     }
// }


//     1
//    23
//   456
//  78910

# include<stdio.h>
void main(){
    int r,c,s;
    int count = 1;
    
    for (r=1;r<5;r++){
        for(s=1;s<=5-r;s++){
            printf(" ");
        }

        for(c=1;c<=r;c++){
            printf("%d",count);
            count++;
            
        }
        printf("\n");
    }
}
