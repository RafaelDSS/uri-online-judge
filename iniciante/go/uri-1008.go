package main

import (
	"fmt"
)

func main(){
	var numero int
	var horas, valor, salario float64

	fmt.Scan(&numero)
	fmt.Scan(&horas)
	fmt.Scan(&valor)

	salario = valor * horas

	fmt.Printf("NUMBER = %d\n", numero)
	fmt.Printf("SALARY = U$ %.2f\n", salario)
}