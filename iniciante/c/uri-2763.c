#include <stdio.h>
#include <string.h>

int main() {

    char cpf[200], caracter=' ', *p;
    int i;

    while (gets(cpf)) {
        for (i = 0; i < strlen(cpf); i++) {
            if (cpf[i] == '.' || cpf[i] == '-')
                printf("\n");
            else
                printf("%c", cpf[i]);
        }
        printf("\n");
    }

    return 0;
}
