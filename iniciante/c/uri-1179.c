#include <stdio.h>

int main() {
    int impares[5],
        index_impares=0,
        pares[5],
        index_pares=0,
        i,
        index,
        numero;

    for (i = 0; i < 15; i++) {
        scanf("%d", &numero);

        if (numero % 2 == 0){
            if (index_pares < 5) {
                pares[index_pares] = numero;
            }
            else {
                for (index = 0; index < 5; index++) {
                    printf("par[%d] = %d\n",index, pares[index]);
                }
                index_pares = 0;
                pares[index_pares] = numero;
            }
            index_pares++;
        }
        else {
            if (index_impares < 5) {
                impares[index_impares] = numero;
            }
            else {
                for (index = 0; index < 5; index++) {
                    printf("impar[%d] = %d\n",index, impares[index]);
                }
                index_impares = 0;
                impares[index_impares] = numero;
            }
            index_impares++;
        }
    }

    for (index = 0; index < index_impares; index++) {
        printf("impar[%d] = %d\n", index, impares[index]);
    }

    for (index = 0; index < index_pares; index++) {
        printf("par[%d] = %d\n", index, pares[index]);
    }

    return 0;
}
