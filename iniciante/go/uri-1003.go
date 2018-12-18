package main

import (
	"fmt"
)

func main(){
	var a, b, soma int

	fmt.Scan(&a)
	fmt.Scan(&b)

	soma = a + b
	fmt.Printf("SOMA = %d\n", soma)
}