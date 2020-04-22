#include <stdio.h>

int main() {
    int numero, horas;
    float valor_hora, salario;

    scanf("%d", &numero);
    scanf("%d", &horas);
    scanf("%f", &valor_hora);

    salario = horas * valor_hora;

    printf("NUMBER = %d\n", numero);
    printf("SALARY = U$ %.2f\n", salario);
    
    return 0;
}
