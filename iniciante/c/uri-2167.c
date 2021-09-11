#include <stdio.h>

int main() {
    int n, i, menor=0, valor, posicao=0;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &valor);
        if (valor < menor) {
            menor = valor;
            posicao = i;
            break;
        }
        menor = valor;

    }
    if (posicao == 0)
        printf("0\n");
    else
        printf("%d\n", posicao+1);

    return 0;
}
