#include <stdio.h>

int main() {
    float a, b, c, media;

    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);

    media = ((a * 2) + (b * 3) + (c * 5)) / 10;

    printf("MEDIA = %.1f\n", media);
    
    return 0;
}
