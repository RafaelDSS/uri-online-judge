package main

import (
	"fmt"
)

func main(){
	var a, b, x int
	fmt.Scan(&a, &b)
	x = a + b
	fmt.Printf("X = %d", x)
}