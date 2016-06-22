package main

import (
	"fmt"
)

func b (a, b int) int {
	return a * b
}

func main() {
	a := func(a, b int) int {
		return a + b
	}
	fmt.Println(a(1, 2))
	fmt.Println(b(1, 2))
}
