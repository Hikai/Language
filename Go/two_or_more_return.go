package main

import (
	"fmt"
)

func add_and_mul (a, b int) (x, y int) {
	x = a + b
	y = a * b
	return
}

func main() {
	fmt.Println(add_and_mul(1, 2))
}
