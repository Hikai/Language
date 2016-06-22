package main

import (
	"fmt"
)

func main() {
	a := func(a, b int) int {
		return a + b
	}
	fmt.Println(a(1, 2))
}
