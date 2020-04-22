package main

import (
	"fmt"
)

func main(){
	var a, b, c, d, diferenca int

	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	fmt.Scan(&d)

	diferenca = (a * b) - (c * d)

	fmt.Printf("DIFERENCA = %d\n", diferenca)


}