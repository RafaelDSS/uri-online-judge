#include <stdio.h>
#include <string.h>

int main() {

    char string1[150] = "",
         string2[150] = "",
         string3[150] = "",
         string1cpy[150] = "",
         string2cpy[150] = "",
         string3cpy[150] = "",
         caracter=' ';

    int index=0;

    gets(string1);
    fflush(stdin);

    gets(string2);
    fflush(stdin);

    gets(string3);
    fflush(stdin);

    printf("%s%s%s\n", string1, string2, string3);
    printf("%s%s%s\n", string2, string3, string1);
    printf("%s%s%s\n", string3, string1, string2);

    strncpy(string1cpy, string1, 10);
    strncpy(string2cpy, string2, 10);
    strncpy(string3cpy, string3, 10);

    printf("%s%s%s\n", string1cpy, string2cpy, string3cpy);


    return 0;
}
