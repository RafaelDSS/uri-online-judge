#include <stdio.h>

int main() {
    const double PI = 3.14159;
    double raio;

    scanf("%lf", &raio);

    printf("A=%.4f\n", PI * (raio * raio));
    
    return 0;
}
