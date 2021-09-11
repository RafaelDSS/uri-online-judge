#include <stdio.h>

int main() {
    int n, menor, posicao=0, valor, index=0;

    scanf("%d\n", &n);

    int x[n];

    for (index = 0; index < n; index++) {
        scanf("%d", &x[index]);
    }

    menor = x[0];
    for (index = 0; index < n; index++) {
        if (x[index] < menor) {
            posicao = index;
            menor = x[index];
        }
    }

    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

    return 0;
}
