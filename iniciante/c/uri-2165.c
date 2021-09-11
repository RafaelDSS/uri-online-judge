#include <stdio.h>

int main() {

    char t[502] = "", caracter=' ';
    int size=0, index=0;

    scanf("%[^\n]", t);

    while (caracter != '\0') {
        caracter = t[index];
        index++;
        size++;
    }

    if(size-1 <= 140)
        printf("TWEET\n");
    else
        printf("MUTE\n");

    return 0;
}
