#include <stdio.h>
#include <string.h>

int main() {

    char frase[300], caracter;
    int i;

    scanf("%[^\n]", &frase);

    for (i = 0; i < strlen(frase); i++) {
        caracter = frase[i];

        if (caracter == ',')
            printf("\n");
        else
            printf("%c", caracter);
    }
    printf("\n");

    return 0;
}
