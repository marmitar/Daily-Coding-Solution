#include <stdlib.h>

int *product_array(int *numbers, size_t size) {
    int *direct = malloc(sizeof(int));
    int *inverse = malloc(sizeof(int));
    int *answer = malloc(sizeof(int));

    direct[0] = 1;
    inverse[size-1] = 1;

    for (size_t i = 1; i < size; i++) {
        direct[i] = direct[i-1] * numbers[i-1];

        inverse[size-i-1] = inverse[size-i] * numbers[size-i];
    }

    for (size_t i = 0; i < size; i++) {
        answer[i] = direct[i] * inverse[i];
    }

    free(direct);
    free(inverse);
    return answer;
}

#include <stdio.h>

int main(int argc, char const *argv[]) {
    int array[5] = {1, 2, 3, 4, 5};

    int *product = product_array(array, 5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", product[i]);
    }
    printf("\n");

    free(product);
    return 0;
}
