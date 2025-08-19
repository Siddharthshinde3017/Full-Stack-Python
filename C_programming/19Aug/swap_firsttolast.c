#include <stdio.h>

int main() {
    int numbers[5];
    int i;

    printf("Enter 5 numbers:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &numbers[i]);
    }

    printf("Original array:\n");
    for (i = 0; i < 5; i++) {
        printf("%d\t", numbers[i]);
    }

    // Swap first and last
    int temp = numbers[0];
    numbers[0] = numbers[4];
    numbers[4] = temp;

    printf("\nArray after swapping first and last:\n");
    for (i = 0; i < 5; i++) {
        printf("%d\t", numbers[i]);
    }

    return 0;
}
