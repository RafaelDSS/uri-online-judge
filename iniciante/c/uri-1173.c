#include <stdio.h>

int main() {
    int vetor[10],
        v,
        i;

    scanf("%d", &v);

    for (i = 0; i < 10; i++) {
        vetor[i] = v;
        v *= 2;
    }

    for (i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, vetor[i]);
    }

    return 0;
}
