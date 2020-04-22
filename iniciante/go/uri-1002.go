package main

import (
	"fmt"
)

func main(){

	var n float64 = 3.14159
	var r, area float64

	fmt.Scan(&r)
	area = n * (r*r)

	fmt.Printf("A=%.4f\n", area)


}